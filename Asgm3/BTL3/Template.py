from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode:
    pass

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    


class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast, ):
        self.ast = ast
        self.BlockFor = 0
        self.function = None
        self.io = [{
                "readNumber" : FuncZcode([], NumberType(), True),
                "readBool" : FuncZcode([], BoolType(), True),
                "readString" : FuncZcode([], StringType(), True),
                "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
                "writeBool" : FuncZcode([BoolType()], VoidType(), True),
                "writeString" : FuncZcode([StringType()], VoidType(), True)
                }]
        
    def check(self):
        self.visit(self.ast, self.io)
        return "successful"    
    
    def comparType(self, LHS, RHS):
        #TODO: so sánh 2 biến type, kiểm tra array type sẽ kiểm tra size và eletype    
    

    def comparListType(self, LHS, RHS):
        #TODO: so sánh 2 list type, kiểm tra về độ dài và thứ tự của type trong đó    
    
    
    def visitProgram(self, ast, param):
        #! duyệt qua các biến và hàm toàn cục
        for i in ast.decl: self.visit(i, param)
        
        #TODO check No definition for a function in param
 
            
        #TODO  check No entry point in param


    def visitVarDecl(self, ast, param):
        #TODO kiểm tra name có trong param[0] hay không nén ra lỗi Redeclared 

    
    
        param[0][ast.name.name] = VarZcode(ast.varType) #! cập nhật param mới
        #! phần này xử lí nhiều hơn ở task2
        if ast.varInit: self.visit(ast.varInit, param)
        return param

    def visitFuncDecl(self, ast, param):
        #TODO kiểm tra name có trong param[0] hay không nén ra lỗi Redeclared 
        

        #TODO kiểm tra Param trong hàm
        listParam = {} #! dạng Dict có name
        typeParam = [] #! dạng mảng không cần name

        
        
        #TODO chia làm 3 TH
        #* trường hợp 1 là method đã so sẵn nghĩa là được khai báo 1 phần trước yêu cầu kiểm tra 2 list có giống nhau không nếu không nén ra Redeclared
        #* TH 2: là khai báo 1 phần ast.body is None
        #* TH 3: là khai báo toàn bộ 
        

        #! nếu không có type khi duyệt qua body thì là voidtype
        if param[0][ast.name.name].typ is None:
            param[0][ast.name.name].typ = VoidType()
        return param

    def visitId(self, ast, param):
        #TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared


    def visitCallStmt(self, ast, param):
        #TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared


    def visitCallExpr(self, ast, param):
        #TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared
    


    def visitBlock(self, ast, param):
        for item in ast.stmt:
            #! trường hợp gặp block
            if type(item) is Block: self.visit(item, [{}] + param)
            else: self.visit(item, param)


    def visitFor(self, ast, param):
        self.BlockFor += 1 #! vào trong vòng for nào anh em
        self.visit(ast.body, [{}] + param)
        self.BlockFor -= 1 #! cút khỏi vòng for nào anh em
        
    def visitContinue(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)


    def visitNumberType(self, ast, param): return ast
    def visitBoolType(self, ast, param): return ast
    def visitStringType(self, ast, param): return ast
    def visitArrayType(self, ast, param): return ast
    def visitNumberLiteral(self, ast, param): return NumberLiteral()
    def visitBooleanLiteral(self, ast, param): return BooleanLiteral()
    def visitStringLiteral(self, ast, param): return StringLiteral()
    def visitArrayLiteral(self, ast, param):
        pass

    def visitBinaryOp(self, ast, param):
        pass

    def visitUnaryOp(self, ast, param):
        pass

    def visitArrayCell(self, ast, param):
        pass

    def visitIf(self, ast, param):
        pass

    def visitAssign(self, ast, param):
        pass

    def visitReturn(self, ast, param):
        pass


