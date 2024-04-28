import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    
    def test_400(self):
        input = """
number a[5]
string a[5]
func main()
begin
    string b[5]
    number a
end
"""
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_401(self):
        input = """
number a[5]
func main()
begin
    string b[5]
    number b
end
"""
        expect = """Redeclared Variable: b"""
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_402(self):
        input = """
func foo(number a[5], string b)
begin
    number a[5]
    var i <- 0
    for i until i >= 5 by 1
    begin
        a[i] <- i * i + 5
    end
    return -1
end

func main()
begin
    string c
    number c
end
"""
        expect = """Redeclared Variable: c"""
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_403(self):
        input = """
func foo(number a[5], string a)
begin
    number a[5]
    var i <- 0
    for i until i >= 5 by 1
    begin
        a[i] <- i * i + 5
    end
    return -1
end

func main()
begin
    string c
end
"""
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_404(self):
        input = """
func hey(string a[5], bool b)
func foo(number a[5], bool b, string c)
begin
    number a[5]
    var i <- 0
    for i until i >= 5 by 1
    begin
        a[i] <- i * i + 5
    end
    return -1
end

func main()
begin
    string c
end
"""
        expect = """No Function Definition: hey"""
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_405(self):
        input = """
func foo(number a[5], string b)
begin
    number a[5]
    var i <- 0
    for i until i >= 5 by 1
    begin
        a[i] <- i * i + 5
    end
    return -1
end

func hey(string a[5], bool b)
func foo(number a[5], string b)

func main()
begin
    string c
end
"""
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_406(self):
        input = """
func f()
begin
    dynamic x
    x <- [[1, 2, 3], [4, 5, 6]]
    return x[0, 0]
end

func main()
begin
    number x <- f()
end
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_407(self):
        input = """
func f(number x)
func f(number x)
begin
    if (x >= 2) return f(x - 1) + f(x - 2)
    return 1
end
func main()
begin
    number x <- f(2)
    writeNumber(x)
end
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_408(self):
        input = """
func main()
begin
    number x
    string s
    bool a
    x <- readNumber()
    writeNumber(x)
    s <- readString()
    writeString(s)
    a <- readBool()
    writeBool(a)
end
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_409(self):
        input = """
func readNumber()
func main()
begin
end
"""
        expect = """Redeclared Function: readNumber"""
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_410(self):
        input = """
func main()
"""
        expect = """No Function Definition: main"""
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_411(self):
        input = """
func main(number a)
begin
    return
end
"""
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_412(self):
        input = """
func main()
begin
    return 0
end
"""
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_413(self):
        input = """
func foo(number a, string a, bool a[3])
func foo(number a, string b, bool c[3])
begin
    return a
end

func main()
begin
    dynamic x <- foo(12, "abc", [true, true, false])
    return
end
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_414(self):
        input = """
dynamic n
func main()
begin
    dynamic a <- n
end
"""
        expect = """Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, Id(n))"""
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_415(self):
        input = """
dynamic n
func main()
begin
    dynamic arr <- [[[n]], [[n]]]
end
"""
        expect = """Type Cannot Be Inferred: VarDecl(Id(arr), None, dynamic, ArrayLit(ArrayLit(ArrayLit(Id(n))), ArrayLit(ArrayLit(Id(n)))))"""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_416(self):
        input = """
func foo(number a, string a)
func main()
begin
    dynamic c <- foo
end
"""
        expect = """Undeclared Identifier: foo"""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_417(self):
        input = """
dynamic x
func main()
begin
    var y <- x
end
"""
        expect = """Type Cannot Be Inferred: VarDecl(Id(y), None, var, Id(x))"""
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_418(self):
        input = """
dynamic x
func main()
begin
    var y <- [[[x]], [[x]]]
end
"""
        expect = """Type Cannot Be Inferred: VarDecl(Id(y), None, var, ArrayLit(ArrayLit(ArrayLit(Id(x))), ArrayLit(ArrayLit(Id(x)))))"""
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_419(self):
        input = """
func foo(number a, string a)
func main()
begin
    var c <- foo
end
"""
        expect = """Undeclared Identifier: foo"""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_420(self):
        input = """
dynamic x
dynamic y
func main()
begin
    number arr[2] <- [x, x, y]
end
"""
        expect = """Type Cannot Be Inferred: VarDecl(Id(arr), ArrayType([2.0], NumberType), None, ArrayLit(Id(x), Id(x), Id(y)))"""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_421(self):
        input = """
dynamic x
dynamic y
func main()
begin
    number arr[2, 3] <- [[x, x], y]
end
"""
        expect = """Type Cannot Be Inferred: VarDecl(Id(arr), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(Id(x), Id(x)), Id(y)))"""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_422(self):
        input = """
dynamic x
dynamic y
func main()
begin
    string arr <- [[x, x], y]
end
"""
        expect = """Type Cannot Be Inferred: VarDecl(Id(arr), StringType, None, ArrayLit(ArrayLit(Id(x), Id(x)), Id(y)))"""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_423(self):
        input = """
func main()
begin
    number a <- "abc" ... "hello"
end
"""
        expect = """Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, BinaryOp(..., StringLit(abc), StringLit(hello)))"""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):
        input = """
dynamic x
dynamic y
func main()
begin
    number arr[2, 3] <- [[x, x, x], y]
end
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
        input = """
dynamic x
dynamic y
func main()
begin
    number arr[3, 2] <- [[x, x], y, ["abc", ""]]
end
"""
        expect = """Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([3.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(x), Id(x)), Id(y), ArrayLit(StringLit(abc), StringLit())))"""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_426(self):
        input = """
func foo() return
func foo()
func main() return
"""
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_427(self):
        input = """
func foo(number a) return
func foo() return
func main() return
"""
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_428(self):
        input = """
func foo(number a, string a)
func foo(number b, string b)
func main() return
"""
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_429(self):
        input = """
func foo()
func foo() return
func main() return
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_430(self):
        input = """
func foo(number a, string a)
func foo(number c) return
func main() return
"""
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_431(self):
        input = """
func foo(number a, string a)
func foo(number c, bool b) return
func main() return
"""
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_432(self):
        input = """
dynamic a
dynamic b
func main()
begin
    dynamic res <- a and (a % b)
end
"""
        expect = """Type Mismatch In Expression: BinaryOp(%, Id(a), Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_433(self):
        input = """
dynamic a
dynamic b
func main()
begin
    dynamic res <- a and (a >= b)
end
"""
        expect = """Type Mismatch In Expression: BinaryOp(>=, Id(a), Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_434(self):
        input = """
dynamic a
dynamic b
func main()
begin
    dynamic res <- a and (a ... b)
end
"""
        expect = """Type Mismatch In Expression: BinaryOp(..., Id(a), Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_435(self):
        input = """
dynamic a
dynamic b
func main()
begin
    dynamic res <- a + (a == b)
end
"""
        expect = """Type Mismatch In Expression: BinaryOp(==, Id(a), Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_436(self):
        input = """
string s
func main()
begin
    dynamic a <- -s
end
"""
        expect = """Type Mismatch In Expression: UnaryOp(-, Id(s))"""
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_437(self):
        input = """
string s
func main()
begin
    dynamic a <- not s
end
"""
        expect = """Type Mismatch In Expression: UnaryOp(not, Id(s))"""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_438(self):
        input = """
func main()
begin
    number a <- foo()
end
"""
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_439(self):
        input = """
func foo(number a, string a)
func foo(number a, string b) return
func main()
begin
    dynamic a <- foo(12)
end
"""
        expect = """Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(12.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_440(self):
        input = """
dynamic x
func foo(number a[2]) return 12
func main()
begin
    dynamic a <- foo([x, x, x]) + 33
end
"""
        expect = """Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, BinaryOp(+, CallExpr(Id(foo), [ArrayLit(Id(x), Id(x), Id(x))]), NumLit(33.0)))"""
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_441(self):
        input = """
dynamic x
func foo(number a[3, 2]) return 12
func main()
begin
    dynamic a <- foo([x, x]) + 13
end
"""
        expect = """Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, BinaryOp(+, CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]), NumLit(13.0)))"""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_442(self):
        input = """
dynamic x
func foo(string a) return 12
func main()
begin
    dynamic a <- foo([x, x]) + 13
end
"""
        expect = """Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, BinaryOp(+, CallExpr(Id(foo), [ArrayLit(Id(x), Id(x))]), NumLit(13.0)))"""
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_443(self):
        input = """
dynamic x
func foo(number a[2]) return 12
func main()
begin
    x <- 10 + 20
    dynamic a <- foo([x, x]) + 13
end
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_444(self):
        input = """
dynamic x
func foo(number a) return 12
func main()
begin
    x <- 10 + 20
    dynamic a <- foo("abc") + 13
end
"""
        expect = """Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(abc)])"""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_445(self):
        input = """
func main() return x
"""
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_446(self):
        input = """
dynamic x
func main()
begin
    number a <- x[0]
end
"""
        expect = """Type Cannot Be Inferred: VarDecl(Id(a), NumberType, None, ArrayCell(Id(x), [NumLit(0.0)]))"""
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_447(self):
        input = """
string s <- "Hello world"
func main()
begin
    string ss <- s[1]
end
"""
        expect = """Type Mismatch In Expression: ArrayCell(Id(s), [NumLit(1.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_448(self):
        input = """
number arr[3, 2, 2] <- [[[3, 4], [1, 9]], [[6, 6], [7, 7]], [[8, 8], [10, 10]]]
func main()
begin
    dynamic x <- arr[2, 1, 1, 2]
end
"""
        expect = """Type Mismatch In Expression: ArrayCell(Id(arr), [NumLit(2.0), NumLit(1.0), NumLit(1.0), NumLit(2.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_449(self):
        input = """
func foo() return
func main()
begin
    number arr[3] <- [1, 2, 3]
    dynamic x <- arr[foo()]
end
"""
        expect = """Type Mismatch In Expression: CallExpr(Id(foo), [])"""
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_450(self):
        input = """
func foo() return
func main()
begin
    if(foo()) dynamic x
end
"""
        expect = """Type Mismatch In Expression: CallExpr(Id(foo), [])"""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_451(self):
        input = """
func foo() return true
func main()
begin
    number x
    if(foo()) dynamic x
end
"""
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_452(self):
        input = """
func foo() return true
func foo1() return
func main()
begin
    if(foo()) dynamic x
    elif(true) dynamic z
    elif(foo1()) dynamic y
end
"""
        expect = """Type Mismatch In Expression: CallExpr(Id(foo1), [])"""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_453(self):
        input = """
func foo() return true
func foo1() return
func main()
begin
    if(foo()) dynamic x
    elif(true) var x <- 123
    elif(foo1()) dynamic y
end
"""
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_454(self):
        input = """
func foo() return true
func foo1() return true
func main()
begin
    if(foo()) dynamic x
    elif(true)
    begin
        var x <- 123
    end
    elif(foo1()) dynamic y
end
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_455(self):
        input = """
func foo() return true
func foo1() return true
func main()
begin
    if(foo()) dynamic x
    elif(true)
    begin
        var x <- 123
    end
    elif(foo1()) dynamic y
    else
        var y <- 12
end
"""
        expect = """Redeclared Variable: y"""
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_456(self):
        input = """
func foo() return true
func foo1() return true
func main()
begin
    if(foo()) dynamic x
    elif(true)
    begin
        var x <- 123
    end
    elif(foo1()) dynamic y
    else
    begin
        var y <- 12
    end
end
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_457(self):
        input = """
func main()
begin
    string i
    for i until true by 1
        dynamic x
end
"""
        expect = """Type Mismatch In Statement: For(Id(i), BooleanLit(True), NumLit(1.0), VarDecl(Id(x), None, dynamic, None))"""
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_458(self):
        input = """
func main()
begin
    number i
    dynamic j
    for i until j + 3 by 1
        dynamic x
end
"""
        expect = """Type Mismatch In Statement: For(Id(i), BinaryOp(+, Id(j), NumLit(3.0)), NumLit(1.0), VarDecl(Id(x), None, dynamic, None))"""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_459(self):
        input = """
func main()
begin
    number i
    dynamic j
    for i until true by j = 2
        dynamic x
end
"""
        expect = """Type Mismatch In Statement: For(Id(i), BooleanLit(True), BinaryOp(=, Id(j), NumLit(2.0)), VarDecl(Id(x), None, dynamic, None))"""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_460(self):
        input = """
func main()
begin
    number x
    number i <- 1
    for i until i < 10 by 1
        dynamic x
end
"""
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_461(self):
        input = """
func main()
begin
    number x
    number i <- 1
    for i until i < 10 by 1
        if(true) dynamic x
end
"""
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_462(self):
        input = """
func main()
begin
    number x
    number i <- 1
    number j <- 1
    for i until i < 10 by 1
        if(true)
            for j until j < 10 by 1
                dynamic x
end
"""
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_463(self):
        input = """
func main()
begin
    number x
    number i <- 1
    number j <- 1
    for i until i < 10 by 1
    begin
        if(true)
            for j until j < 10 by 1
                dynamic x <- i + 12
                number i <- 100
    end
end
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_464(self):
        input = """
func foo()
begin
    continue
end
func main()
begin
    number i <- 1
    number j <- 1
    for i until i < 10 by 1
        for j until j < 10 by 1
            foo()
end
"""
        expect = """Continue Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_465(self):
        input = """
func foo()
begin
    break
end
func main()
begin
    number i <- 1
    number j <- 1
    for i until i < 10 by 1
        for j until j < 10 by 1
            foo()
end
"""
        expect = """Break Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_466(self):
        input = """
func foo()
begin
    return
end
func main()
begin
    number i <- 1
    number j <- 1
    continue
    break
    for i until i < 10 by 1
        for j until j < 10 by 1
            foo()
end
"""
        expect = """Continue Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_467(self):
        input = """
func main()
begin
    number i <- 1
    number j <- 1
    number k <- 1
    for i until i < 10 by 1
    begin
        continue
        for j until j < 10 by 1
        begin
            break
            for k until k < 10 by 1
                if (true) continue
                elif (false) break
                else continue
        end
    end
                
end
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_468(self):
        input = """
dynamic x
func foo() return x
func main() return
"""
        expect = """Type Cannot Be Inferred: Return(Id(x))"""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_469(self):
        input = """
dynamic x
func foo() return [x, x]
func main() return
"""
        expect = """Type Cannot Be Inferred: Return(ArrayLit(Id(x), Id(x)))"""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_470(self):
        input = """
func foo()
func main()
begin
    number a <- foo() + 13
end
func foo() return
"""
        expect = """Type Mismatch In Statement: Return()"""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_471(self):
        input = """
dynamic x
func foo()
func main()
begin
    foo()
end
func foo() return [x, x]
"""
        expect = """Type Cannot Be Inferred: Return(ArrayLit(Id(x), Id(x)))"""
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_472(self):
        input = """
dynamic x
dynamic arr
func foo()
func main()
begin
    number a[3]
    arr <- a
    arr <- foo()
end
func foo() return [[x]]
"""
        expect = """Type Cannot Be Inferred: Return(ArrayLit(ArrayLit(Id(x))))"""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_473(self):
        input = """
dynamic x
dynamic arr
func foo()
func main()
begin
    number a[3]
    arr <- a
    arr <- foo()
end
func foo() return [x, x]
"""
        expect = """Type Cannot Be Inferred: Return(ArrayLit(Id(x), Id(x)))"""
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_474(self):
        input = """
dynamic x
func foo()
func main()
begin
    number a
    a <- foo()
end
func foo() return [x, x]
"""
        expect = """Type Cannot Be Inferred: Return(ArrayLit(Id(x), Id(x)))"""
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_475(self):
        input = """
dynamic x
dynamic arr
func foo()
func main()
begin
    number a[3]
    arr <- a
    arr <- foo()
end
func foo() return [x, x, x]
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_476(self):
        input = """
dynamic x
func foo()
func main()
begin
    number a
    a <- foo()
end
func foo() return true
"""
        expect = """Type Mismatch In Statement: Return(BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_477(self):
        input = """
func main()
begin
    dynamic x
    dynamic y
    x <- y
end
"""
        expect = """Type Cannot Be Inferred: AssignStmt(Id(x), Id(y))"""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_478(self):
        input = """
func main()
begin
    dynamic x
    dynamic y
    x <- [y, y, x]
end
"""
        expect = """Type Cannot Be Inferred: AssignStmt(Id(x), ArrayLit(Id(y), Id(y), Id(x)))"""
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_479(self):
        input = """
func main()
begin
    dynamic x
    number a[2]
    a <- [[x, x], [x, x]]
end
"""
        expect = """Type Cannot Be Inferred: AssignStmt(Id(a), ArrayLit(ArrayLit(Id(x), Id(x)), ArrayLit(Id(x), Id(x))))"""
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_480(self):
        input = """
func main()
begin
    dynamic x
    number a[2]
    a <- [[x, x], [x, 1]]
end
"""
        expect = """Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(ArrayLit(Id(x), Id(x)), ArrayLit(Id(x), NumLit(1.0))))"""
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_481(self):
        input = """
func main()
begin
    dynamic x
    number a[2]
    a <- [x, x, x]
end
"""
        expect = """Type Cannot Be Inferred: AssignStmt(Id(a), ArrayLit(Id(x), Id(x), Id(x)))"""
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_482(self):
        input = """
func main()
begin
    dynamic x
    string a
    a <- [x, x, x]
end
"""
        expect = """Type Cannot Be Inferred: AssignStmt(Id(a), ArrayLit(Id(x), Id(x), Id(x)))"""
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_483(self):
        input = """
func main()
begin
    number x
    string a
    a <- [x, x, x]
end
"""
        expect = """Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(Id(x), Id(x), Id(x)))"""
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_484(self):
        input = """
func main()
begin
    number x
    string a
    a <- x
end
"""
        expect = """Type Mismatch In Statement: AssignStmt(Id(a), Id(x))"""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_485(self):
        input = """
func main()
begin
    foo()
end
"""
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_486(self):
        input = """
func foo() return 12
func main()
begin
    foo()
end
"""
        expect = """Type Mismatch In Statement: CallStmt(Id(foo), [])"""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_487(self):
        input = """
func foo(number a, string a)
func main()
begin
    foo(12, "abc", true)
end
func foo(number x, string y) return
"""
        expect = """Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(12.0), StringLit(abc), BooleanLit(True)])"""
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_488(self):
        input = """
func foo(number a[3], string b) return
func main()
begin
    dynamic x
    foo([[x]], "abc")
end
"""
        expect = """Type Cannot Be Inferred: CallStmt(Id(foo), [ArrayLit(ArrayLit(Id(x))), StringLit(abc)])"""
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_489(self):
        input = """
func foo(number a[1, 3], string b) return
func main()
begin
    dynamic x
    foo([[x]], "abc")
end
"""
        expect = """Type Cannot Be Inferred: CallStmt(Id(foo), [ArrayLit(ArrayLit(Id(x))), StringLit(abc)])"""
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_490(self):
        input = """
func foo(number a, string b) return
func main()
begin
    dynamic x
    foo([[x]], "abc")
end
"""
        expect = """Type Cannot Be Inferred: CallStmt(Id(foo), [ArrayLit(ArrayLit(Id(x))), StringLit(abc)])"""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_491(self):
        input = """
func foo(number a, string b) return
func main()
begin
    dynamic x
    foo([x, false], "abc")
end
"""
        expect = """Type Mismatch In Statement: CallStmt(Id(foo), [ArrayLit(Id(x), BooleanLit(False)), StringLit(abc)])"""
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_492(self):
        input = """
func main()
begin
    dynamic x
    dynamic y
    number a[2, 2, 3]
    a <- [[[x, x]], [y, y]]
end
"""
        expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(Id(x), Id(x))), ArrayLit(Id(y), Id(y)))"""
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_493(self):
        input = """
func main()
begin
    dynamic x
    dynamic y
    number a[2, 2, 3]
    a <- [[1, 1], [[y, y]]]
end
"""
        expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(1.0)), ArrayLit(ArrayLit(Id(y), Id(y))))"""
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_494(self):
        input = """
func main()
begin
    dynamic x
    dynamic y
    number a[2, 2, 3]
    a <- [[[1, 1]], [y, y]]
end
"""
        expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(1.0))), ArrayLit(Id(y), Id(y)))"""
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_495(self):
        input = """
func main()
begin
    dynamic x
    dynamic y
    number a[2, 2, 3]
    a <- [[[y, y]], [1, 1]]
end
"""
        expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(Id(y), Id(y))), ArrayLit(NumLit(1.0), NumLit(1.0)))"""
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_496(self):
        input = """
func main()
begin
    dynamic x
    dynamic y
    number a[2, 2, 3]
    a <- [[y, y], [[1, 1]]]
end
"""
        expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(Id(y), Id(y)), ArrayLit(ArrayLit(NumLit(1.0), NumLit(1.0))))"""
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_497(self):
        input = """
func main()
begin
    number a[2, 2, 3]
    a <- [[1, 2], [[1, 1]]]
end
"""
        expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(ArrayLit(NumLit(1.0), NumLit(1.0))))"""
        self.assertTrue(TestChecker.test(input, expect, 497))

        input = """
func main()
begin
    dynamic x
    number a[2, 2, 3]
    a <- ["abc", [x]]
end
"""
        expect = """Type Mismatch In Expression: ArrayLit(StringLit(abc), ArrayLit(Id(x)))"""
        self.assertTrue(TestChecker.test(input, expect, 497))

        input = """
func main()
begin
    dynamic x
    number a[2, 2, 3]
    a <- [[x], 12]
end
"""
        expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(Id(x)), NumLit(12.0))"""
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_498(self):
        input = """
func x()
func main()
begin
    dynamic x
    number a[2]
    a <- [x, [x, x]]
end
func x() return 12
"""
        expect = """Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"""
        self.assertTrue(TestChecker.test(input, expect, 498))
        
        input = """
func x()
func main()
begin
    dynamic x
    number a[2, 2]
    a <- [x, [x(), x()]]
end
func x() return 12
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 498))

        input = """
func x()
func main()
begin
    dynamic x
    number a[2, 2]
    a <- [x(), [x, x]]
    number c[2] <- x()
end
func x() return [1, 2]
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 498))

        input = """
func x()
func y()
func z()
func main()
begin
    dynamic x
    dynamic y
    dynamic z
    number a[2, 2, 2, 2]
    a <- [[[[y(), x], y], z], [[[x, y()], z()], x()]]
    number x1 <- x
    number x2[2, 2] <- x()
    number y1[2] <- y
    number y2 <- y()
    number z1[2, 2] <- z
    number z2[2] <- z() 
end
func x() return [[1, 2], [3, 4]]
func y() return 5
func z() return [6, 7]
"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_499(self):
        input = """
func main()
begin
    dynamic x
    if ([x]) return
end
"""
        expect = """Type Cannot Be Inferred: If((ArrayLit(Id(x)), Return()), [], None)"""
        self.assertTrue(TestChecker.test(input, expect, 499))

        input = """
func main()
begin
    if ([1, 2, 3]) return
end
"""
        expect = """Type Mismatch In Statement: If((ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), Return()), [], None)"""
        self.assertTrue(TestChecker.test(input, expect, 499))

        input = """
func main()
begin
    dynamic x
    number i <- 1
    for i until [x] by 1
        break
end
"""
        expect = """Type Cannot Be Inferred: For(Id(i), ArrayLit(Id(x)), NumLit(1.0), Break)"""
        self.assertTrue(TestChecker.test(input, expect, 499))

        input = """
func main()
begin
    dynamic x
    number i <- 1
    for i until i < 10 by [x]
        break
end
"""
        expect = """Type Cannot Be Inferred: For(Id(i), BinaryOp(<, Id(i), NumLit(10.0)), ArrayLit(Id(x)), Break)"""
        self.assertTrue(TestChecker.test(input, expect, 499))

        input = """
func main()
begin
    dynamic x
    number i <- 1
    for i until [1, 2] by 1
        break
end
"""
        expect = """Type Mismatch In Statement: For(Id(i), ArrayLit(NumLit(1.0), NumLit(2.0)), NumLit(1.0), Break)"""
        self.assertTrue(TestChecker.test(input, expect, 499))

        input = """
func main()
begin
    dynamic x
    number i <- 1
    for i until i < 10 by [[1, 2], [3, 4]]
        break
end
"""
        expect = """Type Mismatch In Statement: For(Id(i), BinaryOp(<, Id(i), NumLit(10.0)), ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0))), Break)"""
        self.assertTrue(TestChecker.test(input, expect, 499))
