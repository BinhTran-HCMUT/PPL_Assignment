from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.declist()))


    # Visit a parse tree produced by ZCodeParser#declist.
    def visitDeclist(self, ctx:ZCodeParser.DeclistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        return [self.visit(ctx.decl())] + self.visit(ctx.declist())


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        if ctx.variabledec():
            return self.visit(ctx.variabledec())
        return self.visit(ctx.funcdecl())


    # Visit a parse tree produced by ZCodeParser#variabledec.
    def visitVariabledec(self, ctx:ZCodeParser.VariabledecContext):
        if ctx.typedecl():
            return self.visit(ctx.typedecl())
        elif ctx.dyndecl():
            return self.visit(ctx.dyndecl())
        elif ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.arrdecl():
            return self.visit(ctx.arrdecl())


    # Visit a parse tree produced by ZCodeParser#dyndecl.
    def visitDyndecl(self, ctx:ZCodeParser.DyndeclContext):
        if ctx.getChildCount() == 2:
            return VarDecl(Id(ctx.ID().getText()),None, ctx.DYNAMIC().getText(), None)
        if ctx.getChildCount() == 4:
            return VarDecl(Id(ctx.ID().getText()), None, ctx.DYNAMIC().getText(), self.visit(ctx.expr()))


    # Visit a parse tree produced by ZCodeParser#typedecl.
    def visitTypedecl(self, ctx:ZCodeParser.TypedeclContext):
        if ctx.getChildCount() == 2:
            return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.typ()), None, None)
        if ctx.getChildCount() == 4:
            return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.typ()), None, self.visit(ctx.expr()))


    # Visit a parse tree produced by ZCodeParser#vardecl.
    def visitVardecl(self, ctx:ZCodeParser.VardeclContext):
        return VarDecl(Id(ctx.ID().getText()), None, ctx.VAR().getText(), self.visit(ctx.expr()))


    # Visit a parse tree produced by ZCodeParser#arrdecl.
    def visitArrdecl(self, ctx:ZCodeParser.ArrdeclContext):
        arraytype = ArrayType(self.visit(ctx.dimension()), self.visit(ctx.typ()))
        if ctx.getChildCount() == 3:
            return VarDecl(Id(ctx.ID().getText()), arraytype, None, None)
        elif ctx.getChildCount() == 5:
            return VarDecl(Id(ctx.ID().getText()), arraytype, None, self.visit(ctx.expr()))


    # Visit a parse tree produced by ZCodeParser#dimension.
    def visitDimension(self, ctx:ZCodeParser.DimensionContext):
        return self.visit(ctx.numlitlist())


    # Visit a parse tree produced by ZCodeParser#numlitlist.
    def visitNumlitlist(self, ctx:ZCodeParser.NumlitlistContext):
        if ctx.getChildCount() == 1:
            return [float(ctx.NUMLIT().getText())]
        return [float(ctx.NUMLIT().getText())] + self.visit(ctx.numlitlist())


    # Visit a parse tree produced by ZCodeParser#array.
    def visitArray(self, ctx:ZCodeParser.ArrayContext):
        return ArrayLiteral(self.visit(ctx.vallist()))


    # Visit a parse tree produced by ZCodeParser#vallist.
    def visitVallist(self, ctx:ZCodeParser.VallistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.vallist())


    # Visit a parse tree produced by ZCodeParser#typ.
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOL():
            return BoolType()


    # Visit a parse tree produced by ZCodeParser#funcdecl.
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.paramlist()), self.visit(ctx.funcstmt()))


    # Visit a parse tree produced by ZCodeParser#funcstmt.
    def visitFuncstmt(self, ctx:ZCodeParser.FuncstmtContext):
        if ctx.getChildCount() == 0:
            return None
        return self.visit(ctx.funcprime())


    # Visit a parse tree produced by ZCodeParser#funcprime.
    def visitFuncprime(self, ctx:ZCodeParser.FuncprimeContext):
        return self.visit(ctx.returnstmt()) if ctx.returnstmt() else self.visit(ctx.blockstmt())


    # Visit a parse tree produced by ZCodeParser#paramlist.
    def visitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.paramprime())


    # Visit a parse tree produced by ZCodeParser#paramprime.
    def visitParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.paramdecl())]
        return [self.visit(ctx.paramdecl())] + self.visit(ctx.paramprime())


    # Visit a parse tree produced by ZCodeParser#paramdecl.
    def visitParamdecl(self, ctx:ZCodeParser.ParamdeclContext):
        if ctx.dimension():
            return VarDecl(Id(ctx.ID().getText()), ArrayType(self.visit(ctx.dimension()), self.visit(ctx.typ())), None, None)
        return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.typ()), None, None)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visit(ctx.normalstmt()) if ctx.normalstmt() else self.visit(ctx.condstmt())


    # Visit a parse tree produced by ZCodeParser#condstmt.
    def visitCondstmt(self, ctx:ZCodeParser.CondstmtContext):
        return self.visit(ctx.ifstmt()) if ctx.ifstmt() else self.visit(ctx.forstmt())


    # Visit a parse tree produced by ZCodeParser#normalstmt.
    def visitNormalstmt(self, ctx:ZCodeParser.NormalstmtContext):
        if ctx.varstmt():
            return self.visit(ctx.varstmt())
        elif ctx.assignstmt():
            return self.visit(ctx.assignstmt())
        elif ctx.callstmt():
            return self.visit(ctx.callstmt())
        elif ctx.breakstmt():
            return self.visit(ctx.breakstmt())
        elif ctx.contstmt():
            return self.visit(ctx.contstmt())
        elif ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        elif ctx.blockstmt():
            return self.visit(ctx.blockstmt())

# ifstmt: IF R_OPEN expr R_CLOSE null_newline stmt 
#       | IF R_OPEN expr R_CLOSE null_newline stmt eliflist 
#       | IF R_OPEN expr R_CLOSE null_newline stmt ELSE null_newline stmt 
#       | IF R_OPEN expr R_CLOSE null_newline stmt eliflist ELSE null_newline stmt;

# eliflist: elifpart eliflist 
#         | ;

# elifpart: ELIF R_OPEN expr R_CLOSE null_newline stmt;
    # Visit a parse tree produced by ZCodeParser#ifstmt.
    def visitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        return If(self.visit(ctx.expr()), self.visit(ctx.stmt()), self.visit(ctx.eliflist()), self.visit(ctx.elsepart()))


    # Visit a parse tree produced by ZCodeParser#eliflist.
    def visitEliflist(self, ctx:ZCodeParser.EliflistContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.elifpart())] + self.visit(ctx.eliflist())


    # Visit a parse tree produced by ZCodeParser#elifpart.
    def visitElifpart(self, ctx:ZCodeParser.ElifpartContext):
        return (self.visit(ctx.expr()), self.visit(ctx.stmt()))
    
    def visitElsepart(self, ctx:ZCodeParser.ElsepartContext):
        if ctx.getChildCount() == 0:
            return None
        return self.visit(ctx.stmt())

    # Visit a parse tree produced by ZCodeParser#varstmt.
    def visitVarstmt(self, ctx:ZCodeParser.VarstmtContext):
        return self.visit(ctx.variabledec())


    # Visit a parse tree produced by ZCodeParser#assignstmt.
    def visitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.indexop()))


    # Visit a parse tree produced by ZCodeParser#forstmt.
    def visitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        return For(Id(ctx.ID().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.stmt()))


    # Visit a parse tree produced by ZCodeParser#breakstmt.
    def visitBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        return Break()

    # Visit a parse tree produced by ZCodeParser#contstmt.
    def visitContstmt(self, ctx:ZCodeParser.ContstmtContext):
        return Continue()


    # Visit a parse tree produced by ZCodeParser#returnstmt.
    def visitReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        return Return() if ctx.getChildCount() == 1 else Return(self.visit(ctx.expr()))


    # Visit a parse tree produced by ZCodeParser#callstmt.
    def visitCallstmt(self, ctx:ZCodeParser.CallstmtContext):
        return CallStmt(Id(ctx.ID().getText()), self.visit(ctx.exprlist()))


    # Visit a parse tree produced by ZCodeParser#exprlist.
    def visitExprlist(self, ctx:ZCodeParser.ExprlistContext):
        return [] if ctx.getChildCount() == 0 else self.visit(ctx.exprparam())


    # Visit a parse tree produced by ZCodeParser#exprparam.
    def visitExprparam(self, ctx:ZCodeParser.ExprparamContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprparam())


    # Visit a parse tree produced by ZCodeParser#blockstmt.
    def visitBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        return Block(self.visit(ctx.stmtlist()))


    # Visit a parse tree produced by ZCodeParser#stmtlist.
    def visitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        return BinaryOp(self.visit(ctx.rel_op()), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expr5()))


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expr6()))


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        if ctx.ID():
            return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.indexop()))
        if ctx.callexpr():
            return ArrayCell(self.visit(ctx.callexpr()), self.visit(ctx.indexop()))


    # Visit a parse tree produced by ZCodeParser#indexop.
    def visitIndexop(self, ctx:ZCodeParser.IndexopContext):
        return self.visit(ctx.exprparam())


    # Visit a parse tree produced by ZCodeParser#expr8.
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        if ctx.const():
            return self.visit(ctx.const())
        if ctx.array():
            return self.visit(ctx.array())
        if ctx.callexpr():
            return self.visit(ctx.callexpr())
        if ctx.subexpr():
            return self.visit(ctx.subexpr())


    # Visit a parse tree produced by ZCodeParser#subexpr.
    def visitSubexpr(self, ctx:ZCodeParser.SubexprContext):
        return self.visit(ctx.expr())

    def visitCallexpr(self, ctx:ZCodeParser.CallexprContext):
        return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.exprlist()))

    # Visit a parse tree produced by ZCodeParser#rel_op.
    def visitRel_op(self, ctx:ZCodeParser.Rel_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by ZCodeParser#const.
    def visitConst(self, ctx:ZCodeParser.ConstContext):
        if ctx.NUMLIT():
            return NumberLiteral(float(ctx.NUMLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.ID():
            return Id(ctx.ID().getText())
