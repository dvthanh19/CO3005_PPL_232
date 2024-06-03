from Emitter import Emitter, Zcode, ZType
from functools import reduce

from main.zcode.codegen.Frame import Frame
from abc import ABC
from Visitor import *
from AST import *







class Symbol:   # name of variable or funcion
    def __init__(self, name, ztype, value=None):
        self.name = name
        self.ztype = ztype
        self.value = value

    def __str__(self):
        return f'Symbol({self.name},{str(self.ztype)},{str(self.value)})'


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gc = CodeGenVisitor(ast, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym
        self.isGen = False


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst



class Val(ABC):
    pass

class Index(Val):
    # value (int): index of local variable
    def __init__(self, value):
        self.value = value

class CName(Val):
    # value (str): class name of static (global) variable
    def __init__(self, value):
        self.value = value



def isDeterminedType(x):
    if (x is None) or ((type(x) is ArrayType) and (type(x.eleType) is None)):
        return False
      
    return True



# Note: This is code generation phase --> No error anymore

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, path):
        self.astTree = astTree
        self.path = path
        self.className = "ZCodeClass"
        self.emit = Emitter(self.path + "/" + self.className  + ".j")
        
        self.func = None
        self.mainfunc = None
        self.returnStmt = False
        self.isInferred = False
        self.globalDecl = False
        self.libName = 'io'
        self.funcList = {
            "readNumber" :Symbol("readNumber", ZType(list(), NumberType()), CName(self.libName)),
            "readBool" :Symbol("readBool", ZType(list(),BoolType()), CName(self.libName)),
            "readString" :Symbol("readString", ZType(list(),StringType()), CName(self.libName)),
            "writeNumber": Symbol("writeNumber", ZType([NumberType()], VoidType()), CName(self.libName)),
            "writeBool": Symbol("writeBool", ZType([BoolType()], VoidType()), CName(self.libName)),
            "writeString": Symbol("writeString", ZType([StringType()], VoidType()), CName(self.libName))
        }
        
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
        
    # -- Helper function ----------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------
    def printListfunction(self):
        print(f"self.function: {str(self.func)}")
        print(f"self.Return  : {str(self.returnStmt)}" )
        print(f"listFunction : {self.funcList}")
    

    def setType(self, x:Symbol, typ):
               
        if type(x.ztype) is ZType:
            x.ztype.returnType = typ
        else: 
            x.ztype = typ
        
        return typ
    
    def setArray(self, arr, typeArr:ArrayType):
        if len(typeArr.size) == 1:     # 1-D array
            for x in arr:
                self.setType(x, typeArr.eleType)
        
        else:                       # Multi-D array
            for x in arr:
                if type(x) is list:
                    self.setArray(x, ArrayType(x.size[1:], typeArr.eleType))
                else:
                    self.setType(x, ArrayType(x.size[1:], typeArr.eleType))
    
    def inferType(self, lhs, rhs):
        # This code generator is passed Static check, so not need to check case type cannot be infer
        if type(rhs) is list:
            self.setArray(rhs, lhs)
        elif type(lhs) is Symbol:
            self.setType(lhs, rhs)        
        elif type(rhs) is Symbol:
            self.setType(rhs, lhs)
        
    # def write_readValue(self, name, sym, frame, write=True):
    #     typ = sym.ztype
    #     value = sym.value.value  
    #     if write:
    #         if type(sym.value) is Index:
    #             return self.emit.emitWRITEVAR(name, sym.ztype, value, frame), typ
    #         elif type(sym.value) is CName: 
    #             return self.emit.emitPUTSTATIC(f'{value}.{name}', typ, frame), typ
    #     else:
    #         if type(sym.value) is Index:
    #             return self.emit.emitREADVAR(name, typ, value, frame), typ
    #         elif type(sym.value) is CName:
    #             return self.emit.emitGETSTATIC(f'{value}.{name}', typ, frame), typ
    
    def initArray(self, ast, param):
        sym = ast.name.sym
        code = ''
        
        if len(sym.ztype.size) == 1:
            code = self.emit.emitPUSHICONST(int(sym.ztype.size[0]), param.frame)
            code += self.emit.emitNEWARRAY(sym.ztype.eleType, param.frame)
        else:
            for i in sym.ztype.size:
                code += self.emit.emitPUSHICONST(int(i), param.frame)
            code += self.emit.emitMULTIANEWARRAY(sym.ztype, param.frame)

        if isinstance(sym.value, Index):
            code += self.emit.emitWRITEVAR(sym.name, sym.ztype, sym.value.value, param.frame)
        else:
            code += self.emit.emitPUTSTATIC(f"{sym.value.value}.{sym.name}", sym.ztype, param.frame)
            
        return code
        
    
        
    # -- Visit function -----------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------
    # TODO :()
    def visitProgram(self, ast:Program, o):
        # decl: List[Decl]
        # print('visitProgram')
        
        # Init Jasmin Directives
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
    
        # Traverse all global var and func + self.emit.emitATTRIBUTE for global var
        o = [[]]
        mainfunc = None
        func = None
        
        # Traverse all program to infer type
        self.isInferred = False
        for decl in ast.decl:
            self.visit(decl, o)
        
        # Traverse vardecl of global variables
        self.isInferred = True
        for decl in ast.decl:
            if type(decl) is VarDecl:
                self.emit.printout(self.emit.emitATTRIBUTE(
                    decl.name.name, 
                    decl.name.sym.ztype,
                    False, 
                    self.className
                ))
                decl.name.sym.value = CName(self.className)
        
        
        # Init constructor for Zcode class
        frame = Frame('<init>', VoidType())
        self.emit.printout(self.emit.emitMETHOD('<init>', ZType([], VoidType()), False, frame))
        
        frame.enterScope(True)
        
        idx = frame.getNewIndex()
        startLabel = frame.getStartLabel()
        endLabel = frame.getEndLabel()
        
        
        code = self.emit.emitLABEL(startLabel, frame)                              # Label0
        code += self.emit.emitVAR(idx, 'this', Zcode(), startLabel, endLabel, frame) # .var 0 is arg0 [Ljava/lang/String; from Label0 to Label1
        code += self.emit.emitREADVAR('this', self.className, 0, frame)             # aload_0
        code += self.emit.emitINVOKESPECIAL(frame)                                  # invokespecial java/lang/Object/<init>()V
        code += self.emit.emitLABEL(endLabel, frame)                                # Label1
        code += self.emit.emitRETURN(VoidType(), frame)                             # return
        code += self.emit.emitENDMETHOD(frame)                                      # .end method
        self.emit.printout(code)
        frame.exitScope()
        
        
        # Init static Zcode - Contructor for static
        frame = Frame('<clinit>', VoidType())
        self.emit.printout(self.emit.emitMETHOD("<clinit>", ZType([], VoidType()), True, frame))
        
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.globalDecl = True    
        for decl in ast.decl:
            if (type(decl) is VarDecl) and (decl.varInit or (type(decl.varType) is ArrayType)):
                self.visit(decl, Access(frame, None, False))
        self.globalDecl = False
        
        code = self.emit.emitRETURN(VoidType(), frame)
        code += self.emit.emitLABEL(frame.getEndLabel(), frame)
        code += self.emit.emitENDMETHOD(frame)
        self.emit.printout(code)
        frame.exitScope()
    
        
        # Initiate for normal function
        for funcDecl in list(filter(lambda x: type(x) is FuncDecl, ast.decl)):
            self.visit(funcDecl, None)    
        

        self.emit.emitEPILOG()
        
        return o
     
    
    # TODO :() 
    def visitVarDecl(self, ast, o):
        # name: Id
        # varType: Type = None  # None if there is no type
        # modifier: str = None  # None if there is no modifier
        # varInit: Expr = None  # None if there is no initial
        
        # print('visitVarDecl')

        if not self.isInferred:
            sym = Symbol(ast.name.name, ast.varType, None)
            o[0].append(sym)
            ast.name.sym = sym

            if ast.varInit:
                rhs = self.visit(ast.varInit, o)
                lhs = self.visit(ast.name, o)
                self.inferType(lhs, rhs)

        else:
            frame = o.frame
            
            if self.globalDecl:
                if ast.varInit is not None:
                    code = self.visit(ast.varInit, Access(frame, None, False))[0]
                    code += self.visit(ast.name, Access(frame, None, True))[0]
                else:
                    code = self.initArray(ast, o)

                self.emit.printout(code)
                
            else:
                # print("vardecl ",ast.name.name)
                idx = frame.getNewIndex()
                
                startLabel = frame.getStartLabel()
                endLabel = frame.getEndLabel()
                
                ast.name.sym.value = Index(idx)
                code = self.emit.emitVAR(idx, ast.name.name, ast.name.sym.ztype, startLabel, endLabel, frame)
                
                if (not ast.varInit) and (type(ast.name.sym.ztype) is ArrayType):
                    code += self.initArray(ast, o)
                
                if ast.varInit is not None:
                    code += self.visit(ast.varInit, Access(frame, None, False))[0]
                    code += self.visit(ast.name, Access(frame, None, True))[0]
                
                self.emit.printout(code)

        
    # TODO :()                        
    def visitFuncDecl(self, ast, o):
        # name: Id
        # param: List[VarDecl]  # empty list if there is no parameter
        # body: Stmt = None  # None if this is just a declaration-part
        
        if not self.isInferred:
            if ast.body is None:
                ztype = ZType([x.varType for x in ast.param], None)
                self.funcList[ast.name.name] = Symbol(ast.name.name, ztype, CName(self.className))
            
            else:
                newEnv = [[]] + o
                for x in ast.param:
                    self.visit(x, newEnv)
 
                self.returnStmt = False
                
                func = self.funcList.get(ast.name.name)
                if func:
                    self.func = func
                else:
                    ztype = ZType([x.varType for x in ast.param], None)
                    self.func = Symbol(ast.name.name, ztype, CName(self.className))
                    self.funcList[ast.name.name] = self.func
                
                self.visit(ast.body, newEnv)
                if not self.returnStmt: 
                    self.func.ztype.returnType = VoidType()
        
        else:
            if ast.body is not None:
                func = self.funcList.get(ast.name.name)
                self.genCodeMethod(ast, o, Frame(ast.name.name, func.ztype.returnType))
        
        
        
        
    # ...
    def genCodeMethod(self, decl: FuncDecl, o, frame):
        sym = self.funcList.get(decl.name.name)
        returnType = sym.ztype.returnType
        isMain = decl.name.name == "main" 

        # print("genMETHOD", decl.name.name, returnType)

        if not isMain:
            self.emit.printout(
                self.emit.emitMETHOD(decl.name.name, sym.ztype, True, frame)
            )
        else:
            self.emit.printout(
                self.emit.emitMETHOD(
                    'main',
                    ZType([ArrayType([1], StringType())], VoidType()),
                    True, 
                    frame
                )
            )

        frame.enterScope(True)
        body = decl.body
        # print(decl)
        
        # Generate code for parameter declarations
        code = ''
        if isMain:
            code = self.emit.emitVAR(
                frame.getNewIndex(), 
                "args", 
                ArrayType([], StringType()),
                frame.getStartLabel(), 
                frame.getEndLabel(), 
                frame
            )
            
        else:
            for x in decl.param:
                idx = frame.getNewIndex()
                x.name.sym.value = Index(idx)
                # print("param",id(x.name.name))
                code += self.emit.emitVAR(
                    idx, 
                    x.name.name, 
                    x.name.sym.ztype, 
                    frame.getStartLabel(), 
                    frame.getEndLabel(), 
                    frame
                )
        
        self.emit.printout(code)
        
        # Generate code for start label
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        # Generate code for statements
        self.visit(body, SubBody(frame, None))

        # Generate code for end label
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
        # ???
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()



# ----------------------------------------------------------------------------------------------------------------------------------    
    # TODO :()
    def visitCallExpr(self, ast, o):
        # name: Id
        # args: List[Expr]

        func = self.funcList[ast.name.name]
        
        if not self.isInferred:
            args = [self.visit(arg, o) for arg in ast.args]
            for arg, argType in zip(args, func.ztype.paramType):
                if type(arg) is Symbol:
                    self.setType(arg, argType)
            
            return func.ztype.returnType if func.ztype.returnType else func
                    
        else:
            code = ''
            for x in ast.args:
                code += self.visit(x, Access(o.frame, None, False))[0]
            
            code += self.emit.emitINVOKESTATIC(f'{func.value.value}/{ast.name.name}', func.ztype, o.frame)
            return code, func.ztype.returnType    

    
    # TODO :()
    def visitBinaryOp(self, ast: BinaryOp, o):
        # op: str
        # left: Expr
        # right: Expr
        
        op = ast.op    
        
        if not self.isInferred:
            left = self.visit(ast.left, o)
            if type(left) is Symbol:
                self.setType(left, self.binaryInput[op])
            
            right = self.visit(ast.right, o)
            if type(right) is Symbol:
                self.setType(right, self.binaryInput[op])
                
            return self.binaryOutput[op]
            
        else:
            frame = o.frame    
            
            codeLeft, _ = self.visit(ast.left, o)
            codeRight, _ = self.visit(ast.right, o)
            
            code = codeLeft + codeRight
            
            inputType = self.binaryInput[op]
            outputType = self.binaryOutput[op]
            
            if op in ['+', '-']:
                code += self.emit.emitADDOP(op, inputType, frame)
            elif op in ['*', '/']:
                code += self.emit.emitMULOP(op, inputType, frame)
            elif op in ['%']:
                code += self.emit.emitMOD(frame)
            elif op in ["and"]:
                code += self.emit.emitANDOP(frame)
            elif op in ["or"]:
                code += self.emit.emitOROP(frame)
            elif op in ['=', '!=', '<', '>', '>=', '<=']:
                code += self.emit.emitREOP(op, inputType, frame)
            elif op in ['==']:
                code += self.emit.emitINVOKEVIRTUAL("java/lang/String.equals(Ljava/lang/Object;)", BoolType(), frame, 1)
            elif op in ['...']:
                code += self.emit.emitINVOKEVIRTUAL("java/lang/String.concat(Ljava/lang/String;)", StringType(), frame, 1)
            
            return code, outputType
        
        
    # TODO :()
    def visitUnaryOp(self, ast: UnaryOp, o):
        # op: str
        # operand: Expr
        op = ast.op
        
        if not self.isInferred:
            right = self.visit(ast.operand, o)
            
            if type(right) is Symbol:
                self.setType(right, self.unaryInput[op])
            
            return self.unaryOutput[op]
            
        else:
            frame = o.frame
            inputType = self.unaryInput[op]
            outputType = self.unaryOutput[op]
            
            code = self.visit(ast.operand, o)[0]
            if (op == '-'):
                 code += self.emit.emitNEGOP(inputType, frame)
            elif (op == 'not'): 
                code += self.emit.emitNOT(inputType, frame)
            
            return code, outputType
        
        

    
    
    

# ----------------------------------------------------------------------------------------------------------------------------------    
    # TODO :()
    def visitReturn(self, ast, o):
        # expr: Expr = None  # None if there is no expression after return
        self.returnStmt = True
        
        if not self.isInferred:
            returnType = self.visit(ast.expr, o) if ast.expr else VoidType()
            
            if isinstance(returnType, Symbol):
                self.setType(returnType, self.func.ztype.returnType)
            
            elif not self.func.ztype.returnType:
                self.func.ztype.returnType = returnType
        
        else:
            frame = o.frame
            
            if ast.expr is None:
                code = self.emit.emitRETURN(VoidType(), o.frame)
    
            else:
                code = self.visit(ast.expr, Access(o.frame, None, False))[0]
                code += self.emit.emitRETURN(o.frame.returnType, o.frame) # ??? o.frame.returnType

            self.emit.printout(code)
        
        
        
    # TODO :()
    def visitAssign(self, ast: Assign, o):
        # lhs: Expr
        # exp: Expr
                
        if not self.isInferred:
            rhs = self.visit(ast.rhs, o)
            lhs = self.visit(ast.lhs, o)
            
            self.inferType(lhs, rhs)
        
        else:
            frame = o.frame          
            
            if type(ast.lhs) is ArrayCell:
                lhsCode, lhsTyp = self.visit(ast.lhs, Access(frame, None, True))
                rhsCode, rhsTyp = self.visit(ast.rhs, Access(frame, None, False))
                
                code = lhsCode + rhsCode + self.emit.emitASTORE(lhsTyp, frame)
                # print(f'visitAssign {code}')
            else:
                rhsCode, rhsTyp = self.visit(ast.rhs, Access(frame, None, False))
                lhsCode, lhsTyp = self.visit(ast.lhs, Access(frame, None, True)) 
                code = rhsCode + lhsCode
            
            self.emit.printout(code)
 
 
  
    # TODO :()
    def visitCallStmt(self, ast, o):
        # name: Id
        # args: List[Expr]  # empty list if there is no argument
        
        func = self.funcList[ast.name.name]
        
        if not self.isInferred:
            args = [self.visit(arg, o) for arg in ast.args]
            for arg, argType in zip(args, func.ztype.paramType):
                if type(arg) is Symbol:
                    self.setType(arg, argType)
            
            return VoidType()
                    
        else:
            code = ''
            for x in ast.args:
                code += self.visit(x, Access(o.frame, None, False))[0]
            
            code += self.emit.emitINVOKESTATIC(f'{func.value.value}/{func.name}', func.ztype, o.frame)
            self.emit.printout(code)
    
  
    # TODO :()  
    def visitBlock(self, ast, o):
        # stmt: List[Stmt]  # empty list if there is no statement in block
        
        if not self.isInferred:
            newEnv = [[]] + o
            for x in ast.stmt:
                self.visit(x, newEnv)
        else:
            frame = o.frame
            
            frame.enterScope(False)
            self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
            for stmt in ast.stmt: 
                self.visit(stmt, SubBody(frame, None))
                
            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
            frame.exitScope()
    
    
    # TODO :()    
    def visitIf(self, ast, o):
        # expr: Expr
        # thenStmt: Stmt
        # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
        # elseStmt: Stmt = None  # None if there is no else branch
        
        if not self.isInferred:
            cond = self.visit(ast.expr, o)
            if isinstance(cond, Symbol):
                self.setType(cond, BoolType())
            self.visit(ast.thenStmt, o)

            for cond, stmt in ast.elifStmt:
                cond = self.visit(cond, o)
                if isinstance(cond, Symbol):
                    self.setType(cond, BoolType())
                self.visit(stmt, o)
    
            if ast.elseStmt:
                self.visit(ast.elseStmt, o)
        else:
            frame = o.frame
            
            elifFound = bool(len(ast.elifStmt) != 0)
            elseFound = bool(ast.elseStmt is not None)
            
            code = self.visit(ast.expr, Access(frame, None, False))[0]
            
            endIfLabel = frame.getNewLabel()
            
            code += self.emit.emitIFFALSE(endIfLabel, frame)
            self.emit.printout(code)  
            self.visit(ast.thenStmt, Access(frame, None, False))               

            if elifFound or elseFound:
                exitIfLabel = frame.getNewLabel()
                self.emit.printout(self.emit.emitGOTO(exitIfLabel, frame))
            
            code = self.emit.emitLABEL(endIfLabel, o.frame)
            self.emit.printout(code)
            

            for cond, stmt in ast.elifStmt:
                code = self.visit(cond, Access(frame, None, False))[0]
                
                nextLabel = frame.getNewLabel() 
                code += self.emit.emitIFFALSE(nextLabel, frame)
                self.emit.printout(code)
                
                self.visit(stmt, Access(frame, None, False))
                code =  self.emit.emitGOTO(exitIfLabel, frame)
                
                code += self.emit.emitLABEL(nextLabel, frame)
                self.emit.printout(code)
                    
            if elseFound:
                self.visit(ast.elseStmt, Access(frame, None, False))
                code =  self.emit.emitGOTO(exitIfLabel, frame)
                self.emit.printout(code)
                    
            if elifFound or elseFound:   
                self.emit.printout(self.emit.emitLABEL(exitIfLabel, frame))
         
        
    # TODO :()
    def visitFor(self, ast, o):
        # name: Id
        # condExpr: Expr
        # updExpr: Expr
        # body: Stmt
        
        if not self.isInferred:
            counter = self.visit(ast.name, o)
            if type(counter) is Symbol:
                self.setType(counter, NumberType())

            condExpr = self.visit(ast.condExpr, o)
            if type(condExpr) is Symbol:
                self.setType(condExpr, BoolType())

            updExpr = self.visit(ast.updExpr, o)
            if type(updExpr) is Symbol:
                self.setType(updExpr, NumberType())

            self.visit(ast.body, o)
            
        else:
            frame = o.frame
            
            frame.enterLoop()   # ----------------------------------------------------------------------------
            
            continueLabel = frame.getContinueLabel()
            breakLabel = frame.getBreakLabel()
            startLoopLabel = frame.getNewLabel()
            
            idx = frame.getNewIndex()
            code = self.visit(ast.name, Access(frame, None, False))[0]
            self.emit.printout(code)
            
            # Put startLoop label
            code = self.emit.emitLABEL(startLoopLabel, frame)
            self.emit.printout(code)
            
            # Check condition
            code = self.visit(ast.condExpr, Access(frame, None, False))[0]
            code += self.emit.emitIFTRUE(breakLabel, frame)
            self.emit.printout(code)
            
            self.visit(ast.body, Access(frame, None, False))
            
            self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
            updStmt = Assign(ast.name, BinaryOp('+', ast.name, ast.updExpr))
            self.visit(updStmt, Access(frame, None, False))
            
            code = self.emit.emitGOTO(startLoopLabel, frame)      
            code += self.emit.emitLABEL(breakLabel, frame)
            self.emit.printout(code)
            
            # Restore value for the counter
            code = self.visit(ast.name, Access(frame, None, True))[0]   # write dup value about to id
            self.emit.printout(code)
            
            frame.exitLoop()    # ----------------------------------------------------------------------------

    
    def visitContinue(self, ast, o):
        if self.isInferred:
            self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    
    def visitBreak(self, ast, o):
        if self.isInferred:
            self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
        



    
# ----------------------------------------------------------------------------------------------------------------------------------    
    # TODO :()
    def visitArrayLiteral(self, ast, o):
        # print('visitArrayLiteral')
        
        if not self.isInferred:
            baseTyp = None
            for x in ast.value:
                tmp = self.visit(x, o)
                if (not baseTyp) and isinstance(tmp, (BoolType, StringType, NumberType, ArrayType)):
                    baseTyp = tmp
                    break

            if baseTyp is None:
                return [self.visit(x, o) for x in ast.value]
            
            for x in ast.value:
                value = self.visit(x, o)
                self.inferType(value, baseTyp)

        
            if isinstance(baseTyp, (BoolType, StringType, NumberType)):
                return ArrayType([len(ast.value)], baseTyp)
           
            return ArrayType([len(ast.value)] + baseTyp.size, baseTyp.eleType)
        
        else:
            frame = o.frame
            
            baseTyp = None
            o.isLeft = False
            for x in ast.value:
                _, typ = self.visit(x, o)
                if (not baseTyp) and isinstance(typ, (BoolType, StringType, NumberType, ArrayType)):
                    baseTyp = typ
                    break
            
            
            # 1D array
            if isinstance(baseTyp, (BoolType, StringType, NumberType)):
                code = self.emit.emitPUSHICONST(len(ast.value), frame)
                code += self.emit.emitNEWARRAY(baseTyp, frame)
                
                for idx, value in zip(range(0, len(ast.value)), ast.value):
                    code += self.emit.emitDUP(frame)
                    code += self.emit.emitPUSHICONST(idx, frame)
                    code += self.visit(value, o)[0]
                    code += self.emit.emitASTORE(baseTyp, frame)
                    
                return code, ArrayType([len(ast.value)], baseTyp)
            
            # Multi-D array
            else:
                code = self.emit.emitPUSHICONST(len(ast.value), frame)
                code += self.emit.emitANEWARRAY(baseTyp, frame)
                
                for idx, value in zip(range(0, len(ast.value)), ast.value):
                    code += self.emit.emitDUP(frame)
                    code += self.emit.emitPUSHICONST(idx, frame)
                    code += self.visit(value, o)[0]
                    code += self.emit.emitASTORE(baseTyp, frame)
                return code, ArrayType([len(ast.value)] + baseTyp.size, baseTyp.eleType)


     
    # TODO :()
    def visitArrayCell(self, ast, o):
        # arr: Expr
        # idx: List[Expr]
        
        # print('visitArrayCell')
        
        if not self.isInferred:
            arr = self.visit(ast.arr, o)
            for x in ast.idx:
                idx = self.visit(x, o)
                if type(idx) is Symbol:
                    self.setType(idx, NumberType())
                
            if len(ast.idx) == len(arr.size):
                return arr.eleType
            elif len(ast.idx) < len(arr.size):
                return ArrayType(arr.size[len(ast.idx):], arr.eleType)
        
        else:
            frame = o.frame
            cellCode, cellType = self.visit(ast.arr, Access(frame, None, False))
            
            code = cellCode
            # print('***', code)
            for i in range(len(ast.idx) - 1):
                code += self.visit(ast.idx[i], Access(frame, None, False))[0]   # symbol
                code += self.emit.emitF2I(frame)
                code += self.emit.emitALOAD(ArrayType([], None), frame)
                
            code += self.visit(ast.idx[-1], Access(frame, None, False))[0]      # symbol
            code += self.emit.emitF2I(frame)
            
            if o.isLeft:
                if len(ast.idx) == len(cellType.size):
                    returnType = cellType.eleType
                else:
                    returnType = ArrayType(cellType.size[len(ast.idx):], cellType.eleType)
            else:
                if len(ast.idx) == len(cellType.size):
                    code += self.emit.emitALOAD(cellType.eleType, frame)
                    returnType = cellType.eleType
                else:
                    code += self.emit.emitALOAD(ArrayType([], None), frame)
                    returnType = ArrayType(cellType.size[len(ast.idx):], cellType.eleType)
            
            # print('visitArrayCell:     ', code)
            
            return code, returnType
    
         
    def visitNumberLiteral(self, ast, o):
        # value: float
        if not self.isInferred:
            return NumberType()
        else:
            return self.emit.emitPUSHCONST(ast.value, NumberType(), o.frame), NumberType()
    
    
    def visitBooleanLiteral(self, ast, o):
        # value: bool
        if not self.isInferred:
            return BoolType()
        else:
            return self.emit.emitPUSHCONST(ast.value, BoolType(), o.frame), BoolType()

     
    def visitStringLiteral(self, ast, o):
        # value: string
        if not self.isInferred:
            return StringType()
        else:
            return self.emit.emitPUSHCONST(f'"{ast.value}"', StringType(), o.frame), StringType()
    
    
    def visitId(self, ast, o):
        if not self.isInferred:
            for env in o:
                x = list(filter(lambda x: x.name == ast.name, env))  # Assume code pass static check --> must have a name in o
                if len(x) > 0:
                    x = x[0]
                    
                    if not hasattr(ast, 'sym'):
                        ast.sym = x
                    if isDeterminedType(x.ztype):
                        return x.ztype
                    else:
                        # print(x)
                        return x
            
        else:
            sym = ast.sym
            typ = sym.ztype
            value = sym.value.value
            name = sym.name
            frame = o.frame
            
            # print (f'{ast.name}   {sym.name}  {sym.ztype}')
            if o.isLeft:
                if type(sym.value) is Index:
                    return self.emit.emitWRITEVAR(sym.name, sym.ztype, sym.value.value, o.frame), sym.ztype # ....
                elif type(sym.value) is CName: 
                    return self.emit.emitPUTSTATIC(f'{sym.value.value}.{name}', typ, frame), typ
            
            else:
                if type(sym.value) is Index:
                    return self.emit.emitREADVAR(name, typ, value, frame), typ
                elif type(sym.value) is CName:
                    return self.emit.emitGETSTATIC(f'{sym.value.value}.{name}', typ, frame), typ
            
      
    
    
    
    
# ----------------------------------------------------------------------------------------------------------------------------------         
    def visitArrayType(self, ast, param):
        if not self.isInferred:
            return ast
        return None, ast
    
    
    def visitNumberType(self, ast, param):
        if not self.isInferred:
            return NumberType()
        return None, NumberType()
    
    
    def visitVoidType(self, ast, param):
        if not self.isInferred:
            return VoidType()
        return None, VoidType()
    
    
    def visitBoolType(self, ast, param):
        if not self.isInferred:
            return BoolType()
        return None, BoolType()
    
    
    def visitStringType(self, ast, param):
        if not self.isInferred:
            return StringType()
        return None, StringType()
    
    
    def visitFuncZcode(self, ast, param):
        return None, ast.typ if ast.typ else ast
    
    
    def visitVarZcode(self, ast, param):
        return None, ast.typ if ast.typ else ast
    