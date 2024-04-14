from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce







class Zcode(Type): pass    # Type that not be infered 

class FuncZcode(Zcode):
    def __init_(self, param = [], typ = None, body = False):
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
        # List[Type] (Type = {Zcode, ArrayZcode, String, bool, number, arraytype})
        self.eleType = eleType  






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
    
    # Helper functions --------------------------------------------------------------------------------
    
    def check(self):
        self.visit(self.ast, [{}])
        return None
    
    
    def compareType(self, LHS, RHS):
        allowedType = [NumberType, StringType, BoolType, VoidType, ArrayType]
        
        if type(LHS) not in allowedType or type(RHS) not in allowedType:
            return False
        
        if (type(LHS) is ArrayType) and (type(RHS) is ArrayType):
            if ((LHS.size == RHS.size) and (type(LHS.eleType) is type(RHS.eleType))):
                return True
            return False
        
        return True if (type(LHS) is type(RHS)) else False   
    
    
    # ... Chua hieu muc dich ham 
    def compareListType(self, LHS, RHS):
        allowedType = [NumberType, StringType, BoolType, VoidType, ArrayType]
        
        
        if LHS.size != RHS.size:
            return False        
        
        if (LHS.eleType != RHS.eleType) \
            or (type(LHS.eleType) not in allowedType) \
            or (type(RHS.eleType) not in allowedType):
            return False

        
        if type(LHS.eleType) is ArrayType:
            return self.compareListType(LHS.eleType, RHS.eleType)
        
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
                # Chua hieu dung cho TH nao
                if isinstance(x, Zcode):
                    x.typ = typeArray.eleType
                
                # number x[2][2] = [y, [6, 9]] --> y is number[2]
                if type(x) is ArrayZcode:
                    # self.setTypeArray(ArrayType(typeArray.size[1:], ...), x)
                    pass
                    
                    
                
        
    
    
    # Main visit functions ----------------------------------------------------------------------------
   
    # decl: List[Decl]
    def visitProgram(self, ast:Program, param):
        for i in ast.decl:
            self.visit(i, param)
        

    # name: Id
    # varType: Type = None  # None if there is no type
    # modifier: str = None  # None if there is no modifier
    # varInit: Expr = None  # None if there is no initial
    def visitVarDecl(self, ast:VarDecl, param):
        if ast.name in param[0]:
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
        
        # Build paramList and paramType
        paramList = {}
        paramType = []
        for x in ast.param:
            if x.name.name in paramList:
                raise Redeclared(Variable(), x.name.name)
            
            paramList[x.name.name] = VarZcode(x.varType)
            paramType.append(x.varType)

        
        
        self.returnStmt = False

        # Redeclared function
        if method and not (not method.body and ast.body):
            raise Redeclared(Function(), ast.name.name)
        
                
        if ast.body is None:
            self.funcList[ast.name.name] = FuncZcode(paramType, VoidType(), False)        
        else:
            if method:
                method.body = True
                self.function = method
            else:
                self.function = self.funcList[ast.name.name] = FuncZcode(paramType, None, False)
                
            self.visit(ast.body, [paramList] + param)
            if not self.Return:
                method.typ = VoidType()

        
        self.function = None
        self.returnStmt = False
        
    
    
    # op: str
    # left: Expr
    # right: Expr
    def visitBinaryOp(self, ast:BinaryOp, param):
        left = self.visit(ast.left, param)
        right = self.visit(ast.right, param)
        
        if isinstance(left, Zcode):
            left = self.binaryInput[ast.op]
            
        if isinstance(right, Zcode):
            right = self.binaryInput[ast.op]
            
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
            right = self.unaryInput[ast.op]
        
        if  (ast.op in self.unaryInput) and (type(right) is self.unaryInput[ast.op]): 
            return self.unaryOutput[ast.op]
        
        raise TypeMismatchInExpression(ast)
        # ...

    
    # name: Id
    # args: List[Expr]
    def visitCallExpr(self, ast, param):
        pass

    
    # name: str
    def visitId(self, ast, param):
        for block in param:
            if ast.name in block:
                if isinstance(block[ast.name], Zcode):
                    return block[ast.name].typ
                
                if isinstance(block[ast.name], ArrayZcode):
                    # return ... 
                    pass
                
                return block[ast.name]
               
        raise Undeclared(ast, ast.name)
    
    
    # arr: Expr
    # idx: List[Expr]
    def visitArrayCell(self, ast, param):
        arr = self.visit(ast.arr, param)
        
        if type(arr) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        
        for x in ast.idx:
            idx = self.visit(x, param)
            if type(idx) is not NumberType:
                raise TypeMismatchInExpression(ast)
        
        if len(arr.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        
        if len(arr.size) == len(ast.idx):
            return arr.eleType
        
        if len(arr.size) > len(ast.idx):
            return ArrayType(arr.size[len(ast.idx):], arr.eleType)
        
        
        
        # ...
        
        
    
    
    # stmt: List[Stmt]  # empty list if there is no statement in block
    def visitBlock(self, ast, param):
        for x in ast.stmt:
            self.visit(x, param if type(x) is Block else [{}] + param)
    
    
    # expr: Expr
    # thenStmt: Stmt
    # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
    # elseStmt: Stmt = None  # None if there is no else branch
    def visitIf(self, ast, param):
        cond = self.visit(ast.expr, param)
        if type(cond) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, [{}] + param)
        
        for (elifExpr, elifStmt) in ast.elifStmt:
            cond = self.visit(elifExpr, param)
            if type(cond) is not BoolType:
                raise TypeMismatchInStatement(ast)
            
            self.visit(elifStmt, [{}] + param)
            
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, [{}] + param)
    
    
    # name: Id
    # condExpr: Expr
    # updExpr: Expr
    # body: Stmt
    def visitFor(self, ast, param):
        i = self.visit(ast.name, param)
        if type(i) is not NumberType:
            raise TypeMismatchInStatement(ast)
        
        cond = self.visit(ast.condExpr, param)
        if type(cond) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        updExpr = self.visit(ast.updExpr, param)
        if type(updExpr) is not NumberType:
            raise TypeMismatchInStatement(ast)
        
        
        self.inLoop += 1
        self.visit(ast.body, [{}] + param)
        self.inLoop -= 1
    
    
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
            # Can we from 1 infer a then infer func  
        if (isinstance(funcType, Zcode) or isinstance(funcType, ArrayZcode)) \
        and (isinstance(retType, Zcode) or isinstance(retType, ArrayZcode)):
            raise TypeCannotBeInferred(ast)

        # Case 2: retType is ArrayZcode and can be infered by funcType
        if not (isinstance(funcType, Zcode) or isinstance(funcType, ArrayZcode))\
        and (isinstance(retType, ArrayZcode)):
            if type(funcType) in [NumberType, StringType, BoolType]:
                raise TypeMismatchInStatement(ast)
            
            # funcType is arraytype
            if not self.setTypeArray(funcType, retType):     
                raise TypeMismatchInStatement(ast)
     
        elif isinstance(funcType, Zcode):
            funcType.typ = retType
        
        elif isinstance(retType, Zcode):
            retType.typ = funcType

        elif not self.compareType(funcType, retType):
            raise TypeMismatchInStatement(ast)
        
        
    # lhs: Expr
    # exp: Expr
    def visitAssign(self, ast, param):
        rhs = self.visit(ast.exp, param)
        lhs = self.visit(ast.lhs, param)
        
        # Case 1: both side can not be infered
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
     
        elif isinstance(lhs, Zcode):
            lhs.typ = rhs
        
        elif isinstance(rhs, Zcode):
            rhs.typ = lhs

        elif not self.compareType(lhs, rhs):
            raise TypeMismatchInStatement(ast)
        
    
    # name: Id
    # args: List[Expr]  # empty list if there is no argument
    def visitCallStmt(self, ast:CallStmt, param):
        pass
    
    
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
    def visitArrayLiteral(self, ast:ArrayLiteral, param):
        typ = None
        
        # Get the 1st ele has primitive type
        for x in ast.value:
            if not (isinstance(typ, Zcode) or isinstance(typ, ArrayZcode)):
                typ = self.visit(x, param)
                break
        
        if typ is None:
            # return ArrayZcode(..., ...)
            pass
        elif type(typ) in [StringType, BoolType, NumberType]:
            for x in ast.value:
                if type(x) in [ArrayZcode, ArrayType] or (not self.compareType(typ, x)):
                    raise TypeMismatchInExpression(ast)
                
                x.typ = typ
            # return ArrayType(..., typ)
        else:
            for x in ast.value:
                if type(x) in [StringType, BoolType, NumberType] or (not self.compareType(typ, x)):
                    raise TypeMismatchInExpression(ast)
                
                if type(x) is ArrayZcode:
                    self.setTypeArray(typ, x)
            
            # return ArrayType(..., self)
            
    
    def visitNumberType(self, ast:NumberType, param):
        return ast


    def visitBoolType(self, ast:BoolType, param):
        return ast


    def visitStringType(self, ast:StringType, param):
        return ast
    
    
    # size: List[float]
    # eleType: Type
    def visitArrayType(self, ast:ArrayType, param):
        return ast


