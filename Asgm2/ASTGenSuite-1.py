import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """var str <- "Doan Minh Hieu"
"""
        expect =str(Program([VarDecl(Id("str"), None, "var", StringLiteral("Doan Minh Hieu"))]))
        self.assertTrue(TestAST.test(input, expect, 301))
    def test_2(self):
        input = """number a[5] <- [1, 2, 3, 4, 5]
        """
        expect =str(Program([VarDecl(Id("a"), ArrayType([5.0], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0), NumberLiteral(5.0)]))]))
        self.assertTrue(TestAST.test(input,expect,302))
    def test_3(self):
        input = """number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
        """
        expect =str(Program([VarDecl(Id("b"), ArrayType([2.0, 3.0], NumberType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]), ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0)])]))]))
        self.assertTrue(TestAST.test(input,expect,303)) 
    def test_4(self):
        input = """ var MinhHieu <- "Minh" ... "Hieu" 
        """
        expect =str(Program([VarDecl(Id("MinhHieu"), None, "var", BinaryOp("...", StringLiteral("Minh"), StringLiteral("Hieu")))]))
        self.assertTrue(TestAST.test(input,expect,304))       
    def test_5(self):
        input = """var test <- 1 = 2
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", BinaryOp("=", NumberLiteral(1.0), NumberLiteral(2.0)))]))
        self.assertTrue(TestAST.test(input,expect,305)) 
    def test_6(self):
        input = """var test <- 1 == 2
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", BinaryOp("==", NumberLiteral(1.0), NumberLiteral(2.0)))]))
        self.assertTrue(TestAST.test(input,expect,306)) 
    def test_7(self):
        input = """var test <- 1 != 2
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", BinaryOp("!=", NumberLiteral(1.0), NumberLiteral(2.0)))]))
        self.assertTrue(TestAST.test(input,expect,307))    
    def test_8(self):
        input = """var test <- 1 < 2
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", BinaryOp("<", NumberLiteral(1.0), NumberLiteral(2.0)))]))
        self.assertTrue(TestAST.test(input,expect,308))   
    def test_9(self):
        input = """var test <- 1 > 2
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", BinaryOp(">", NumberLiteral(1.0), NumberLiteral(2.0)))]))
        self.assertTrue(TestAST.test(input,expect,309))
    def test_10(self):
        input = """var test <- 1 <= 2
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", BinaryOp("<=", NumberLiteral(1.0), NumberLiteral(2.0)))]))
        self.assertTrue(TestAST.test(input,expect,310))
    def test_11(self):
        input = """var test <- 1 >= 2
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", BinaryOp(">=", NumberLiteral(1.0), NumberLiteral(2.0)))]))
        self.assertTrue(TestAST.test(input,expect,311))
    def test_12(self):
        input = """var test <- 1 == 2 ... 1 > 2
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", BinaryOp("...", BinaryOp("==", NumberLiteral(1.0), NumberLiteral(2.0)), BinaryOp(">", NumberLiteral(1.0), NumberLiteral(2.0))))]))
        self.assertTrue(TestAST.test(input,expect,312))   
    def test_13(self):
        input = """var test <- 1 and 2
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", BinaryOp("and", NumberLiteral(1.0), NumberLiteral(2.0)))]))
        self.assertTrue(TestAST.test(input,expect,313))
    def test_14(self):
        input = """var test <- 1 or 2
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", BinaryOp("or", NumberLiteral(1.0), NumberLiteral(2.0)))]))
        self.assertTrue(TestAST.test(input,expect,314))
    def test_15(self):
        input = """var test <- 1 + 2
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)))]))
        self.assertTrue(TestAST.test(input,expect,315))
    def test_16(self):
        input = """var test <- 1 - 2
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", BinaryOp("-", NumberLiteral(1.0), NumberLiteral(2.0)))]))
        self.assertTrue(TestAST.test(input,expect,316))
    def test_17(self):
        input = """var test <- 1 * 2
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", BinaryOp("*", NumberLiteral(1.0), NumberLiteral(2.0)))]))
        self.assertTrue(TestAST.test(input,expect,317))    
    def test_18(self):
        input = """var test <- 1 / 2
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", BinaryOp("/", NumberLiteral(1.0), NumberLiteral(2.0)))]))
        self.assertTrue(TestAST.test(input,expect,318))   
    def test_19(self):
        input = """var test <- 1 % 2
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", BinaryOp("%", NumberLiteral(1.0), NumberLiteral(2.0)))]))
        self.assertTrue(TestAST.test(input,expect,319))   
    def test_20(self):
        input = """var test <- not 1
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", UnaryOp("not", NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input,expect,320))  
    def test_21(self):
        input = """var test <- - 1
        """
        expect =str(Program([VarDecl(Id("test"), None, "var", UnaryOp("-", NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input,expect,321))        
    def test_22(self):
        input = """number a <- 1
        """
        expect =str(Program([VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0))]))
        self.assertTrue(TestAST.test(input,expect,322)) 
    def test_23(self):
        input = """bool a <- true
        """
        expect =str(Program([VarDecl(Id("a"), BoolType(), None, BooleanLiteral(True))]))
        self.assertTrue(TestAST.test(input,expect,323)) 
    def test_24(self):
        input = """string str <- "hello"
        """
        expect =str(Program([VarDecl(Id("str"), StringType(), None, StringLiteral("hello"))]))
        self.assertTrue(TestAST.test(input,expect,324)) 
    def test_25(self):
        input = """number a
        """
        expect =str(Program([VarDecl(Id("a"), NumberType(), None, None)]))
        self.assertTrue(TestAST.test(input,expect,325)) 
    def test_26(self):
        input = """var a <- 1
        """
        expect =str(Program([VarDecl(Id("a"), None, "var", NumberLiteral(1.0))]))
        self.assertTrue(TestAST.test(input,expect,326))
    def test_27(self):
        input = """var a <- true
        """
        expect =str(Program([VarDecl(Id("a"), None, "var", BooleanLiteral(True))]))
        self.assertTrue(TestAST.test(input,expect,327))
    def test_28(self):
        input = """dynamic a <- 1
        """
        expect =str(Program([VarDecl(Id("a"), None, "dynamic", NumberLiteral(1.0))]))
        self.assertTrue(TestAST.test(input,expect,328))
    def test_29(self):
        input = """dynamic a
        """
        expect =str(Program([VarDecl(Id("a"), None, "dynamic", None)]))
        self.assertTrue(TestAST.test(input,expect,329))
    def test_30(self):
        input = """func main()
        """
        expect =str(Program([FuncDecl(Id("main"), [], None)]))
        self.assertTrue(TestAST.test(input,expect,330))
    def test_31(self):
        input = """func main(number a)
        """
        expect =str(Program([FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType(), None, None)], None)]))
        self.assertTrue(TestAST.test(input,expect,331))
    def test_32(self):
        input = """func main(number a, number b)
        """
        expect =str(Program([FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], None)]))
        self.assertTrue(TestAST.test(input,expect,332))
    def test_33(self):
        input = """func main() return 1
        """
        expect =str(Program([FuncDecl(Id("main"), [], Return(NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input,expect,333))
    def test_34(self):
        input = """func main()
            begin
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([]))]))
        self.assertTrue(TestAST.test(input,expect,334))    
    def test_35(self):
        input = """func main()
            begin
                var a <- 1
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), None, "var", NumberLiteral(1.0))]))]))
        self.assertTrue(TestAST.test(input,expect,335))           
    def test_36(self):
        input = """func foo(number a[5], string b)
                begin
                    var i <- 0
                    for i until i >= 5 by 1
                        begin
                            a[i] <- i * i + 5
                        end
                    return -1
                end
            """
        expect =str(Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), ArrayType([5.0], NumberType()), None, None), VarDecl(Id("b"), StringType(), None, None)], Block([VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp(">=", Id("i"), NumberLiteral(5.0)), NumberLiteral(1.0), Block([Assign(ArrayCell(Id("a"), [Id("i")]), BinaryOp("+", BinaryOp("*", Id("i"), Id("i")), NumberLiteral(5.0)))])), Return(UnaryOp("-", NumberLiteral(1.0)))]))]))
        self.assertTrue(TestAST.test(input,expect,336))
    def test_37(self):
        input = """func areDivisors(number num1, number num2)
                return ((num1 % num2 = 0) or (num2 % num1 = 0))
                """
        expect =str(Program([FuncDecl(Id("areDivisors"), [VarDecl(Id("num1"), NumberType(), None, None), VarDecl(Id("num2"), NumberType(), None, None)], Return(BinaryOp("or", BinaryOp("=", BinaryOp("%", Id("num1"), Id("num2")), NumberLiteral(0.0)), BinaryOp("=", BinaryOp("%", Id("num2"), Id("num1")), NumberLiteral(0.0)))))]))
        self.assertTrue(TestAST.test(input,expect,337))
    def test_38(self):
        input = """func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) writeString("Yes")
                else writeString("No")
            end
"""
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("num1"), None, "var", CallExpr(Id("readNumber"), [])), VarDecl(Id("num2"), None, "var", CallExpr(Id("readNumber"), [])), 
                If((CallExpr(Id("areDivisors"), [Id("num1"), Id("num2")])), CallStmt(Id("writeString"), [StringLiteral("Yes")]), [], CallStmt(Id("writeString"), [StringLiteral("No")]))]))]))
        self.assertTrue(TestAST.test(input,expect,338))
    def test_39(self):
        input = """func isPrime(number x)
                    func main()
                        begin
                            number x <- readNumber()
                            if (isPrime(x)) writeString("Yes")
                            else writeString("No")
                        end
                    func isPrime(number x)
                        begin
                            if (x <= 1) return false
                            var i <- 2
                            for i until i > x / 2 by 1
                                begin
                                    if (x % i = 0) return false
                                end
                            return true
                        end
                """
        expect =str(Program([FuncDecl(Id("isPrime"), [VarDecl(Id("x"), NumberType(), None, None)], None), FuncDecl(Id("main"), [], Block([VarDecl(Id("x"), NumberType(), None, CallExpr(Id("readNumber"), [])), 
                If((CallExpr(Id("isPrime"), [Id("x")])), CallStmt(Id("writeString"), [StringLiteral("Yes")]), [], CallStmt(Id("writeString"), [StringLiteral("No")]))])), FuncDecl(Id("isPrime"), [VarDecl(Id("x"), NumberType(), None, None)], Block([
                If((BinaryOp("<=", Id("x"), NumberLiteral(1.0))), Return(BooleanLiteral(False)), [], None), VarDecl(Id("i"), None, "var", NumberLiteral(2.0)), For(Id("i"), BinaryOp(">", Id("i"), BinaryOp("/", Id("x"), NumberLiteral(2.0))), NumberLiteral(1.0), Block([
                If((BinaryOp("=", BinaryOp("%", Id("x"), Id("i")), NumberLiteral(0.0))), Return(BooleanLiteral(False)), [], None)])), Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.test(input,expect,339))
    def test_40(self):
        input = """func main()
                begin
                    ##this is a comment
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([]))]))
        self.assertTrue(TestAST.test(input,expect,340))  
    def test_41(self):
        input = """func main() 
                begin
                    break 
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block(["Break"]))]))
        self.assertTrue(TestAST.test(input,expect,341)) 
    def test_42(self):
        input = """func main()
                begin
                    dynamic a <- 1
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), None, "dynamic", NumberLiteral(1.0))]))]))
        self.assertTrue(TestAST.test(input,expect,342)) 
    def test_43(self):
        input = """func main()
                begin
                    number a ## This comment
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType(), None, None)]))]))
        self.assertTrue(TestAST.test(input,expect,343))
    def test_44(self):
        input = """func main()
                begin
                    begin
                        begin
                           i <- i + 1
                        end
                    end
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([Block([Block([Assign(Id("i"), BinaryOp("+", Id("i"), NumberLiteral(1.0)))])])]))]))
        self.assertTrue(TestAST.test(input,expect,344))
    def test_45(self):
        input = """
                func main()
                begin
                    number a <- 0
                    if (1 < 2) if (2 < 3) a <- 1
                    if (5 < 6) a <- 2
                    else a <- 3
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType(), None, NumberLiteral(0.0)), 
                If((BinaryOp("<", NumberLiteral(1.0), NumberLiteral(2.0))), 
                   If((BinaryOp("<", NumberLiteral(2.0), NumberLiteral(3.0))), Assign(Id("a"), NumberLiteral(1.0)), [], None), [], None), 
                If((BinaryOp("<", NumberLiteral(5.0), NumberLiteral(6.0))), Assign(Id("a"), NumberLiteral(2.0)), [], Assign(Id("a"), NumberLiteral(3.0)))]))]))
        self.assertTrue(TestAST.test(input,expect,345)) 
    def test_46(self):
        input ="""func main()
                begin
                    readNumber()
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([CallStmt(Id("readNumber"), [])]))]))
        self.assertTrue(TestAST.test(input,expect,346))    
    def test_47(self):  
        input ="""func merge(number arr[100], number left, number mid, number right)
begin
    number i
    number j
    number k
    number n1 <- mid - left + 1
    number n2 <- right - mid
    number L[100]
    number R[100]

    for i until i < n1 by 1
        L[i] <- arr[left + i]

    for j until j < n2 by 1
        R[j] <- arr[mid + 1 + j]

    i <- 0
    j <- 0
    k <- left

    for k until k <= right by 1
    begin
        if ((i < n1) and (j >= n2) or (L[i] <= R[j]))
        begin
            arr[k] <- L[i]
            i <- i + 1
        end
        else begin
            arr[k] <- R[j]
            j <- j + 1
        end
    end
end

func mergeSort(number arr[100], number left, number right)
begin
    if (left < right)
    begin
        number mid <- (left + right) / 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)

        merge(arr, left, mid, right)
    end
end
                """
        expect =str(Program([FuncDecl(Id("merge"), [VarDecl(Id("arr"), ArrayType([100.0], NumberType()), None, None), VarDecl(Id("left"), NumberType(), None, None), VarDecl(Id("mid"), NumberType(), None, None), VarDecl(Id("right"), NumberType(), None, None)], Block([VarDecl(Id("i"), NumberType(), None, None), VarDecl(Id("j"), NumberType(), None, None), VarDecl(Id("k"), NumberType(), None, None), VarDecl(Id("n1"), NumberType(), None, BinaryOp("+", BinaryOp("-", Id("mid"), Id("left")), NumberLiteral(1.0))), VarDecl(Id("n2"), NumberType(), None, BinaryOp("-", Id("right"), Id("mid"))), VarDecl(Id("L"), ArrayType([100.0], NumberType()), None, None), VarDecl(Id("R"), ArrayType([100.0], NumberType()), None, None), For(Id("i"), BinaryOp("<", Id("i"), Id("n1")), NumberLiteral(1.0), Assign(ArrayCell(Id("L"), [Id("i")]), ArrayCell(Id("arr"), [BinaryOp("+", Id("left"), Id("i"))]))), For(Id("j"), BinaryOp("<", Id("j"), Id("n2")), NumberLiteral(1.0), Assign(ArrayCell(Id("R"), [Id("j")]), ArrayCell(Id("arr"), [BinaryOp("+", BinaryOp("+", Id("mid"), NumberLiteral(1.0)), Id("j"))]))), Assign(Id("i"), NumberLiteral(0.0)), Assign(Id("j"), NumberLiteral(0.0)), Assign(Id("k"), Id("left")), For(Id("k"), BinaryOp("<=", Id("k"), Id("right")), NumberLiteral(1.0), Block([
            If((BinaryOp("or", BinaryOp("and", BinaryOp("<", Id("i"), Id("n1")), BinaryOp(">=", Id("j"), Id("n2"))), BinaryOp("<=", ArrayCell(Id("L"), [Id("i")]), ArrayCell(Id("R"), [Id("j")])))), Block([Assign(ArrayCell(Id("arr"), [Id("k")]), ArrayCell(Id("L"), [Id("i")])), Assign(Id("i"), BinaryOp("+", Id("i"), NumberLiteral(1.0)))]), [], Block([Assign(ArrayCell(Id("arr"), [Id("k")]), ArrayCell(Id("R"), [Id("j")])), Assign(Id("j"), BinaryOp("+", Id("j"), NumberLiteral(1.0)))]))]))])), FuncDecl(Id("mergeSort"), [VarDecl(Id("arr"), ArrayType([100.0], NumberType()), None, None), VarDecl(Id("left"), NumberType(), None, None), VarDecl(Id("right"), NumberType(), None, None)], Block([
            If((BinaryOp("<", Id("left"), Id("right"))), Block([VarDecl(Id("mid"), NumberType(), None, BinaryOp("/", BinaryOp("+", Id("left"), Id("right")), NumberLiteral(2.0))), CallStmt(Id("mergeSort"), [Id("arr"), Id("left"), Id("mid")]), CallStmt(Id("mergeSort"), [Id("arr"), BinaryOp("+", Id("mid"), NumberLiteral(1.0)), Id("right")]), CallStmt(Id("merge"), [Id("arr"), Id("left"), Id("mid"), Id("right")])]), [], None)]))]))
        self.assertTrue(TestAST.test(input,expect,347))    
    def test_48(self):
        input ="""func add(number a, number b)
                return a + b
            func main()
            begin
                number a <- 10
                number b <- 3
                number sum <- add(a, b)
                print(sum)
            end
                """
        expect =str(Program([FuncDecl(Id("add"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Return(BinaryOp("+", Id("a"), Id("b")))), FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType(), None, NumberLiteral(10.0)), VarDecl(Id("b"), NumberType(), None, NumberLiteral(3.0)), VarDecl(Id("sum"), NumberType(), None, CallExpr(Id("add"), [Id("a"), Id("b")])), CallStmt(Id("print"), [Id("sum")])]))]))
        self.assertTrue(TestAST.test(input,expect,348))    
    def test_49(self):
        input ="""func isEven(number x)
      begin
        if (x % 2 = 0) return true
        return false
      end
                """
        expect =str(Program([FuncDecl(Id("isEven"), [VarDecl(Id("x"), NumberType(), None, None)], Block([
            If((BinaryOp("=", BinaryOp("%", Id("x"), NumberLiteral(2.0)), NumberLiteral(0.0))), Return(BooleanLiteral(True)), [], None), Return(BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.test(input,expect,349))    
    def test_50(self):
        input ="""func isPrime(number x)
      begin
        if (x <= 1) return false
        number i <- 2
        for i until i < x by 1
            if (x % i = 0) return false
        return true 
      end
                """
        expect =str(Program([FuncDecl(Id("isPrime"), [VarDecl(Id("x"), NumberType(), None, None)], Block([
            If((BinaryOp("<=", Id("x"), NumberLiteral(1.0))), Return(BooleanLiteral(False)), [], None), VarDecl(Id("i"), NumberType(), None, NumberLiteral(2.0)), For(Id("i"), BinaryOp("<", Id("i"), Id("x")), NumberLiteral(1.0), 
            If((BinaryOp("=", BinaryOp("%", Id("x"), Id("i")), NumberLiteral(0.0))), Return(BooleanLiteral(False)), [], None)), Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.test(input,expect,350))    
    def test_51(self):
        input ="""func isPalindrome(string str)
      begin
            number i <- 0
            for i until i < len(str) by 1
                if (str[i] != str[len(str) - i - 1])
                    return false
            return true
      end
                """
        expect =str(Program([FuncDecl(Id("isPalindrome"), [VarDecl(Id("str"), StringType(), None, None)], Block([VarDecl(Id("i"), NumberType(), None, NumberLiteral(0.0)), For(Id("i"), BinaryOp("<", Id("i"), CallExpr(Id("len"), [Id("str")])), NumberLiteral(1.0), 
                    If((BinaryOp("!=", ArrayCell(Id("str"), [Id("i")]), ArrayCell(Id("str"), [BinaryOp("-", BinaryOp("-", CallExpr(Id("len"), [Id("str")]), Id("i")), NumberLiteral(1.0))]))), Return(BooleanLiteral(False)), [], None)), Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.test(input,expect,351))    
    def test_52(self):
        input ="""func max(number a[100], number length)
begin
    if (length <= 0)
        return -1e9 ## Represent negative infinity
    var max <- a[0]
    var i <- 0
    for i until i >= length by 1
        if (a[i] > max) max <- a[i]
    return max
end
                """
        expect =str(Program([FuncDecl(Id("max"), [VarDecl(Id("a"), ArrayType([100.0], NumberType()), None, None), VarDecl(Id("length"), NumberType(), None, None)], Block([
            If((BinaryOp("<=", Id("length"), NumberLiteral(0.0))), Return(UnaryOp("-", NumberLiteral(1000000000.0))), [], None), VarDecl(Id("max"), None, "var", ArrayCell(Id("a"), [NumberLiteral(0.0)])), VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp(">=", Id("i"), Id("length")), NumberLiteral(1.0), 
            If((BinaryOp(">", ArrayCell(Id("a"), [Id("i")]), Id("max"))), Assign(Id("max"), ArrayCell(Id("a"), [Id("i")])), [], None)), Return(Id("max"))]))]))
        self.assertTrue(TestAST.test(input,expect,352))    
    def test_53(self):
        input ="""func min(number a[100], number length)
begin
    if (length <= 0)
        return 1E+9 ## Represent possitive infinity
    var min <- a[0]
    var i <- 0
    for i until i >= length by 1
        if (a[i] < min) min <- a[i]
    return min
end
                """
        expect =str(Program([FuncDecl(Id("min"), [VarDecl(Id("a"), ArrayType([100.0], NumberType()), None, None), VarDecl(Id("length"), NumberType(), None, None)], Block([
            If((BinaryOp("<=", Id("length"), NumberLiteral(0.0))), Return(NumberLiteral(1000000000.0)), [], None), VarDecl(Id("min"), None, "var", ArrayCell(Id("a"), [NumberLiteral(0.0)])), VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp(">=", Id("i"), Id("length")), NumberLiteral(1.0), 
            If((BinaryOp("<", ArrayCell(Id("a"), [Id("i")]), Id("min"))), Assign(Id("min"), ArrayCell(Id("a"), [Id("i")])), [], None)), Return(Id("min"))]))]))
        self.assertTrue(TestAST.test(input,expect,353))    
    def test_54(self):
        input ="""func gcd(number a, number b)
begin
    if (b = 0) return a
    return gcd(b, a % b)
end

func main() begin
    writeNumber(gcd(6, 9))
    writeNumber(gcd(24, 16))
    writeNumber(gcd(1, 7))
end
                """
        expect =str(Program([FuncDecl(Id("gcd"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Block([
            If((BinaryOp("=", Id("b"), NumberLiteral(0.0))), Return(Id("a")), [], None), Return(CallExpr(Id("gcd"), [Id("b"), BinaryOp("%", Id("a"), Id("b"))]))])), FuncDecl(Id("main"), [], Block([CallStmt(Id("writeNumber"), [CallExpr(Id("gcd"), [NumberLiteral(6.0), NumberLiteral(9.0)])]), CallStmt(Id("writeNumber"), [CallExpr(Id("gcd"), [NumberLiteral(24.0), NumberLiteral(16.0)])]), CallStmt(Id("writeNumber"), [CallExpr(Id("gcd"), [NumberLiteral(1.0), NumberLiteral(7.0)])])]))]))
        self.assertTrue(TestAST.test(input,expect,354))    
    def test_55(self):
        input ="""func main() return 1
                """
        expect =str(Program([FuncDecl(Id("main"), [], Return(NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input,expect,355))    
    def test_56(self):
        input ="""number a[5] <- [1, 2, 3, 4, 5]
                """
        expect =str(Program([VarDecl(Id("a"), ArrayType([5.0], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0), NumberLiteral(5.0)]))]))
        self.assertTrue(TestAST.test(input,expect,356))    
    def test_57(self):
        input ="""func fun(number a[5], number n)
                begin
                    break
                end
                """
        expect =str(Program([FuncDecl(Id("fun"), [VarDecl(Id("a"), ArrayType([5.0], NumberType()), None, None), VarDecl(Id("n"), NumberType(), None, None)], Block(["Break"]))]))
        self.assertTrue(TestAST.test(input,expect,357))    
    def test_58(self):
        input ="""func concat(string a, string b)
                return a ... b
                """
        expect =str(Program([FuncDecl(Id("concat"), [VarDecl(Id("a"), StringType(), None, None), VarDecl(Id("b"), StringType(), None, None)], Return(BinaryOp("...", Id("a"), Id("b"))))]))
        self.assertTrue(TestAST.test(input,expect,358))    
    def test_59(self):
        input =""" func main() return 0
                func main1() return 1
                func main2() return 2
                func main3() return 3
                func main4() return 4
                func main5() return 5 
                """
        expect =str(Program([FuncDecl(Id("main"), [], Return(NumberLiteral(0.0))), FuncDecl(Id("main1"), [], Return(NumberLiteral(1.0))), FuncDecl(Id("main2"), [], Return(NumberLiteral(2.0))), FuncDecl(Id("main3"), [], Return(NumberLiteral(3.0))), FuncDecl(Id("main4"), [], Return(NumberLiteral(4.0))), FuncDecl(Id("main5"), [], Return(NumberLiteral(5.0)))]))
        self.assertTrue(TestAST.test(input,expect,359))
    def test_60(self):
        input ="""func check(number x)
                """
        expect =str(Program([FuncDecl(Id("check"), [VarDecl(Id("x"), NumberType(), None, None)], None)]))
        self.assertTrue(TestAST.test(input,expect,360))    
    def test_61(self):
        input ="""string a[3] <- ["Doan", "Minh", "Hieu"]
                """
        expect =str(Program([VarDecl(Id("a"), ArrayType([3.0], StringType()), None, ArrayLiteral([StringLiteral("Doan"), StringLiteral("Minh"), StringLiteral("Hieu")]))]))
        self.assertTrue(TestAST.test(input,expect,361))    
    def test_62(self):
        input ="""number a <- 0
                """
        expect =str(Program([VarDecl(Id("a"), NumberType(), None, NumberLiteral(0.0))]))
        self.assertTrue(TestAST.test(input,expect,362))    
    def test_63(self):
        input ="""number a <- 199
                """
        expect =str(Program([VarDecl(Id("a"), NumberType(), None, NumberLiteral(199.0))]))
        self.assertTrue(TestAST.test(input,expect,363))    
    def test_64(self):
        input ="""number a <- 12.
                """
        expect =str(Program([VarDecl(Id("a"), NumberType(), None, NumberLiteral(12.0))]))
        self.assertTrue(TestAST.test(input,expect,364))    
    def test_65(self):
        input ="""number a <- 12.3
                """
        expect =str(Program([VarDecl(Id("a"), NumberType(), None, NumberLiteral(12.3))]))
        self.assertTrue(TestAST.test(input,expect,365))    
    def test_66(self):
        input ="""number a <- 12.3e3
                """
        expect =str(Program([VarDecl(Id("a"), NumberType(), None, NumberLiteral(12300.0))]))
        self.assertTrue(TestAST.test(input,expect,366))    
    def test_67(self):
        input ="""number a <- 12e3
                """
        expect =str(Program([VarDecl(Id("a"), NumberType(), None, NumberLiteral(12000.0))]))
        self.assertTrue(TestAST.test(input,expect,367))    
    def test_68(self):
        input ="""number a <- 12.3e-30
                """
        expect =str(Program([VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.23e-29))]))
        self.assertTrue(TestAST.test(input,expect,368))    
    def test_69(self):
        input =""" func optional(number a)
      begin
        if (a = 1) 
        begin
            number sum <- 0
            number i <- 1
            for i until i <= 10 by 1
            begin
                sum <- sum + i
                return sum 
            end
        end
        else 
        begin
            number product <- 1
            number i <- 1
            for i until i <= 10 by 1
                product <- product * i
            return product
        end
      end
                """
        expect =str(Program([FuncDecl(Id("optional"), [VarDecl(Id("a"), NumberType(), None, None)], Block([
            If((BinaryOp("=", Id("a"), NumberLiteral(1.0))), Block([
                VarDecl(Id("sum"), NumberType(), None, NumberLiteral(0.0)), 
                VarDecl(Id("i"), NumberType(), None, NumberLiteral(1.0)), 
                For(Id("i"), BinaryOp("<=", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), 
                    Block([Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("i"))), Return(Id("sum"))]))]), [], Block([VarDecl(Id("product"), NumberType(), None, NumberLiteral(1.0)), VarDecl(Id("i"), NumberType(), None, NumberLiteral(1.0)), For(Id("i"), BinaryOp("<=", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), Assign(Id("product"), BinaryOp("*", Id("product"), Id("i")))), Return(Id("product"))]))]))]))
        self.assertTrue(TestAST.test(input,expect,369))    
    def test_70(self):
        input ="""func calculateAverage(number num1, number num2, number num3) 
                return (num1 + num2 + num3) / 3

                func main()
                begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                var num3 <- readNumber()

                var average <- calculateAverage(num1, num2, num3)

                writeNumber(average)
                end
                """
        expect =str(Program([FuncDecl(Id("calculateAverage"), [VarDecl(Id("num1"), NumberType(), None, None), VarDecl(Id("num2"), NumberType(), None, None), VarDecl(Id("num3"), NumberType(), None, None)], Return(BinaryOp("/", BinaryOp("+", BinaryOp("+", Id("num1"), Id("num2")), Id("num3")), NumberLiteral(3.0)))), FuncDecl(Id("main"), [], Block([VarDecl(Id("num1"), None, "var", CallExpr(Id("readNumber"), [])), VarDecl(Id("num2"), None, "var", CallExpr(Id("readNumber"), [])), VarDecl(Id("num3"), None, "var", CallExpr(Id("readNumber"), [])), VarDecl(Id("average"), None, "var", CallExpr(Id("calculateAverage"), [Id("num1"), Id("num2"), Id("num3")])), CallStmt(Id("writeNumber"), [Id("average")])]))]))
        self.assertTrue(TestAST.test(input,expect,370))    
    def test_71(self):
        input ="""func printArr(number a[100], number length)
begin
    if (length < 0)
        return
    printArr(a, length - 1)
    writeNumber(a[length - 1])
    writeString(" ")
end
                """
        expect =str(Program([FuncDecl(Id("printArr"), [VarDecl(Id("a"), ArrayType([100.0], NumberType()), None, None), VarDecl(Id("length"), NumberType(), None, None)], Block([If((BinaryOp("<", Id("length"), NumberLiteral(0.0))), Return(), [], None), CallStmt(Id("printArr"), [Id("a"), BinaryOp("-", Id("length"), NumberLiteral(1.0))]), CallStmt(Id("writeNumber"), [ArrayCell(Id("a"), [BinaryOp("-", Id("length"), NumberLiteral(1.0))])]), CallStmt(Id("writeString"), [StringLiteral(" ")])]))]))
        self.assertTrue(TestAST.test(input,expect,371))    
    def test_72(self):
        input ="""func round(number n)

func dec_to_bin(number n) begin
    if (n < 0) return "not implemented"
    if (n = 0) return "0"
    
    var res <- ""
    var i <- 0
    for i until n <= 0 by 0 begin
        if (n % 2 == 0) res <- "0" ... res
        else res <- "1" ... res
        n <- round(n/2)
    end
    
    return res
end

func round(number n) return n - n % 1
                """
        expect =str(Program([FuncDecl(Id("round"), [VarDecl(Id("n"), NumberType(), None, None)], None), FuncDecl(Id("dec_to_bin"), [VarDecl(Id("n"), NumberType(), None, None)], Block([If((BinaryOp("<", Id("n"), NumberLiteral(0.0))), Return(StringLiteral("not implemented")), [], None), If((BinaryOp("=", Id("n"), NumberLiteral(0.0))), Return(StringLiteral("0")), [], None), VarDecl(Id("res"), None, "var", StringLiteral("")), VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp("<=", Id("n"), NumberLiteral(0.0)), NumberLiteral(0.0), Block([
            If((BinaryOp("==", BinaryOp("%", Id("n"), NumberLiteral(2.0)), NumberLiteral(0.0))), Assign(Id("res"), BinaryOp("...", StringLiteral("0"), Id("res"))), [], Assign(Id("res"), BinaryOp("...", StringLiteral("1"), Id("res")))), Assign(Id("n"), CallExpr(Id("round"), [BinaryOp("/", Id("n"), NumberLiteral(2.0))]))])), Return(Id("res"))])), FuncDecl(Id("round"), [VarDecl(Id("n"), NumberType(), None, None)], Return(BinaryOp("-", Id("n"), BinaryOp("%", Id("n"), NumberLiteral(1.0)))))]))
        self.assertTrue(TestAST.test(input,expect,372))    
    def test_73(self):
        input ="""func fib(number n)
begin
    if (res[n] != -1) return res[n]
    res[n] <- fib(n - 1) + fib(n - 2)
    return res[n]
end

func main() begin
    res[0] <- 0
    res[1] <- 1
    
    var i <- 2
    for i until i = 100 by 1 res[i] <- -1
    
    writeNumber(fib(5))
    writeNumber(fib(10))
    writeNumber(fib(50))
end
                """
        expect =str(Program([FuncDecl(Id("fib"), [VarDecl(Id("n"), NumberType(), None, None)], Block([
            If((BinaryOp("!=", ArrayCell(Id("res"), [Id("n")]), UnaryOp("-", NumberLiteral(1.0)))), Return(ArrayCell(Id("res"), [Id("n")])), [], None), Assign(ArrayCell(Id("res"), [Id("n")]), BinaryOp("+", CallExpr(Id("fib"), [BinaryOp("-", Id("n"), NumberLiteral(1.0))]), CallExpr(Id("fib"), [BinaryOp("-", Id("n"), NumberLiteral(2.0))]))), Return(ArrayCell(Id("res"), [Id("n")]))])), FuncDecl(Id("main"), [], Block([Assign(ArrayCell(Id("res"), [NumberLiteral(0.0)]), NumberLiteral(0.0)), Assign(ArrayCell(Id("res"), [NumberLiteral(1.0)]), NumberLiteral(1.0)), VarDecl(Id("i"), None, "var", NumberLiteral(2.0)), For(Id("i"), BinaryOp("=", Id("i"), NumberLiteral(100.0)), NumberLiteral(1.0), Assign(ArrayCell(Id("res"), [Id("i")]), UnaryOp("-", NumberLiteral(1.0)))), CallStmt(Id("writeNumber"), [CallExpr(Id("fib"), [NumberLiteral(5.0)])]), CallStmt(Id("writeNumber"), [CallExpr(Id("fib"), [NumberLiteral(10.0)])]), CallStmt(Id("writeNumber"), [CallExpr(Id("fib"), [NumberLiteral(50.0)])])]))]))
        self.assertTrue(TestAST.test(input,expect,373))    
    def test_74(self):
        input ="""func main() begin 
var i<-0
for i until i=1 by 1
    if (i=0) break 
end 
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp("=", Id("i"), NumberLiteral(1.0)), NumberLiteral(1.0), If((BinaryOp("=", Id("i"), NumberLiteral(0.0))), "Break", [], None))]))]))
        self.assertTrue(TestAST.test(input,expect,374))    
    def test_75(self):
        input ="""func main() begin 
var i<-0
for i until i=10 by 1
    begin 
        var j <- 1
        i <- i*j
        continue
    end
end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), For(Id("i"), BinaryOp("=", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), Block([VarDecl(Id("j"), None, "var", NumberLiteral(1.0)), Assign(Id("i"), BinaryOp("*", Id("i"), Id("j"))), "Continue"]))]))]))
        self.assertTrue(TestAST.test(input,expect,375))    
    def test_76(self):
        input ="""func main() begin 
    return 0
end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([Return(NumberLiteral(0.0))]))]))
        self.assertTrue(TestAST.test(input,expect,376))    
    def test_77(self):
        input ="""func returnArray() 
    return [[1,2,3,4],[2,3],2]
func main() begin 
    dynamic a <- returnArray()[0,1]
end
                """
        expect =str(Program([FuncDecl(Id("returnArray"), [], Return(ArrayLiteral([ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0)]), ArrayLiteral([NumberLiteral(2.0), NumberLiteral(3.0)]), NumberLiteral(2.0)]))), FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), None, "dynamic", ArrayCell(CallExpr(Id("returnArray"), []), [NumberLiteral(0.0), NumberLiteral(1.0)]))]))]))
        self.assertTrue(TestAST.test(input,expect,377))    
    def test_78(self):
        input ="""func main()
begin
    number arr[5] <- [5, 1, 4, 2, 8] ## declaring and initializing an array of numbers
    var n <- 5 ## number of elements in the array
    dynamic i 
    dynamic j ## loop variables
    dynamic temp ## temporary variable for swapping
    i<-0
    for i until i > n-1 by 1
    begin
        j<-0
        for j  until j > n-i-2 by 1
        begin
            if (arr[j] > arr[j+1])
            begin
                ## Swap arr[j] and arr[j+1]
                temp <- arr[j]
                arr[j] <- arr[j+1]
                arr[j+1] <- temp
            end
        end
    end
    
    ## After sorting, print the sorted array
    writeString("Sorted Array: ")
    i<-0
    for i until i > n-1 by 1
    begin
        writeNumber(arr[i])
    end
    return
end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("arr"), ArrayType([5.0], NumberType()), None, ArrayLiteral([NumberLiteral(5.0), NumberLiteral(1.0), NumberLiteral(4.0), NumberLiteral(2.0), NumberLiteral(8.0)])), VarDecl(Id("n"), None, "var", NumberLiteral(5.0)), VarDecl(Id("i"), None, "dynamic", None), VarDecl(Id("j"), None, "dynamic", None), VarDecl(Id("temp"), None, "dynamic", None), Assign(Id("i"), NumberLiteral(0.0)), For(Id("i"), BinaryOp(">", Id("i"), BinaryOp("-", Id("n"), NumberLiteral(1.0))), NumberLiteral(1.0), Block([Assign(Id("j"), NumberLiteral(0.0)), For(Id("j"), BinaryOp(">", Id("j"), BinaryOp("-", BinaryOp("-", Id("n"), Id("i")), NumberLiteral(2.0))), NumberLiteral(1.0), Block([If((BinaryOp(">", ArrayCell(Id("arr"), [Id("j")]), ArrayCell(Id("arr"), [BinaryOp("+", Id("j"), NumberLiteral(1.0))]))), Block([Assign(Id("temp"), ArrayCell(Id("arr"), [Id("j")])), Assign(ArrayCell(Id("arr"), [Id("j")]), ArrayCell(Id("arr"), [BinaryOp("+", Id("j"), NumberLiteral(1.0))])), Assign(ArrayCell(Id("arr"), [BinaryOp("+", Id("j"), NumberLiteral(1.0))]), Id("temp"))]), [], None)]))])), CallStmt(Id("writeString"), [StringLiteral("Sorted Array: ")]), Assign(Id("i"), NumberLiteral(0.0)), For(Id("i"), BinaryOp(">", Id("i"), BinaryOp("-", Id("n"), NumberLiteral(1.0))), NumberLiteral(1.0), Block([CallStmt(Id("writeNumber"), [ArrayCell(Id("arr"), [Id("i")])])])), Return()]))]))
        self.assertTrue(TestAST.test(input,expect,378))    
    def test_79(self):
        input ="""func inc(number x) return x+1
number a <-  inc(inc(inc(inc(3))))
                """
        expect =str(Program([FuncDecl(Id("inc"), [VarDecl(Id("x"), NumberType(), None, None)], Return(BinaryOp("+", Id("x"), NumberLiteral(1.0)))), VarDecl(Id("a"), NumberType(), None, CallExpr(Id("inc"), [CallExpr(Id("inc"), [CallExpr(Id("inc"), [CallExpr(Id("inc"), [NumberLiteral(3.0)])])])]))]))
        self.assertTrue(TestAST.test(input,expect,379))    
    def test_80(self):
        input ="""func print(string src, string dst, string aux)

func tower_of_hanoi(number n, string src, string dst, string aux)
begin
    if (n = 1) print(src, dst)
    else begin
        tower_of_hanoi(n - 1, src, aux, dst)
        tower_of_hanoi(1, src, dst, aux)
        tower_of_hanoi(n - 1, aux, dst, src)
    end
end

func print(string src, string dst) begin
    output <- "Move 1 disk from tower "
    output <- output ... src
    output <- output ... " to tower "
    output <- output ... des
    writeString(output)
end
                """
        expect =str(Program([FuncDecl(Id("print"), [VarDecl(Id("src"), StringType(), None, None), VarDecl(Id("dst"), StringType(), None, None), VarDecl(Id("aux"), StringType(), None, None)], None), FuncDecl(Id("tower_of_hanoi"), [VarDecl(Id("n"), NumberType(), None, None), VarDecl(Id("src"), StringType(), None, None), VarDecl(Id("dst"), StringType(), None, None), VarDecl(Id("aux"), StringType(), None, None)], Block([
            If((BinaryOp("=", Id("n"), NumberLiteral(1.0))), CallStmt(Id("print"), [Id("src"), Id("dst")]), [], Block([CallStmt(Id("tower_of_hanoi"), [BinaryOp("-", Id("n"), NumberLiteral(1.0)), Id("src"), Id("aux"), Id("dst")]), CallStmt(Id("tower_of_hanoi"), [NumberLiteral(1.0), Id("src"), Id("dst"), Id("aux")]), CallStmt(Id("tower_of_hanoi"), [BinaryOp("-", Id("n"), NumberLiteral(1.0)), Id("aux"), Id("dst"), Id("src")])]))])), FuncDecl(Id("print"), [VarDecl(Id("src"), StringType(), None, None), VarDecl(Id("dst"), StringType(), None, None)], Block([Assign(Id("output"), StringLiteral("Move 1 disk from tower ")), Assign(Id("output"), BinaryOp("...", Id("output"), Id("src"))), Assign(Id("output"), BinaryOp("...", Id("output"), StringLiteral(" to tower "))), Assign(Id("output"), BinaryOp("...", Id("output"), Id("des"))), CallStmt(Id("writeString"), [Id("output")])]))]))
        self.assertTrue(TestAST.test(input,expect,380))    
    def test_81(self):
        input ="""string a <- "Khong biet viet gi"
                """
        expect =str(Program([VarDecl(Id("a"), StringType(), None, StringLiteral("Khong biet viet gi"))]))
        self.assertTrue(TestAST.test(input,expect,381))    
    def test_82(self):
        input ="""func main() begin 
var num <- readNumber() 
number count <- 1 
number core <- 10 
for core until false by 0
    if (num < core) break
    else core <- 10*core
    count<-count+1
writeNumber(num)
writeString(" has ")
writeNumber(count) 
writeString(" digits.")
end 
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("num"), None, "var", CallExpr(Id("readNumber"), [])), VarDecl(Id("count"), NumberType(), None, NumberLiteral(1.0)), VarDecl(Id("core"), NumberType(), None, NumberLiteral(10.0)), For(Id("core"), BooleanLiteral(False), NumberLiteral(0.0), 
            If((BinaryOp("<", Id("num"), Id("core"))), "Break", [], Assign(Id("core"), BinaryOp("*", NumberLiteral(10.0), Id("core"))))), Assign(Id("count"), BinaryOp("+", Id("count"), NumberLiteral(1.0))), CallStmt(Id("writeNumber"), [Id("num")]), CallStmt(Id("writeString"), [StringLiteral(" has ")]), CallStmt(Id("writeNumber"), [Id("count")]), CallStmt(Id("writeString"), [StringLiteral(" digits.")])]))]))
        self.assertTrue(TestAST.test(input,expect,382))    
    def test_83(self):
        input ="""func main() 
begin 
    if (1) number a[3,2] <- [[1,2],[3,4],[5,6]]
end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If((NumberLiteral(1.0)), 
               VarDecl(Id("a"), ArrayType([3.0, 2.0], NumberType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)]), ArrayLiteral([NumberLiteral(3.0), NumberLiteral(4.0)]), ArrayLiteral([NumberLiteral(5.0), NumberLiteral(6.0)])])), [], None)]))]))
        self.assertTrue(TestAST.test(input,expect,383))    
    def test_84(self):
        input ="""func main()
begin 
    string s<-"check cmt"
end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("s"), StringType(), None, StringLiteral("check cmt"))]))]))
        self.assertTrue(TestAST.test(input,expect,384))    
    def test_85(self):
        input ="""func main() begin
number r
number s
r <- 2.0
number a[5]
number b[5]
s <- r * r * 3.14
a[0] <- s
end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("r"), NumberType(), None, None), VarDecl(Id("s"), NumberType(), None, None), Assign(Id("r"), NumberLiteral(2.0)), VarDecl(Id("a"), ArrayType([5.0], NumberType()), None, None), VarDecl(Id("b"), ArrayType([5.0], NumberType()), None, None), Assign(Id("s"), BinaryOp("*", BinaryOp("*", Id("r"), Id("r")), NumberLiteral(3.14))), Assign(ArrayCell(Id("a"), [NumberLiteral(0.0)]), Id("s"))]))]))
        self.assertTrue(TestAST.test(input,expect,385))    
    def test_86(self):
        input ="""number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
                """
        expect =str(Program([VarDecl(Id("b"), ArrayType([2.0, 3.0], NumberType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]), ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0)])]))]))
        self.assertTrue(TestAST.test(input,expect,386))    
    def test_87(self):
        input ="""number a[3] <- a[b[2, 3]] + 4
                """
        expect =str(Program([VarDecl(Id("a"), ArrayType([3.0], NumberType()), None, BinaryOp("+", ArrayCell(Id("a"), [ArrayCell(Id("b"), [NumberLiteral(2.0), NumberLiteral(3.0)])]), NumberLiteral(4.0)))]))
        self.assertTrue(TestAST.test(input,expect,387))    
    def test_88(self):
        input ="""var i <- 0
        func main() begin
                    for i until i >= 10 by 1
                    writeNumbe(i)
        end
                """
        expect =str(Program([VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), FuncDecl(Id("main"), [], Block([For(Id("i"), BinaryOp(">=", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), CallStmt(Id("writeNumbe"), [Id("i")]))]))]))
        self.assertTrue(TestAST.test(input,expect,388))    
    def test_89(self):
        input ="""func fibonacci(number n)
            begin
                if (n < 1) return n
                else return fibonacci(n - 1) + fibonacci(n - 2)
            end
                """
        expect =str(Program([FuncDecl(Id("fibonacci"), [VarDecl(Id("n"), NumberType(), None, None)], Block([
            If((BinaryOp("<", Id("n"), NumberLiteral(1.0))), 
               Return(Id("n")), 
               [], 
               Return(BinaryOp("+", CallExpr(Id("fibonacci"), [BinaryOp("-", Id("n"), NumberLiteral(1.0))]), CallExpr(Id("fibonacci"), [BinaryOp("-", Id("n"), NumberLiteral(2.0))]))))]))]))
        self.assertTrue(TestAST.test(input,expect,389))    
    def test_90(self):
        input ="""func calculateArea(number radius)
            begin
                var pi <- 3.14
                var area <- pi * radius * radius
                return area
            end
                """
        expect =str(Program([FuncDecl(Id("calculateArea"), [VarDecl(Id("radius"), NumberType(), None, None)], Block([VarDecl(Id("pi"), None, "var", NumberLiteral(3.14)), VarDecl(Id("area"), None, "var", BinaryOp("*", BinaryOp("*", Id("pi"), Id("radius")), Id("radius"))), Return(Id("area"))]))]))
        self.assertTrue(TestAST.test(input,expect,390))    
    def test_91(self):
        input ="""func checkNumberSign(number num)
            begin
                if (num > 0)
                    return "Positive"
                elif (num < 0)
                    return "Negative"
                else
                    return "Zero"
            end
                """
        expect =str(Program([FuncDecl(Id("checkNumberSign"), [VarDecl(Id("num"), NumberType(), None, None)], Block([
            If((BinaryOp(">", Id("num"), NumberLiteral(0.0))), 
               Return(StringLiteral("Positive")), 
               [(BinaryOp("<", Id("num"), NumberLiteral(0.0)), Return(StringLiteral("Negative")))], 
               Return(StringLiteral("Zero")))]))]))
        self.assertTrue(TestAST.test(input,expect,391))    
    def test_92(self):
        input ="""func main()
                begin
                    number a <- 1
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0))]))]))
        self.assertTrue(TestAST.test(input,expect,392))    
    def test_93(self):
        input ="""func main()
                begin
                    string a <- "hello"
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), StringType(), None, StringLiteral("hello"))]))]))
        self.assertTrue(TestAST.test(input,expect,393))    
    def test_94(self):
        input ="""func main()
                begin
                    bool a <- true
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), BoolType(), None, BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.test(input,expect,394))    
    def test_95(self):
        input ="""func main()
                begin
                    number a[3] <- [1,2,3]
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([3.0], NumberType()), None, ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]))]))]))
        self.assertTrue(TestAST.test(input,expect,395))    
    def test_96(self):
        input ="""func main()
                begin
                    string a[3] <- ["a","b","c"]
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([3.0], StringType()), None, ArrayLiteral([StringLiteral("a"),StringLiteral("b"), StringLiteral("c")]))]))]))
        self.assertTrue(TestAST.test(input,expect,396))    
    def test_97(self):
        input ="""func main()
                begin
                    bool a[3] <- [true, true, false]
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), ArrayType([3.0], BoolType()), None, ArrayLiteral([BooleanLiteral(True), BooleanLiteral(True), BooleanLiteral(False)]))]))]))
        self.assertTrue(TestAST.test(input,expect,397))    
    def test_98(self):
        input ="""func main()
                begin
                    return 0
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([Return(NumberLiteral(0.0))]))]))
        self.assertTrue(TestAST.test(input,expect,398))    
    def test_99(self):
        input ="""func main()
                begin
                    print("Sap ket thuc roi")
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([CallStmt(Id("print"), [StringLiteral("Sap ket thuc roi")])]))]))
        self.assertTrue(TestAST.test(input,expect,399))    
    def test_100(self):
        input ="""func main()
                begin
                    print("Ket thuc 100 test")
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([CallStmt(Id("print"), [StringLiteral("Ket thuc 100 test")])]))]))
        self.assertTrue(TestAST.test(input,expect,400))    
    