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


    # Visit a parse tree produced by ZCodeParser#declist.
    def visitDeclist(self, ctx:ZCodeParser.DeclistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variabledec.
    def visitVariabledec(self, ctx:ZCodeParser.VariabledecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dyndecl.
    def visitDyndecl(self, ctx:ZCodeParser.DyndeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typedecl.
    def visitTypedecl(self, ctx:ZCodeParser.TypedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl.
    def visitVardecl(self, ctx:ZCodeParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrdecl.
    def visitArrdecl(self, ctx:ZCodeParser.ArrdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dimension.
    def visitDimension(self, ctx:ZCodeParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numlitlist.
    def visitNumlitlist(self, ctx:ZCodeParser.NumlitlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array.
    def visitArray(self, ctx:ZCodeParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vallist.
    def visitVallist(self, ctx:ZCodeParser.VallistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typ.
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcdecl.
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcstmt.
    def visitFuncstmt(self, ctx:ZCodeParser.FuncstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcprime.
    def visitFuncprime(self, ctx:ZCodeParser.FuncprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramlist.
    def visitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramprime.
    def visitParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramdecl.
    def visitParamdecl(self, ctx:ZCodeParser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#condstmt.
    def visitCondstmt(self, ctx:ZCodeParser.CondstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#normalstmt.
    def visitNormalstmt(self, ctx:ZCodeParser.NormalstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifstmt.
    def visitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#eliflist.
    def visitEliflist(self, ctx:ZCodeParser.EliflistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifpart.
    def visitElifpart(self, ctx:ZCodeParser.ElifpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elsepart.
    def visitElsepart(self, ctx:ZCodeParser.ElsepartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#varstmt.
    def visitVarstmt(self, ctx:ZCodeParser.VarstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignstmt.
    def visitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forstmt.
    def visitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#breakstmt.
    def visitBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#contstmt.
    def visitContstmt(self, ctx:ZCodeParser.ContstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#returnstmt.
    def visitReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#callstmt.
    def visitCallstmt(self, ctx:ZCodeParser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprlist.
    def visitExprlist(self, ctx:ZCodeParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprparam.
    def visitExprparam(self, ctx:ZCodeParser.ExprparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockstmt.
    def visitBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmtlist.
    def visitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newlines.
    def visitNewlines(self, ctx:ZCodeParser.NewlinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#null_newline.
    def visitNull_newline(self, ctx:ZCodeParser.Null_newlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexop.
    def visitIndexop(self, ctx:ZCodeParser.IndexopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr8.
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#subexpr.
    def visitSubexpr(self, ctx:ZCodeParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#callexpr.
    def visitCallexpr(self, ctx:ZCodeParser.CallexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#rel_op.
    def visitRel_op(self, ctx:ZCodeParser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#const.
    def visitConst(self, ctx:ZCodeParser.ConstContext):
        return self.visitChildren(ctx)



del ZCodeParser