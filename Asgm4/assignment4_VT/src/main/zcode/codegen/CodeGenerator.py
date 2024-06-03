from Emitter import *
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class CodeGenerator:
    def gen(self, ast, path):
        # ast: AST
        # dir_: String
        gc = CodeGenVisitor(ast, path)
        gc.visit(ast, None)

class Access():
    def __init__(self, frame, symbol, isLeft, checkTypeLHS_RHS = False):
        self.frame = frame                          #* không gian stack và local cần dùng để chạy 1 hàm
        self.symbol = symbol                        #* giống phần param ở BTL3 nhưng này hiện thực list<list>> (có thể dùng list<dict> như btl3)
        self.isLeft = isLeft                        #* hiện tại vế trên trái hay bên phải để xác định get và put cho biến
        self.checkTypeLHS_RHS = checkTypeLHS_RHS    #* kiểm tra kiểu đúng không

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, path):
        self.astTree = astTree
        self.path = path
        self.className = "ZCodeClass"
        self.emit = Emitter(self.path + "/" + self.className  + ".j")
        self.funcList = []
        self.function = None
        self.Return = False
        self.arrayCell = ""  
    
    def printListfunction(self):
        print(f"self.function: {str(self.function)}" )
        print(f"self.Return  : {str(self.Return)}" )
        print(f"listFunction :")
        
        for item in self.funcList:
            print(f"         : {str(item)}" )
    


    
    #* CẬP NHẬT TYPE
    def LHS_RHS(self, LHS, RHS, o):
        #* TRUYỀN checkTypeLHS_RHS = False -> nghĩa là chúng ta xét type trước, trước khi lấy stack
        _, rhsType = self.visit(RHS, Access(o.frame, o.symbol, False, True))
        _, lhsType = self.visit(LHS, Access(o.frame, o.symbol, True, True))
        
        if (isinstance(lhsType, Zcode) and isinstance(rhsType, Zcode)):
            return False
        
        if isinstance(lhsType, Zcode):
            lhsType.typ = rhsType
            self.emit.setType(lhsType)         #* cập nhật lại type vì trước đó type là None
            return True, rhsType            
            
        elif isinstance(rhsType, Zcode):
           rhsType.typ = lhsType
           self.emit.setType(rhsType)           #* cập nhật lại type vì trước đó type là None
           return True, lhsType
           
        
    
    # TODO :(( 
    def visitProgram(self, ast:Program, o):
        # decl: List[Decl]
        # print('visitProgram')
        
        # Init Jasmin Directives
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
    
        # Traverse all global var and func + self.emit.emitATTRIBUTE for global var
        symbol = [[]]
        Main = None
        function = None
        for decl in ast.decl:
            if type(decl) is VarDecl:
                # index = -1
                symbol[0].append(VarZcode(decl.name.name, decl.varType, -1, True if decl.varInit else False))
                self.emit.printout(self.emit.emitATTRIBUTE(decl.name.name, decl.varType if decl.varType else symbol[0][-1], False, self.className))
                symbol[0][-1].line = self.emit.printIndexNew()
                
            elif type(decl) is FuncDecl and decl.body is not None:
                self.funcList += [FuncZcode(decl.name.name, None, [i.varType for i in decl.param])]
                if decl.name.name == "main":
                    function = self.funcList[-1]
                    Main = decl
        
    
        # Init constructor for Zcode class
        frame = Frame("<init>", VoidType)
        # self.emit.printout(self.emit.emitMETHOD(lexeme="<init>", in_=FuncZcode("init", VoidType(), []), isStatic=False, frame=frame))
        self.emit.printout(self.emit.emitMETHOD("<init>", FuncZcode("init", VoidType(), []), False, frame))
        
        frame.enterScope(True)
        # .var 0 is arg0 [Ljava/lang/String; from Label0 to Label1
        self.emit.printout(self.emit.emitVAR(
            frame.getNewIndex(), 
            "this", 
            Zcode(), 
            frame.getStartLabel(), 
            frame.getEndLabel(), 
            frame
        ))
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))           # Label0
        self.emit.printout(self.emit.emitREADVAR("this", self.className, 0, frame))     # aload_0
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))                          # invokespecial java/lang/Object/<init>()V
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))             # Label1
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))                     # return
        self.emit.printout(self.emit.emitENDMETHOD(frame))                              # .end method
        frame.exitScope()



        # Init static Zcode - Contructor for static
        frame = Frame("<clinit>", VoidType)
        # self.emit.printout(self.emit.emitMETHOD(lexeme="<clinit>", in_=FuncZcode("clinit", VoidType(), []), isStatic=True, frame=frame))
        self.emit.printout(self.emit.emitMETHOD("<clinit>", FuncZcode("clinit", VoidType(), []), True, frame))
        
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))        
        for decl in ast.decl:
            if (type(decl) is VarDecl) and (decl.varInit is not None):            # Primitive type
                self.visit(Assign(decl.name, decl.varInit), Access(frame, symbol, False))
            
            elif (type(decl) is VarDecl) and (type(decl.varType) is ArrayType):   # Array type
                if len(decl.varType.size) == 1:                                      # 1D array    
                    self.emit.printout(self.visit(NumberLiteral(decl.varType.size[0]), Access(frame, symbol, False))[0])
                    self.emit.printout(self.emit.emitF2I(frame))
                    self.emit.printout(self.emit.emitNEWARRAY(decl.varType.eleType, frame))
                    self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + decl.name.name, decl.varType, frame))
                else:                                                               # Multi-D array
                    for i in decl.varType.size:
                        self.emit.printout(self.visit(NumberLiteral(i), Access(frame, symbol, False))[0])
                        self.emit.printout(self.emit.emitF2I(frame))
                    self.emit.printout(self.emit.emitMULTIANEWARRAY(decl.varType, frame))
                    self.emit.printout(self.emit.emitPUTSTATIC(self.className + "." + decl.name.name, decl.varType, frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
    
    
        
        # Initiate for normal function
        for idx, decl in zip(range(0, len(ast.decl)), ast.decl):
            if (type(decl) is FuncDecl) and (decl.body is not None):
                if (decl.name.name != "main"):
                    self.function = self.funcList[idx]
                    self.visit(decl, symbol)
                
                
        
        # Init main function
        frame = Frame("main", VoidType)
        # self.emit.printout(self.emit.emitMETHOD(lexeme="main", in_=FuncZcode("main", VoidType(), [ArrayType([1], StringType())]), isStatic=True, frame=frame))
        # method public static main([Ljava/lang/String;)V
        self.emit.printout(self.emit.emitMETHOD("main", FuncZcode("main", VoidType(), [ArrayType([1], StringType())]), True, frame))
        
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        index = frame.getNewIndex()
        typeParam = [VarZcode("for", NumberType(), index, True)]
        self.emit.printout(self.emit.emitVAR(index, "for", NumberType(), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.function = function
        self.visit(Main.body, Access(frame, [typeParam] + symbol, False))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))   
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()    
        
        self.emit.emitEPILOG()
    
    
    
    # TODO :() 
    def visitVarDecl(self, ast, o):
        # name: Id
        # varType: Type = None  # None if there is no type
        # modifier: str = None  # None if there is no modifier
        # varInit: Expr = None  # None if there is no initial
        
        """#TODO: Implement
        #* tạo emitVAR và o.symbol[0].append, cập nhật o.symbol[0][-1].line
        #* if ast.varInit is not None:
            #* elf.visit(Assign(ast.name, ast.varInit), o) 
        #* elif type(ast.varType) is ArrayType:
            #* giống phần khai báo biến static gần giống ý tưởng
        """

        frame = o.frame
        symbol = o.symbol
        
        symbol[0].append(VarZcode(ast.name.name, ast.varType, -1, True if ast.varInit else False))
        startLabel = o.frame.getStartLabel()
        endLabel = o.frame.getEndLabel()
        
        self.emit.printout(self.emit.emitVAR(o.frame.getNewIndex(), ast.name.name, ast.varType if ast.varType else symbol[0][-1], startLabel, endLabel, o.frame))
        symbol[0][-1].line = self.emit.printIndexNew()
        
        if ast.varInit is not None:
            self.visit(Assign(ast.name, ast.varInit), o)
        
        
        if (type(ast) is VarDecl) and (ast.varInit is not None):            # Primitive type
                self.visit(Assign(ast.name, ast.varInit), Access(frame, symbol, False))
            
        elif (type(ast) is VarDecl) and (type(ast.varType) is ArrayType):   # Array type
            if len(ast.varType.size) == 1:                                      # 1D array    
                self.emit.printout(self.visit(NumberLiteral(ast.varType.size[0]), Access(frame, symbol, False))[0])
                self.emit.printout(self.emit.emitF2I(frame))
                self.emit.printout(self.emit.emitNEWARRAY(ast.varType.eleType, frame))
                self.emit.printout(self.emit.emitPUTSTATIC(f'{self.className}.{ast.name.name}', ast.varType, frame))
            else:                                                               # Multi-D array
                for i in ast.varType.size:
                    self.emit.printout(self.visit(NumberLiteral(i), Access(frame, symbol, False))[0])
                    self.emit.printout(self.emit.emitF2I(frame))
                self.emit.printout(self.emit.emitMULTIANEWARRAY(ast.varType, frame))
                self.emit.printout(self.emit.emitPUTSTATIC(f'{self.className}.{ast.name.name}', ast.varType, frame))
              
        
      
    # TODO :()                        
    def visitFuncDecl(self, ast, symbol):
        # name: Id
        # param: List[VarDecl]  # empty list if there is no parameter
        # body: Stmt = None  # None if this is just a declaration-part
        self.Return = False
        self.function = function
        
        if ast.body is None: 
            return
        
        """TODO: Implement
        #* giống hàm main, nhưng phần này có param
        """
        frame = Frame(ast.name.name, None)
        func = list(filter(lambda x: x.name == ast.name.name, self.funcList))
        if len(func) == 0:
            raise f"No function named {ast.name.name} found"
        func = func[0]
        
        self.emit.printout(self.emit.emitMETHOD(ast.name.name, func, True, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        frame.enterScope(True)
        newSymbol = [[]] + symbol
        for param in ast.param:
            idx = frame.getNewIndex()
            code = self.emitemitVAR(
                idx,
                param.name.name,
                param.varType,
                frame.getStartLabel(),
                frame.getEndLabel(),
                frame
            )
            self.emit.printout(code)
        
        
        self.visit(ast.body, Access(frame, newSymbol, False))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        # if type(returnType) is VoidType:
        #     self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()    
        
        self.emit.emitEPILOG()
               
            
    def genMethod(self, decl: FuncDecl, o, frame):
        pass



# ----------------------------------------------------------------------------------------------------------------------------------    
    # TODO :()
    def visitCallExpr(self, ast, o):
        # name: Id
        # args: List[Expr]
        
        #* phần io -> gọi qua class io.java trong phan lib
        if ast.name.name in ["readNumber", "readBool", "readString"]:
            if ast.name.name == "readNumber": 
                if o.checkTypeLHS_RHS: 
                    return None, NumberType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, NumberType(), []), o.frame), NumberType
            
            elif ast.name.name == "readBool": 
                if o.checkTypeLHS_RHS: 
                    return None, BoolType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, BoolType(), []), o.frame), NumberType
            
            elif ast.name.name == "readString": 
                if o.checkTypeLHS_RHS: 
                    return None, StringType()
                return self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, StringType(), []), o.frame), NumberType

        #* tìm function trong self.Listfunction
        func = list(filter(lambda x: x.name == ast.name.name, self.funcList))
        if len(func) == 0:
            raise f"No function named {ast.name.name} found"
        func = func[0]
            
        # for item in self.funcList:
        #     if item.name == ast.name.name:
        #         func = item
                
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            for i in range(len(func.param)):
                self.LHS_RHS(func.param[i], ast.args[i], o)
                
            return None, func.typ if func.typ else func            
            
        
        """#TODO : gọi emitINVOKESTATIC
        ví dụ : 
        .line 12 -> foo(1,true)
        0: iconst_1
        1: iconst_1
        2: invokestatic ZCodeClass/foo(IZ)V        
        """
        
        code = ""
        for x in ast.args:
            code += self.visit(x, Access(o.frame, None, False, False))[0]
        code += self.emit.emitINVOKESTATIC(f'{self.className}.{ast.name.name}', func.typ, o.frame)

        return code, func.typ
    
    
    # TODO :() 
    def visitBinaryOp(self, ast: BinaryOp, o):
        # op: str
        # left: Expr
        # right: Expr
        
        op = ast.op
        frame = o.frame
        symbol = o.symbol
        
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            if op in ['+', '-', '*', '/', '%']:
                self.LHS_RHS(ast.left, NumberType(), o)
                self.LHS_RHS(ast.right, NumberType(), o)
                return None, NumberType()
            elif op in ['=', '!=', '<', '>', '>=', '<=']:
                self.LHS_RHS(ast.left, NumberType(), o)
                self.LHS_RHS(ast.right, NumberType(), o)
                return None, BoolType()
            elif op in ['and', 'or']:
                self.LHS_RHS(ast.left, BoolType(), o)
                self.LHS_RHS(ast.right, BoolType(), o)
                return None, BoolType()
            elif op in ['==']:
                self.LHS_RHS(ast.left, StringType(), o)
                self.LHS_RHS(ast.right, StringType(), o)
                return None, BoolType()
            elif op in ['...']:
                self.LHS_RHS(ast.left, StringType(), o)
                self.LHS_RHS(ast.right, StringType(), o)
                return None, StringType()
        
        codeLeft, _ = self.visit(ast.left, o)
        codeRight, _ = self.visit(ast.right, o)
        """#TODO emitADDOP, emitMULOP, emitREOP, emitANDOP,emitOROP, emitREOP, emitINVOKEVIRTUAL (dùng java/lang/String/concat và java/lang/String/equals)
        #^ mọi năm có tính toán lười cho and và or năm này thấy thầy ko mô tả lạ thật :((
        #* khó nhất chắc là % ta dùng như sau 
            codeLeft
            codeRight
            codeLeft
            codeRight
            '/'
            emitF2I -> ép kiểu sang int
            emitI2F -> từ in ép kiểu ngược lại
            '*'
            '-'
        """
        
        code = codeLeft + codeRight
        typ = None
        if op in ['+', '-']:
            code += self.emit.emitADDOP(op, NumberType(), frame)
        elif op in ['*', '/']:
            code += self.emit.emitMULOP(op, NumberType(), frame)
        elif op in ['%']:
            code += self.emit.emitMOD(op, NumberType(), frame)
        elif op in ["and"]:
            code += self.emit.emitANDOP(frame)
            typ = BoolType()
        elif op in ["or"]:
            code += self.emit.emitOROP(frame)
            typ = BoolType()
        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            code += self.emit.emitREOP(op, NumberType(), frame)
            typ = BoolType()
        elif op in ['==']:
            code += self.emit.emitINVOKEVIRTUAL("java/lang/String.equals(Ljava/lang/String;)", BoolType(), frame)
            typ = BoolType()
        elif op in ['...']:
            code += self.emit.emitINVOKEVIRTUAL("java/lang/String.concat(Ljava/lang/String;)", StringType(), frame)
            typ = StringType()
        
        return code, typ
        
        
    
    # TODO :()
    def visitUnaryOp(self, ast: UnaryOp, o):
        # op: str
        # operand: Expr
        frame = o.frame
        op = ast.op
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            if op in ['-']:
                self.LHS_RHS(ast.operand, NumberType(), o)
                return None, NumberType()
            elif op in ['not']:
                self.LHS_RHS(ast.operand, BoolType(), o)
                return None, BoolType()
        """#TODO emitNEGOP, emitNOT
        """
        
        code = self.visit(ast.operand, o)[0]
        code += self.emit.emitNEGOP(NumberType, frame) if (op == '-') else self.emit.emitNOT(NumberType, frame)
        typ = NumberType() if (op == '-') else BoolType()
        
        return code, typ
        
        

    
    
    

# ----------------------------------------------------------------------------------------------------------------------------------    
    # TODO :()
    def visitReturn(self, ast, o):
        # expr: Expr = None  # None if there is no expression after return

        #* CHECK TYPE BTL3
        # self.LHS_RHS(self.function, ast.expr if ast.expr else VoidType(), o)
        
        self.Return = True #* đã có return
        frame = o.frame
        
        """#TODO emitRETURN
        #* TH1 : nếu  ast.expr is None
        #* TH2 : Ngc lại
        vd : return 1
        iconst_1
        freturn
        """
        code = ''
        if ast.expr is None:
            typ = None
        else:
            code, typ = self.visit(ast.expr, Access(frame, o.symbol, False))
        
        returnTyp = self.LHS_RHS(self.function, VoidType() if (typ is None) else typ, o)[1]
        code += self.emit.emitRETURN(returnTyp, frame)
        self.emit.printout(code)
        
        
        
    # TODO :()
    def visitAssign(self, ast: Assign, o):
        # lhs: Expr
        # exp: Expr
        
        frame = o.frame
        symbol = o.symbol
    
        self.LHS_RHS(ast.lhs, ast.rhs, o)
        
        rhsCode, rhsTyp = self.visit(ast.rhs, Access(frame, o.symbol, False))
        lhsCode, lhsTyp = self.visit(ast.lhs, Access(frame, o.symbol, True))
        
        """TODo
        TH1 : LHS = ArrayCell
        lhsCode
        rhsCode
        self.emit.emitASTORE(self.arrayCell, frame))
        
        TH2 : 
        lhsCode
        rhsCode        
        """
        
        code = ''
        if type(ast.lhs) is ArrayCell:
            code = lhsCode + rhsCode + self.emit.emitASTORE(lhsTyp, frame)
        else:
            code = rhsCode + lhsCode            
        
        self.emit.printout(code)
 
 
  
    # TODO :()
    def visitCallStmt(self, ast, o):
        # name: Id
        # args: List[Expr]  # empty list if there is no argument
        
        #* phần io
        if ast.name.name in ["writeNumber", "writeBool", "writeString"]:
            if ast.name.name == "writeNumber": self.LHS_RHS(NumberType(), ast.args[0], o)
            elif ast.name.name == "writeBool": self.LHS_RHS(BoolType(), ast.args[0], o)
            elif ast.name.name == "writeString": self.LHS_RHS(StringType(), ast.args[0], o)
            
            argsCode, argsType = self.visit(ast.args[0], o)
            self.emit.printout(argsCode)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"io/{ast.name.name}", FuncZcode(ast.name.name, VoidType(), [argsType]), o.frame))
            return

        """#TODO giống call expr"""
        
        # name: Id
        # args: List[Expr]
        

        #* tìm function trong self.Listfunction
        func = list(filter(lambda x: x.name == ast.name.name, self.funcList))
        if len(func) == 0:
            raise f'No function named {ast.name.name} found'
        func = func[0]
                
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            for i in range(len(func.param)):
                self.LHS_RHS(func.param[i], ast.args[i], o)
                
            return None, func.typ if func.typ else func
        
        code = ""
        for x in ast.args:
            code += self.visit(x, Access(o.frame, None, False, False))[0]
        code += self.emit.emitINVOKESTATIC(f'{self.className}.{ast.name.name}', VoidType(), o.frame)

        return code, VoidType()
    
  
      
    def visitBlock(self, ast, o):
        # stmt: List[Stmt]  # empty list if there is no statement in block
        
        newSymbol = [[]] + o.symbol
        
        o.frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame))
        for stmt in ast.stmt: 
            self.visit(stmt, Access(o.frame, newSymbol, False))
            
        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))
        o.frame.exitScope()
    
    
    # TODO :()    
    def visitIf(self, ast, o):
        # expr: Expr
        # thenStmt: Stmt
        # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
        # elseStmt: Stmt = None  # None if there is no else branch
        
        #* CHECK TYPE BTL3       
        self.LHS_RHS(BoolType(), ast.expr, o)        
        for item in ast.elifStmt:
            self.LHS_RHS(BoolType(), item[0], o)   
        
        
        """_enterLoop_
            điều kiện if -> nhảy đến đặt label end if
                |
            visit body
                |
            goto exit
                |
            đặt label end if
                |
            nếu có eilf -> for
                tạo lable mới
                    |
                điều kiện -> nhảy lable mới
                    | 
                visit
                    |
                goto exit
                    |
                đặt đến lable mới
                    |
            -- end for
                |
            nếu có else
                |
              visit
                |
            lable exit
        """
        frame = o.frame
        symbol = o.symbol
        
        hasElif = True if (len(ast.elifStmt) == 0) else False
        hasElse = True if ast.elseStmt is not None else False
        
        code = self.visit(ast.expr, Access(frame, symbol, False))[0]
        endIfLabel = frame.getNewLabel()
        code += self.emit.emitIFFALSE(endIfLabel, frame)    
        code += self.visit(ast.thenStmt, Access(frame, symbol, False))[0]
        exitIfLabel = frame.getNewLabel()
        code += self.emit.emitGOTO(exitIfLabel, frame)

        code += self.emit.emitLABEL(endIfLabel, o.frame)
        self.emit.printout(code)
        
        if hasElif:
            for cond, stmt in ast.elifStmt:
                code = self.visit(cond, Access(frame, symbol, False))[0]
                
                nextElifLabel = frame.getNewLabel() 
                code += self.emit.emitIFFALSE(nextElifLabel, frame)
                
                code += self.visit(stmt, Access(frame, symbol, False))[0]
                code +=  self.emit.emitGOTO(exitIfLabel, frame)
                
                code += self.emit.emitLABEL(nextElifLabel, frame)
                self.emit.printout(code)
                
        if hasElse:
            code += self.visit(ast.elseStmt, Access(frame, symbol, False))[0]
            code +=  self.emit.emitGOTO(exitIfLabel, frame)
            self.emit.printout(code)
                
                
        code += self.emit.emitLABEL(exitIfLabel, o.frame)
        
        
        
    # TODO :()
    def visitFor(self, ast, o):
        # name: Id
        # condExpr: Expr
        # updExpr: Expr
        # body: Stmt
        
        #* CHECK TYPE BTL3
        """_typID_"""        
        self.LHS_RHS(NumberType(), ast.name, o)        
        
        """_typCondExpr_"""    
        self.LHS_RHS(BoolType(), ast.condExpr, o) 

        """_typUpdExpr_"""            
        self.LHS_RHS(NumberType(), ast.updExpr, o) 

        frame = o.frame
        symbol = o.symbol
        self.visit(ast.name, o)
        """_enterLoop_
            gán for <- ast.name
                |
            tạo Loop
                |
            lable_new
                |
            kiểm tra exp để goto đến lable_Break
                |
            visit body
                |
            đặt lable continue
                |
            gọi phép gán Assign(ast.name, BinaryOp('+', ast.name, ast.updExpr))
                |
            goto đến lable_new
                |
            đặt lable_Break
                |
            end loop
                |
            gán for <- ast.name
            
        """
        frame.enterLoop()   # ----------------------------------------------------------------------------
        
        continueLabel = frame.getContinueLabel()
        breakLabel = frame.getBreakLabel()
        startLoopLabel = frame.getNewLabel()
                
        
        idx = frame.getNewIndex()
        code = self.visit(ast.name, Access(o.frame, o.symbol, False))[0]
        

        
        self.emitprintout(self.emit.emitLABEL(startLoopLabel, frame))
        code += self.visit(ast.condExpr, Access(o.frame, o.symbol, False))[0]
        code += self.emit.emitIFFALSE(breakLabel, frame)
        self.emit.printout(code)
        
        self.visit(ast.body, Access(frame, symbol, False))
        
        self.emitprintout(self.emit.emitLABEL(continueLabel, frame))
        updExpr = Assign(ast.name, BinaryOp('+', ast.name, ast.updExpr))
        code = self.visit(updExpr, Access(frame, symbol, False))
        code += self.emit.emitGOTO(startLoopLabel, frame)      
        


        self.emitprintout(self.emit.emitLABEL(breakLabel, frame))
        
        
        # self.visit(Assign(Id("for"), ast.name), o)
     
        # self.visit(Assign(ast.name, Id("for")), o)

        
        frame.exitLoop()    # ----------------------------------------------------------------------------


    
    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    
    
    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
        



    
# ----------------------------------------------------------------------------------------------------------------------------------    
    # TODO :()
    def visitArrayLiteral(self, ast, o):
        frame = o.frame
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            baseTyp = None
            for value in ast.value:
                _, typ = self.visit(value, o)
                if (baseTyp is None) and isinstance(typ, (BoolType, StringType, NumberType, ArrayType)):
                    baseTyp = typ
                    break
            
            if baseTyp is None:
                raise "Array withou primitive type"
            
            for value in ast.value:
                self.LHS_RHS(baseTyp, value, o)
            
            # if isinstance(baseTyp, (BoolType, StringType, NumberType)):
            #     return None, ArrayType([len(ast.value)], baseTyp)
            
            # return None, ArrayType([float(len(ast.value))] + baseTyp.size, baseTyp.eleType)
        
            code = ''
            
            # 1D array
            if isinstance(baseTyp, (BoolType, StringType, NumberType)):
                code = self.emit.emitPUSHCONST(len(ast.value), NumberType(), o.frame)
                code += self.emit.emitNEWARRAY(baseTyp, o.frame)
                
                for idx, value in zip(range(0, len(ast.value)), ast.value):
                    code += self.emit.emitDUP(o.frame)
                    code += self.emit.emitPUSHCONST(idx, NumberType(),o.frame)
                    code += self.visit(ast.value, o)[0]
                    code += self.emit.emitASTORE(baseTyp, frame)
                return code, ArrayType([len(ast.value)], baseTyp)
            
            # Multi-D array
            else:
                code = self.emit.emitPUSHICONST(len(ast.value), o.frame)
                code += self.emit.emitANEWARRAY(baseTyp, o.frame)
                
                for idx, value in zip(range(0, len(ast.value)), ast.value):
                    code += self.emit.emitDUP(o.frame)
                    code += self.emit.emitPUSHICONST(idx,o.frame)
                    code += self.visit(ast.value, o)[0]
                    code += self.emit.emitASTORE(baseTyp, frame)
                return code, ArrayType([float(len(ast.value))] + baseTyp.size, baseTyp.eleType)






        """#TODO:
        #* trường hợp mảng 1 chiều
            emitPUSHCONST -> giá trị khởi tạo của mảng
            emitF2I -> ép kiểu sang int
            emitNEWARRAY -> khởi tạo mảng
            for
                emitDUP -> nhân 2 ở đây là địa chỉ của mảng khởi tạo phía trên
                emitPUSHCONST -> giá trị index trong mảng
                emitF2I
                visit -> giá trị biến
                emitASTORE -> lưu trữ
    
        #* trường hợp mảng nhiều chiều
            emitPUSHCONST -> giá trị khởi tạo của mảng
            emitF2I -> ép kiểu sang int
            emitANEWARRAY -> khởi tạo mảng
            for
                emitDUP -> nhân 2 ở đây là địa chỉ của mảng khởi tạo phía trên
                emitPUSHCONST -> giá trị index trong mảng
                emitF2I
                visit -> giá trị biến
                emitASTORE -> lưu trữ             
        """
        
    
    
    # TODO :(( 
    def visitArrayCell(self, ast, o):
        # arr: Expr
        # idx: List[Expr]
        
        
        frame = o.frame
        symbol = o.symbol 
        
        #* cập nhật type lhs or RHS giống btl3
        if o.checkTypeLHS_RHS:
            _, arr = self.visit(ast.arr, Access(frame, symbol, False, False))
            for i in ast.idx:
                self.LHS_RHS(NumberType(), i, o)
            
            if len(arr.size) == len(ast.idx): return None, arr.eleType
            return None, ArrayType(arr.size[len(ast.idx):], arr.eleType)   


        """#TODO:
        #* Trường hợp trả về giá trị khác mảng
            visit(ast.arr) -> lấy ra get/put/read/write
            for 0 -> size - 1
               giá trị tại index
               f2i
               aload
            giá trị tại index = -1
            f2i
            float/bload/aload(string)  (nếu o.isLeft thì bỏ qua không gọi mà gán self.arrayCell = typ)  
    
        #* Trường hợp tra về mảng
            visit(ast.arr) -> lấy ra get/put/read/write
            for 0 -> size - 1
               giá trị tại index
               f2i
               aload
            giá trị tại index = -1
            f2i
            aload -> địa chỉ   (nếu o.isLeft thì bỏ qua không gọi mà gán self.arrayCell = typ)            
        """
        
        lhsCode, lhsTyp = self.visit(ast.arr, Access(frame, symbol, False))
        
        code = lhsCode
        for i in range(len(ast.idx) - 1):
            code += self.visit(ast.idx[i], Access(frame, symbol, False))[0]
            code += self.emit.emitF2I(frame)
            code += self.emit.emitALOAD(ArrayType([], None), frame)
            
        code += self.visit(ast.idx[-1], Access(frame, symbol, False))[0]
        code += self.emit.emitF2I(frame)
        
        if o.isLeft:
                if len(ast.idx) == len(lhsTyp.size):
                    return code, lhsTyp.eleType
                else:
                    return code, ArrayType(lhsTyp.size[len(ast.idx):], lhsTyp.eleType)
        else:
            if len(ast.idx) == len(lhsTyp.size):
                code += self.emit.emitALOAD(lhsTyp.eleType, frame)
                return code, lhsTyp.eleType
            else:
                code += self.emit.emitALOAD(ArrayType([],None), frame)
                return code, ArrayType(lhsTyp.size[len(ast.idx):], lhsTyp.eleType)
        
        
        
        
       
    def visitNumberLiteral(self, ast, o):
        # value: float
        return self.emit.emitPUSHCONST(ast.value, NumberType(), o.frame) if (not o.checkTypeLHS_RHS) else None, NumberType()
    
    
    
    def visitBooleanLiteral(self, ast, o):
        # value: bool
        return self.emit.emitPUSHCONST(ast.value, BoolType(), o.frame) if (not o.checkTypeLHS_RHS) else None, BoolType()
    
    
    
    def visitStringLiteral(self, ast, o):
        # value: string
        return self.emit.emitPUSHCONST("\"" + ast.value + "\"", StringType(), o.frame) if (not o.checkTypeLHS_RHS) else None, StringType()
    
    
    
    
    
    
# ----------------------------------------------------------------------------------------------------------------------------------
    def visitId(self, ast, o):
        frame = o.frame
        symbol = o.symbol
        
        if o.checkTypeLHS_RHS:
            for x in symbol:
                for sym in x:
                    if sym.name == ast.name:
                        return None, (sym.typ if sym.typ else sym)
        
        id = list(filter(lambda x: x.name == ast.name, symbol))
        if len(id) == 0:
            return None, None
        else:
            id = id[0]
        
        if o.isLeft:
            if id.index == -1:
                return self.emit.emitPUTSTATIC(f'{self.className}.{id.name}', id.typ, frame), id.typ
            else: 
                return self.emit.emitWRITEVAR(id.name, id.typ, id.index,frame), id.typ
        else:
            if id.index == -1:
                return self.emit.emitGETSTATIC(f'{self.className}.{id.name}', id.typ, frame), id.typ
            else: 
                return self.emit.emitREADVAR(id.name, id.typ, id.index, frame), id.typ
        
                   
    
    def visitArrayType(self, ast, param):
        return None, ast
    
    
    def visitNumberType(self, ast, param):
        return None, NumberType()
    
    
    def visitVoidType(self, ast, param):
        return None, VoidType()
    
    
    def visitBoolType(self, ast, param):
        return None, BoolType()
    
    
    def visitStringType(self, ast, param):
        return None, StringType()
    
    
    def visitFuncZcode(self, ast, param):
        return None, ast.typ if ast.typ else ast
    
    
    def visitVarZcode(self, ast, param):
        return None, ast.typ if ast.typ else ast
    