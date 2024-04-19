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




# Main class /////////////////////////////////////////////////////////////////////////////////////////////////////////////
class StaticChecker(BaseVisitor, Utils):
    
    def __init__(self, ast):
        self.ast = ast
        self.function = None
        self.inLoop = 0
        self.func = None
        self.returnStmt = False
        self.funcList = {
            "readNumber"    : FuncZcode([], NumberType(), True),
            "readBool"      : FuncZcode([], BoolType(), True),
            "readString"    : FuncZcode([], StringType(), True),
            "writeNumber"   : FuncZcode([NumberType()], VoidType(), True),
            "writeBool"     : FuncZcode([BoolType()], VoidType(), True),
            "writeString"   : FuncZcode([StringType()], VoidType(), True),
        }
        # ...
        # self.funcList = {}
        
        self.binaryInput = {
            'and': BoolType(), 'or': BoolType(),
            '+': NumberType(), '-': NumberType(), '*': NumberType(), '/': NumberType(), '%': NumberType(),
            '=': NumberType(), '!=': NumberType(),
            '>': NumberType(), '>=': NumberType(), '<': NumberType(), '<=': NumberType(),
            '...': StringType(), '==': StringType(),
        }
        self.binaryOutput = {
            'and': BoolType(), 'or': BoolType(),
            '+': NumberType(), '-': NumberType(), '*': NumberType(), '/': NumberType(), '%': NumberType(),
            '=': BoolType(), '!=': BoolType(),
            '>': BoolType(), '>=': BoolType(), '<': BoolType(), '<=': BoolType(),
            '...': StringType(), '==': BoolType(),
        }     
        
        self.unaryInput = {"-": NumberType(), 
                         "not": BoolType()}
        self.unaryOutput = {"-": NumberType(),
                          "not": BoolType()}
    
    
    
    # Helper functions ===================================================================================================
    
    def check(self):
        self.visit(self.ast, [{}])
        return None
    
    
    def compareType(self, lhs, rhs):
        allowedType = [NumberType, StringType, BoolType, VoidType, ArrayType]
        
        if isinstance(lhs, Zcode) and (not isinstance(rhs, Zcode)):
            lhs = self.setType(rhs, lhs).typ
        
        if isinstance(rhs, Zcode) and (not isinstance(lhs, Zcode)):
            rhs = self.setType(lhs, rhs).typ
        
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
    # def compareListType(self, lhs, rhs):
    #     allowedType = [NumberType, StringType, BoolType, VoidType, ArrayType]
        
        
    #     if lhs.size != rhs.size:
    #         return False        
        
    #     for i in range(lhs.size):
    #         if  (type(lhs.eleType[i]) not in allowedType) \
    #             or (type(rhs.eleType[i]) not in allowedType) \
    #             or (lhs.eleType[i] != rhs.eleType[i]):
    #             return False
        
    #     return True
        
        
    # Infer type for array
    def setTypeArray(self, typeArray, typeArrayZcode):
        # Type of error: 
        #   -1: for statement
        #   -2: for expression     
        
        # print('setTypeArray ', typeArrayZcode)
        if typeArray.size[0] != len(typeArrayZcode.eleType):
            # print('setTypeArray 1', typeArray.eleType)
            # print('setTypeArray 1', typeArrayZcode.eleType)
            return -1

        # Base case: 1D array
        if len(typeArray.size) == 1:
            # print('setTypeArray 2')
            for x in typeArrayZcode.eleType:
                if type(x) in [ArrayZcode, ArrayType]:
                    # print('setTypeArray 2.1')
                    return -2
                
                elif isinstance(x, Zcode):
                    # print('setTypeArray 2.2')
                    res = self.setType(typeArray.eleType, x)
                    if not res:
                        # print('setTypeArray 2.2.1')
                        return -2
                    x = res.typ
                         
        
        # >2D array
        else:
            # print('setTypeArray 3: len = ', len(typeArrayZcode.eleType))
            for x in typeArrayZcode.eleType:
                # number x[2][3][1] = [[y], [[6], [6], [6]]] --> y is number[3][1]
                # base case
                if isinstance(x, Zcode):
                    # print('setTypeArray 3.1')
                    x.typ = ArrayType(typeArray.size[1:], typeArray.eleType)
                
                elif type(x) is ArrayZcode:
                    # print('setTypeArray 3.2')
                    res = self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType), x)
                    if res < 0:
                        # print('setTypeArray 3.2.1')
                        return res
        return 1
    
                    
    def setType(self, typ, zObject):
        if type(zObject) is VarZcode:
            if (zObject.typ is None) or (type(zObject.typ) is type(typ)):
                zObject.typ = typ
                return zObject
        
        if type(zObject) is FuncZcode:
            if (zObject.typ is None) or (type(zObject.typ) is type(typ)):
                zObject.typ = typ
                return zObject
            
        return False
    
    
    def normalizeUtils(self, arr: ArrayType):
    # Base case
        if type(arr.eleType) is not ArrayType:
            return arr.size, arr.eleType
        
        return arr.size + self.normalizeUtils(arr.eleType)[0], self.normalizeUtils(arr.eleType)[1]

    def normalizeArrayType(self, arr: ArrayType):
        return ArrayType(self.normalizeUtils(arr)[0], self.normalizeUtils(arr)[1])
    
    
    def getLargestArray(self, eleList, param):
        pass
        # standard = self.visit(eleList[0], param)
        # for i in range(1, len(eleList)):
        #     ele = self.visit(eleList[i], param)
        #     if (type(standard) is VarZcode) and (type(ele) is ArrayZcode):
    
    
    
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
        # print('visitVarDecl')
        if ast.name.name in param[0]:
            raise Redeclared(Variable(), ast.name.name)
        
        if ast.varInit is not None:
            param[0][ast.name.name] = VarZcode(ast.varType)
            # print('visitVarDecl - visitLeft1')
            lhs = self.visit(ast.name, param)
            # print('visitVarDecl - visitRight')
            rhs = self.visit(ast.varInit, param)
            # print('visitVarDecl - visitLeft2')
            lhs = self.visit(ast.name, param)
            
            # Case 1: Both sides need infering
            if isinstance(lhs, Zcode) and (isinstance(rhs, Zcode) or isinstance(rhs, ArrayZcode)):
                # print('VarDecl 1')
                raise TypeCannotBeInferred(ast)           

            # Case 2:  LHS not need infering
            if (not isinstance(lhs, Zcode)) and isinstance(rhs, ArrayZcode):
                # print('VarDecl 2')
                if type(lhs) in [NumberType, BoolType, StringType]:
                    # print('VarDecl 2.1')
                    raise TypeMismatchInStatement(ast)
                
                if type(lhs) is ArrayType:
                    # print('VarDecl 2.2')
                    res = self.setTypeArray(self.normalizeArrayType(lhs), rhs)
                    if res == -1:
                        # print('VarDecl 2.2.1')
                        raise TypeMismatchInStatement(ast)
                    if res == -2:
                        # print('VarDecl 2.2.2')
                        raise TypeMismatchInExpression(ast.varInit)

                    
                        
            
            # RHS infer type for LHS 
            # elif isinstance(lhs, Zcode) and (type(rhs) in [NumberType, BoolType, StringType, ArrayType]): # Can remove the 'and ...' because we have check for rhs in the first if 
            elif isinstance(lhs, Zcode):
                lhs.typ = rhs
                # lhs = self.visit(ast.name.name, param)
            
            # LHS infer type for RHS
            elif isinstance(rhs, Zcode):
                rhs.typ = lhs
                # rhs = self.visit(ast.varInit, param)
            
            # Both sides not need infer type
            elif (type(lhs) in [NumberType, BoolType, StringType, ArrayType]) \
            and (type(rhs) in [NumberType, BoolType, StringType, ArrayType]):
                if not self.compareType(lhs, rhs):
                    raise TypeMismatchInStatement(ast)
            
        else:
            param[0][ast.name.name] = VarZcode(ast.varType)
        
        # print('param:   ', param)

    
    # name: Id
    # param: List[VarDecl]  # empty list if there is no parameter
    # body: Stmt = None  # None if this is just a declaration-part
    def visitFuncDecl(self, ast:FuncDecl, param):
        # print('visitFuncDecl')
        method = self.funcList.get(ast.name.name)
        # print(self.funcList)
        
        # Build paramList and paramType
        paramList = {}
        paramType = []
        for x in ast.param:
            if x.name.name in paramList:
                # print('FuncDecl 1')
                raise Redeclared(Parameter(), x.name.name)
            
            paramList[x.name.name] = VarZcode(x.varType)
            paramType.append(x.varType)

        
        
        self.returnStmt = False
        self.function = None
        
        # Redeclared function
        if method:
            if method.body:
                # print('FuncDecl 2')
                raise Redeclared(Function(), ast.name.name)
            else:
                # print('FuncDecl 3')
                if not (ast.body and len(paramType) == len(method.param) \
                and not (False in [type(paramType[i]) is type(method.param[i]) for i in range(len(paramType))])):
                    # print('FuncDecl 3.1')
                    raise Redeclared(Function(), ast.name.name)
        
        
        if ast.body is None:
            self.funcList[ast.name.name] = FuncZcode(paramType, None, False)        
        else:
            inferedType = None
            if method:
                inferedType = method.typ
                method.body = True
                self.function = method
            else:
                self.funcList[ast.name.name] = FuncZcode(paramType, None, True)
                self.function = self.funcList[ast.name.name]
                

            self.visit(ast.body, ([paramList] + param) if (type(ast.body) is Block) else ([{}] + [paramList] + param))
            
            if not self.returnStmt:
                self.function.typ = VoidType()
            
            if inferedType and (type(inferedType) is not type(self.function.typ)):
                raise TypeMismatchInStatement(Return(None))
                 
    
    
    # ====================================================================================================================
    
    # op: str
    # left: Expr
    # right: Expr
    def visitBinaryOp(self, ast:BinaryOp, param):
        left = self.visit(ast.left, param)
        if isinstance(left, Zcode):
            left = self.setType(self.binaryInput[ast.op], left).typ
        
        right = self.visit(ast.right, param)
        if isinstance(right, Zcode):
            right = self.setType(self.binaryInput[ast.op], right).typ
            
        if  (ast.op in self.binaryInput) \
        and (type(left) is type(self.binaryInput[ast.op])) \
        and (type(right) is type(self.binaryInput[ast.op])):
            return self.binaryOutput[ast.op]
        
        raise TypeMismatchInExpression(ast)
    
    
    # op: str
    # operand: Expr
    def visitUnaryOp(self, ast, param):
        # print('visitUnaryOp')
        right = self.visit(ast.operand, param)
        
        if isinstance(right, Zcode):
            right = self.setType(self.unaryInput[ast.op], right).typ
        
        # print(ast.op)
        # print((type(right) is type(self.unaryInput[ast.op])))
        if  (ast.op in self.unaryInput) and (type(right) is type(self.unaryInput[ast.op])): 
            return self.unaryOutput[ast.op]
        
        raise TypeMismatchInExpression(ast)

    
    # name: Id
    # args: List[Expr]
    def visitCallExpr(self, ast, param):
        # print('visitCallExpr')
        method = self.funcList.get(ast.name.name)
        
        if not method:
            # print('CallExpr 1')
            raise Undeclared(Function(), ast.name.name)
        
        if type(method.typ) is VoidType:
            # print('CallExpr 2')
            raise TypeMismatchInExpression(ast)
        
        if len(ast.args) != len(method.param):
            # print('CallExpr 3')
            raise TypeMismatchInExpression(ast)
        
        
        args = [self.visit(arg, param) for arg in ast.args]
        for i in range(len(args)):
            x = method.param[i] # x always have primitive types
            y = args[i]  
            
            
            if (not (isinstance(y, Zcode) or isinstance(y, ArrayZcode))):
                if (type(y) is not type(x)):
                    # print('CallExpr 4')
                    raise TypeMismatchInExpression(ast)
            
            if isinstance(y, Zcode):
                # print('CallExpr 5')
                y = self.setType(x, y).typ
                
            elif isinstance(y, ArrayZcode) and (self.setTypeArray(self.normalizeArrayType(x), y) <= 0):
                # print('CallExpr 6')
                raise TypeMismatchInExpression(ast)
        
            
        return method.typ if method.typ else method


    
    # ====================================================================================================================
    
    # stmt: List[Stmt]  # empty list if there is no statement in block
    def visitBlock(self, ast, param):
        # print('visitBlock')
        # print('blockparam: ', param)
        block_param = [{}] + param
        for x in ast.stmt:
            self.visit(x, ([{}] + block_param) if (type(x) is Block) else block_param)
    
    
    # expr: Expr
    # thenStmt: Stmt
    # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
    # elseStmt: Stmt = None  # None if there is no else branch
    def visitIf(self, ast, param):
        # print('visitIf')
        # If stmt
        cond = self.visit(ast.expr, param)
        if isinstance(cond, Zcode):
            # print('If 1')
            cond = self.setType(BoolType(), cond).typ
            
        if type(cond) is not BoolType:
            # print('If 2')
            raise TypeMismatchInStatement(ast)
        
        # ThenStmt
        self.visit(ast.thenStmt, param)
        
        # ElifStmt
        for (elifExpr, elifStmt) in ast.elifStmt:
            cond = self.visit(elifExpr, param)
            
            if isinstance(cond, Zcode):
                cond = self.setType(BoolType(), cond).typ
            if type(cond) is not BoolType:
                raise TypeMismatchInStatement(ast)
            
            self.visit(elifStmt, param)
        
        # ElseStmt
        if ast.elseStmt:
            self.visit(ast.elseStmt, param)
    
    
    # name: Id
    # condExpr: Expr
    # updExpr: Expr
    # body: Stmt
    def visitFor(self, ast, param):
        # index
        i = self.visit(ast.name, param)
        if isinstance(i, Zcode):
            i = self.setType(NumberType(), i).typ
        if type(i) is not NumberType:
            raise TypeMismatchInStatement(ast)
        
        # condExpr
        cond = self.visit(ast.condExpr, param)
        if isinstance(cond, Zcode):
            cond = self.setType(BoolType(), cond).typ
        if type(cond) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        # upExpr
        updExpr = self.visit(ast.updExpr, param)
        if isinstance(updExpr, Zcode):
            updExpr = self.setType(NumberType(), updExpr).typ
        if type(updExpr) is not NumberType:
            raise TypeMismatchInStatement(ast)
        
        # body
        self.inLoop += 1    # 1 go in Loop
        self.visit(ast.body, param)
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
        
        
        # Case 1: not sure: func foo() begin if a then return k else return 1
            # Can we from 1 infer a then infer func ?
        if (isinstance(funcType, Zcode) or isinstance(funcType, ArrayZcode)) \
        and (isinstance(retType, Zcode) or isinstance(retType, ArrayZcode)):
            # print("return 1")
            raise TypeCannotBeInferred(ast)

        # Case 2: retType is ArrayZcode and can be infered by funcType
        if (not (isinstance(funcType, Zcode) or isinstance(funcType, ArrayZcode)))\
        and (isinstance(retType, ArrayZcode)):
            if type(funcType) in [NumberType, StringType, BoolType]:
                raise TypeMismatchInStatement(ast)
            
            # funcType is arraytype
            if self.setTypeArray(self.normalizeArrayType(funcType), retType) <= 0:
                raise TypeMismatchInStatement(ast)

        # Case 3: funcType need infering from retType
        elif isinstance(funcType, Zcode):
            funcType.typ = retType
            # print("return 3")
        
        # Case 4: retType need infering from funcType
        elif isinstance(retType, Zcode):
            retType.typ = funcType
            # print("return 4")

        # Case 4: No need infering
        elif not self.compareType(funcType, retType):
            raise TypeMismatchInStatement(ast)
    
    
    # lhs: Expr
    # rhs: Expr
    def visitAssign(self, ast, param):
        # ...
        lhs = self.visit(ast.lhs, param)  # You can comment this line for checking
        rhs = self.visit(ast.rhs, param)
        lhs = self.visit(ast.lhs, param)
        
        # Case 1: Both side can not be infered
        if (isinstance(lhs, Zcode) or isinstance(lhs, ArrayZcode)) \
        and (isinstance(rhs, Zcode) or isinstance(rhs, ArrayZcode)):
            # print('Assign 1')
            raise TypeCannotBeInferred(ast)
        
        # Case 2: rhs is ArrayZcode and can be infered by lhs
        if not (isinstance(lhs, Zcode) or isinstance(lhs, ArrayZcode))\
        and (isinstance(rhs, ArrayZcode)):
            if type(lhs) in [NumberType, StringType, BoolType]:
                # print('Assign 2.1')
                raise TypeMismatchInStatement(ast)
            
            # lhs is arraytype
            if self.setTypeArray(self.normalizeArrayType(lhs), rhs) <= 0:
                # print('Assign 2.2')
                raise TypeMismatchInStatement(ast)
            # print('Assign 2.3')

        # Case 3: lhs need infering from rhs
        elif isinstance(lhs, Zcode):
            lhs.typ = rhs
            # print('Assign 3')
        
        # Case 4: lhs need infering from rhs
        elif isinstance(rhs, Zcode):
            rhs.typ = lhs
            # print('Assign 4')

        # Case 5: No need infering
        elif not self.compareType(lhs, rhs):
            # print('Assign 5')
            raise TypeMismatchInStatement(ast)
    
    
    # name: Id
    # args: List[Expr]  # empty list if there is no argument
    def visitCallStmt(self, ast, param):
        # print('visitCallStmt')
        method = self.funcList.get(ast.name.name)
        
        # if (method is None) or (method and ast.name.name in param[0]):
        if not method:
            raise Undeclared(Function(), ast.name.name)
        
        # print('visitCallStmt')
        method = self.funcList.get(ast.name.name)
        
        if method is None:
            # print('CallStmt 1')
            raise Undeclared(Function(), ast.name.name)
        
        if (method.typ is None):
            method = self.setType(VoidType(), method)
        
        if type(method.typ) is not VoidType:
            # print('CallStmt 2')
            raise TypeMismatchInStatement(ast)
        
        if len(ast.args) != len(method.param):
            # print('CallStmt 3')
            raise TypeMismatchInStatement(ast)
        
        args = [self.visit(arg, param) for arg in ast.args]
        for i in range(len(args)):
            x = method.param[i] # x always have primitive types
            y = args[i]  
            
            if (not (isinstance(y, Zcode) or isinstance(y, ArrayZcode))) \
            and (not self.compareType(x, y)):
                # print('CallStmt 4')
                raise TypeMismatchInStatement(ast)
            
            if isinstance(y, Zcode):
                y = self.setType(x, y).typ
                
            elif isinstance(y, ArrayZcode) and (self.setTypeArray(x, y) <= 0):
                # print('CallStmt 5')
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
    
    
    # value: List[Expr]
    def visitArrayLiteral(self, ast, param):
        # print('visitArrayLiteral', ast.value)
            
        typ = None
        # Get the 1st ele has primitive type
        for x in ast.value:
            ele = self.visit(x, param)
            if not (isinstance(ele, Zcode) or isinstance(ele, ArrayZcode)):
                typ = ele
                break
        
        if typ is None: # There is no primitive type
            # print('arrayLiteral 1.0')
            return ArrayZcode([self.visit(x, param) for x in ast.value])
        
        elif type(typ) in [StringType, BoolType, NumberType]:
            # print('arrayLiteral 2.0')
            for x in ast.value:
                ele = self.visit(x, param)
                
                if isinstance(ele, Zcode):
                    if not self.setType(typ, ele):
                        # print('arrayLiteral 2.1')
                        raise TypeMismatchInExpression(ast)
                
                if (type(ele) in [ArrayZcode, ArrayType]) or (not self.compareType(typ, ele)):
                    # print('arrayLiteral 2.2')
                    raise TypeMismatchInExpression(ast)
                
            return ArrayType([len(ast.value)], typ)
        
        else: # typ is arrayType
            # print('arrayLiteral 3.0')
            for x in ast.value:
                ele = self.visit(x, param)
                
                # print(type(ele))
                if (type(ele) not in [ArrayZcode, ArrayType]) and (not isinstance(ele, Zcode)):
                    # raise TypeMismatchInExpression(self.ast[0])
                    # print('arrayLiteral 3.1')
                    raise TypeMismatchInExpression(ast)
                
                if isinstance(ele, Zcode):
                    ele = self.setType(typ, ele).typ
                    
                elif type(ele) is ArrayZcode:
                    if self.setTypeArray(self.normalizeArrayType(typ), ele) <= 0:
                        # print('arrayLiteral 3.2')
                        raise TypeMismatchInExpression(ast)
                
                elif not self.compareType(typ, ele):
                    # print('arrayLiteral 3.2')
                    raise TypeMismatchInExpression(ast)
            
            return ArrayType([len(ast.value)], typ)

    
    # name: str+
    def visitId(self, ast, param):
        # print('visitId')
        for block in param:
            if ast.name in block:
                if block[ast.name].typ:
                    return block[ast.name].typ
                return block[ast.name]
               
        raise Undeclared(Identifier(), ast.name)
    
    
    # arr: Expr
    # idx: List[Expr]
    def visitArrayCell(self, ast, param):
        # print('visitArrayCell')
        arr = self.visit(ast.arr, param)
        # print(type(arr))
        
        if type(arr) is not ArrayType:
            # print('ArrayCell 1')
            raise TypeMismatchInExpression(ast)
        
        for x in ast.idx:
            idx = self.visit(x, param)
            
            if type(idx) in [VarZcode, FuncZcode]:
                idx = self.setType(NumberType(), idx).typ
                if not idx:
                    raise TypeMismatchInExpression(ast)
            
            if type(idx) is not NumberType:
                # print('ArrayCell 3')
                raise TypeMismatchInExpression(ast)
        
        if len(arr.size) < len(ast.idx):
            # print('ArrayCell 4')
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


