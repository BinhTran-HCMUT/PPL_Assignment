from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Utils:

    def lookupVar(self, name, lst, func):
        for x in lst:
            if name == func(x) and type(x) is VarSym:
                return x
        return None
    
    def lookupFunc(self, name, lst, func):
        for x in lst:
            if name == func(x) and type(x) is FuncSym:
                return x
        return None
    
    def infer(self, name, typ, param):
        if type(name) is Id:
            for env in param:
                for sym in env:
                    if sym.name == name.name and type(sym) is VarSym:
                        if type(sym.typ) is ArrayType and sym.typ.eleType is None:
                            sym.typ = typ
                        if sym.typ is None:
                            sym.typ = typ
                        return sym.typ
        elif type(name) is CallExpr or type(name) is CallStmt:
            for sym in param[-1]:
                if sym.name == name.name.name and type(sym) is FuncSym:
                    sym.typ = typ
                    return typ
            
    
    def inferArrayLit(self, obj, typ, param):
        for ele in obj.value:
            if type(ele) is ArrayLiteral:
                self.inferArrayLit(ele, ArrayType(typ.size[1:], typ.eleType), param)
            else:
                if type(ele) is Id:
                    if len(typ.size) == 1:
                        _ = self.infer(ele, typ.eleType, param)
                    else:
                        _ = self.infer(ele, ArrayType(typ.size[1:], typ.eleType), param)
                if type(ele) is CallExpr:
                    if len(typ.size) == 1:
                        _ = self.infer(ele, typ.eleType, param)
                    else:
                        _ = self.infer(ele, ArrayType(typ.size[1:], typ.eleType), param)
        return
        
class VarSym:
    def __init__(self, name, typ=None):
        self.name = name
        self.typ = typ

class FuncSym:
    def __init__(self, name, typ=None, paramList = [], body=False):
        self.name = name
        self.typ = typ
        self.paramList = paramList
        self.body = body

class StaticChecker(BaseVisitor, Utils):
    
    def __init__(self, asttree):
        self.__asttree = asttree
        self.__inloop = 0
        self.__stmtlist = []

    
    def check(self):
        return self.visit(self.__asttree, None)
    
    def visitNumberType(self, ast, param):
        return NumberType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitArrayType(self, ast, param):
        return ArrayType(ast.size, ast.eleType)
    
    def visitProgram(self, ast, param):
        env = [[FuncSym('readNumber', NumberType(),[],True), 
                FuncSym('writeNumber', VoidType(),[NumberType()],True), 
                FuncSym('readBool', BoolType(), [], True), 
                FuncSym('writeBool', VoidType(), [BoolType()], True),
                FuncSym('readString', StringType(), [], True),
                FuncSym('writeString', VoidType(), [StringType()], True)]]
        for e in ast.decl:
            env =  self.visit(e, env)
        # No definition function Error 
        for sym in env[-1]:
            if type(sym) is FuncSym and sym.body == False:
                raise NoDefinition(sym.name)
        # No entry point Error
        if self.lookupFunc('main', env[-1], lambda x: x.name) is None:
            raise NoEntryPoint()
        else:
            idx = self.lookupFunc('main', env[-1], lambda x: x.name)
            if type(idx.typ) != VoidType or idx.paramList != []:
                raise NoEntryPoint()
        return ""

    def visitVarDecl(self, ast, param):
        self.__stmtlist.append(ast)
        id = ast.name
        if self.lookupVar(id.name, param[0], lambda x: x.name) is not None:
            raise Redeclared(Variable(), id.name)
        if ast.varType is None:
            if ast.modifier == 'dynamic':
                if ast.varInit is None:
                    return [param[0] + [VarSym(id.name, None)]] + param[1:]
                else:
                    param = [param[0] + [VarSym(id.name, None)]] + param[1:]
                    init_type = self.visit(ast.varInit, param)
                    if init_type is None:
                        raise TypeCannotBeInferred(ast)
                    if type(init_type) is ArrayType:
                        if init_type.eleType is None:
                            raise TypeCannotBeInferred(ast)
                    self.infer(id, init_type, param)
                    return param
            else:
                param = [param[0] + [VarSym(id.name, None)]] + param[1:]
                init_type = self.visit(ast.varInit, param)
                if init_type is None:
                    id_type = self.lookupVar(id.name, param[0], lambda x: x.name).typ
                    if id_type is None:
                        raise TypeCannotBeInferred(ast)
                    else:
                        init_type = self.infer(ast.varInit, id_type, param)
                if type(init_type) is ArrayType:
                    if init_type.eleType is None:
                        raise TypeCannotBeInferred(ast)
                infer_type = self.infer(id, init_type, param)
                if type(infer_type) is not type(init_type):
                    raise TypeMismatchInStatement(ast)
                return param
        else:
            if ast.varInit is None:
                return [param[0] + [VarSym(id.name, ast.varType)]] + param[1:]
            # Type check for explicit type
            param = [param[0] + [VarSym(id.name, ast.varType)]] + param[1:]
            init_type = self.visit(ast.varInit, param)

            if init_type is None:
                init_type = self.infer(ast.varInit, ast.varType, param)
            if type(init_type) is ArrayType and init_type.eleType is None:
                if type(ast.varType) is not ArrayType:
                    raise TypeCannotBeInferred(ast)
            
            if type(init_type) is ArrayType and type(ast.varType) is ArrayType:
                if init_type.size == ast.varType.size[:len(init_type.size)]:
                    if len(init_type.size) == len(ast.varType.size):
                        if init_type.eleType is None:
                            init_type.eleType = ast.varType.eleType
                            self.inferArrayLit(ast.varInit, ArrayType(ast.varType.size, ast.varType.eleType), param)
                        if type(init_type.eleType) is not type(ast.varType.eleType):
                            raise TypeMismatchInStatement(ast)
                    elif init_type.eleType is None:
                        init_type.eleType = ast.varType.eleType
                        self.inferArrayLit(ast.varInit, ArrayType(ast.varType.size, ast.varType.eleType), param)
                    else:
                        raise TypeMismatchInStatement(ast)
                else:
                    if init_type.eleType is None:
                        raise TypeCannotBeInferred(ast)
                    else:
                        raise TypeMismatchInStatement(ast)
                
            if type(init_type) is not type(ast.varType):
                raise TypeMismatchInStatement(ast) 
            return [param[0] +  [VarSym(id.name, ast.varType)]] + param[1:]

    def visitFuncDecl(self, ast, param):
        id = ast.name
        if self.lookupFunc(id.name, param[0], lambda x: x.name) != None:
            idx = self.lookupFunc(id.name, param[0], lambda x: x.name)
            if idx.body == True:
                raise Redeclared(Function(), id.name)
            else:
                if ast.body is None:
                    raise Redeclared(Function(), id.name)
                else:
                    if len(ast.param) != len(idx.paramList):
                        raise Redeclared(Function(), id.name)
                    else:
                        for i in range(len(ast.param)):
                            if type(ast.param[i].varType) != type(idx.paramList[i]):
                                raise Redeclared(Function(), id.name)
                    idx.body = True
                    #Type check for the function
                    env = [[],[idx] + [sym for sym in param[0] if sym.name != idx.name]]
                    # Visit param list
                    for decl in ast.param:
                        # If exists name
                        if self.lookupVar(decl.name.name, env[0], lambda x: x.name) != None:
                            raise Redeclared(Parameter(), decl.name.name)
                        else: # Not then visit normally
                            env = self.visit(decl, env)
                    returnType = self.visit(ast.body, env)
                    # If the body contains only returnType
                    if returnType is None:
                        returnType = VoidType()
                    if idx.typ is None:
                        idx.typ = returnType
                    if type(returnType) is not type(idx.typ):
                        raise TypeMismatchInStatement(ast)
                    return param
        else:
            # Create scope for param
            env = [[]] + param
            paramList = []
            # Visit param list
            for decl in ast.param:
                if ast.body is None:
                    paramList = paramList + [decl.varType]
                else:
                    # If exists name
                    if self.lookupVar(decl.name.name, env[0], lambda x: x.name) != None:
                        raise Redeclared(Parameter(), decl.name.name)
                    else: # Not then visit normally
                        env = self.visit(decl, env)
                        paramList = paramList + [decl.varType]
            # Visit body
            if ast.body is None:
                return [param[0] + [FuncSym(id.name, None, paramList, False)]]
            else:
                # Create scope for body from env
                env = [[]] + env[:-1] + [[FuncSym(id.name, None, paramList, False)]+ env[-1]] 
                # Visit body
                returnType = self.visit(ast.body, env)
                if returnType is None:
                    returnType = VoidType()
                return [param[0] + [FuncSym(id.name, returnType, paramList, True)]]
                       
    def visitBinaryOp(self, ast, param):
        l_type = self.visit(ast.left, param)
        
        # Arithmetic operators
        if ast.op in ['+', '-', '*', '/', '%']:
            if l_type is None:
                l_type = self.infer(ast.left, NumberType(), param)

            r_type = self.visit(ast.right, param)
            if r_type is None:
                r_type = self.infer(ast.right, NumberType(), param)

            if type(l_type) is NumberType and type(r_type) is NumberType:
                return NumberType()
            else:
                raise TypeMismatchInExpression(ast)
        
        # Relational operators for number
        elif ast.op in ['<', '<=', '>', '>=', '=','!=']:
            if l_type is None:
                l_type = self.infer(ast.left, NumberType(), param)
                
            r_type = self.visit(ast.right, param)
            
            if r_type is None:
                r_type = self.infer(ast.right, NumberType(), param)

            if type(l_type) is NumberType and type(r_type) is NumberType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        
        # Logical operators
        elif ast.op in ['and', 'or']:
            if l_type is None:
                l_type = self.infer(ast.left, BoolType(), param)

            r_type = self.visit(ast.right, param)
            if r_type is None:
                r_type = self.infer(ast.right, BoolType(), param)

            if type(l_type) is BoolType and type(r_type) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        
        # Compare String
        elif ast.op in ['==']:
            if l_type is None:
                l_type = self.infer(ast.left, StringType(), param)

            r_type = self.visit(ast.right, param)
            
            if r_type is None:
                r_type = self.infer(ast.right, StringType(), param)

            if type(l_type) is StringType and type(r_type) is StringType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        
        # Concat String
        else:
            if l_type is None:
                l_type = self.infer(ast.left, StringType(), param)

            r_type = self.visit(ast.right, param)
            
            if r_type is None:
                r_type = self.infer(ast.right, StringType(), param)

            if type(l_type) is StringType and type(r_type) is StringType:
                return StringType()
            else:
                raise TypeMismatchInExpression(ast)                    

    def visitUnaryOp(self, ast, param):
        op_type = self.visit(ast.operand, param)
        if ast.op == '-':
            if op_type is None:
                op_type = self.infer(ast.operand, NumberType(), param)

            if type(op_type) is NumberType:
                return NumberType()
            else:
                raise TypeMismatchInExpression(ast)
            
        elif ast.op == 'not':
            if op_type is None:
                op_type = self.infer(ast.operand, BoolType(), param)

            if type(op_type) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, param):
        for sym in param[-1]:
            if sym.name == ast.name.name and type(sym) is FuncSym:
                # Check the list of param type is valid here: typemistmatch
                if len(ast.args) != len(sym.paramList):
                    raise TypeMismatchInExpression(ast)
                else:
                    for i in range(len(ast.args)):
                        args_type = self.visit(ast.args[i], param)
                        if self.visit(ast.args[i], param) is None:
                            args_type = self.infer(ast.args[i], sym.paramList[i], param)
                        if type(args_type) != type(sym.paramList[i]):
                            if type(args_type) is ArrayType and args_type.eleType is None:
                                raise TypeCannotBeInferred(self.__stmtlist[-1])
                            else:
                                raise TypeMismatchInExpression(ast)
                        if type(args_type) is ArrayType and type(sym.paramList[i]) is ArrayType:
                            if args_type.size == sym.paramList[i].size[:len(args_type.size)]:
                                if len(args_type.size) == len(sym.paramList[i].size):
                                    if args_type.eleType is None:
                                        args_type.eleType = sym.paramList[i].eleType
                                        self.inferArrayLit(ast.args[i], sym.paramList[i], param)
                                    if type(args_type.eleType) is not type(sym.paramList[i].eleType):
                                        raise TypeMismatchInExpression(ast)
                                elif args_type.eleType is None:
                                    args_type.eleType = sym.paramList[i].eleType
                                    self.inferArrayLit(ast.args[i], ArrayType(sym.paramList[i].size, sym.paramList[i].eleType), param)
                                else:
                                    raise TypeMismatchInExpression(ast)
                            else:
                                if args_type.eleType is None:
                                    raise TypeCannotBeInferred(self.__stmtlist[-1])
                                else:
                                    raise TypeMismatchInExpression(ast)
                if type(sym.typ) is VoidType:
                    raise TypeMismatchInExpression(ast)
                return sym.typ
        raise Undeclared(Function(), ast.name.name)
            
    def visitId(self, ast, param):
        for env in param:
            for sym in env:
                if sym.name == ast.name and type(sym) is VarSym:
                    return sym.typ
        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast, param):
        arr_type = self.visit(ast.arr, param)
        #Type checking for array cell
        if arr_type is None:
            raise TypeCannotBeInferred(self.__stmtlist[-1])
        if type(arr_type) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        for dim in ast.idx:
            idx_type = self.visit(dim, param)
            if idx_type is None:
                idx_type = self.infer(dim, NumberType(), param)
            if type(idx_type) is not NumberType:
                raise TypeMismatchInExpression(ast)
        # Return the type
        if len(arr_type.size) == len(ast.idx):
            return arr_type.eleType
        elif len(arr_type.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        else:
            return ArrayType(arr_type.size[len(ast.idx):], arr_type.eleType)

    
    def visitAssign(self, ast, param):
        self.__stmtlist.append(ast)
        lhs_type = self.visit(ast.lhs, param)
        rhs_type = self.visit(ast.rhs, param)
        if lhs_type is None and rhs_type is None:
            raise TypeCannotBeInferred(ast)
        if lhs_type is None:
            if type(ast.lhs) is Id:
                if type(rhs_type) is ArrayType and rhs_type.eleType is None:
                    raise TypeCannotBeInferred(ast)
                lhs_type = self.infer(ast.lhs, rhs_type, param)
            if type(ast.lhs) is ArrayCell:
                lhs_type = self.inferArrayLit(ast.lhs, rhs_type, param)
        if rhs_type is None:
            rhs_type = self.infer(ast.rhs, lhs_type, param)

        if type(lhs_type) is ArrayType and type(rhs_type) is ArrayType:
            for i in range(len(lhs_type.size)):
                if i >= len(rhs_type.size):
                    break
                if lhs_type.size[i] != rhs_type.size[i]:
                    if rhs_type.eleType is None:
                        raise TypeCannotBeInferred(ast)
                    if lhs_type.eleType is None:
                        raise TypeCannotBeInferred(ast)
                    raise TypeMismatchInStatement(ast)
            if lhs_type.eleType is None and rhs_type.eleType is None:
                raise TypeCannotBeInferred(ast)
            if lhs_type.eleType is None:
                if len(lhs_type.size) > len(rhs_type.size):
                    raise TypeCannotBeInferred(ast)
                lhs_type.eleType = rhs_type.eleType
                self.inferArrayLit(ast.lhs, rhs_type, param)
            if rhs_type.eleType is None:
                if len(lhs_type.size) < len(rhs_type.size):
                    raise TypeCannotBeInferred(ast)
                rhs_type.eleType = lhs_type.eleType
                self.inferArrayLit(ast.rhs, lhs_type, param)
            if type(lhs_type.eleType) is not type(rhs_type.eleType):
                raise TypeMismatchInStatement(ast)
            if len(lhs_type.size) != len(rhs_type.size):
                raise TypeMismatchInStatement(ast)
        if type(lhs_type) != type(rhs_type):
            if type(rhs_type) is ArrayType and rhs_type.eleType is None:
                raise TypeCannotBeInferred(ast)
            else:
                raise TypeMismatchInStatement(ast)

        # Assignment statement always return None
        return None
        
    def visitIf(self, ast, param):
        # Visit the expr of if to get type
        returnType = None
        expr_type = self.visit(ast.expr, param)
        if expr_type is None:
            expr_type = self.infer(ast.expr, BoolType(), param)

        if type(expr_type) is not BoolType:
            if type(expr_type) is ArrayType and expr_type.eleType is None:
                raise TypeCannotBeInferred(ast)
            else:
                raise TypeMismatchInStatement(ast)
        #Visit the stmt of if
        if type(ast.thenStmt) is VarDecl:
            param = self.visit(ast.thenStmt, param)
        else:
            returnType = self.visit(ast.thenStmt, param)
        for elifStmt in ast.elifStmt:
            #Visit the expr of elif to get type
            elifexpr_type = self.visit(elifStmt[0], param)
            if elifexpr_type is None:
                elifexpr_type = self.infer(elifStmt[0], BoolType(), param)

            if type(elifexpr_type) is not BoolType:
                raise TypeMismatchInStatement(ast)
            #Visit the stmt of elif
            if type(elifStmt[1]) is VarDecl:
                param = self.visit(elifStmt[1], param)
            else:
                if returnType is not None and self.visit(elifStmt[1], param) is not None and type(returnType) is not type(self.visit(elifStmt[1], param)):
                    raise TypeMismatchInStatement(elifStmt[1])
                if self.visit(elifStmt[1], param) is not None:
                    returnType = self.visit(elifStmt[1], param)
        if ast.elseStmt is not None:
            #Visit the stmt of else
            if type(ast.elseStmt) is VarDecl:
                param = self.visit(ast.elseStmt, param)
            else:
                if returnType is not None and self.visit(ast.elseStmt, param) is not None and type(returnType) is not type(self.visit(ast.elseStmt, param)):
                    raise TypeMismatchInStatement(ast.elseStmt)
                if self.visit(ast.elseStmt, param) is not None:
                    returnType = self.visit(ast.elseStmt, param)
        # Return the type of if statement
        return returnType 
        
    def visitFor(self, ast, param):
        self.__inloop += 1
        returnType = None
        name_type = self.visit(ast.name, param)
        if name_type is None:
            name_type = self.infer(ast.name, NumberType(), param)
        if type(name_type) is not NumberType:
            raise TypeMismatchInStatement(ast)
        cond_type = self.visit(ast.condExpr, param)
        if cond_type is None:
            cond_type = self.infer(ast.condExpr, BoolType(), param)

        if type(cond_type) is not BoolType:
            if type(cond_type) is ArrayType and cond_type.eleType is None:
                raise TypeCannotBeInferred(ast)
            else:
                raise TypeMismatchInStatement(ast)
        update_type = self.visit(ast.updExpr, param)
        if update_type is None:
            update_type = self.infer(ast.updExpr, NumberType(), param)

        if type(update_type) is not NumberType:
            if type(update_type) is ArrayType and update_type.eleType is None:
                raise TypeCannotBeInferred(ast)
            else:
                raise TypeMismatchInStatement(ast)
        # Visit the stmt of for to get the type
        if type(ast.body) is VarDecl:
            param = self.visit(ast.body, param)
        else:
            returnType = self.visit(ast.body, param)
        self.__inloop -= 1
        return returnType

    def visitBreak(self, ast, param):
        if self.__inloop == 0:
            raise MustInLoop(ast)
        return None

    def visitContinue(self, ast, param):
        if self.__inloop == 0:
            raise MustInLoop(ast)
        return None


    def visitReturn(self, ast, param):
        typ = None
        if ast.expr is None:
            typ = VoidType()
        else:
            typ = self.visit(ast.expr, param)
        if param[-1][0].typ is None:
            if typ is None:
                raise TypeCannotBeInferred(ast)
            else:
                param[-1][0].typ = typ
                #New part
                if type(typ) is ArrayType:
                    if typ.eleType is None:
                        raise TypeCannotBeInferred(ast)
        else:
            if type(param[-1][0].typ) in [NumberType, BoolType, StringType, VoidType]:
                if typ is None:
                    typ = self.infer(ast.expr, param[-1][0].typ, param)

                if type(param[-1][0].typ) is not type(typ):
                    if type(typ) is ArrayType and typ.eleType is None:
                        raise TypeCannotBeInferred(ast)
                    raise TypeMismatchInStatement(ast)
            else: # The type of fuction is ArrayType and explicit, check the typ having same ArrayType
                if type(typ) is ArrayType:
                    if len(param[-1][0].typ.size) < len(typ.size):
                        if typ.eleType is None:
                            raise TypeCannotBeInferred(ast)
                        else:
                            raise TypeMismatchInStatement(ast)
                    for i in range(len(param[-1][0].typ.size)):
                        if i >= len(typ.size):
                            break
                        if param[-1][0].typ.size[i] != typ.size[i]:
                            if typ.eleType is None:
                                raise TypeCannotBeInferred(ast)
                            else:
                                raise TypeMismatchInStatement(ast)                        
                    if typ.eleType is None:
                        typ.eleType = param[-1][0].typ.eleType
                        self.inferArrayLit(ast.expr, param[-1][0].typ, param)
                    else: 
                        if len(param[-1][0].typ.size) > len(typ.size):
                            raise TypeMismatchInStatement(ast)
                    if type(param[-1][0].typ.eleType) is not type(typ.eleType):
                        raise TypeMismatchInStatement(ast)
                else:
                    return TypeMismatchInStatement(ast)
        return typ
     
    def visitCallStmt(self, ast, param):
        for sym in param[-1]:
            if sym.name == ast.name.name and type(sym) is FuncSym:
                # Check the list of param type is valid here: typemistmatch
                if len(ast.args) != len(sym.paramList):
                    raise TypeMismatchInStatement(ast)
                else:
                    for i in range(len(ast.args)):
                        args_type = self.visit(ast.args[i], param)
                        if args_type is None:
                            args_type = self.infer(ast.args[i], sym.paramList[i], param)

                        if type(args_type) != type(sym.paramList[i]):
                            if type(args_type) is ArrayType and args_type.eleType is None:
                                raise TypeCannotBeInferred(ast)
                            else:
                                raise TypeMismatchInStatement(ast)
                        if type(args_type) is ArrayType and type(sym.paramList[i]) is ArrayType:
                            if args_type.size == sym.paramList[i].size[:len(args_type.size)]:
                                if len(args_type.size) == len(sym.paramList[i].size):
                                    if args_type.eleType is None:
                                        args_type.eleType = sym.paramList[i].eleType
                                        self.inferArrayLit(ast.args[i], sym.paramList[i], param)
                                    if type(args_type.eleType) is not type(sym.paramList[i].eleType):
                                        raise TypeMismatchInStatement(ast)
                                elif args_type.eleType is None:
                                    args_type.eleType = sym.paramList[i].eleType
                                    self.inferArrayLit(ast.args[i], ArrayType(sym.paramList[i].size, sym.paramList[i].eleType), param)
                                else:
                                    raise TypeMismatchInStatement(ast)
                            else:
                                if args_type.eleType is None:
                                    raise TypeCannotBeInferred(ast)
                                else:
                                    raise TypeMismatchInStatement(ast)
                if sym.typ is None:
                    _ = self.infer(ast, VoidType(), param)
                if type(sym.typ) is not VoidType:
                    raise TypeMismatchInStatement(ast)
                else:
                    return None
        raise Undeclared(Function(), ast.name.name)

    def visitBlock(self, ast, param):
        returnType = None
        # Create scope for block
        env = [[]] + param
        body = ast.stmt
        for stmt in body:
            if type(stmt) is VarDecl:
                env = self.visit(stmt, env)
            else:
                returnType = self.visit(stmt, env)                                       
        return returnType

    def visitNumberLiteral(self, ast, param):
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        return BoolType()

    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayLiteral(self, ast, param):
        cur_type = None
        for ele in ast.value:
            ele_type = self.visit(ele, param)
            if cur_type is None:
                if ele_type is not None:
                    cur_type = ele_type
            else:
                if ele_type is not None:
                    if type(cur_type) is not type(ele_type):
                        raise TypeMismatchInExpression(ast)
                    else: 
                        if type(ele_type) is ArrayType:
                            cur_type.size = ele_type.size if len(ele_type.size) > len(cur_type.size) else cur_type.size
                            if cur_type.eleType is None:
                                cur_type.eleType = ele_type.eleType

        for ele in ast.value:          
            ele_type = self.visit(ele, param)
            if type(cur_type) in [NumberType, BoolType, StringType]:
                if ele_type is None:
                    ele_type = self.infer(ele, cur_type, param)

                if type(cur_type) is not type(ele_type):
                    raise TypeMismatchInExpression(ast)
            elif type(cur_type) is ArrayType:
                if ele_type is None:
                    ele_type = self.infer(ele, cur_type, param)

                elif type(ele_type) in ['NumberType', 'BoolType','StringType']:
                    raise TypeMismatchInExpression(ast)
                else:
                    if ele_type.eleType is not None and cur_type.eleType is not None:
                        if type(cur_type.eleType) is not type(ele_type.eleType):
                            raise TypeMismatchInExpression(ast)
                    if cur_type.size[:len(ele_type.size)] != ele_type.size:
                        raise TypeMismatchInExpression(ast)
                    if len(cur_type.size) == len(ele_type.size):
                        if cur_type.eleType is not None and ele_type.eleType is None:
                            ele_type.eleType = cur_type.eleType
                            self.inferArrayLit(ele, cur_type, param)
                    if len(cur_type.size) > len(ele_type.size):
                        self.inferArrayLit(ele, cur_type, param)
        if type(cur_type) is ArrayType:
            size = [float(len(ast.value))] + cur_type.size
            return ArrayType(size, cur_type.eleType)
        else:
            return ArrayType([float(len(ast.value))], cur_type)  
        