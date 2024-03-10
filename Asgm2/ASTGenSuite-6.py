
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    """declared  declared  declared  declared"""
    def test301(self):
        input = """
            number ppl
        """
        expect = str(Program([
                VarDecl(Id("ppl"), NumberType())
            ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 301))
    
    
    def test302(self):
        input = """
            string ppl <- 10
        """
        expect = str(Program([
                VarDecl(Id("ppl"), StringType(), None, NumberLiteral(10.0))
            ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 302))
    
    
    def test303(self):
        input = """
            string ppl
            bool ppl
            string ppl <- 1
            bool ppl <- 1
        """
        expect = str(Program([
                VarDecl(Id("ppl"), StringType()),
                VarDecl(Id("ppl"), BoolType()),
                VarDecl(Id("ppl"), StringType(), None, NumberLiteral(1.0)),
                VarDecl(Id("ppl"), BoolType(), None, NumberLiteral(1.0))
            ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 303))
    
    
    def test304(self):
        input = """
            string ppl[5] <- 1
            string ppl[5]
        """
        expect = str(Program([
                VarDecl(Id("ppl"), ArrayType([5.0], StringType()), None, NumberLiteral(1.0)),
                VarDecl(Id("ppl"), ArrayType([5.0], StringType()))
            ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 304))
        
        
    def test305(self):
        input = """
            number ppl[5,3,4.2] <- 1
            bool ppl[2,3,4]
        """
        expect = str(Program([
                VarDecl(Id("ppl"), ArrayType([5.0, 3.0, 4.2], NumberType()), None, NumberLiteral(1.0)),
                VarDecl(Id("ppl"), ArrayType([2.0, 3.0, 4.0], BoolType()))
            ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 305))
        
        
    def test306(self):
        input = """
            dynamic ppl <- 1
            dynamic ppl
        """
        expect = str(Program([
                    VarDecl(Id("ppl"), None, "dynamic", NumberLiteral(1.0)),
                    VarDecl(Id("ppl"), None, "dynamic")
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 306))
        
        
    def test307(self):
        input = """
            var ppl <- 1
        """
        expect = str(Program([
                    VarDecl(Id("ppl"), None, "var", NumberLiteral(1.0))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 307))
        
        
    def test308(self):
        input = """
            func main()
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], None)
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 308))
        
        
    def test309(self):
        input = """
            func main()
                begin
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 309))


    def test310(self):
        input = """
            func main()
                begin
                break
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Break()]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 310))
         
         
    def test311(self):       
        input = """
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number ppl[1,2])
                return
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("ppl"), ArrayType([1.0, 2.0], NumberType()))], Return(None))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 311))
    
    
    """Expression Expression Expression"""
    def test312(self):
        input = """
            var x <- 1
            var x <- "123"
            var x <- true
            var x <- false
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  NumberLiteral(1.0)),
                    VarDecl(Id("x"), None, "var",  StringLiteral("123")),
                    VarDecl(Id("x"), None, "var",  BooleanLiteral(True)),
                    VarDecl(Id("x"), None, "var",  BooleanLiteral(False))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 312))
        
        
    def test313(self):
        input = """
            var x <- [1, "a", true, false]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([NumberLiteral(1.0), StringLiteral("a"), BooleanLiteral(True), BooleanLiteral(False)]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 313))   
        
        
    def test314(self):
        input = """
            var x <- [[1], [1]]
            var x <- [[1]]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)]), ArrayLiteral([NumberLiteral(1.0)])])),
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)])]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 314))  
        
        
    def test315(self):
        input = """
            var x <- 1 ... "2"
            var x <- 1 <= "2"
            var x <- 1 and 2 or 3
            var x <- 1 + 2 - 3
            var x <- 1 * 2 / 3 % 4
            var x <- ---1
            var x <- not not 1
            var x <- x 
            var x <- a[1,2,3]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", NumberLiteral(1.0), StringLiteral("2"))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("<=", NumberLiteral(1.0), StringLiteral("2"))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("or", BinaryOp("and", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("-", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("%", BinaryOp("/", BinaryOp("*", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0)), NumberLiteral(4.0))),
                    VarDecl(Id("x"), None, "var",  UnaryOp("-", UnaryOp("-", UnaryOp("-", NumberLiteral(1.0))))),
                    VarDecl(Id("x"), None, "var",  UnaryOp("not", UnaryOp("not", NumberLiteral(1.0)))),
                    VarDecl(Id("x"), None, "var",  Id("x")),
                    VarDecl(Id("x"), None, "var",  ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 315))  
        
        
    def test316(self):
        input = """
            var x <- 2 or 3 and 1 <= 2 ... 4 <= 5 + a * 3 + c - -1 + not - 2
        """
        expect = str(Program([
                VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("<=", BinaryOp("and", BinaryOp("or", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(1.0)), NumberLiteral(2.0)), BinaryOp("<=", NumberLiteral(4.0), BinaryOp("+", BinaryOp("-", BinaryOp("+", BinaryOp("+", NumberLiteral(5.0), BinaryOp("*", Id("a"), NumberLiteral(3.0))), Id("c")), UnaryOp("-", NumberLiteral(1.0))), UnaryOp("not", UnaryOp("-", NumberLiteral(2.0)))))))
            ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 316))  
        
        
    def test317(self):
        input = """
            var x <- -a[1+2] ... 2
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", UnaryOp("-", ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0))])), NumberLiteral(2.0)))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 317))  
        
        
    def test318(self):
        input = """
            var x <- fun()
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), []))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 318)) 
        
        
    def test319(self):
        input = """
            var x <- fun(1+1, "a")
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), StringLiteral("a")]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 319)) 
        
        
    def test320(self):
        input = """
            var x <- fun(fun())
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), [CallExpr(Id("fun"), [])]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 320)) 
        
        
    def test321(self):
        input = """
            var x <- (2 ... 3) ... 4
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("...", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(4.0)))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 321)) 
    
    
    """Expression Expression Expression"""
    def test322(self):
        input = """
            func main()
                begin
                    continue
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue()]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 322))


    def test323(self):
        input = """
            func main()
                begin
                    continue
                    continue
                    break
                    begin
                        continue
                        continue
                        break                    
                    end
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue(),
                    Continue(),
                    Break(),
                        Block([
                        Continue(),
                        Continue(),
                        Break()])]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 323))
        
        
    def test324(self):
        input = """
            func main()
                begin
                    return  1 + 1
                    return
                end
            func main()
                return 1
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Return(BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0))),
                    Return()])),
                    FuncDecl(Id("main"), [], Return(NumberLiteral(1.0)))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 324))


    def test325(self):
        input = """
            func main()
                begin
                    main(a)
                    main(1,1)
                end
            func main()
                begin
                main()
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    CallStmt(Id("main"), [Id("a")]),
                    CallStmt(Id("main"), [NumberLiteral(1.0), NumberLiteral(1.0)])])),
                    FuncDecl(Id("main"), [], Block([
                    CallStmt(Id("main"), [])]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 325))
        
        
    def test326(self):
        input = """
            func main()
                begin
                    a <- 1
                    a[1] <- 2
                    a[3,2] <- 4 + 2
                end
            func main()
                begin
                a[1+1, 3] <- 1
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Assign(Id("a"), NumberLiteral(1.0)),
                    Assign(ArrayCell(Id("a"), [NumberLiteral(1.0)]), NumberLiteral(2.0)),
                    Assign(ArrayCell(Id("a"), [NumberLiteral(3.0), NumberLiteral(2.0)]), BinaryOp("+", NumberLiteral(4.0), NumberLiteral(2.0)))])),
                    FuncDecl(Id("main"), [], Block([
                    Assign(ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), NumberLiteral(3.0)]), NumberLiteral(1.0))]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 326))
        
        
    def test327(self):
        input = """
            func main()
                begin
                    for i until i > 2 by 1 + 1
                        print(1)
                end
            func main()
                begin
                    for i until i by [1]
                    begin
                        print(1)
                    end
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    For(Id("i"), BinaryOp(">", Id("i"), NumberLiteral(2.0)), BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), CallStmt(Id("print"), [NumberLiteral(1.0)]))])),
                    FuncDecl(Id("main"), [], Block([
                    For(Id("i"), Id("i"), ArrayLiteral([NumberLiteral(1.0)]), Block([
                    CallStmt(Id("print"), [NumberLiteral(1.0)])]))]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 327))
        
        
    def test328(self):
        input = """
            func main()
                begin
                    if (true) return 1
                end
            func main()
                begin
                    if (true) return 2
                    else return 3
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [] , None)])),
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(2.0)), [] ,Return(NumberLiteral(3.0)))]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 328))
        

    def test329(self):
        input = """
            func main()
                begin
                    if (true) return 1
                    elif (true) return 1
                    elif (true) return 1
                    else return 1
                end

        """
        expect =str(Program([
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(1.0)), 
                       [(BooleanLiteral(True),Return(NumberLiteral(1.0))),
                        (BooleanLiteral(True),Return(NumberLiteral(1.0)))] 
                    ,Return(NumberLiteral(1.0)))]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 329))     
        
        
    def test330(self):
        input = """
            var c <- a[1,2]
            var c <- fun()[1,2]
            var c <- fun(1,2)[1,3]
        """
        expect = str(Program([
            VarDecl(Id("c"), None, "var", ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0)])),
            VarDecl(Id("c"), None, "var", ArrayCell(CallExpr(Id("fun"), []), [NumberLiteral(1.0), NumberLiteral(2.0)])),
            VarDecl(Id("c"), None, "var", ArrayCell(CallExpr(Id("fun"), [NumberLiteral(1.0), NumberLiteral(2.0)]), [NumberLiteral(1.0), NumberLiteral(3.0)]))
        ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 330))    
        
        
    def test331(self):
        input = """
            func main()
            begin
                var c <- 2e5
                dynamic c <- 2.56
                dynamic c
                number c[2e2, 2] <- 3.6
                string c[3.823]
            end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block(
                [VarDecl(Id("c"), None, "var", NumberLiteral(200000.0)), 
                 VarDecl(Id("c"), None, "dynamic", NumberLiteral(2.56)), 
                 VarDecl(Id("c"), None, "dynamic"),
                 VarDecl(Id("c"), ArrayType([200.0, 2.0], NumberType()), None, NumberLiteral(3.6)),
                 VarDecl(Id("c"), ArrayType([3.823], StringType()), None)
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 331))    
        
             
    def test332(self):
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        else return 1
                end

        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [], Return(NumberLiteral(1.0))), [], None)
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 332))     
        
        
    def test333(self):
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        else return 1
                    else return 1
                end

        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [], Return(NumberLiteral(1.0))), 
               [], Return(NumberLiteral(1.0)))
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 333))   
        
        
    def test334(self):
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        elif (true) return 1
                        else return 1
                end

        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0))), [], None)
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 334))   
        
        
    def test335(self):
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        elif (true) return 1
                        elif (true) return 1
                end

        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(1.0))), (BooleanLiteral(True),Return(NumberLiteral(1.0)))]), [], None)
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 335))
        
    
    def test336(self):
        input = """
            func main()
                begin
                    if (true)
                        if(true) return 1
                        elif (true) return 1
                        elif (true) return 1
                        else return 1
                    elif (true) return 1
                    elif (true) return 1                        
                    else return 1
                end

        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
               If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(1.0))), (BooleanLiteral(True),Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0)))
            , [(BooleanLiteral(True),Return(NumberLiteral(1.0))), (BooleanLiteral(True),Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0)))
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 336))   
        

    def test337(self):
        input = """
            func main()
            begin
                if (true) return 1
                elif (false) return 2  
                else return 3
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), Return(NumberLiteral(1.0)), 
               [(BooleanLiteral(False),Return(NumberLiteral(2.0)))], 
               Return(NumberLiteral(3.0))
               )
        ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 337))
    
    
    def test338(self):
        input = """
            func main()
            begin
                if (true) 
                    if (true) return 1.1
                    elif (false) return 1.2
                    else return 1.3
                elif (false) return 2  
                else return 3
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
                    If(BooleanLiteral(True), Return(NumberLiteral(1.1)), 
                    [(BooleanLiteral(False), Return(NumberLiteral(1.2)))],
                    Return(NumberLiteral(1.3))), 
               [(BooleanLiteral(False), Return(NumberLiteral(2.0)))], 
               Return(NumberLiteral(3.0))
               )
        ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 338))
        
    
    def test339(self):
        input = """
            func main()
            begin
                if (true) 
                    if (true) return 1.1
                    elif (false) return 1.2
                    elif (false) return 1.3
                else return 1.4
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
                    If(BooleanLiteral(True), Return(NumberLiteral(1.1)), 
                    [(BooleanLiteral(False), Return(NumberLiteral(1.2))), (BooleanLiteral(False), Return(NumberLiteral(1.3)))], 
                    Return(NumberLiteral(1.4)))
                )
        ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 339))
    
    
    def test340(self):
        input = """
            func main()
                begin
                    if (1)
                        b()
                    elif (2)
                        if (3)
                            c()
                        elif (4)
                            d()
                        else
                            e()
                end

        """

        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(NumberLiteral(1.0), CallStmt(Id("b"), []), 
               [[NumberLiteral(2.0), If(NumberLiteral(3.0), CallStmt(Id("c"), []), [[NumberLiteral(4.0), CallStmt(Id("d"), [])]], CallStmt(Id("e"), []))]], None)
            ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 340))
    
    
    def test341(self):
        input = """
            func main()
            begin
                if (true) 
                    if (true) return 1.1
                    elif (false) return 1.2
                    elif (false) return 1.3
                    else return 1.4
                else return 2
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
                    If(BooleanLiteral(True), Return(NumberLiteral(1.1)), 
                    [(BooleanLiteral(False), Return(NumberLiteral(1.2))), (BooleanLiteral(False), Return(NumberLiteral(1.3)))], 
                    Return(NumberLiteral(1.4))),
                [],
                Return(NumberLiteral(2.0))
                )
        ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 341))
    
    
    def test342(self):
        input = """
            func main()
            begin
                if (true) 
                    if (true) return 1.1
                    elif (false) return 1.2
                    elif (false) return 1.3
                    else return 1.4
                elif (true) return 2
                elif (false) return 3
                else return 4
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
                    If(BooleanLiteral(True), Return(NumberLiteral(1.1)), 
                    [(BooleanLiteral(False), Return(NumberLiteral(1.2))), (BooleanLiteral(False), Return(NumberLiteral(1.3)))], 
                    Return(NumberLiteral(1.4))),
                [(BooleanLiteral(True), Return(NumberLiteral(2.0))), (BooleanLiteral(False), Return(NumberLiteral(3.0)))],
                Return(NumberLiteral(4.0))
                )
        ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 342))
    
    
    def test343(self):
        input = """
            func main()
            begin
                if (true) 
                    if (true) return 1.1
                    elif (true) 
                        if (true) return 1.21
                        elif (true) return 1.22
                        else return 1.23
                    elif (true) return 1.3
                    else return 1.4
                elif (true) return 2
                elif (true) return 3
                else return 4
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
                    If(BooleanLiteral(True), Return(NumberLiteral(1.1)), 
                    [(BooleanLiteral(True), 
                        If(BooleanLiteral(True), Return(NumberLiteral(1.21)), 
                        [(BooleanLiteral(True), Return(NumberLiteral(1.22)))],
                        Return(NumberLiteral(1.23)))), 
                    (BooleanLiteral(True), Return(NumberLiteral(1.3)))], 
                    Return(NumberLiteral(1.4))),
                [(BooleanLiteral(True), Return(NumberLiteral(2.0))), (BooleanLiteral(True), Return(NumberLiteral(3.0)))],
                Return(NumberLiteral(4.0))
                )
        ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 343))
    
    
    def test344(self):
        input = """
            func main()
            begin
                if (true) 
                    if (true) return 1.1
                    elif (true) 
                        if (true) return 1.21
                        elif (true) return 1.22
                        else return 1.23
                    elif (true) return 1.3
                    else return 1.4
                elif (true) return 2
                elif (true) return 3
                else 
                    if (true) return 4.1
                    elif (true) return 4.2
                    elif (true) return 4.3
                    else return 4.4
            end
        """
        expect =str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
                    If(BooleanLiteral(True), Return(NumberLiteral(1.1)), 
                    [(BooleanLiteral(True), 
                        If(BooleanLiteral(True), Return(NumberLiteral(1.21)), 
                        [(BooleanLiteral(True), Return(NumberLiteral(1.22)))],
                        Return(NumberLiteral(1.23)))), 
                    (BooleanLiteral(True), Return(NumberLiteral(1.3)))], 
                    Return(NumberLiteral(1.4))),
                [(BooleanLiteral(True), Return(NumberLiteral(2.0))), (BooleanLiteral(True), Return(NumberLiteral(3.0)))],
                If(BooleanLiteral(True), Return(NumberLiteral(4.1)), 
                    [(BooleanLiteral(True), Return(NumberLiteral(4.2))), (BooleanLiteral(True), Return(NumberLiteral(4.3)))],
                    Return(NumberLiteral(4.4)))
                )
        ]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 344))
    
    
    def test345(self):
        input = """
            func main(number a, string a, bool a[2])
            func main(number arr[1,2])
                return 
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("arr"), ArrayType([1.0, 2.0], NumberType()))], Return(None))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 345))
    
    
    def test346(self):
        input = """
            func foo(number a, string a, bool a[2])
            func foo(number arr[1, 2], string arr[1, 9])
                return 
        """
        expect = str(Program([
                    FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("foo"), [VarDecl(Id("arr"), ArrayType([1.0, 2.0], NumberType())),
                                        VarDecl(Id("arr"), ArrayType([1.0, 9.0], StringType()))], Return(None))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 346))
    
    
    def test347(self):
        input = """
            func foo(number a, string a, bool a[2])
            begin
                for i until 0 by 1
                    for j until 0 by -1
                    begin
                    end
            end
            
            
            func foo(number arr[1, 2], string arr[1, 9])
                return 
        """
        expect = str(Program([
                    FuncDecl(Id("foo"), [VarDecl(Id("a"), NumberType()), 
                                        VarDecl(Id("a"), StringType()), 
                                        VarDecl(Id("a"), ArrayType([2.0], BoolType()))], Block([
                                            For(Id("i"), NumberLiteral(0.0), NumberLiteral(1.0), 
                                                For(Id("j"), NumberLiteral(0.0), UnaryOp('-', NumberLiteral(1.0)), Block([]))),
                                            ])),
                    FuncDecl(Id("foo"), [VarDecl(Id("arr"), ArrayType([1.0, 2.0], NumberType())),
                                        VarDecl(Id("arr"), ArrayType([1.0, 9.0], StringType()))], Return(None))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 347))
    
    
    def test348(self):
        input = """
            var a <- foo(1 + 1, foo(100)[2, 1 + 1], foo([1, 9], [0, 9]))
        """
        expect = str(Program([
                    VarDecl(Id("a"), None, "var", CallExpr(Id("foo"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), 
                                                                       ArrayCell(CallExpr(Id("foo"), [NumberLiteral(100.0)]), [NumberLiteral(2.0), BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0))]), 
                                                                       CallExpr(Id("foo"), [ArrayLiteral([NumberLiteral(1.0), NumberLiteral(9.0)]), ArrayLiteral([NumberLiteral(0.0), NumberLiteral(9.0)])])]))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 348))
    
    def test349(self):
        input = """
    func a()
        begin
        end
    var x <-2 
    dynamic x <- "hello\\\\"..."world\\'"----------22
    func a()
        begin
        end
        
    """
        expect = """Program([FuncDecl(Id(a), [], Block([])), VarDecl(Id(x), None, var, NumLit(2.0)), VarDecl(Id(x), None, dynamic, BinaryOp(..., StringLit(hello\\\\), BinaryOp(-, StringLit(world\\\'), UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(22.0))))))))))))), FuncDecl(Id(a), [], Block([]))])"""
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 349))
    
    
    
    '''NAM's testcases ----------------------------------------------------------------'''
    def test378(self):
        input = """
            number a
            string b
            bool c
        """
        expect = str(Program([VarDecl(Id("a"), NumberType()), VarDecl(
            Id("b"), StringType()), VarDecl(Id("c"), BoolType())]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 378))

    
    def test380(self):
        input = """
            string a <- "hello"
            number b <- 1
            bool c <- true 
        """
        expect = str(Program([VarDecl(Id("a"), StringType(), None, StringLiteral("hello")), VarDecl(
            Id("b"), NumberType(), None, NumberLiteral(1.0)), VarDecl(Id("c"), BoolType(), None, BooleanLiteral(True))
        ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 380))

    
    def test381(self):
        input = """ 
            string a <- "hello"
            number b <- 1
            bool c <- true
            number d
            string e
            bool f
        """
        expect = str(Program([VarDecl(Id("a"), StringType(), None, StringLiteral("hello")), VarDecl(
            Id("b"), NumberType(),
            None, NumberLiteral(1.0)), VarDecl(Id("c"), BoolType(), None, BooleanLiteral(True)), VarDecl(Id("d"), NumberType()),
            VarDecl(Id("e"),
                    StringType()), VarDecl(Id("f"), BoolType())]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 381))

    
    def test382(self):
        input = """
            number a[4,5]
            number b[2,3] <- [[1,2,3],[4,5,6]] 
        """
        expect = str(
            Program([VarDecl(Id("a"), ArrayType([4.0, 5.0], NumberType()), None, None), VarDecl(Id("b"), ArrayType([2.0, 3.0], NumberType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]), ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0)])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 382))

    
    def test383(self):
        input = """
            number a[1.2,3.4]<-"hello"
            bool b[1,2]
            string c[2,3]<-[[1,2,3],[4,5,6]]
        """
        expect = str(Program([VarDecl(Id("a"), ArrayType([1.2, 3.4], NumberType()), None, StringLiteral("hello")), VarDecl(Id("b"), ArrayType([1.0, 2.0], BoolType())), VarDecl(Id("c"), ArrayType(
            [2.0, 3.0], StringType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]), ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0)])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 383))


    def test384(self):
        input = """
            var a <- 1
            dynamic b <- "hello"
            var c <- true 
        """
        expect = str(Program([VarDecl(Id("a"), None, "var", NumberLiteral(1.0)), VarDecl(
            Id("b"), None, "dynamic", StringLiteral("hello")), VarDecl(Id("c"), None, "var", BooleanLiteral(True))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 384))

    
    def test385(self):
        input = """ 
            dynamic b
        """
        expect = str(Program([VarDecl(Id("b"), None, "dynamic", None)]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 385))

    
    def test386(self):
        input = """
            func main() 
        """
        expect = str(Program([FuncDecl(Id("main"), [], None)]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 386))

    
    def test387(self):
        input = """ 
            func main() begin
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 387))

    
    def test388(self):
        input = """
            func main() return 0
        """
        expect = str(Program([FuncDecl(Id("main"), [], Return(NumberLiteral(0.0)))])
                     )
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 388))

    
    def test389(self):
        input = """ 
            func main()
                begin 
                    break
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([Break()]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 389))

    
    def test390(self):
        input = """ 
            func swap(number a, number b)
                begin
                    var temp <- a
                    a <- b
                    b <- temp
                end
            func main()
                begin
                    number a <- 1
                    number b <- 2
                    swap(a, b)
                    return 0
                end
        """
        expect = str(Program([FuncDecl(Id("swap"), [VarDecl(Id("a"), NumberType()), VarDecl(Id("b"), NumberType())], Block([VarDecl(Id("temp"), None, "var", Id("a")), Assign(Id("a"), Id("b")), Assign(Id("b"), Id("temp"))])), FuncDecl(
            Id("main"), [], Block([VarDecl(Id("a"), NumberType(), None, NumberLiteral(1.0)), VarDecl(Id("b"), NumberType(), None, NumberLiteral(2.0)), CallStmt(Id("swap"), [Id("a"), Id("b")]), Return(NumberLiteral(0.0))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 390))
    

    def test391(self):
        input = """
            var a <- [1,"hello",true]
        """
        expect = str(Program([VarDecl(Id("a"), None, "var", ArrayLiteral(
            [NumberLiteral(1.0), StringLiteral("hello"), BooleanLiteral(True)]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 391))


    def test392(self):
        input = """
            var x <- 1 ... "2"
            var x <- 1 <= "2"
            var x <- 1 and 2 or 3
            var x <- 1 + 2 - 3
            var x <- 1 * 2 / 3 % 4
            var x <- ---1
            var x <- not not 1
            var x <- x 
            var x <- a[1,2,3]
        """
        expect = str(
            Program([VarDecl(Id("x"), None, "var", BinaryOp("...", NumberLiteral(1.0), StringLiteral("2"))),
                    VarDecl(Id("x"), None, "var",  BinaryOp(
                        "<=", NumberLiteral(1.0), StringLiteral("2"))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("or", BinaryOp(
                        "and", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
                    VarDecl(Id("x"), None, "var",  BinaryOp(
                        "-", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("%", BinaryOp(
                        "/", BinaryOp("*", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0)), NumberLiteral(4.0))),
                    VarDecl(Id("x"), None, "var",  UnaryOp(
                        "-", UnaryOp("-", UnaryOp("-", NumberLiteral(1.0))))),
                    VarDecl(Id("x"), None, "var",  UnaryOp(
                        "not", UnaryOp("not", NumberLiteral(1.0)))),
                    VarDecl(Id("x"), None, "var",  Id("x")),
                    VarDecl(Id("x"), None, "var",  ArrayCell(
                        Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]))
                     ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 392))


    def test393(self):
        input = """
            var a <- ppl()
        """
        expect = str(
            Program([VarDecl(Id("a"), None, "var", CallExpr(Id("ppl"), []))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 393))


    def test394(self):
        input = """
            func main()
                begin
                    if (true)
                        print("Hello")
                    else
                        print("World") 
                end 
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([If(BooleanLiteral(True), CallStmt(
            Id("print"), [StringLiteral("Hello")]), [], CallStmt(Id("print"), [StringLiteral("World")]))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 394))

    
    def test395(self):
        input = """
            func main()
                begin
                    for i until i < 10 by i=i+1
                        print(i) 
                end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)),
                                                                  BinaryOp("=", Id("i"), BinaryOp("+", Id("i"), NumberLiteral(1.0))), CallStmt(Id("print"), [Id("i")]))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 395))

    
    def test396(self):
        input = """
            func main()
                begin
                    a <- b
                    continue
                end
        """
        expect = str(Program(
            [FuncDecl(Id("main"), [], Block([Assign(Id("a"), Id("b")), Continue()]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 396))


    def test397(self):
        input = """
            func quickSort(number arr[10], number low, number high)
                begin
                    hongconho <- 1
                    return 0
                end
            func main()
                begin
                    number arr[10] <- [4, 3, 2, 1, 5, 7, 6, 8, 9, 0]
                    quickSort(arr, 0, 9)
                    print(arr)
                    return 0
                end
        """
        expect = str(Program([FuncDecl(Id("quickSort"), [VarDecl(Id("arr"), ArrayType([10.0], NumberType())), VarDecl(Id("low"), NumberType()), VarDecl(Id("high"), NumberType())], Block([Assign(Id("hongconho"), NumberLiteral(1.0)), Return(NumberLiteral(0.0))])), FuncDecl(Id("main"), [], Block([VarDecl(Id("arr"), ArrayType([10.0], NumberType()), None, ArrayLiteral(
            [NumberLiteral(4.0), NumberLiteral(3.0), NumberLiteral(2.0), NumberLiteral(1.0), NumberLiteral(5.0), NumberLiteral(7.0), NumberLiteral(6.0), NumberLiteral(8.0), NumberLiteral(9.0), NumberLiteral(0.0)])), CallStmt(Id("quickSort"), [Id("arr"), NumberLiteral(0.0), NumberLiteral(9.0)]), CallStmt(Id("print"), [Id("arr")]), Return(NumberLiteral(0.0))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 397))

    
    def test398(self):
        input = """
            func main()
                begin
                    var a <- 1
                    var b <- 2
                    var c <- 3
                    if (a < b)
                        print("a < b")
                    elif (a > b)
                        print("a > b")
                    else
                        print("a = b")
                    return 0
                end 
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), None, "var", NumberLiteral(1.0)),
                                                             VarDecl(
                                                                 Id("b"), None, "var", NumberLiteral(2.0)),
                                                              VarDecl(
                                                                  Id("c"), None, "var", NumberLiteral(3.0)),
                                                              If(BinaryOp("<", Id("a"), Id("b")), CallStmt(Id("print"), [StringLiteral("a < b")]),
                                                                 [(BinaryOp(">", Id("a"), Id("b")), CallStmt(Id("print"), [StringLiteral("a > b")]))], CallStmt(Id("print"), [StringLiteral("a = b")])), Return(NumberLiteral(0.0))]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 398))

    
    def test399(self):
        input = """ 
            func call()
                begin
                    continue
                    continue
                    break 
                    break
                    no <- yes
                    begin
                        return 0
                    end
                    for i until i < 10 by i=i+1
                        print(i)
                    return 0 
                end
            func main()
                begin
                    call() 
                end 
        """
        expect = str(Program([FuncDecl(Id("call"), [], Block([Continue(), Continue(), Break(), Break(), Assign(Id("no"), Id("yes")),
                                                              Block([Return(NumberLiteral(0.0))]), For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)),
                                                                                                       BinaryOp("=", Id("i"), BinaryOp(
                                                                                                           "+", Id("i"), NumberLiteral(1.0))),
                                                                                                       CallStmt(Id("print"), [Id("i")])), Return(NumberLiteral(0.0))])), FuncDecl(Id("main"), [], Block([CallStmt(Id("call"), [])]))]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 399))    