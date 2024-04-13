"""
^name : Võ Tiến
^FB : https://www.facebook.com/profile.php?id=100056605580171
^GROUP: https://www.facebook.com/groups/211867931379013/
^DAY : 10/4/2024
"""

"""
Kiến thức cần 
List : https://www.w3schools.com/python/python_lists.asp
Dict : https://www.w3schools.com/python/python_dictionaries.asp
isinstance() : https://www.w3schools.com/python/ref_func_isinstance.asp
"""

from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

"""
    * Type gồm
        * NumberType, BoolType, StringType
        * ArrayType : gồm size, eleType (NumberType, BoolType, StringType)
        * ArrayZcode : eleType chỉ bao gồm các type kiểu Zcode và ArrayZcode, typ chưa được suy diễn
        * Zcode : typ chưa được suy diễn cần xác định khi lần dùng đầu tiên
            *  FuncZcode : kiểu typ của hàm chưa suy diễn or có thể đã được suy diễn gồm
                ^ param : danh sách các biến cần truyền vào hàm được biểu diễn dưới dạng danh sách kiêu
                ^ typ : kiểu type của hàm hiện tại nếu typ là None thì hàm này chưa xác định kiểu ngược lại có typ thì đã xác định được kiểu
                ^ body : xem thử hàm khai báo trước 1 phần (nghĩa là không có body) hay không
            * VarZcode : kiểu typ của biến chưa được suy diễn or có thể đã được suy diễn
                ^ typ : kiểu type của hàm hiện tại nếu typ là None thì biến này chưa xác định kiểu ngược lại có typ thì đã xác định được kiểu
"""

class Zcode(Type):
    pass

class FuncZcode(Zcode):
    #* param : list[Type]
    #* typ : Type có thể là number, bool, string, arrayType or None (có thể hiểu nhanh đang FuncZcode)
        #! -> nên khi gọi callFunc thì trả về typ nếu có (khác None) không thì trả về chính nó this (FuncZcode)
    #* body : Bool nếu là true nghĩa là body đã có (khai báo toàn bộ có body hàm), nếu False nghĩa là khai báo 1 phần (khai báo không có body)
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body

class VarZcode(Zcode):
    #* typ : Type có thể là number, bool, string, arrayType or None (có thể hiểu nhanh đang FuncZcode)
        #! -> nên khi gọi callFunc thì trả về typ nếu có (khác None) không thì trả về chính nó this (VarZcode)    
    def __init__(self, typ = None):
        self.typ = typ    

class ArrayZcode(Type):
    #* eleType: List[Type]
    #* Type ở đây có thể là Zcode, ArrayZcode, String, bool, number, arraytype
    def __init__(self, eleType):
        self.eleType = eleType




class StaticChecker(BaseVisitor, Utils):
    #* ast : cây ở BTL2
    #* BlockFor : int, kiểm tra xem chúng ta đang ở trong vòng for thứ mấy
    #* function: FuncZcode, kiểm tra hàm hiện tại chúng ta đang vào body của nó checkStatic
    #* listFunction : Dict<string, FuncZcode>, Danh sách các hàm, ban đầu sẽ mặc định các hàm read, write file
    #* return : Bool, kiểm tra hàm hiện tại có return hay không nếu không có thì xác đinh hàm này là VoidType
    def __init__(self,ast):
        self.ast = ast 
        self.BlockFor = 0
        self.function = None
        self.Return = False
        self.listFunction = {
            "readNumber" : FuncZcode([], NumberType(), True),
            "readBool" : FuncZcode([], BoolType(), True),
            "readString" : FuncZcode([], StringType(), True),
            "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
            "writeBool" : FuncZcode([BoolType()], VoidType(), True),
            "writeString" : FuncZcode([StringType()], VoidType(), True)
        }
        
        
    def check(self):
        self.visit(self.ast, [{}])
        return None
    
    """_comparType_
        #* LHS và RHS chỉ có thể là Void, number, string, bool, arrayType
        #* TH1 nếu LHS và RHS đều là array
            #^ xét kích thước size có giống nhau không nếu không giống nhau trả False
            #^ xét từng phần tử trong size của 2 thằng nếu không giống nhau trả False
            #^ xét tiếp eleType nếu không giống nhau trả Flase
        #* TH2 nếu cả 2 không phải array -> so sánh type của 2 nó thôi      
    """
    def comparType(self, LHS, RHS):
        #TODO implement
    
    """_comparListType
        #* LHS và RHS chỉ có thể list các type sau Void, number, string, bool, arrayType
        #* TH1 nếu LHS và RHS khác kích thước -> False
        #* duyệt từng phần tử gọi self.comparType(LHS[i], RHS[i])
    """    
    def comparListType(self, LHS, RHS):
        #TODO implement
    
    def setTypeArray(self, typeArray, typeArrayZcode):
        #* Trường hợp size khác nhau
        if typeArray.size[0] != len(typeArrayZcode.eleType):
            return False
        
        #* trường hợp bên trong array là các kiểu nguyên thủy (array 1 chiều)
           #^ nếu typeArrayZcode.eleType[i] là Zcode : gán typeArrayZcode.eleType[i].typ = typeArray.eleType
           #^ nếu typeArrayZcode.eleType[i] là arrayZcode : trả về False (vì 1 chiều mà bắt gán 2 chiều :) )
        if len(typeArray.size) == 1:
            #TODO implement
        #* trường hợp bên trong array là các arrayType (array >= 2 chiều)
           #^ nếu typeArrayZcode.eleType[i] là Zcode : gán typeArrayZcode.eleType[i].typ = typeArray.eleType
           #^ nếu typeArrayZcode.eleType[i] là arrayZcode : gọi đệ quy self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType),typeArrayZcode[i]) để vào bên trong xem có lỗi gì không       
        else:
            #TODO implement

        
    
    def visitProgram(self, ast, param):
        #* duyệt qua các biến và hàm toàn cục
        for i in ast.decl: self.visit(i, param)
        
        """_NoDefinition_
            #TODO check No definition for a function in self.listFunction
            ví dụ 1 -> đúng
            func foo(number a)
            func foo(number a) return
            
            ví dụ 2 -> đúng
            func foo(number a) return
            
            ví dụ 3 -> sai NoDefinition
            func foo(number a)
        """
        #TODO implement

        """_NoEntryPoint_
            #TODO check No entry Point in listFunction, tìm hàm tên "main"
            ví dụ 1 -> đúng
            func main() return
            
            ví dụ 2 -> đúng
            func main()
            func main() begin
            end
            
            ví dụ 3 -> sai NoEntryPonumber, sai param
            func main(number a) return
            
            ví dụ 4 -> sai NoEntryPonumber, sai returnType
            func main() return 1       
            
            ví dụ 5 -> sai NoEntryPonumber, không tồn tại
            không có hàm main      
        """        
        #TODO implement

    def visitVarDecl(self, ast, param):
        """_Redeclared_
            #TODO kiểm tra name có trong param[0] hay không nén ra lỗi Redeclared
            ví dụ 1 -> đúng
            number a

            ví dụ 2 -> Redeclared(Variable(), ast.name.name)
            number a
            string a    

        """           
        #TODO implement
        param[0][ast.name.name] = VarZcode(ast.varType) #! cập nhật param mới đưa tên vào, biến dynamic hay var sẽ type = None
        
        
        """_TypeCannotBeInferred_TypeMismatchInStatement_
            # TODO kiểm tra TypeCannotBeInferred và TypeMismatchInStatement xử lí ast.varInit (nếu khác None)
            #* nguyên lí LHS (ast.varType) và RHS (ast.varInit), cả 2 đều là Type, chú ý LHS không bao giờ là ArrayZcode
                #^ TH1 cả 2 đều là Zcode chưa suy diễn được : raise TypeCannotBeInferred(ast)
                #^ TH2 nếu LHS là Zcode và RHS là ArrayZcode: raise TypeCannotBeInferred(ast) 
                #^ TH3 nếu LHS không phải Zcode và RHS là ArrayZcode:
                    #^ TH3.1 nếu LHS là string, bool, number : raise TypeMismatchInStatement(ast) 
                    #^ TH3.2 nếu LHS là arrayType kiểm tra self.setTypeArray(LHS, RHS) nếu không đúng raise TypeMismatchInStatement(ast)
                #^ TH4 nếu LHS là Zcode và RHS là string, bool, number, arrytype : LHS.typ = RHS
                #^ TH5 ngược lại TH4
                #^ TH6 cả LHS và RHS có kiểu string, bool, number, arrytype -> kiểm tra self.comparType(LHS, RHS): raise TypeMismatchInStatement(ast)
            
            #! TH1 TypeCannotBeInferred
            func foo()
            var a <- foo()    
            
            #! TH2 TypeCannotBeInferred(ast)
            dynamic x
            var a <- [x]
            
            #! TH3.1 TypeMismatchInStatement(ast)
            dynamic x
            number a <- [x] -> raise TypeMismatchInStatement(ast) 
            
            #! TH3.2 : X = arraytype([3], number)
            dynamic x
            number a[1][3] <- [x]
                        
            #! TH4, 5 : foo().typ = b.typ = numberType()
            func foo()
            number a <- foo()
            var b <- a            

            #! TH6 TypeMismatchInStatement
            number a <- "1"                
        """ 
        if ast.varInit:
            #TODO implement

    def visitFuncDecl(self, ast, param):
        """
            #TODO kiểm tra name có trong self.listFunction hay không nén ra lỗi Redeclared 
            ví dụ 1 -> đúng
            func foo() return

            ví dụ 2 -> đúng
            func foo()
            func foo() return
            
            ví dụ 3 -> Redeclared
            func foo() return
            func foo()

            ví dụ 4 -> Redeclared
            func foo()
            func foo()
            
            ví dụ 5 -> Redeclared
            func foo() return
            func foo() return
        """ 
        method = self.listFunction.get(ast.name.name)
        #TODO implement
        
        
        
        listParam = {} #! dạng Dict có name khi visit dùng self.visit(ast.body, [listParam] + param)
        typeParam = [] #! dạng mảng không cần name truyền agrc vào FuncZcode
        """
            # TODO kiểm tra ast.param trong hàm trong listParam giống phần vardecl
                #^ cập nhật listParam (giống prama) và typeParam (chỉ gồm các type)
                #^ typeParam = [numberType, stringType, ...], listParam dạng DICT giống param
            
            ví dụ 1 -> đúng 
            func foo(number a, string b) return  
            -> typeParam = [numberType, stringType], listParam = {'a' : VarZcode(numberType), 'b' : VarZcode(stringType}         
            
            ví dụ 2 -> Redeclared
            func foo(number a, string a) return
        """ 
        #TODO implement
        
        
        """
            # TODO kiểm tra self.function = method hàm hiện tại chuẩn bị vào body nó xử lí
                #^ TH1 : method khai báo 1 phần
                    #todo : cập nhật trong self.listFunction
            func foo()
            
                #^ TH2 : method đã khai bó 1 phần trước đó
                    #todo 1 : kiểm trả list param có giống nhau không không nếu không trả về Redeclared(Function(), ast.name.name)
                    #todo 2 : cập nhật self.listFunction[].body, self.Return, self.function và self.visit(ast.body, [listParam] + param) 
                    #todo 3 : sau khi gọi hàm kiểm tra self.Return có trong hàm hay không nếu không thì xác định typ nó VoidType, rồi xem xét với typ của hàm, nếu hàm cũng voidtype thì đúng nếu không thì lỗi  raise TypeMismatchInStatement(Return(None))
            func foo() 
            func foo() begin
            end
            
                #^ TH3 : method khai báo đầu đủ lần đầu không có khai báo 1 phần
                    #todo 1 : cập nhật self.listFunction[].body, self.Return, self.function, self.listFunction
                    #todo 2 : giống todo 3 trên
            func foo() begin 
            end
            
                #^ ví dụ todo 3 của TH2
            #! xác định kiểu
            func foo() begin 
            end     
            -> type foo là VoidType  
            
            #! xác định kiểu
            func foo()
            number a <- foo() -> foo() có typ là number
            func foo() begin  -> này lại có typ là void nên lỗi raise TypeMismatchInStatement(Return(None))
            end     
        
        """
        self.Return = False
        if ast.body is None:
            #todo: implement TH1

        if method:
            #todo: implement TH2

        else:
            #todo: implement TH3

        
  
        

    def visitId(self, ast, param):
        """
            # TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared
                #^ đối với giá trị trả về nếu Id.typ = None thì trả về chính nó luôn varZcode, nếu cso Id.typ thì trả về typ của nó
            VD 1:
            number b <- a -> Undeclared(Identifier(), 'a') 
            
            VD 2:
            number a
            number b <- a -> a đã có VarZcode.typ nên return VarZcode.typ

            VD 3:
            var a
            number b <- a -> a có VarZcode.typ = None nên return VarZcode              
        """
        #TODO implement

    def visitCallExpr(self, ast, param):
        """
            TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared
            VD 1: đúng 
            func foo()
            func main()begin
                var a <- foo()
            end
            
            VD 2: Undeclared
            func foo()
            func main()begin
                var a <- foo1()
            end
            
            VD 3: Undeclared
            func foo()
            func main()begin
                var foo <- 1
                var a <- foo()
            end
        """   
        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí ast.varInit nếu tồn tại
            ^ xét listLHS (là method.param) và listRHS (là ast.args)
                ^ nếu len khác nhau TypeMismatchInExpression
                ^ nếu self.comparType(LHS[i], RHS[i]) -> TypeMismatchInExpression
            ^ nếu FuncZcode.typ is None thì return FuncZcode
            ^ nếu comparType(FuncZcode.typ, VoidType()) -> TypeMismatchInExpression
            ^ còn lại return FuncZcode.typ (giống phần VarZcode)
        """   

        method = self.listFunction.get(ast.name.name)
        
        #TODO implement

    def visitCallStmt(self, ast, param):
        """như CallExpr chỉ khác ở chỗ not comparType(FuncZcode.typ, VoidType()) -> TypeMismatchInStatement"""
        method = self.listFunction.get(ast.name.name)
        #TODO implement

    def visitIf(self, ast, param):
        """_typExpr_
            # TODO giống phần kiểm tra TypeMismatchInStatement theo nguyên lí LHS và RHS
                #^ xét typExpr và self.visit(ast.thenStmt, [{}] + param)
            ^ LHS = BoolType(), RHS = self.visit(ast.expr, param)
        """   
        #TODO implement 
        
        """_elifStmt_
            #TODO giống trên, LHS = BoolType()
        """   
        #TODO implement
        
        """_elseStmt_
        """            
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, [{}] + param)
        
    def visitFor(self, ast, param):
        """_typID_
            #TODO giống mấy thằng trong if, LHS = NumberType()
        """        
        #TODO implement
        
        """_typCondExpr_
            #TODO giống mấy thằng trong if, LHS = BoolType()
        """    
        #TODO implement

        """_typUpdExpr_
            #TODO giống mấy thằng trong if, LHS = NumberType()
        """            
        #TODO implement       
        
        
        self.BlockFor += 1 #! vào trong vòng for nào anh em
        self.visit(ast.body, [{}] + param) #! tạo ra tầm vực mới
        self.BlockFor -= 1 #! cút khỏi vòng for nào anh em
    
    def visitReturn(self, ast, param):
        """
            # TODO kiểm tra TypeCannotBeInferred và TypeMismatchInStatement nguyên lí LHS và RHS
                #^ LHS là self.function.typ if self.function.typ else self.function
                #^ RHS là self.visit(ast.expr, param) if ast.expr else VoidType()
        """
        self.Return = True
        LHS = self.function.typ if self.function.typ else self.function
        RHS = self.visit(ast.expr, param) if ast.expr else VoidType()

        #TODO implement   

    def visitAssign(self, ast, param):
        """
            # TODO kiểm tra TypeCannotBeInferred và TypeMismatchInStatement nguyên lí LHS và RHS
        """
        LHS = self.visit(ast.lhs, param)
        RHS = self.visit(ast.rhs, param)

        #TODO implement
            
    def visitBinaryOp(self, ast, param):
        #! vì các Association đều là left nên tiến hành ở left rồi tiếp theo right, thầy mà cho có Association right thì trúng bẫy hết
        op = ast.op
        """_left_ 
            # TODO kiểm tra TypeCannotBeInferred và TypeMismatchInExpression nguyên lí LHS và RHS
            #! op in ['+', '-', '*', '/', '%']
                #^ LHS = NumberType(), left = self.visit(ast.left, param)
            #! op in ['=', '!=', '<', '>', '>=', '<=']
                #^ LHS = NumberType(), left = self.visit(ast.left, param)
            #! op in ['and', 'or']
                #^ LHS = boolType(), left = self.visit(ast.left, param)
            #! op in ['==']
                #^ LHS = StringType(), left = self.visit(ast.left, param)           
            #! op in ['...']
                #^ LHS = StringType(), left = self.visit(ast.left, param)  
        """        
        
        left = self.visit(ast.left, param)
        #TODO implement

        """_right_             
        """        
        right = self.visit(ast.right, param)
        #TODO implement
    

    def visitUnaryOp(self, ast, param):
        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí giống BinaryOp
            ^ '+', '-' -> kiểu numbertype -> return Numbertype
            ^ ['not'] -> kiểu booltype -> return booltype
        """       
        right = self.visit(ast.operand, param)
        op = ast.op
        #TODO implement       
            

    def visitArrayCell(self, ast, param):
        """
            TODO kiểm tra TypeMismatchInExpression
            ^ Phần type ast.arr phải là array type nếu không lỗi TypeMismatchInExpression
        """ 
        left = self.visit(ast.arr, param)
        if type(left) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        
        """
            # TODO kiểm tra TypeMismatchInExpression
            ^ từng phần tử trong ast.idx với LHS = NumberType(), RHS = ....
        """         
        #TODO implement

       
        """
            # TODO kiểm tra TypeMismatchInExpression kiểm tra len(left.size) và len(ast.idx) 
            ^ len(left.size) < len(ast.idx) -> trả về lỗi TypeMismatchInExpression ví dụ
            number a[1,2]
            var c <- a[1,2,3]
            ^ len(left.size) = len(ast.idx) -> trả về type eleType không phải là arraytype
            number a[1,2]
            var c <- a[1,2] -> c : numbertype
            ^ len(left.size) > len(ast.idx) -> trả về arraytype cắt đi đoạn ban đầu
            number a[1,2,3]
            var c <- a[1] -> c : number c[2,3]                   
        """ 
        #TODO implement

    def visitArrayLiteral(self, ast, param):
        #* bước 1 chọn được type đã xác định kiểm trong ast.value (typ không phải là Zcode và ArrayZcode)
        typ = None
        for item in ast.value:
            checkTyp = self.visit(item, param)
            if not (isinstance(checkTyp, Zcode) or isinstance(checkTyp, ArrayZcode)):
                typ = checkTyp
                break
        
        #* Bước 2: xét kiểu từng phần tử
        #^ TH1 : typ is None nghĩa là trong array chỉ gồm Zcode và ArrayZcode nên return ArrayZcode
        #^ TH2 : typ in [StringType, BoolType, NumberType] duyệt qua ast.value nếu typ từng phần tử có ArrayZcode hay là comparType bị khác thì nén TypeMismatchInExpression
        """_VD_
            [1, "2"] -> lỗi TypeMismatchInExpression vì khác type trong array
            dymaic x
            [1, [x,x]] -> lỗi TypeMismatchInExpression
            [1, x] -> x = numbertype
        """
        #^ TH3 : typ in arraytype duyệt qua ast.value giống TH2 nhưng nếu ArrayType yêu cầu dùng setTypeArray để chỉnh typ 
        #^ bước 2 và 3 trả về arraytype
        if typ is None:
            #TODO implement
        elif type(typ) in [StringType, BoolType, NumberType]:
            #TODO implement
        else:
            #TODO implement
            




    """phần này sẽ là cố định do ngắn quá :(( """
    def visitBlock(self, ast, param):
        for item in ast.stmt:
            #! trường hợp gặp block
            if type(item) is Block: self.visit(item, [{}] + param)
            else: self.visit(item, param)           
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
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()

        
        





