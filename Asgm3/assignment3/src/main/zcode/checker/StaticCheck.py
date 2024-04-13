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
    #* typ : Type có thể là number, bool, string, arrayType or None (có thể hiểu nhanh đang FuncZcode)
        #! -> nên khi gọi callFunc thì trả về typ nếu có (khác None) không thì trả về chính nó this (VarZcode)    
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
        self.inBlockFor = 0
        self.func = None
        self.returnStmt = False
        self.listFunction = {
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
        allowedType = [NumberType, StringType, BoolType, ArrayType, VoidType]
        
        if type(LHS) not in allowedType or type(RHS) not in allowedType:
            return False
        
        if (type(LHS) is ArrayType) and (type(RHS) is ArrayType):
            if ((LHS.size == RHS.size) and (type(LHS.eleType) is type(RHS.eleType))):
                return True
            return False
        
        return True if (type(LHS) is type(RHS)) else False   
    
    
    def compareListType(self, LHS, RHS):
        allowedType = [NumberType, StringType, BoolType, ArrayType, VoidType]
        
        
        if LHS.size != RHS.size:
            return False        
        
        if (LHS.eleType != RHS.eleType) \
            or (type(LHS.eleType) not in allowedType) \
            or (type(RHS.eleType) not in allowedType):
            return False

        
        if type(LHS.eleType) is ArrayType:
            return self.compareListType(LHS.eleType, RHS.eleType)
        return True
        
        
    
    
    def setTypeArray(self, typeArray, typeArrayZcode):
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
    def visitProgram(self, ast, param):
        for i in ast.decl:
            self.visit(i, param)
        

    # name: Id
    # varType: Type = None  # None if there is no type
    # modifier: str = None  # None if there is no modifier
    # varInit: Expr = None  # None if there is no initial
    def visitVarDecl(self, ast, param):
        if ast.name in param[0]:
            raise Redeclared(Variable(), ast.name)

        
        param[0][ast.name] = VarZcode(ast.varType)
        
        if ast.varInit != None:
            rhs = self.visit(ast.varInit)
            lhs = self.visit(ast.name)
            
            if isinstance(lhs, Zcode) and \
            (isinstance(rhs, Zcode) or isinstance(rhs, ArrayZcode)):
                raise TypeCannotBeInferred(ast)           

            
            if (not isinstance(lhs, Zcode)) and isinstance(rhs, ArrayZcode):
                if type(lhs) in [NumberType, BoolType, StringType]:
                    raise TypeMismatchInStatement(ast)
                
                if type(lhs) is ArrayType:
                    if not self.setTypeArray(lhs, rhs):
                        raise TypeMismatchInStatement(ast)
            
            elif isinstance(lhs, Zcode) and (type(rhs) in [NumberType, BoolType, StringType]):
                lhs.typ = rhs
            
            elif (type(lhs) in [NumberType, BoolType, StringType]) and isinstance(rhs, Zcode):
                rhs.typ = lhs
            
            elif  (type(lhs) in [NumberType, BoolType, StringType, ArrayType]) \
            and (type(rhs) in [NumberType, BoolType, StringType, ArrayType]):
                if not self.compareType(lhs, rhs):
                    raise TypeMismatchInStatement(ast)
            
        else:
            pass
        
        
    
    # name: Id
    # param: List[VarDecl]  # empty list if there is no parameter
    # body: Stmt = None  # None if this is just a declaration-part
    def visitFuncDecl(self, ast, param):
        method = self.listFunction.get(ast.name)
        
        # Build paramList and paramType
        paramList = {}
        paramType = []
        for x in param:
            if x.name in paramList:
                raise Redeclared(Variable(), x.name)
            
            paramList[x.name] = self.visit(x)
            paramType.append(paramList[x.name].typ)

        
        self.returnStmt = False
        
        if ast.body is None:
            pass
        
        if  method:
            pass
        
        else:
            pass
    
    
    
    
     
    # op: str
    # left: Expr
    # right: Expr
    def visitBinaryOp(self, ast, param):
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
               
        raise Undeclared(ast)
    
    
    # arr: Expr
    # idx: List[Expr]
    def visitArrayCell(self, ast, param):
        arr = self.visit(ast.arr, param)
        if type(arr) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        
        # ...
        
        
    
    
    # stmt: List[Stmt]  # empty list if there is no statement in block
    def visitBlock(self, ast, param):
        for x in ast.stmt:
            if type(x) is Block:
                self.visit(x, [{}] + param)
            else:
                self.visit(x, param)
    
    
    # expr: Expr
    # thenStmt: Stmt
    # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
    # elseStmt: Stmt = None  # None if there is no else branch
    def visitIf(self, ast, param):
        pass
    
    
    # name: Id
    # condExpr: Expr
    # updExpr: Expr
    # body: Stmt
    def visitFor(self, ast, param):
        self.inBlockFor = 1
        
        
        
        self.inBlockFor = 0
    
    
    def visitContinue(self, ast, param):
        if self.inBlockFor == 0:
            raise MustInLoop(ast)

    
    def visitBreak(self, ast, param):
        if self.inBlockFor == 0:
            raise MustInLoop(ast)  
    
    
    def visitReturn(self, ast, param):
        pass
    
    
    # lhs: Expr
    # exp: Expr
    def visitAssign(self, ast, param):
        rhs = self.visit(ast.exp, param)
        lhs = self.visit(ast.lhs, param)
        
        if (isinstance(lhs, Zcode) or isinstance(lhs, ArrayZcode)) \
        and (not (isinstance(rhs, Zcode) or isinstance(rhs, ArrayZcode))) :
            lhs.typ = rhs
        
        if (isinstance(rhs, Zcode) or isinstance(rhs, ArrayZcode)) \
        and (not (isinstance(lhs, Zcode) or isinstance(lhs, ArrayZcode))) :
            rhs.typ = lhs # ???
        
        if not self.compareType(lhs, rhs):
            raise TypeMismatchInStatement(ast)
        
        # ...
        
        
    
    # name: Id
    # args: List[Expr]  # empty list if there is no argument
    def visitCallStmt(self, ast, param):
        pass
    
    
    # value: float
    def visitNumberLiteral(self, ast, param):
        return NumberType()
    
    
    # value: bool
    def visitBooleanLiteral(self, ast, param):
        return BoolType() 
    
    
    # value: str
    def visitStringLiteral(self, ast, param):
        return StringType()
    
    
    # value: List[Expr]
    def visitArrayLiteral(self, ast, param):
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
            
    
    def visitNumberType(self, ast, param):
        return ast


    def visitBoolType(self, ast, param):
        return ast


    def visitStringType(self, ast, param):
        return ast
    
    
    # size: List[float]
    # eleType: Type
    def visitArrayType(self, ast, param):
        return ast


