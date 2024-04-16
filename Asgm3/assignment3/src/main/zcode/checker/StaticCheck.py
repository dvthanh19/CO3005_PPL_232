from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce






# Build new class ////////////////////////////////////////////////////////////////////////////////////////////////////////

class Zcode(Type): pass    # Type that not be infered 

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        # param: list[Type]
        # typ: Type = {number, bool, string, arrayType, None}
        # body: Bool = True if there is a body content, otherwise false
        self.param = param
        self.typ = typ
        self.body = body

class VarZcode(Zcode):
    def __init__(self, typ = None):
        # typ = {number, bool, string, arrayType, None}
        self.typ = typ    

class ArrayZcode(Type):
    def __init__(self, eleType):
        # List[Type] (Type = {Zcode, ArrayZcode, String, Bool, Number, Arraytype})
        self.eleType = eleType  




# Helper functions ///////////////////////////////////////////////////////////////////////////////////////////////////////

def normalizeUtils(self, arr: ArrayType):
    # Base case
    if type(arr.eleType) is not ArrayType:
        return arr.size, arr.eleType
    
    return arr.size + normalizeUtils(arr.eleType)[0], normalizeUtils(arr.eleType)[1]



# Main class /////////////////////////////////////////////////////////////////////////////////////////////////////////////
class StaticChecker(BaseVisitor, Utils):
    
    def __init__(self, ast):
        self.ast = ast
        self.function = None
        self.inLoop = 0
        self.func = None
        self.returnStmt = False
        # self.funcList = {
        #     "readNumber"    : FuncZcode([], NumberType(), True),
        #     "readBool"      : FuncZcode([], BoolType(), True),
        #     "readString"    : FuncZcode([], StringType(), True),
        #     "writeNumber"   : FuncZcode([NumberType()], VoidType(), True),
        #     "writeBool"     : FuncZcode([BoolType()], VoidType(), True),
        #     "writeString"   : FuncZcode([StringType()], VoidType(), True),
        # }
        self.funcList = {}
        
        self.binaryInput = {
            'and': BoolType(), 'or': BoolType(),
            '+': NumberType(), '-': NumberType(), '*': NumberType(), '/': NumberType(),
            '=': NumberType(), '!=': NumberType(),
            '>': NumberType(), '>=': NumberType(), '<': NumberType(), '<=': NumberType(),
            '...': StringType(), '==': StringType(),
        }
        self.binaryOutput = {
            'and': BoolType(), 'or': BoolType(),
            '+': NumberType(), '-': NumberType(), '*': NumberType(), '/': NumberType(),
            '=': NumberType(), '!=': NumberType(),
            '>': NumberType(), '>=': NumberType(), '<': NumberType(), '<=': NumberType(),
            '...': StringType(), '==': StringType(),
        }     
        
        self.unaryInput = {"-": [NumberType()], 
                         "not": [BoolType()]}
        self.unaryOutput = {"-": [NumberType()],
                          "not": [BoolType()]}
    
    
    
    # Helper functions ===================================================================================================
    
    def check(self):
        self.visit(self.ast, [{}])
        return None
    
    
    def compareType(self, lhs, rhs):
        allowedType = [NumberType, StringType, BoolType, VoidType, ArrayType]
        
        if type(lhs) not in allowedType or type(rhs) not in allowedType:
            return False
        
        if (type(lhs) is ArrayType) and (type(rhs) is ArrayType):
            
            _lhs = self.normalizeArrayType(lhs)
            _rhs = self.normalizeArrayType(rhs)
            if ((_lhs.size == _rhs.size) and (type(_lhs.eleType) is type(_rhs.eleType))):
                return True
            return False
        
        return True if (type(lhs) is type(rhs)) else False   
    
    
    # ... Chua hieu muc dich ham 
    # LHS: ArrayZcode, RHS: ArrayZcode
    def compareListType(self, lhs, rhs):
        allowedType = [NumberType, StringType, BoolType, VoidType, ArrayType]
        
        
        if lhs.size != rhs.size:
            return False        
        
        for i in range(lhs.size):
            if  (type(lhs.eleType[i]) not in allowedType) \
                or (type(rhs.eleType[i]) not in allowedType) \
                or (lhs.eleType[i] != rhs.eleType[i]):
                return False
        
        return True
        
        
    # Infer type for array
    def setTypeArray(self, typeArray:ArrayType, typeArrayZcode:ArrayZcode):
        if typeArray.size[0] != len(typeArrayZcode.eleType):
            return False

        # Base case: 1D array
        if len(typeArray.size) == 1:
            for x in typeArrayZcode.eleType:
                if type(x) in [ArrayZcode, ArrayType]:
                    return False
                
                if isinstance(x, Zcode):
                    x.typ = typeArray.eleType
        
        # >2D array
        else:
            for x in typeArrayZcode.eleType:
                # number x[2][3][1] = [[y], [[6], [6], [6]]] --> y is number[3][1]
                # base case
                if isinstance(x, Zcode):
                    x.typ = ArrayType(typeArray.size[1:], typeArray.eleType)
                
                if type(x) is ArrayZcode:
                    self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType), x)
     
                    
    def setType(self, typ, zObject):
        if type(zObject) is VarZcode:
            zObject.typ = typ
            return True
        
        if type(zObject) is FuncZcode:
            if zObject.name.name in self.funcList:
                tmp = zObject.funcList[zObject.name.name]
                if tmp.typ is None:
                    tmp.typ = typ
                    return True
            
        
        return False
    
    
    def normalizeArrayType(self, arr: ArrayType):
        return ArrayType(normalizeUtils(arr)[0], normalizeUtils(arr)[1])
    
    
    
    # Main visit functions ===============================================================================================
    
    # decl: List[Decl]
    def visitProgram(self, ast:Program, param):
        for x in ast.decl:
            # print('decl') #cmt
            self.visit(x, param)
        
        for funcName, funcAttr in self.funcList.items():
            if not funcAttr.body:
                raise NoDefinition(funcName)

        
        entry = self.funcList.get('main')
        if (not entry) or (type(entry.typ) is not VoidType) or (len(entry.param) != 0):
            raise NoEntryPoint()


    

    # name: Id
    # varType: Type = None  # None if there is no type
    # modifier: str = None  # None if there is no modifier
    # varInit: Expr = None  # None if there is no initial
    def visitVarDecl(self, ast:VarDecl, param):
        if ast.name.name in param[0]:
            raise Redeclared(Variable(), ast.name.name)
        
        if ast.varInit is not None:
            rhs = self.visit(ast.varInit)
            
            # number x <- x + 1 (RHS use undeclared x => Add LHS into param after done checking RHS)
            param[0][ast.name.name] = VarZcode(ast.varType)
            lhs = self.visit(ast.name.name)
            
            
            # Both sides need infering
            if isinstance(lhs, Zcode) and (isinstance(rhs, Zcode) or isinstance(rhs, ArrayZcode)):
                raise TypeCannotBeInferred(ast)           

            # LHS not need infering
            if (not isinstance(lhs, Zcode)) and isinstance(rhs, ArrayZcode):
                if type(lhs) in [NumberType, BoolType, StringType]:
                    raise TypeMismatchInStatement(ast)
                
                if type(lhs) is ArrayType:
                    if not self.setTypeArray(lhs, rhs):
                        raise TypeMismatchInStatement(ast)
            
            # RHS infer type for LHS 
            # elif isinstance(lhs, Zcode) and (type(rhs) in [NumberType, BoolType, StringType, ArrayType]):
            elif isinstance(lhs, Zcode): # Can remove the and ... because we have check for rhs in the first if 
                lhs.typ = rhs
            
            # LHS infer type for RHS
            elif isinstance(rhs, Zcode):
                rhs.typ = lhs
            
            # Both sides not need infer type
            elif (type(lhs) in [NumberType, BoolType, StringType, ArrayType]) \
            and (type(rhs) in [NumberType, BoolType, StringType, ArrayType]):
                if not self.compareType(lhs, rhs):
                    raise TypeMismatchInStatement(ast)
            
        else:
            param[0][ast.name.name] = VarZcode(ast.varType)

    
    # name: Id
    # param: List[VarDecl]  # empty list if there is no parameter
    # body: Stmt = None  # None if this is just a declaration-part
    def visitFuncDecl(self, ast:FuncDecl, param):
        method = self.funcList.get(ast.name.name)
        print(self.funcList)
        
        # Build paramList and paramType
        paramList = {}
        paramType = []
        for x in ast.param:
            if x.name.name in paramList:
                raise Redeclared(Parameter(), x.name.name)
            
            paramList[x.name.name] = VarZcode(x.varType)
            paramType.append(x.varType)

        
        
        self.returnStmt = False
        
        # Redeclared function
        # if method:
        #     print(1.1)
        #     if method.body:
        #         print(1.2)
        # if (ast.body):
        #     print(1.3)
            
        if method and (not (not method.body and ast.body)):
            raise Redeclared(Function(), ast.name.name)
        
                
        if ast.body is None:
            self.funcList[ast.name.name] = FuncZcode(paramType, None, False)        
        else:
            if method:
                method.body = True
                self.function = method
            else:
                self.funcList[ast.name.name] = FuncZcode(paramType, None, True)
                self.function = self.funcList[ast.name.name]
                print("function:    ", self.funcList[ast.name.name], self.function)
                
                
            self.visit(ast.body, [paramList] + param)
            if not self.returnStmt:
                self.function.typ = VoidType()

        
        self.function = None
        self.returnStmt = False
     
    
    
    # ====================================================================================================================
    
    # op: str
    # left: Expr
    # right: Expr
    def visitBinaryOp(self, ast:BinaryOp, param):
        left = self.visit(ast.left, param)
        right = self.visit(ast.right, param)
        
        if isinstance(left, Zcode):
            left = self.binaryInput[ast.op]
            left = self.visit(ast.left, param)
            
        if isinstance(right, Zcode):
            right = self.binaryInput[ast.op]
            right = self.visit(ast.right, param)
            
        if  (ast.op in self.binaryInput) \
        and (type(left) is self.binaryInput[ast.op]) \
        and (type(right) is self.binaryInput[ast.op]):
            return self.binaryOutput[ast.op]
        
        raise TypeMismatchInExpression(ast)
    
    
    # op: str
    # operand: Expr
    def visitUnaryOp(self, ast, param):
        right = self.visit(ast.operand, param)
        
        if isinstance(right, Zcode):
            right = self.setType(self.unaryInput[ast.op], )
            right = self.visit(ast.right, param)
        
        if  (ast.op in self.unaryInput) and (type(right) is self.unaryInput[ast.op]): 
            return self.unaryOutput[ast.op]
        
        raise TypeMismatchInExpression(ast)

    
    # name: Id
    # args: List[Expr]
    def visitCallExpr(self, ast, param):
        method = self.funcList.get(ast.name.name)
        
        if (method is None) or (method and method.name.name in param[0]):
            raise Undeclared(Function(), ast.name.name)
        
        if type(method.typ) is VoidType():
            raise TypeMismatchInExpression(ast)
        
        check = [self.compareType(self.visit(ast.args[i], param), method.param[i]) \
            for i in range(len(ast.args))]
        if False in check:
            raise TypeMismatchInExpression(ast)
        
        
        return method.typ if method.typ else method


    
    # ====================================================================================================================
    
    # stmt: List[Stmt]  # empty list if there is no statement in block
    def visitBlock(self, ast, param):
        for x in ast.stmt:
            self.visit(x, param if type(x) is Block else [{}] + param)
    
    
    # expr: Expr
    # thenStmt: Stmt
    # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
    # elseStmt: Stmt = None  # None if there is no else branch
    def visitIf(self, ast, param):
        # If stmt
        cond = self.visit(ast.expr, param)
        if isinstance(cond, Zcode):
            self.setType(BoolType(), cond)
        if type(cond) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        # ThenStmt
        self.visit(ast.thenStmt, [{}] + param)
        
        # ElifStmt
        for (elifExpr, elifStmt) in ast.elifStmt:
            cond = self.visit(elifExpr, param)
            
            if isinstance(cond, Zcode):
                self.setType(BoolType(), cond)
            if type(cond) is not BoolType:
                raise TypeMismatchInStatement(ast)
            
            self.visit(elifStmt, [{}] + param)
        
        # ElseStmt
        if ast.elseStmt:
            self.visit(ast.elseStmt, [{}] + param)
    
    
    # name: Id
    # condExpr: Expr
    # updExpr: Expr
    # body: Stmt
    def visitFor(self, ast, param):
        # index
        i = self.visit(ast.name, param)
        if isinstance(i, Zcode):
            self.setType(NumberType(), i)
        if type(i) is not NumberType:
            raise TypeMismatchInStatement(ast)
        
        # condExpr
        cond = self.visit(ast.condExpr, param)
        if isinstance(cond, Zcode):
            self.setType(BoolType(), i)
        if type(cond) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        # upExpr
        updExpr = self.visit(ast.updExpr, param)
        if isinstance(updExpr, Zcode):
            self.setType(NumberType(), updExpr)
        if type(updExpr) is not NumberType:
            raise TypeMismatchInStatement(ast)
        
        # body
        self.inLoop += 1    # 1 go in Loop
        self.visit(ast.body, [{}] + param)
        self.inLoop -= 1    # 1 go out Loop
    
    
    def visitContinue(self, ast, param):
        if self.inLoop == 0:
            raise MustInLoop(ast)

    
    def visitBreak(self, ast, param):
        if self.inLoop == 0:
            raise MustInLoop(ast)  
    
    
    # expr: Expr = None  # None if there is no expression after return
    def visitReturn(self, ast, param):
        self.returnStmt = True
        
        funcType = self.function.typ if self.function.typ else self.function
        retType = self.visit(ast.expr, param) if ast.expr else VoidType()
        print("helloooooooo: ", funcType, retType)
        
        
        # Case 1: not sure: func foo() begin if a then return k else return 1
            # Can we from 1 infer a then infer func ?
        if (isinstance(funcType, Zcode) or isinstance(funcType, ArrayZcode)) \
        and (isinstance(retType, Zcode) or isinstance(retType, ArrayZcode)):
            print("return 1")
            raise TypeCannotBeInferred(ast)

        # Case 2: retType is ArrayZcode and can be infered by funcType
        if not (isinstance(funcType, Zcode) or isinstance(funcType, ArrayZcode))\
        and (isinstance(retType, ArrayZcode)):
            if type(funcType) in [NumberType, StringType, BoolType]:
                raise TypeMismatchInStatement(ast)
            
            # funcType is arraytype
            if not self.setTypeArray(funcType, retType):     
                raise TypeMismatchInStatement(ast)

        # Case 3: funcType need infering from retType
        elif isinstance(funcType, Zcode):
            funcType.typ = VoidType()
            print("return 3")
        
        # Case 4: retType need infering from funcType
        elif isinstance(retType, Zcode):
            retType.typ = funcType
            print("return 4")

        # Case 4: No need infering
        elif not self.compareType(funcType, retType):
            raise TypeMismatchInStatement(ast)
    
    
    # lhs: Expr
    # exp: Expr
    def visitAssign(self, ast, param):
        rhs = self.visit(ast.exp, param)
        lhs = self.visit(ast.lhs, param)
        
        # Case 1: Both side can not be infered
        if (isinstance(lhs, Zcode) or isinstance(lhs, ArrayZcode)) \
        and (isinstance(rhs, Zcode) or isinstance(rhs, ArrayZcode)):
            raise TypeCannotBeInferred(ast)
        
        # Case 2: rhs is ArrayZcode and can be infered by lhs
        if not (isinstance(lhs, Zcode) or isinstance(lhs, ArrayZcode))\
        and (isinstance(rhs, ArrayZcode)):
            if type(lhs) in [NumberType, StringType, BoolType]:
                raise TypeMismatchInStatement(ast)
            
            # lhs is arraytype
            if not self.setTypeArray(lhs, rhs):     
                raise TypeMismatchInStatement(ast)

        # Case 3: lhs need infering from rhs
        elif isinstance(lhs, Zcode):
            lhs.typ = rhs
        
        # Case 4: lhs need infering from rhs
        elif isinstance(rhs, Zcode):
            rhs.typ = lhs

        # Case 5: No need infering
        elif not self.compareType(lhs, rhs):
            raise TypeMismatchInStatement(ast)
    
    
    # name: Id
    # args: List[Expr]  # empty list if there is no argument
    def visitCallStmt(self, ast:CallStmt, param):
        method = self.funcList.get(ast.name.name)
        
        # ...
        if (method is None) or (method and method.name.name in param[0]):
            raise Undeclared(Function(), ast.name.name)
        
        if (method.typ is None):
            self.setType(VoidType(), method)
        
        if not (type(method.typ) is VoidType()):
            raise TypeMismatchInStatement(ast)
        
        check = [self.compareType(self.visit(ast.args[i], param), method.param[i]) \
            for i in range(len(ast.args))]
        if False in check:
            raise TypeMismatchInStatement(ast)
        
        
        return method.typ if method.typ else method
    
    
    
    # ====================================================================================================================
    
    # value: float
    def visitNumberLiteral(self, ast:NumberLiteral, param):
        return NumberType()
    
    
    # value: bool
    def visitBooleanLiteral(self, ast:BooleanLiteral, param):
        return BoolType() 
    
    
    # value: str
    def visitStringLiteral(self, ast:StringLiteral, param):
        return StringType()
    
    
    # ...... still
    # value: List[Expr]
    def visitArrayLiteral(self, ast:ArrayLiteral, param):
        if ast not in self.ast:
            self.ast.append(ast)
            
        typ = None
        # Get the 1st ele has primitive type
        for x in ast.value:
            ele = self.visit(x, param)
            if not (isinstance(ele, Zcode) or isinstance(ele, ArrayZcode)):
                typ = ele
                break
        
        if type(typ) is None: # There is no primitive type
            return ArrayZcode([self.visit(x, param) for x in ast.value])
        
        elif type(typ) in [StringType, BoolType, NumberType]:
            for x in ast.value:
                ele = self.visit(ast, x)
                
                if type(ele) in [VarZcode, FuncZcode]:
                    if self.setType(NumberType(), x):
                        raise TypeMismatchInExpression(ast[0])
                
                if (type(ele) in [ArrayZcode, ArrayType]) or (not self.compareType(typ, ele)):
                    raise TypeMismatchInExpression(ast[0])
                
            return ArrayType([len(ast.value)], typ)
        
        
        
        else: # typ is arrayType
            for x in ast.value:
                ele = self.visit(ast, x)
                
                if type(ele) is Zcode:
                    ele.typ = typ
                
                if type(ele) not in [ArrayZcode, ArrayType]:
                    raise TypeMismatchInExpression(ast)
                
                if type(ele) is ArrayZcode:
                    if self.setTypeArray(typ, ele):
                        raise TypeMismatchInExpression(ast[0])
                
                elif not self.compareType(typ, ele): 
                    raise TypeMismatchInExpression(ast[0])
            
            return ArrayType([len(ast.value)], typ)
        
    
    # name: str+
    def visitId(self, ast, param):
        for block in param:
            if ast.name in block:
                if isinstance(block[ast.name], Zcode):
                    return block[ast.name]
                
                if isinstance(block[ast.name], ArrayZcode):
                    # return ... 
                    pass
                
                return block[ast.name].typ
               
        raise Undeclared(ast, ast.name)
    
    
    # arr: Expr
    # idx: List[Expr]
    def visitArrayCell(self, ast, param):
        arr = self.visit(ast.arr, param)
        
        if type(arr) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        
        for x in ast.idx:
            idx = self.visit(x, param)
            
            if type(idx) in [VarZcode, FuncZcode]:
                if self.setType(NumberType(), x):
                    raise TypeMismatchInExpression(ast)
            
            if type(idx) is not NumberType:
                raise TypeMismatchInExpression(ast)
        
        if len(arr.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        
        if len(arr.size) == len(ast.idx):
            return arr.eleType
        
        if len(arr.size) > len(ast.idx):
            return ArrayType(arr.size[len(ast.idx):], arr.eleType)  



    # ====================================================================================================================

    def visitNumberType(self, ast:NumberType, param):
        return ast
        # return NumberType() 


    def visitBoolType(self, ast:BoolType, param):
        return ast
        # return BoolType()


    def visitStringType(self, ast:StringType, param):
        return ast
        # return StringType()
    
    
    # size: List[float]
    # eleType: Type
    def visitArrayType(self, ast:ArrayType, param):
        return ast
        # return ArrayType(ast.size, ast.eleType))


