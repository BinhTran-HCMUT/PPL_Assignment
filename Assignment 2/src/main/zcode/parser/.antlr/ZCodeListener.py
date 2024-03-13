# Generated from d:/ASM 2/assignment2-initial/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#declist.
    def enterDeclist(self, ctx:ZCodeParser.DeclistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#declist.
    def exitDeclist(self, ctx:ZCodeParser.DeclistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decl.
    def enterDecl(self, ctx:ZCodeParser.DeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decl.
    def exitDecl(self, ctx:ZCodeParser.DeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#variabledec.
    def enterVariabledec(self, ctx:ZCodeParser.VariabledecContext):
        pass

    # Exit a parse tree produced by ZCodeParser#variabledec.
    def exitVariabledec(self, ctx:ZCodeParser.VariabledecContext):
        pass


    # Enter a parse tree produced by ZCodeParser#dyndecl.
    def enterDyndecl(self, ctx:ZCodeParser.DyndeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#dyndecl.
    def exitDyndecl(self, ctx:ZCodeParser.DyndeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#typedecl.
    def enterTypedecl(self, ctx:ZCodeParser.TypedeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#typedecl.
    def exitTypedecl(self, ctx:ZCodeParser.TypedeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vardecl.
    def enterVardecl(self, ctx:ZCodeParser.VardeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vardecl.
    def exitVardecl(self, ctx:ZCodeParser.VardeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrdecl.
    def enterArrdecl(self, ctx:ZCodeParser.ArrdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrdecl.
    def exitArrdecl(self, ctx:ZCodeParser.ArrdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#dimension.
    def enterDimension(self, ctx:ZCodeParser.DimensionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#dimension.
    def exitDimension(self, ctx:ZCodeParser.DimensionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#numlitlist.
    def enterNumlitlist(self, ctx:ZCodeParser.NumlitlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#numlitlist.
    def exitNumlitlist(self, ctx:ZCodeParser.NumlitlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array.
    def enterArray(self, ctx:ZCodeParser.ArrayContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array.
    def exitArray(self, ctx:ZCodeParser.ArrayContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vallist.
    def enterVallist(self, ctx:ZCodeParser.VallistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vallist.
    def exitVallist(self, ctx:ZCodeParser.VallistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#typ.
    def enterTyp(self, ctx:ZCodeParser.TypContext):
        pass

    # Exit a parse tree produced by ZCodeParser#typ.
    def exitTyp(self, ctx:ZCodeParser.TypContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcdecl.
    def enterFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcdecl.
    def exitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcstmt.
    def enterFuncstmt(self, ctx:ZCodeParser.FuncstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcstmt.
    def exitFuncstmt(self, ctx:ZCodeParser.FuncstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcprime.
    def enterFuncprime(self, ctx:ZCodeParser.FuncprimeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcprime.
    def exitFuncprime(self, ctx:ZCodeParser.FuncprimeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramlist.
    def enterParamlist(self, ctx:ZCodeParser.ParamlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramlist.
    def exitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramprime.
    def enterParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramprime.
    def exitParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramdecl.
    def enterParamdecl(self, ctx:ZCodeParser.ParamdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramdecl.
    def exitParamdecl(self, ctx:ZCodeParser.ParamdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt.
    def enterStmt(self, ctx:ZCodeParser.StmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt.
    def exitStmt(self, ctx:ZCodeParser.StmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#unmatchifstmt.
    def enterUnmatchifstmt(self, ctx:ZCodeParser.UnmatchifstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#unmatchifstmt.
    def exitUnmatchifstmt(self, ctx:ZCodeParser.UnmatchifstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#matchifstmt.
    def enterMatchifstmt(self, ctx:ZCodeParser.MatchifstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#matchifstmt.
    def exitMatchifstmt(self, ctx:ZCodeParser.MatchifstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#otherstmt.
    def enterOtherstmt(self, ctx:ZCodeParser.OtherstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#otherstmt.
    def exitOtherstmt(self, ctx:ZCodeParser.OtherstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#noncondstmt.
    def enterNoncondstmt(self, ctx:ZCodeParser.NoncondstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#noncondstmt.
    def exitNoncondstmt(self, ctx:ZCodeParser.NoncondstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#eliflist.
    def enterEliflist(self, ctx:ZCodeParser.EliflistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#eliflist.
    def exitEliflist(self, ctx:ZCodeParser.EliflistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elifpart.
    def enterElifpart(self, ctx:ZCodeParser.ElifpartContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elifpart.
    def exitElifpart(self, ctx:ZCodeParser.ElifpartContext):
        pass


    # Enter a parse tree produced by ZCodeParser#varstmt.
    def enterVarstmt(self, ctx:ZCodeParser.VarstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#varstmt.
    def exitVarstmt(self, ctx:ZCodeParser.VarstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignstmt.
    def enterAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignstmt.
    def exitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#lhs.
    def enterLhs(self, ctx:ZCodeParser.LhsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#lhs.
    def exitLhs(self, ctx:ZCodeParser.LhsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#forstmt.
    def enterForstmt(self, ctx:ZCodeParser.ForstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#forstmt.
    def exitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#breakstmt.
    def enterBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#breakstmt.
    def exitBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#contstmt.
    def enterContstmt(self, ctx:ZCodeParser.ContstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#contstmt.
    def exitContstmt(self, ctx:ZCodeParser.ContstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#returnstmt.
    def enterReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#returnstmt.
    def exitReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#callstmt.
    def enterCallstmt(self, ctx:ZCodeParser.CallstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#callstmt.
    def exitCallstmt(self, ctx:ZCodeParser.CallstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#exprlist.
    def enterExprlist(self, ctx:ZCodeParser.ExprlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#exprlist.
    def exitExprlist(self, ctx:ZCodeParser.ExprlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#exprparam.
    def enterExprparam(self, ctx:ZCodeParser.ExprparamContext):
        pass

    # Exit a parse tree produced by ZCodeParser#exprparam.
    def exitExprparam(self, ctx:ZCodeParser.ExprparamContext):
        pass


    # Enter a parse tree produced by ZCodeParser#blockstmt.
    def enterBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#blockstmt.
    def exitBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmtlist.
    def enterStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmtlist.
    def exitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#newlines.
    def enterNewlines(self, ctx:ZCodeParser.NewlinesContext):
        pass

    # Exit a parse tree produced by ZCodeParser#newlines.
    def exitNewlines(self, ctx:ZCodeParser.NewlinesContext):
        pass


    # Enter a parse tree produced by ZCodeParser#null_newline.
    def enterNull_newline(self, ctx:ZCodeParser.Null_newlineContext):
        pass

    # Exit a parse tree produced by ZCodeParser#null_newline.
    def exitNull_newline(self, ctx:ZCodeParser.Null_newlineContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr.
    def enterExpr(self, ctx:ZCodeParser.ExprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr.
    def exitExpr(self, ctx:ZCodeParser.ExprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr1.
    def enterExpr1(self, ctx:ZCodeParser.Expr1Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr1.
    def exitExpr1(self, ctx:ZCodeParser.Expr1Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr2.
    def enterExpr2(self, ctx:ZCodeParser.Expr2Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr2.
    def exitExpr2(self, ctx:ZCodeParser.Expr2Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr3.
    def enterExpr3(self, ctx:ZCodeParser.Expr3Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr3.
    def exitExpr3(self, ctx:ZCodeParser.Expr3Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr4.
    def enterExpr4(self, ctx:ZCodeParser.Expr4Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr4.
    def exitExpr4(self, ctx:ZCodeParser.Expr4Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr5.
    def enterExpr5(self, ctx:ZCodeParser.Expr5Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr5.
    def exitExpr5(self, ctx:ZCodeParser.Expr5Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr6.
    def enterExpr6(self, ctx:ZCodeParser.Expr6Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr6.
    def exitExpr6(self, ctx:ZCodeParser.Expr6Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr7.
    def enterExpr7(self, ctx:ZCodeParser.Expr7Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr7.
    def exitExpr7(self, ctx:ZCodeParser.Expr7Context):
        pass


    # Enter a parse tree produced by ZCodeParser#indexop.
    def enterIndexop(self, ctx:ZCodeParser.IndexopContext):
        pass

    # Exit a parse tree produced by ZCodeParser#indexop.
    def exitIndexop(self, ctx:ZCodeParser.IndexopContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr8.
    def enterExpr8(self, ctx:ZCodeParser.Expr8Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr8.
    def exitExpr8(self, ctx:ZCodeParser.Expr8Context):
        pass


    # Enter a parse tree produced by ZCodeParser#subexpr.
    def enterSubexpr(self, ctx:ZCodeParser.SubexprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#subexpr.
    def exitSubexpr(self, ctx:ZCodeParser.SubexprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#rel_op.
    def enterRel_op(self, ctx:ZCodeParser.Rel_opContext):
        pass

    # Exit a parse tree produced by ZCodeParser#rel_op.
    def exitRel_op(self, ctx:ZCodeParser.Rel_opContext):
        pass


    # Enter a parse tree produced by ZCodeParser#const.
    def enterConst(self, ctx:ZCodeParser.ConstContext):
        pass

    # Exit a parse tree produced by ZCodeParser#const.
    def exitConst(self, ctx:ZCodeParser.ConstContext):
        pass



del ZCodeParser