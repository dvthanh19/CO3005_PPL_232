from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

    

class ASTGeneration(ZCodeVisitor):
    # program:		NEWLINE* declare_list EOF;
    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.declare_list()))

    
    
    # declare_list: 	declare declare_list | declare;
    # Visit a parse tree produced by ZCodeParser#declare_list.
    def visitDeclare_list(self, ctx: ZCodeParser.Declare_listContext):
        return ([self.visit(ctx.declare())] + self.visit(ctx.declare_list())) if (ctx.declare_list()) else [self.visit(ctx.declare())]

    # declare:		var_declare newlines | func_declare;
    # Visit a parse tree produced by ZCodeParser#declare.
    def visitDeclare(self, ctx: ZCodeParser.DeclareContext):
        return self.visit(ctx.var_declare()) if (ctx.var_declare()) else self.visit(ctx.func_declare())


    
    # var_declare: 	implicit_var | keyword_var | dynamic_var;
    # Visit a parse tree produced by ZCodeParser#var_declare.
    def visitVar_declare(self, ctx: ZCodeParser.Var_declareContext):
        return self.visit(ctx.getChild(0))


    
    # implicit_var:	VAR IDENTIFIER ASSIGN_OPS expr;
    # Visit a parse tree produced by ZCodeParser#implicit_var.
    def visitImplicit_var(self, ctx: ZCodeParser.Implicit_varContext):
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, 'var', self.visit(ctx.expr()))


    
    # keyword_var:	typ IDENTIFIER (LSB numList_prime RSB)? (ASSIGN_OPS expr)?; 
    # Visit a parse tree produced by ZCodeParser#keyword_var.
    def visitKeyword_var(self, ctx: ZCodeParser.Keyword_varContext):
        varType = self.visit(ctx.typ())
        if (ctx.numList_prime()): 
            varType = ArrayType(self.visit(ctx.numList_prime()), varType)
    
        varInit = self.visit(ctx.expr()) if (ctx.expr()) else None
        
        return VarDecl(Id(ctx.IDENTIFIER().getText()), varType, None, varInit)


    
    # dynamic_var:	DYNAMIC IDENTIFIER (ASSIGN_OPS expr)?;   
    # Visit a parse tree produced by ZCodeParser#dynamic_var.
    def visitDynamic_var(self, ctx: ZCodeParser.Dynamic_varContext):
        varInit = self.visit(ctx.expr()) if (ctx.expr()) else None
        
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, 'dynamic', varInit)

    
    
    # func_declare:	FUNC IDENTIFIER LB paramList RB body;
    # Visit a parse tree produced by ZCodeParser#func_declare.
    def visitFunc_declare(self, ctx:ZCodeParser.Func_declareContext):
        return FuncDecl(
            Id(ctx.IDENTIFIER().getText()), 
            self.visit(ctx.paramList()), 
            self.visit(ctx.body())
        )
 

    
    # body:			newlines? (return_stmt | block_stmt) | newlines;
    # Visit a parse tree produced by ZCodeParser#body.
    def visitBody(self, ctx: ZCodeParser.BodyContext):      
        if (ctx.return_stmt()):
            return self.visit(ctx.return_stmt())
        elif (ctx.block_stmt()):
            return self.visit(ctx.block_stmt())
        
        return None


    
    # expr: 			expr_concat;
    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx: ZCodeParser.ExprContext):
        return self.visit(ctx.expr_concat())



    # expr_concat:	expr_rela CONCAT_OPS expr_rela | expr_rela; 								// (1)
    # Visit a parse tree produced by ZCodeParser#expr_concat.
    def visitExpr_concat(self, ctx: ZCodeParser.Expr_concatContext):
        if (ctx.getChildCount() == 3):
            return BinaryOp(
                ctx.getChild(1).getText(), 
                self.visit(ctx.expr_rela()[0]), 
                self.visit(ctx.expr_rela()[1])
            )
            
        return self.visit(ctx.expr_rela(0))
    
    

    # expr_rela:		expr_logic (EQS | EQ | NEQ | LT | LEQ | GT | GEQ) expr_logic | expr_logic;	// (2)    
    # Visit a parse tree produced by ZCodeParser#expr_rela.
    def visitExpr_rela(self, ctx: ZCodeParser.Expr_relaContext):
        if (ctx.getChildCount() == 3):
            return BinaryOp(
                ctx.getChild(1).getText(), 
                self.visit(ctx.expr_logic(0)), 
                self.visit(ctx.expr_logic(1))
            )
            
        return self.visit(ctx.expr_logic(0))
        

    
    # expr_logic: 	expr_logic (AND | OR) expr_add | expr_add;									// (3)
    # Visit a parse tree produced by ZCodeParser#expr_logic.
    def visitExpr_logic(self, ctx:ZCodeParser.Expr_logicContext):
        if (ctx.getChildCount() == 3):
            return BinaryOp(
                ctx.getChild(1).getText(), 
                self.visit(ctx.expr_logic()), 
                self.visit(ctx.expr_add())
            )
            
        return self.visit(ctx.expr_add())
        


    # expr_add:		expr_add (ADD_OPS | SUB_OPS) expr_mul | expr_mul;							// (4)
    # Visit a parse tree produced by ZCodeParser#expr_add.
    def visitExpr_add(self, ctx:ZCodeParser.Expr_addContext):
        if (ctx.getChildCount() == 3):
            return BinaryOp(
                ctx.getChild(1).getText(), 
                self.visit(ctx.expr_add()), 
                self.visit(ctx.expr_mul())
            )
            
        return self.visit(ctx.expr_mul())

    
    
    # expr_mul:		expr_mul (MUL_OPS | DIV_OPS | MOD_OPS) expr_not | expr_not;					// (5)
    # Visit a parse tree produced by ZCodeParser#expr_mul.
    def visitExpr_mul(self, ctx:ZCodeParser.Expr_mulContext):
        if (ctx.getChildCount() == 3):
            return BinaryOp(
                ctx.getChild(1).getText(), 
                self.visit(ctx.expr_mul()), 
                self.visit(ctx.expr_not())
            )
        
        return self.visit(ctx.expr_not())


    
    # expr_not:  		NOT expr_not | expr_sign;											// (6)
    # Visit a parse tree produced by ZCodeParser#expr_not.
    def visitExpr_not(self, ctx:ZCodeParser.Expr_notContext):
        if (ctx.getChildCount() == 2):
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.expr_not()))
        
        return self.visit(ctx.expr_sign())


   
   # expr_sign:		SUB_OPS expr_sign | expr_idx;												// (7)
    # Visit a parse tree produced by ZCodeParser#expr_sign.
    def visitExpr_sign(self, ctx:ZCodeParser.Expr_signContext):
        if (ctx.getChildCount() == 2):
            return UnaryOp(ctx.SUB_OPS().getText(), self.visit(ctx.expr_sign()))
        
        return self.visit(ctx.expr_idx())


    
    # expr_idx:		(IDENTIFIER | funcCall) LSB exprList_prime RSB | operand;					// (8) Index
    # Visit a parse tree produced by ZCodeParser#expr_idx.
    def visitExpr_idx(self, ctx:ZCodeParser.Expr_idxContext):
        if (ctx.getChildCount() == 4):
            arr_name = None
            if (ctx.IDENTIFIER()):
                arr_name = Id(ctx.IDENTIFIER().getText())
            elif (ctx.funcCall()):
                arr_name = self.visit(ctx.funcCall())
            
            return ArrayCell(arr_name, self.visit(ctx.exprList_prime()))
        
        return self.visit(ctx.operand())
    
    
    # operand: 		IDENTIFIER | literal | LB expr RB | funcCall;								// (9) Operands
    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx: ZCodeParser.OperandContext):
        if (ctx.IDENTIFIER()):
            return Id(ctx.IDENTIFIER().getText())
        elif (ctx.literal()):
            return self.visit(ctx.literal())
        elif (ctx.expr()):
            return self.visit(ctx.expr())
        elif (ctx.funcCall()):
            return self.visit(ctx.funcCall())
    
    
    
    # funcCall:		IDENTIFIER LB argList RB;
    # Visit a parse tree produced by ZCodeParser#funcCall.
    def visitFuncCall(self, ctx: ZCodeParser.FuncCallContext):
        return CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.argList()))

    
    
    # literal:		NUM_LIT | STRING_LIT | BOOL_LIT | array_lit;
    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx: ZCodeParser.LiteralContext):
        if (ctx.NUM_LIT()):
            return NumberLiteral(float(ctx.NUM_LIT().getText()))
        elif (ctx.STRING_LIT()):
            return StringLiteral(ctx.STRING_LIT().getText())
        elif (ctx.BOOL_LIT()):
            return BooleanLiteral(ctx.BOOL_LIT().getText()  == 'true')
        elif (ctx.array_lit()):
            return self.visit(ctx.array_lit())
    

    
    # array_lit:		LSB exprList_prime RSB;
    # Visit a parse tree produced by ZCodeParser#array_lit.
    def visitArray_lit(self, ctx:ZCodeParser.Array_litContext):
        return ArrayLiteral(self.visit(ctx.exprList_prime()))


    
    # stmt:   if_stmt|for_stmt|decl_stmt|assign_stmt|break_stmt|continue_stmt|return_stmt|funcCall_stmt|block_stmt;
    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visit(ctx.getChild(0))



    # if_stmt:			(IF LB expr RB newlines? stmt) (elif_stmtList) (else_stmt)?;
    def visitIf_stmt(self, ctx: ZCodeParser.If_stmtContext):
        return If(
            self.visit(ctx.expr()), 
            self.visit(ctx.stmt()),
            self.visit(ctx.elif_stmtList()),
            self.visit(ctx.else_stmt()) if (ctx.else_stmt()) else None
        )

    # elif_stmtList:		elif_stmt elif_stmtTail | ;
    # Visit a parse tree produced by ZCodeParser#elif_stmtList.
    def visitElif_stmtList(self, ctx: ZCodeParser.Elif_stmtListContext):
        return ([self.visit(ctx.elif_stmt())] + self.visit(ctx.elif_stmtList())) if (ctx.elif_stmtList()) else []
    
 
    
    # elif_stmt:			ELIF LB expr RB newlines? stmt;
    # Visit a parse tree produced by ZCodeParser#elif_stmt.
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        return (self.visit(ctx.expr()), self.visit(ctx.stmt()))

    # # else_stmt:			ELSE newlines? stmt;
    # # Visit a parse tree produced by ZCodeParser#else_stmt.
    def visitElse_stmt(self, ctx:ZCodeParser.Else_stmtContext):
        return self.visit(ctx.stmt())
    
    
    
    # for_stmt:			FOR IDENTIFIER UNTIL expr BY expr newlines? stmt;
    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx: ZCodeParser.For_stmtContext):
        return For(
            Id(ctx.IDENTIFIER().getText()), 
            self.visit(ctx.expr(0)),
            self.visit(ctx.expr(1)),
            self.visit(ctx.stmt())
        )


    
    # decl_stmt:			var_declare newlines;
    # Visit a parse tree produced by ZCodeParser#decl_stmt.
    def visitDecl_stmt(self, ctx: ZCodeParser.Decl_stmtContext):
        return self.visit(ctx.var_declare())


    
    # assign_stmt:		leftSide ASSIGN_OPS expr newlines;
    # Visit a parse tree produced by ZCodeParser#assign_stmt.
    def visitAssign_stmt(self, ctx: ZCodeParser.Assign_stmtContext):
        return Assign(self.visit(ctx.leftSide()), self.visit(ctx.expr()))

    
    
    # leftSide:			IDENTIFIER (LSB exprList_prime RSB)?;
    # Visit a parse tree produced by ZCodeParser#leftSide.
    def visitLeftSide(self, ctx: ZCodeParser.LeftSideContext):
        if (ctx.exprList_prime()):
            return ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.exprList_prime()))
        return Id(ctx.IDENTIFIER().getText())
    #note
    
    
    # break_stmt:			BREAK newlines;
    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx: ZCodeParser.Break_stmtContext):
        return Break()


    
    # continue_stmt:		CONTINUE newlines;
    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx: ZCodeParser.Continue_stmtContext):
        return Continue()


    
    # return_stmt:		RETURN expr? newlines;
    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx: ZCodeParser.Return_stmtContext):
        return Return(self.visit(ctx.expr()) if (ctx.expr()) else None)


    
    # funcCall_stmt:		IDENTIFIER LB argList RB newlines;
    # Visit a parse tree produced by ZCodeParser#funcCall_stmt.
    def visitFuncCall_stmt(self, ctx: ZCodeParser.FuncCall_stmtContext):
        return CallStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.argList()))


    
    # block_stmt: 		BEGIN newlines stmtList END newlines;
    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx: ZCodeParser.Block_stmtContext):
        return Block(self.visit(ctx.stmtList()))
    

      
    # typ:			NUM_TYP | BOOL_TYP | STR_TYP;
    # Visit a parse tree produced by ZCodeParser#typ.
    def visitTyp(self, ctx: ZCodeParser.TypContext):
        return NumberType() if (ctx.NUM_TYP()) else BoolType() if (ctx.BOOL_TYP()) else StringType()
    
    
    
    # paramList:		paramList_prime | ;
    # Visit a parse tree produced by ZCodeParser#paramList.
    def visitParamList(self, ctx:ZCodeParser.ParamListContext):
        return self.visit(ctx.paramList_prime()) if (ctx.paramList_prime()) else []
    
    # paramList_prime:param COMMA paramList_prime | param;
    # Visit a parse tree produced by ZCodeParser#paramList_prime.
    def visitParamList_prime(self, ctx:ZCodeParser.ParamList_primeContext):
        return ([self.visit(ctx.param())] + self.visit(ctx.paramList_prime())) if (ctx.paramList_prime()) else [self.visit(ctx.param())]

    # param:			typ IDENTIFIER (LSB numList_prime RSB)?;
    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):    
        varType = self.visit(ctx.typ())
        if (ctx.numList_prime()): varType = ArrayType(self.visit(ctx.numList_prime()), varType)
        
        return VarDecl(Id(ctx.IDENTIFIER().getText()), varType, None, None)
    
    
    
    # numList:		numList_prime | ;
    # Visit a parse tree produced by ZCodeParser#numList.
    def visitNumList(self, ctx: ZCodeParser.NumListContext):
        return self.visit(ctx.numList_prime()) if (ctx.numList_prime()) else []

    # numList_prime:	NUM_LIT COMMA numList_prime| NUM_LIT;
    # Visit a parse tree produced by ZCodeParser#numList_prime.
    def visitNumList_prime(self, ctx: ZCodeParser.NumList_primeContext):
        return ([float(ctx.NUM_LIT().getText())] + self.visit(ctx.numList_prime())) if (ctx.numList_prime()) else [float(ctx.NUM_LIT().getText())]


    
    # argList:		exprList;
    # Visit a parse tree produced by ZCodeParser#argList.
    def visitArgList(self, ctx: ZCodeParser.ArgListContext):
        return self.visit(ctx.exprList())
    
    # exprList:		exprList_prime | ;
    # Visit a parse tree produced by ZCodeParser#exprList.
    def visitExprList(self, ctx: ZCodeParser.ExprListContext):
        return self.visit(ctx.exprList_prime()) if (ctx.exprList_prime()) else []

    # exprList_prime: expr COMMA exprList_prime | expr;
    # Visit a parse tree produced by ZCodeParser#exprList_prime.
    def visitExprList_prime(self, ctx: ZCodeParser.ExprList_primeContext):
        return ([self.visit(ctx.expr())] + self.visit(ctx.exprList_prime())) if (ctx.exprList_prime()) else [self.visit(ctx.expr())]

    
    
    # stmtList: 		stmtList_prime | ;
    # Visit a parse tree produced by ZCodeParser#stmtList.
    def visitStmtList(self, ctx: ZCodeParser.StmtListContext):
        return self.visit(ctx.stmtList_prime()) if ctx.stmtList_prime() else []

    # stmtList_prime:	stmt stmtList_prime | stmt;
    # Visit a parse tree produced by ZCodeParser#stmtList_prime.
    def visitStmtList_prime(self, ctx: ZCodeParser.StmtList_primeContext):
        return ([self.visit(ctx.stmt())] + self.visit(ctx.stmtList_prime())) if ctx.stmtList_prime() else [self.visit(ctx.stmt())]
