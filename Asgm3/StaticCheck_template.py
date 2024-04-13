from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class StaticChecker(BaseVisitor, Utils):
    
    def visitProgram(self, ast, param):
        for i in ast.decl: self
        pass 
    
    # decl: List[Decl]
    def visitProgram(self, ast, param):
        for i in ast.decl:
            self.visit(i, param)
        

    # name: Id
    # varType: Type = None  # None if there is no type
    # modifier: str = None  # None if there is no modifier
    # varInit: Expr = None  # None if there is no initial
    def visitVarDecl(self, ast, param):
        pass

    
    # name: Id
    # param: List[VarDecl]  # empty list if there is no parameter
    # body: Stmt = None  # None if this is just a declaration-part
    def visitFuncDecl(self, ast, param):
        pass

    
    def visitNumberType(self, ast, param):
        pass


    def visitBoolType(self, ast, param):
        pass


    def visitStringType(self, ast, param):
        pass
    
    
    # size: List[float]
    # eleType: Type
    def visitArrayType(self, ast, param):
        pass

        
    # op: str
    # left: Expr
    # right: Expr
    def visitBinaryOp(self, ast, param):
        pass
    
    
    # op: str
    # operand: Expr
    def visitUnaryOp(self, ast, param):
        pass

    
    # name: Id
    # args: List[Expr]
    def visitCallExpr(self, ast, param):
        pass

    
    # name: str
    def visitId(self, ast, param):
        pass
    
    
    # arr: Expr
    # idx: List[Expr]
    def visitArrayCell(self, ast, param):
        pass
    
    
    # stmt: List[Stmt]  # empty list if there is no statement in block
    def visitBlock(self, ast, param):
        pass
    
    
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
        pass
    
    
    def visitContinue(self, ast, param):
        pass

    
    def visitBreak(self, ast, param):
        pass
    
    
    def visitReturn(self, ast, param):
        pass
    
    
    # lhs: Expr
    # exp: Expr
    def visitAssign(self, ast, param):
        pass
    
    
    # name: Id
    # args: List[Expr]  # empty list if there is no argument
    def visitCallStmt(self, ast, param):
        pass
    
    
    # value: float
    def visitNumberLiteral(self, ast, param):
        pass
    
    
    # value: bool
    def visitBooleanLiteral(self, ast, param):
        pass
    
    
    # value: str
    def visitStringLiteral(self, ast, param):
        pass
    
    
    # value: List[Expr]
    def visitArrayLiteral(self, ast, param):
        pass
