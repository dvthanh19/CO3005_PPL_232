# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declare_list.
    def visitDeclare_list(self, ctx:ZCodeParser.Declare_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declare.
    def visitDeclare(self, ctx:ZCodeParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newlines.
    def visitNewlines(self, ctx:ZCodeParser.NewlinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_declare.
    def visitVar_declare(self, ctx:ZCodeParser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_var.
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#keyword_var.
    def visitKeyword_var(self, ctx:ZCodeParser.Keyword_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dynamic_var.
    def visitDynamic_var(self, ctx:ZCodeParser.Dynamic_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_declare.
    def visitFunc_declare(self, ctx:ZCodeParser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#body.
    def visitBody(self, ctx:ZCodeParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_concat.
    def visitExpr_concat(self, ctx:ZCodeParser.Expr_concatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_rela.
    def visitExpr_rela(self, ctx:ZCodeParser.Expr_relaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_logic.
    def visitExpr_logic(self, ctx:ZCodeParser.Expr_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_add.
    def visitExpr_add(self, ctx:ZCodeParser.Expr_addContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_mul.
    def visitExpr_mul(self, ctx:ZCodeParser.Expr_mulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_not.
    def visitExpr_not(self, ctx:ZCodeParser.Expr_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_sign.
    def visitExpr_sign(self, ctx:ZCodeParser.Expr_signContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_idx.
    def visitExpr_idx(self, ctx:ZCodeParser.Expr_idxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcCall.
    def visitFuncCall(self, ctx:ZCodeParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_lit.
    def visitArray_lit(self, ctx:ZCodeParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_stmtList.
    def visitElif_stmtList(self, ctx:ZCodeParser.Elif_stmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_stmt.
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_stmt.
    def visitElse_stmt(self, ctx:ZCodeParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_stmt.
    def visitDecl_stmt(self, ctx:ZCodeParser.Decl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assign_stmt.
    def visitAssign_stmt(self, ctx:ZCodeParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#leftSide.
    def visitLeftSide(self, ctx:ZCodeParser.LeftSideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcCall_stmt.
    def visitFuncCall_stmt(self, ctx:ZCodeParser.FuncCall_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typ.
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramList.
    def visitParamList(self, ctx:ZCodeParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramList_prime.
    def visitParamList_prime(self, ctx:ZCodeParser.ParamList_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numList.
    def visitNumList(self, ctx:ZCodeParser.NumListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numList_prime.
    def visitNumList_prime(self, ctx:ZCodeParser.NumList_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argList.
    def visitArgList(self, ctx:ZCodeParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprList.
    def visitExprList(self, ctx:ZCodeParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprList_prime.
    def visitExprList_prime(self, ctx:ZCodeParser.ExprList_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtList.
    def visitStmtList(self, ctx:ZCodeParser.StmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtList_prime.
    def visitStmtList_prime(self, ctx:ZCodeParser.StmtList_primeContext):
        return self.visitChildren(ctx)



del ZCodeParser