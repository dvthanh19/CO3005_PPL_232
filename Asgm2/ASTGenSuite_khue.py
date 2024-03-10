
import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

    def test_601(self):
        self.assertTrue(TestAST.test('''
func main ()
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

    ''', '''Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(b), [])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(c), [])), [(NumLit(4.0), CallStmt(Id(d), []))], CallStmt(Id(e), [])))], None)]))])''', 601))


    def test_602(self):
        self.assertTrue(TestAST.test('''
    func a()
        begin
        end
    var x <-2 
    dynamic x <- "hello\\\\"..."world\\'"----------22
    func a()
        begin
        end
        
    ''', '''Program([FuncDecl(Id(a), [], Block([])), VarDecl(Id(x), None, var, NumLit(2.0)), VarDecl(Id(x), None, dynamic, BinaryOp(..., StringLit(hello\\\\), BinaryOp(-, StringLit(world\\\'), UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(22.0))))))))))))), FuncDecl(Id(a), [], Block([]))])''', 602))


    def test_603(self):
        self.assertTrue(TestAST.test('''
    string x<- a...b
    ''', '''Program([VarDecl(Id(x), StringType, None, BinaryOp(..., Id(a), Id(b)))])''', 603))


    def test_604(self):
        self.assertTrue(TestAST.test('''
    func x()
    begin

        return
    end
    
    ''', '''Program([FuncDecl(Id(x), [], Block([Return()]))])''', 604))


    def test_605(self):
        self.assertTrue(TestAST.test('''
    bool lit <- not true and true and false or 2 
    
    ''', '''Program([VarDecl(Id(lit), BoolType, None, BinaryOp(or, BinaryOp(and, BinaryOp(and, UnaryOp(not, BooleanLit(True)), BooleanLit(True)), BooleanLit(False)), NumLit(2.0)))])''', 605))


    def test_606(self):
        self.assertTrue(TestAST.test('''
    func x()






    begin 
    hello()
    kkap(kk(yeah(ha(idk(2,4,[2,4,[[[[[[[[[[[2]]]]]]]]]]],45],4)))))
    end






    ''', '''Program([FuncDecl(Id(x), [], Block([CallStmt(Id(hello), []), CallStmt(Id(kkap), [CallExpr(Id(kk), [CallExpr(Id(yeah), [CallExpr(Id(ha), [CallExpr(Id(idk), [NumLit(2.0), NumLit(4.0), ArrayLit(NumLit(2.0), NumLit(4.0), ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(2.0)))))))))))), NumLit(45.0)), NumLit(4.0)])])])])])]))])''', 606))

    def test_607(self):
        self.assertTrue(TestAST.test('''
    ##nothing
        func a()
        begin
            begin
                begin
                    begin
                        begin
                            begin
                                begin
                                call()
                                begin
                                ##aaaa
                                call()
                                call()

                                end
                                end
                            end
                        end
                    end
                end
            end
        end
        
    ''', '''Program([FuncDecl(Id(a), [], Block([Block([Block([Block([Block([Block([Block([CallStmt(Id(call), []), Block([CallStmt(Id(call), []), CallStmt(Id(call), [])])])])])])])])]))])''', 607))


    def test_608(self):
        self.assertTrue(TestAST.test('''
    func a()
        begin
            begin
                begin
                    begin
                        begin
                            begin
                                begin
                                call()
                                begin
                                ##aaaa
                                call()
                                end
                                end
                            end
                        end
                    end
                end
            end
        end
        
    ''', '''Program([FuncDecl(Id(a), [], Block([Block([Block([Block([Block([Block([Block([CallStmt(Id(call), []), Block([CallStmt(Id(call), [])])])])])])])])]))])''', 608))


    def test_609(self):
        self.assertTrue(TestAST.test('''
    dynamic x
    func foo()
        begin
            var x <- 2
        end

    ''', '''Program([VarDecl(Id(x), None, dynamic, None), FuncDecl(Id(foo), [], Block([VarDecl(Id(x), None, var, NumLit(2.0))]))])''', 609))


    def test_610(self):
        self.assertTrue(TestAST.test('''
    string x<- 2 and 2
    func a()
        begin
        
        end

    ''', '''Program([VarDecl(Id(x), StringType, None, BinaryOp(and, NumLit(2.0), NumLit(2.0))), FuncDecl(Id(a), [], Block([]))])''', 610))


    def test_611(self):
        self.assertTrue(TestAST.test('''
    string x<-2 and 2
    func a()
        begin
        return
        end

    ''', '''Program([VarDecl(Id(x), StringType, None, BinaryOp(and, NumLit(2.0), NumLit(2.0))), FuncDecl(Id(a), [], Block([Return()]))])''', 611))


    def test_612(self):
        self.assertTrue(TestAST.test('''
    func a()
        

    ''', '''Program([FuncDecl(Id(a), [], None)])''', 612))


    def test_613(self):
        self.assertTrue(TestAST.test('''
    func a(number a,number b[2],number c[1])
    ''', '''Program([FuncDecl(Id(a), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), ArrayType([2.0], NumberType), None, None), VarDecl(Id(c), ArrayType([1.0], NumberType), None, None)], None)])''', 613))


    def test_614(self):
        self.assertTrue(TestAST.test('''
    func a(number a1)
        begin
            return a
        end
    ''', '''Program([FuncDecl(Id(a), [VarDecl(Id(a1), NumberType, None, None)], Block([Return(Id(a))]))])''', 614))


    def test_615(self):
        self.assertTrue(TestAST.test('''
    var x<- 2
    dynamic v 
    string a <- "'"...'"'"" 
    string b <- 203-3+4*(2*foo(4))
    
    
    ''', '''Program([VarDecl(Id(x), None, var, NumLit(2.0)), VarDecl(Id(v), None, dynamic, None), VarDecl(Id(a), StringType, None, StringLit(\'\"...\'\"\'\")), VarDecl(Id(b), StringType, None, BinaryOp(+, BinaryOp(-, NumLit(203.0), NumLit(3.0)), BinaryOp(*, NumLit(4.0), BinaryOp(*, NumLit(2.0), CallExpr(Id(foo), [NumLit(4.0)])))))])''', 615))


    def test_616(self):
        self.assertTrue(TestAST.test('''
    func a()
    func a()
    func a()
        func a()
        func a()
        func a()
        func a()
        

    ''', '''Program([FuncDecl(Id(a), [], None), FuncDecl(Id(a), [], None), FuncDecl(Id(a), [], None), FuncDecl(Id(a), [], None), FuncDecl(Id(a), [], None), FuncDecl(Id(a), [], None), FuncDecl(Id(a), [], None)])''', 616))


    def test_617(self):
        self.assertTrue(TestAST.test('''
    func a()
        return
    func b()
    func a()
        return
    func b()
    func a()
        return
    func b()
    func a()
        return
    func b()
    func c(number w)
    
    ''', '''Program([FuncDecl(Id(a), [], Return()), FuncDecl(Id(b), [], None), FuncDecl(Id(a), [], Return()), FuncDecl(Id(b), [], None), FuncDecl(Id(a), [], Return()), FuncDecl(Id(b), [], None), FuncDecl(Id(a), [], Return()), FuncDecl(Id(b), [], None), FuncDecl(Id(c), [VarDecl(Id(w), NumberType, None, None)], None)])''', 617))


    def test_618(self):
        self.assertTrue(TestAST.test('''
    func PvHu ()	return false

    func OzL (number Zf[8.511E-90])
        return

    ''', '''Program([FuncDecl(Id(PvHu), [], Return(BooleanLit(False))), FuncDecl(Id(OzL), [VarDecl(Id(Zf), ArrayType([8.511e-90], NumberType), None, None)], Return())])''', 618))


    def test_619(self):
        self.assertTrue(TestAST.test('''
    func eKUz (string TM)	return

    ## j*P=KgvSl)nd7
    func hIZe (bool hIkf[177.188E82,234.375])	begin
            bW <- kMUh
        end

    ''', '''Program([FuncDecl(Id(eKUz), [VarDecl(Id(TM), StringType, None, None)], Return()), FuncDecl(Id(hIZe), [VarDecl(Id(hIkf), ArrayType([1.77188e+84, 234.375], BoolType), None, None)], Block([AssignStmt(Id(bW), Id(kMUh))]))])''', 619))


    def test_620(self):
        self.assertTrue(TestAST.test('''
    func u12 (bool dPuS, bool Qoz5[24.913,8], bool ol[5,5,3.217])	return

    ## y<|P*]I@
    string jXjF <- "F$\\''"\\t\\b'"\\'"
    ## -G?P8p?311 >,]rk%`x
    
    ''', '''Program([FuncDecl(Id(u12), [VarDecl(Id(dPuS), BoolType, None, None), VarDecl(Id(Qoz5), ArrayType([24.913, 8.0], BoolType), None, None), VarDecl(Id(ol), ArrayType([5.0, 5.0, 3.217], BoolType), None, None)], Return()), VarDecl(Id(jXjF), StringType, None, StringLit(F$\\\'\'\"\\t\\b\'\"\\\'))])''', 620))


    def test_621(self):
        self.assertTrue(TestAST.test('''


    func a()
    var x <-2

    ''', '''Program([FuncDecl(Id(a), [], None), VarDecl(Id(x), None, var, NumLit(2.0))])''', 621))


    def test_622(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
        if (a) if (b) if (c) if (d) if (e) if (f) if (g) if (j) if (k) return
        end

    ''', '''Program([FuncDecl(Id(a), [], Block([If((Id(a), If((Id(b), If((Id(c), If((Id(d), If((Id(e), If((Id(f), If((Id(g), If((Id(j), If((Id(k), Return()), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))])''', 622))


    def test_623(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
        if (a) if (b) if (c) if (d) if (e) if (f) if (g) if (j) if (a) return
        end

    ''', '''Program([FuncDecl(Id(a), [], Block([If((Id(a), If((Id(b), If((Id(c), If((Id(d), If((Id(e), If((Id(f), If((Id(g), If((Id(j), If((Id(a), Return()), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))])''', 623))


    def test_624(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
        if (a) if (b) if (c) if (d) if (e) if (f) if (g) if (j) if (i) return
        elif (b) if (c) return
        end
    ''', '''Program([FuncDecl(Id(a), [], Block([If((Id(a), If((Id(b), If((Id(c), If((Id(d), If((Id(e), If((Id(f), If((Id(g), If((Id(j), If((Id(i), Return()), [(Id(b), If((Id(c), Return()), [], None))], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))])''', 624))


    def test_625(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
        if (a) if (b) if (c) if (d) if (e) if (f) if (g) if (j) if (i) return
        elif (b) return
        elif (c) return
        end

    ''', '''Program([FuncDecl(Id(a), [], Block([If((Id(a), If((Id(b), If((Id(c), If((Id(d), If((Id(e), If((Id(f), If((Id(g), If((Id(j), If((Id(i), Return()), [(Id(b), Return()), (Id(c), Return())], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)]))])''', 625))


    def test_626(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
        if (a) if (b) if (c) if (d) if (e) if (f) if (g) if (j) if (i) return
        elif (b) if (c) return
        var x <-  2
        end
        
    ''', '''Program([FuncDecl(Id(a), [], Block([If((Id(a), If((Id(b), If((Id(c), If((Id(d), If((Id(e), If((Id(f), If((Id(g), If((Id(j), If((Id(i), Return()), [(Id(b), If((Id(c), Return()), [], None))], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None)), [], None), VarDecl(Id(x), None, var, NumLit(2.0))]))])''', 626))


    def test_627(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
             return
        end

    ''', '''Program([FuncDecl(Id(a), [], Block([Return()]))])''', 627))


    def test_628(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
            if (a) call()
            else return
        end

    ''', '''Program([FuncDecl(Id(a), [], Block([If((Id(a), CallStmt(Id(call), [])), [], Return())]))])''', 628))


    def test_629(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
            if (d) if (b) d()
            else return
        end
        
    ''', '''Program([FuncDecl(Id(a), [], Block([If((Id(d), If((Id(b), CallStmt(Id(d), [])), [], Return())), [], None)]))])''', 629))


    def test_630(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
            if (d) if (b) d()
            else return
        end
    ''', '''Program([FuncDecl(Id(a), [], Block([If((Id(d), If((Id(b), CallStmt(Id(d), [])), [], Return())), [], None)]))])''', 630))


    def test_631(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
            if (d) if (b) d()
            else return
            else return
        end

    ''', '''Program([FuncDecl(Id(a), [], Block([If((Id(d), If((Id(b), CallStmt(Id(d), [])), [], Return())), [], Return())]))])''', 631))


    def test_632(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
            if (d) if (b) d()
            else return
            else return
        end

    ''', '''Program([FuncDecl(Id(a), [], Block([If((Id(d), If((Id(b), CallStmt(Id(d), [])), [], Return())), [], Return())]))])''', 632))


    def test_633(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
            if (d) if (b) if(g) d()
            else return
            else return
            elif (j) return 2
            
        end
        
    ''', '''Program([FuncDecl(Id(a), [], Block([If((Id(d), If((Id(b), If((Id(g), CallStmt(Id(d), [])), [], Return())), [], Return())), [(Id(j), Return(NumLit(2.0)))], None)]))])''', 633))


    def test_634(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
            if (d) if (b) d()
            else return
            else return
            if (tiep) ha()
            elif (dung) ha()
        end
        

    ''', '''Program([FuncDecl(Id(a), [], Block([If((Id(d), If((Id(b), CallStmt(Id(d), [])), [], Return())), [], Return()), If((Id(tiep), CallStmt(Id(ha), [])), [(Id(dung), CallStmt(Id(ha), []))], None)]))])''', 634))


    def test_635(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
        for doo until doo <= 2 by "hello\\\\'"" exe()
        end
        

    ''', '''Program([FuncDecl(Id(a), [], Block([For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), StringLit(hello\\\\\'\"), CallStmt(Id(exe), []))]))])''', 635))


    def test_636(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
        for doo until doo <= 2 by "hello\\''""
        
            exe()
        end
        

    ''', '''Program([FuncDecl(Id(a), [], Block([For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), StringLit(hello\\\'\'\"), CallStmt(Id(exe), []))]))])''', 636))


    def test_637(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
        for doo until (doo <= 2) by "hello\\\\"...l
        
            exe()
        end
        
        

    ''', '''Program([FuncDecl(Id(a), [], Block([For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello\\\\), Id(l)), CallStmt(Id(exe), []))]))])''', 637))


    def test_638(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
        for doo until (doo <= 2) by "hello"...l
            exe()
            exe()
            exe()
            exe()
            exe()
            exe()
                        exe()
            exe()
            exe()
            if  (a) 
            if (b) return
            elif (c) return
            else return
            else return
        end
        

    ''', '''Program([FuncDecl(Id(a), [], Block([For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello), Id(l)), CallStmt(Id(exe), [])), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), CallStmt(Id(exe), []), If((Id(a), If((Id(b), Return()), [(Id(c), Return())], Return())), [], Return())]))])''', 638))


    def test_639(self):
        self.assertTrue(TestAST.test('''
    func a() 
        begin
        for doo until (doo <= 2) by "hello\\\\"...l
        for doo until (doo <= 2) by "hello\\\\"...l
        for doo until (doo <= 2) by "hello\\\\"...l
        for doo until (doo <= 2) by "hello\\\\"...l
        for doo until (doo <= 2) by "hello\\\\"...l

        doNothing()
        
        end
        
    ''', '''Program([FuncDecl(Id(a), [], Block([For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello\\\\), Id(l)), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello\\\\), Id(l)), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello\\\\), Id(l)), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello\\\\), Id(l)), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello\\\\), Id(l)), CallStmt(Id(doNothing), []))))))]))])''', 639))


    def test_640(self):
        self.assertTrue(TestAST.test('''

    func a() 
        begin
        for doo until (doo <= 2) by "hello'""...l
for doo until (doo <= 2) by "hello'""...l
for doo until (doo <= 2) by "hello'""...l
        if (a) 
for doo until (doo <= 2) by "hello'""...l
        return
        elif (b) 
for doo until (doo <= 2) by "hello'""...l
        return
        else no()
        
        
        end
        

    
    ''', '''Program([FuncDecl(Id(a), [], Block([For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello\'\"), Id(l)), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello\'\"), Id(l)), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello\'\"), Id(l)), If((Id(a), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello\'\"), Id(l)), Return())), [(Id(b), For(Id(doo), BinaryOp(<=, Id(doo), NumLit(2.0)), BinaryOp(..., StringLit(hello\'\"), Id(l)), Return()))], CallStmt(Id(no), [])))))]))])''', 640))


    def test_641(self):
        self.assertTrue(TestAST.test('''
    func IYf ()	begin
            continue
        end
    func UY ()	return
    ''', '''Program([FuncDecl(Id(IYf), [], Block([Continue])), FuncDecl(Id(UY), [], Return())])''', 641))


    def test_642(self):
        self.assertTrue(TestAST.test('''
    var x <- 2

    ''', '''Program([VarDecl(Id(x), None, var, NumLit(2.0))])''', 642))


    def test_643(self):
        self.assertTrue(TestAST.test('''
    string x <- "2\\''"\\''"\\\\"..."'"2222\\\\"
    

    ''', '''Program([VarDecl(Id(x), StringType, None, BinaryOp(..., StringLit(2\\\'\'\"\\\'\'\"\\\\), StringLit(\'\"2222\\\\)))])''', 643))


    def test_644(self):
        self.assertTrue(TestAST.test('''
    func _1()
    func _2()
    func _3()
    func a()
        return
        
    ''', '''Program([FuncDecl(Id(_1), [], None), FuncDecl(Id(_2), [], None), FuncDecl(Id(_3), [], None), FuncDecl(Id(a), [], Return())])''', 644))


    def test_645(self):
        self.assertTrue(TestAST.test('''
    func _1() return 

    ''', '''Program([FuncDecl(Id(_1), [], Return())])''', 645))


    def test_646(self):
        self.assertTrue(TestAST.test('''
    string a  <- "		aaaa\\\\"
    string b <- a...b ==2

    ''', '''Program([VarDecl(Id(a), StringType, None, StringLit(		aaaa\\\\)), VarDecl(Id(b), StringType, None, BinaryOp(..., Id(a), BinaryOp(==, Id(b), NumLit(2.0))))])''', 646))

    def test_647(self):
        self.assertTrue(TestAST.test('''
    func __self__()
    begin
        string abcaa <- "43817807asda890982835"
        number a <- --0019212878.20011238273e-182531233
        number arr <- [[1], [1]]
    end
    
    ''', '''Program([FuncDecl(Id(__self__), [], Block([VarDecl(Id(abcaa), StringType, None, StringLit(43817807asda890982835)), VarDecl(Id(a), NumberType, None, UnaryOp(-, UnaryOp(-, NumLit(0.0)))), VarDecl(Id(arr), NumberType, None, ArrayLit(ArrayLit(NumLit(1.0)), ArrayLit(NumLit(1.0))))]))])''', 647))


    def test_648(self):
        self.assertTrue(TestAST.test('''
    func T7b ()	return
    ## a
    func f() return
    
    ''', '''Program([FuncDecl(Id(T7b), [], Return()), FuncDecl(Id(f), [], Return())])''', 648))


    def test_649(self):
        self.assertTrue(TestAST.test('''
    func __aaa__()
    begin
        number arr[0, 0, 0] <- [[1, 2, 3], ["a\\'" ... "b\\'", foo()["index\\\\"]], [(a and not c) = d]]
    end
    
    ''', '''Program([FuncDecl(Id(__aaa__), [], Block([VarDecl(Id(arr), ArrayType([0.0, 0.0, 0.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(BinaryOp(..., StringLit(a\\'), StringLit(b\\')), ArrayCell(CallExpr(Id(foo), []), [StringLit(index\\\\)])), ArrayLit(BinaryOp(=, BinaryOp(and, Id(a), UnaryOp(not, Id(c))), Id(d)))))]))])''', 649))


    def test_650(self):
        self.assertTrue(TestAST.test('''
    bool r_[791.790E92] <- 3.348E60 ## !
    bool aaaa[71.175e12,534.322260,2.30202,2] ## ~F`Rr8MhOd1
    func gwUz (number MJ)	begin
            ## I-ue3cajiH
        end

    func I1 (number t6sadiu, number lasdSM, bool gasdF)
        begin
            for VPmR until 4.181 by 26
                begin
                    ## 9T:
                end
        end

    var fZ1  <- 2 ## t~%mu8[IJ
    
    ''', '''Program([VarDecl(Id(r_), ArrayType([7.9179e+94], BoolType), None, NumLit(3.348e+60)), VarDecl(Id(aaaa), ArrayType([71175000000000.0, 534.32226, 2.30202, 2.0], BoolType), None, None), FuncDecl(Id(gwUz), [VarDecl(Id(MJ), NumberType, None, None)], Block([])), FuncDecl(Id(I1), [VarDecl(Id(t6sadiu), NumberType, None, None), VarDecl(Id(lasdSM), NumberType, None, None), VarDecl(Id(gasdF), BoolType, None, None)], Block([For(Id(VPmR), NumLit(4.181), NumLit(26.0), Block([]))])), VarDecl(Id(fZ1), None, var, NumLit(2.0))])''', 650))


    def test_651(self):
        self.assertTrue(TestAST.test('''
    number b6 <- ndok
    ## ;4tT hk~QD_Pd^5
    ''', '''Program([VarDecl(Id(b6), NumberType, None, Id(ndok))])''', 651))


    def test_652(self):
        self.assertTrue(TestAST.test('''
    string ceH3[386.880E37,30] <- ST ## nd
    func oF (bool qMDC[893,11e-26,41.997e-76], bool zho[911.283,63,9.349E49], string d0o)	return false
    func vJ (bool cr)
        return

    string zz[1e+59] <- true
    
    ''', '''Program([VarDecl(Id(ceH3), ArrayType([3.8688e+39, 30.0], StringType), None, Id(ST)), FuncDecl(Id(oF), [VarDecl(Id(qMDC), ArrayType([893.0, 1.1e-25, 4.1997e-75], BoolType), None, None), VarDecl(Id(zho), ArrayType([911.283, 63.0, 9.349e+49], BoolType), None, None), VarDecl(Id(d0o), StringType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(vJ), [VarDecl(Id(cr), BoolType, None, None)], Return()), VarDecl(Id(zz), ArrayType([1e+59], StringType), None, BooleanLit(True))])''', 652))


    def test_653(self):
        self.assertTrue(TestAST.test('''
    var Rwe <- "}\\'\\''"f\\\\" ## }8BPqn]D&J>_1$sGD
    dynamic Ram <-2222
    
    ''', '''Program([VarDecl(Id(Rwe), None, var, StringLit(}\\\'\\\'\'\"f\\\\)), VarDecl(Id(Ram), None, dynamic, NumLit(2222.0))])''', 653))


    def test_654(self):
        self.assertTrue(TestAST.test('''
    func lIPS (string OMrG[3,8.617E-25,82.558], string hn[62.657], string BOP[6])	return
    bool Rz[0.084e43,5.286,2e+59] ## epe"DfZIsb(.&b
    ## ?pty_li1lHNKy0-
    
    ''', '''Program([FuncDecl(Id(lIPS), [VarDecl(Id(OMrG), ArrayType([3.0, 8.617e-25, 82.558], StringType), None, None), VarDecl(Id(hn), ArrayType([62.657], StringType), None, None), VarDecl(Id(BOP), ArrayType([6.0], StringType), None, None)], Return()), VarDecl(Id(Rz), ArrayType([8.4e+41, 5.286, 2e+59], BoolType), None, None)])''', 654))


    def test_655(self):
        self.assertTrue(TestAST.test('''
    ## sVi0,]7Z?/rVg7N`
    bool ymW[8]
    func vq_Y (string dM[241E-12], number akM5[3e-209,4.404E+59])	return 363
    ## fG4DlM^_
    func sss (bool aa, number H3[34.172e+70,997.])	return 32
    
    ''', '''Program([VarDecl(Id(ymW), ArrayType([8.0], BoolType), None, None), FuncDecl(Id(vq_Y), [VarDecl(Id(dM), ArrayType([2.41e-10], StringType), None, None), VarDecl(Id(akM5), ArrayType([3e-209, 4.404e+59], NumberType), None, None)], Return(NumLit(363.0))), FuncDecl(Id(sss), [VarDecl(Id(aa), BoolType, None, None), VarDecl(Id(H3), ArrayType([3.4172e+71, 997.0], NumberType), None, None)], Return(NumLit(32.0)))])''', 655))


    def test_656(self):
        self.assertTrue(TestAST.test('''
    func asd ()	
    func asd (bool yk6d)
        return asd

    func FUb ()
        begin
            begin
                NVC <- "Z\\\\"
            end
        end

    ''', '''Program([FuncDecl(Id(asd), [], None), FuncDecl(Id(asd), [VarDecl(Id(yk6d), BoolType, None, None)], Return(Id(asd))), FuncDecl(Id(FUb), [], Block([Block([AssignStmt(Id(NVC), StringLit(Z\\\\))])]))])''', 656))


    def test_657(self):
        self.assertTrue(TestAST.test('''
    func aa (number b[7])
        return

    ## asd[tG)aa/x
    func PUBG ()	return Fy

    number Kb9 ## .M`X6mAM~O=fH_j~l
    
    ''', '''Program([FuncDecl(Id(aa), [VarDecl(Id(b), ArrayType([7.0], NumberType), None, None)], Return()), FuncDecl(Id(PUBG), [], Return(Id(Fy))), VarDecl(Id(Kb9), NumberType, None, None)])''', 657))


    def test_658(self):
        self.assertTrue(TestAST.test('''
    string sVT <- true
    func asd (number bbb)	begin
            ## u<-zs_v|UE
        end
    number hm8 <- "+\\\\" ## [/y}%?ekT3ae
    
    ''', '''Program([VarDecl(Id(sVT), StringType, None, BooleanLit(True)), FuncDecl(Id(asd), [VarDecl(Id(bbb), NumberType, None, None)], Block([])), VarDecl(Id(hm8), NumberType, None, StringLit(+\\\\))])''', 658))


    def test_659(self):
        self.assertTrue(TestAST.test('''
    ## /Df4E
    var x <- 3
    ''', '''Program([VarDecl(Id(x), None, var, NumLit(3.0))])''', 659))


    def test_660(self):
        self.assertTrue(TestAST.test('''
    func IP (number aTdZ[6,742])	return E4

    ''', '''Program([FuncDecl(Id(IP), [VarDecl(Id(aTdZ), ArrayType([6.0, 742.0], NumberType), None, None)], Return(Id(E4)))])''', 660))


    def test_661(self):
        self.assertTrue(TestAST.test('''
    func Xwv (bool Zc8s[9.623])
        begin
            break
        end

    ''', '''Program([FuncDecl(Id(Xwv), [VarDecl(Id(Zc8s), ArrayType([9.623], BoolType), None, None)], Block([Break]))])''', 661))


    def test_662(self):
        self.assertTrue(TestAST.test('''
    func sofJ (number fu0)	return G2
    func q9 (number pTEB, number Gqbl, number HBz[51e-54,42.038E25])	return Pb9p
    bool YyHw[63,0.351e+80] <- L82
    
    ''', '''Program([FuncDecl(Id(sofJ), [VarDecl(Id(fu0), NumberType, None, None)], Return(Id(G2))), FuncDecl(Id(q9), [VarDecl(Id(pTEB), NumberType, None, None), VarDecl(Id(Gqbl), NumberType, None, None), VarDecl(Id(HBz), ArrayType([5.1e-53, 4.2038e+26], NumberType), None, None)], Return(Id(Pb9p))), VarDecl(Id(YyHw), ArrayType([63.0, 3.51e+79], BoolType), None, Id(L82))])''', 662))


    def test_663(self):
        self.assertTrue(TestAST.test('''
    bool vm5b[297.574,2.657e+88,20.053] <- false ## _]QeQWgTLEo=WT>Iml)
    bool a[258,571.469e+47]
    var RCs <- a or b
    ## sJb%#-Q`+=M
    func MZp (bool ICjQ[1e-39,169.761e58])	return
    

    ''', '''Program([VarDecl(Id(vm5b), ArrayType([297.574, 2.657e+88, 20.053], BoolType), None, BooleanLit(False)), VarDecl(Id(a), ArrayType([258.0, 5.71469e+49], BoolType), None, None), VarDecl(Id(RCs), None, var, BinaryOp(or, Id(a), Id(b))), FuncDecl(Id(MZp), [VarDecl(Id(ICjQ), ArrayType([1e-39, 1.69761e+60], BoolType), None, None)], Return())])''', 663))


    def test_664(self):
        self.assertTrue(TestAST.test('''
    func g33K ()	return true
    ## d,e[rpPH`&dTCa:K6v
    
    ''', '''Program([FuncDecl(Id(g33K), [], Return(BooleanLit(True)))])''', 664))


    def test_665(self):
        self.assertTrue(TestAST.test('''
    func vI (bool aG5T, number KF[913.661,168.354])
        
    ''', '''Program([FuncDecl(Id(vI), [VarDecl(Id(aG5T), BoolType, None, None), VarDecl(Id(KF), ArrayType([913.661, 168.354], NumberType), None, None)], None)])''', 665))


    def test_666(self):
        self.assertTrue(TestAST.test('''
    ## +lw$
    ## z?+pnDE
    var eaku <- 4 ## aaaa
    
    ''', '''Program([VarDecl(Id(eaku), None, var, NumLit(4.0))])''', 666))


    def test_667(self):
        self.assertTrue(TestAST.test('''
    func aasd (string vvv[492.443,5.953], string Zy, string aaa[25.651,290E+69,824])	return
    bool eee[62.758,945.877,85E+48] <- true
    string kC
    ## 5`@dL@Yx{OehzAiSv
    string Xc[238e30,23] <- 85E-97 ## ]xGSJB
    ''', '''Program([FuncDecl(Id(aasd), [VarDecl(Id(vvv), ArrayType([492.443, 5.953], StringType), None, None), VarDecl(Id(Zy), StringType, None, None), VarDecl(Id(aaa), ArrayType([25.651, 2.9e+71, 824.0], StringType), None, None)], Return()), VarDecl(Id(eee), ArrayType([62.758, 945.877, 8.5e+49], BoolType), None, BooleanLit(True)), VarDecl(Id(kC), StringType, None, None), VarDecl(Id(Xc), ArrayType([2.38e+32, 23.0], StringType), None, NumLit(8.5e-96))])''', 667))


    def test_668(self):
        self.assertTrue(TestAST.test('''
    func u1 (number qjj2[8.195,494.197e+82])	return "\\'\\''"\\''"\\''"\\\\"
    

    ''', '''Program([FuncDecl(Id(u1), [VarDecl(Id(qjj2), ArrayType([8.195, 4.94197e+84], NumberType), None, None)], Return(StringLit(\\\'\\\'\'\"\\\'\'\"\\\'\'\"\\\\)))])''', 668))


    def test_669(self):
        self.assertTrue(TestAST.test('''
    ## }61xD2$*67-A
    var R6y <- true
    string pzW[2.526E21,83] <- "c\\\\"
    ## J/*N5C
    
    ''', '''Program([VarDecl(Id(R6y), None, var, BooleanLit(True)), VarDecl(Id(pzW), ArrayType([2.526e+21, 83.0], StringType), None, StringLit(c\\\\))])''', 669))


    def test_670(self):
        self.assertTrue(TestAST.test('''
    func c18 (string Hhu, bool nR4)	return

    func hpUs (bool D4K4)	

    ## uRtsM
    ''', '''Program([FuncDecl(Id(c18), [VarDecl(Id(Hhu), StringType, None, None), VarDecl(Id(nR4), BoolType, None, None)], Return()), FuncDecl(Id(hpUs), [VarDecl(Id(D4K4), BoolType, None, None)], None)])''', 670))


    def test_671(self):
        self.assertTrue(TestAST.test('''
    ## BK
    ## )p"nwSC- ]h9
    func hpUs (bool D4K4)	
    ''', '''Program([FuncDecl(Id(hpUs), [VarDecl(Id(D4K4), BoolType, None, None)], None)])''', 671))


    def test_672(self):
        self.assertTrue(TestAST.test('''
    ## 8M8*FHEfy)r
    dynamic pR ## YQg>oT2
    func CK (bool JIMG)	begin
            ## j6^xYY/%xFKJ?
        end

    ## qzVWb
    func Ykon (bool aVn[782.326e+50], bool W8mB[3], number ua[76.173E12,9.279e-04])	return true
    
    ''', '''Program([VarDecl(Id(pR), None, dynamic, None), FuncDecl(Id(CK), [VarDecl(Id(JIMG), BoolType, None, None)], Block([])), FuncDecl(Id(Ykon), [VarDecl(Id(aVn), ArrayType([7.82326e+52], BoolType), None, None), VarDecl(Id(W8mB), ArrayType([3.0], BoolType), None, None), VarDecl(Id(ua), ArrayType([76173000000000.0, 0.0009279], NumberType), None, None)], Return(BooleanLit(True)))])''', 672))


    def test_673(self):
        self.assertTrue(TestAST.test('''
    func yt (string hgL[70.785E+47,32,1.516e-24], string ZF[38,2.233E+86], string r9o1[27.035,8])
        return "\\''"\\''"\\'\\''"\\'\\''"\\b'\\''"\\\\"

    ## &xizZXWQT~
    
    ''', '''Program([FuncDecl(Id(yt), [VarDecl(Id(hgL), ArrayType([7.0785e+48, 32.0, 1.516e-24], StringType), None, None), VarDecl(Id(ZF), ArrayType([38.0, 2.233e+86], StringType), None, None), VarDecl(Id(r9o1), ArrayType([27.035, 8.0], StringType), None, None)], Return(StringLit(\\\'\'\"\\\'\'\"\\\'\\\'\'\"\\\'\\\'\'\"\\b\'\\\'\'\"\\\\)))])''', 673))


    def test_674(self):
        self.assertTrue(TestAST.test('''
    ## (123123
    ## 434343
    bool aa[53.994,212312.141,2e+61235] ##  123123123
    number aaa <- false
    ''', '''Program([VarDecl(Id(aa), ArrayType([53.994, 212312.141, inf], BoolType), None, None), VarDecl(Id(aaa), NumberType, None, BooleanLit(False))])''', 674))


    def test_675(self):
        self.assertTrue(TestAST.test('''
    func aaa (bool a[2.32267], bool wwe)
        return
    func bbb ()
        return

    func ccc ()	return
    func ddd (bool Q8)
        begin
            break
        end
        
    ''', '''Program([FuncDecl(Id(aaa), [VarDecl(Id(a), ArrayType([2.32267], BoolType), None, None), VarDecl(Id(wwe), BoolType, None, None)], Return()), FuncDecl(Id(bbb), [], Return()), FuncDecl(Id(ccc), [], Return()), FuncDecl(Id(ddd), [VarDecl(Id(Q8), BoolType, None, None)], Block([Break]))])''', 675))


    def test_676(self):
        self.assertTrue(TestAST.test('''
    ## W-.:@V(
    func eee (string r[8E23,459.221324], string vUu[41233e+03,99.094E12372], string bb)	return
    func www ()	begin
            ## 123
        end

    func qqq (string www)
        begin
            ## aaamm
        end
    func b8 ()	return
    
    ''', '''Program([FuncDecl(Id(eee), [VarDecl(Id(r), ArrayType([8e+23, 459.221324], StringType), None, None), VarDecl(Id(vUu), ArrayType([41233000.0, inf], StringType), None, None), VarDecl(Id(bb), StringType, None, None)], Return()), FuncDecl(Id(www), [], Block([])), FuncDecl(Id(qqq), [VarDecl(Id(www), StringType, None, None)], Block([])), FuncDecl(Id(b8), [], Return())])''', 676))


    def test_677(self):
        self.assertTrue(TestAST.test('''
    bool aaa[9e8,55124,6.54121]
    func ll ()
        

    func aaa ()	return
    func cc (bool gb)	begin
            ## aaaaa
        end

    ''', '''Program([VarDecl(Id(aaa), ArrayType([900000000.0, 55124.0, 6.54121], BoolType), None, None), FuncDecl(Id(ll), [], None), FuncDecl(Id(aaa), [], Return()), FuncDecl(Id(cc), [VarDecl(Id(gb), BoolType, None, None)], Block([]))])''', 677))


    def test_678(self):
        self.assertTrue(TestAST.test('''
    ## asddddw
    func asss (number aq)
        return 22
    number aaa[5280,88124e+612,33325] <- "D'"" ## )
    ''', '''Program([FuncDecl(Id(asss), [VarDecl(Id(aq), NumberType, None, None)], Return(NumLit(22.0))), VarDecl(Id(aaa), ArrayType([5280.0, inf, 33325.0], NumberType), None, StringLit(D\'\"))])''', 678))


    def test_679(self):
        self.assertTrue(TestAST.test('''
    string aaaa[904.812312,736.321343e+17]
    ## zxc
    number zzz
    ## (12333
    ''', '''Program([VarDecl(Id(aaaa), ArrayType([904.812312, 7.36321343e+19], StringType), None, None), VarDecl(Id(zzz), NumberType, None, None)])''', 679))


    def test_680(self):
        self.assertTrue(TestAST.test('''
    func bbb (string asd[470.689,722], string Y8[4.12176,486.96125], bool Dccc)	

    ## "WM5Pf
    string aaa[53336.214,222] <- "\\''"\\''"8\\''"\\''"\\\\" ## SW
    
    ##asd
    ''', '''Program([FuncDecl(Id(bbb), [VarDecl(Id(asd), ArrayType([470.689, 722.0], StringType), None, None), VarDecl(Id(Y8), ArrayType([4.12176, 486.96125], StringType), None, None), VarDecl(Id(Dccc), BoolType, None, None)], None), VarDecl(Id(aaa), ArrayType([53336.214, 222.0], StringType), None, StringLit(\\\'\'\"\\\'\'\"8\\\'\'\"\\\'\'\"\\\\))])''', 680))


    def test_681(self):
        self.assertTrue(TestAST.test('''
    ## M8q
    ## h*{.> 
        func qq (number bbb, number qqq, string a)	
        begin
        if(a) return
        elif(b) if (c) if (d) call() 
        else return
        else return
        elif (c) call()
        end
        
    ''', '''Program([FuncDecl(Id(qq), [VarDecl(Id(bbb), NumberType, None, None), VarDecl(Id(qqq), NumberType, None, None), VarDecl(Id(a), StringType, None, None)], Block([If((Id(a), Return()), [(Id(b), If((Id(c), If((Id(d), CallStmt(Id(call), [])), [], Return())), [], Return())), (Id(c), CallStmt(Id(call), []))], None)]))])''', 681))


    def test_682(self):
        self.assertTrue(TestAST.test('''
    func qq (number bbb, number qqq, string a)	return true

    ''', '''Program([FuncDecl(Id(qq), [VarDecl(Id(bbb), NumberType, None, None), VarDecl(Id(qqq), NumberType, None, None), VarDecl(Id(a), StringType, None, None)], Return(BooleanLit(True)))])''', 682))


    def test_683(self):
        self.assertTrue(TestAST.test('''
    bool eeqr[347,23.031]
    bool aasd
    ''', '''Program([VarDecl(Id(eeqr), ArrayType([347.0, 23.031], BoolType), None, None), VarDecl(Id(aasd), BoolType, None, None)])''', 683))


    def test_684(self):
        self.assertTrue(TestAST.test('''
  func qwe (number rrrt)
        return
    bool zz[344.218] <- pZT ## eeeee"C}mm
    func K8S (bool CEK, number qI9[895.140E79,467.403E34])	return w3gn
    
    ''', '''Program([FuncDecl(Id(qwe), [VarDecl(Id(rrrt), NumberType, None, None)], Return()), VarDecl(Id(zz), ArrayType([344.218], BoolType), None, Id(pZT)), FuncDecl(Id(K8S), [VarDecl(Id(CEK), BoolType, None, None), VarDecl(Id(qI9), ArrayType([8.9514e+81, 4.67403e+36], NumberType), None, None)], Return(Id(w3gn)))])''', 684))


    def test_685(self):
        self.assertTrue(TestAST.test('''
    ## zxczxczxc
    func a (bool a, number Un[6.643,545])
        return false

    string wwww ##zxcck
    ## vzxc
    string fff[238e-2200,43.5325E-123] ## svwqw
    
    ''', '''Program([FuncDecl(Id(a), [VarDecl(Id(a), BoolType, None, None), VarDecl(Id(Un), ArrayType([6.643, 545.0], NumberType), None, None)], Return(BooleanLit(False))), VarDecl(Id(wwww), StringType, None, None), VarDecl(Id(fff), ArrayType([0.0, 4.35325e-122], StringType), None, None)])''', 685))


    def test_686(self):
        self.assertTrue(TestAST.test('''
    func zzz (bool zz[936], string qqq)	return
    ## vsasd
    ## comment
    ''', '''Program([FuncDecl(Id(zzz), [VarDecl(Id(zz), ArrayType([936.0], BoolType), None, None), VarDecl(Id(qqq), StringType, None, None)], Return())])''', 686))


    def test_687(self):
        self.assertTrue(TestAST.test('''
    number aa[0.050E-10,0] <- vv
    ## asd
    bool aaa[2,63]
    
    ''', '''Program([VarDecl(Id(aa), ArrayType([5e-12, 0.0], NumberType), None, Id(vv)), VarDecl(Id(aaa), ArrayType([2.0, 63.0], BoolType), None, None)])''', 687))


    def test_688(self):
        self.assertTrue(TestAST.test('''
    var aaa <- "\\'\\''"\\\\" ## lV
    func aa ()
        begin
            bbb("b[\\'\\''"\\''\\''"\\'\\''"\\\\", false)
        end
    func cv (number oisps)	return

    var Tcgc <- "\\'\\''"J}#\\\\" ## 7_49NPx/gi
    
    ''', '''Program([VarDecl(Id(aaa), None, var, StringLit(\\\'\\\'\'\"\\\\)), FuncDecl(Id(aa), [], Block([CallStmt(Id(bbb), [StringLit(b[\\\'\\\'\'\"\\\'\'\\\'\'\"\\\'\\\'\'\"\\\\), BooleanLit(False)])])), FuncDecl(Id(cv), [VarDecl(Id(oisps), NumberType, None, None)], Return()), VarDecl(Id(Tcgc), None, var, StringLit(\\\'\\\'\'\"J}#\\\\))])''', 688))


    def test_689(self):
        self.assertTrue(TestAST.test('''
    func epic ()	begin
            qwww()
        end

    string FWF[474E02] ## s:y,Dc
    ''', '''Program([FuncDecl(Id(epic), [], Block([CallStmt(Id(qwww), [])])), VarDecl(Id(FWF), ArrayType([47400.0], StringType), None, None)])''', 689))


    def test_690(self):
        self.assertTrue(TestAST.test('''
    func ja_U (bool a_, bool _av, number avcd[2]) 
        return trueee
    ## n`6xclP.!
    dynamic hXRo ## #Hne
    ## ,)
    
    ''', '''Program([FuncDecl(Id(ja_U), [VarDecl(Id(a_), BoolType, None, None), VarDecl(Id(_av), BoolType, None, None), VarDecl(Id(avcd), ArrayType([2.0], NumberType), None, None)], Return(Id(trueee))), VarDecl(Id(hXRo), None, dynamic, None)])''', 690))


    def test_691(self):
        self.assertTrue(TestAST.test('''
    ##  abcdf
    ## i12345
    var hello <- "Hello"..."hi"
    func a()

    ''', '''Program([VarDecl(Id(hello), None, var, BinaryOp(..., StringLit(Hello), StringLit(hi))), FuncDecl(Id(a), [], None)])''', 691))


    def test_692(self):
        self.assertTrue(TestAST.test('''
    ## Z>K7-(I}
    func vvv (string PeH[105.862E-49,6E-82], bool fn[648.235])	return 

    dynamic QSk ## BM>M
    
    ''', '''Program([FuncDecl(Id(vvv), [VarDecl(Id(PeH), ArrayType([1.05862e-47, 6e-82], StringType), None, None), VarDecl(Id(fn), ArrayType([648.235], BoolType), None, None)], Return()), VarDecl(Id(QSk), None, dynamic, None)])''', 692))


    def test_693(self):
        self.assertTrue(TestAST.test('''
    func abc (bool aaa, string ccc)
        return 1.326E+02
    bool oQ4e[30.720E84,15e+06,3.626e-88]
    string u6CZ[269,54,96683] <- "FP"
    
    ''', '''Program([FuncDecl(Id(abc), [VarDecl(Id(aaa), BoolType, None, None), VarDecl(Id(ccc), StringType, None, None)], Return(NumLit(132.6))), VarDecl(Id(oQ4e), ArrayType([3.072e+85, 15000000.0, 3.626e-88], BoolType), None, None), VarDecl(Id(u6CZ), ArrayType([269.0, 54.0, 96683.0], StringType), None, StringLit(FP))])''', 693))


    def test_694(self):
        self.assertTrue(TestAST.test('''
    number A_f
    string XgMv[42.783e76,3.418] <- ej ## ZC
    func pgWK (number OI, number GX[48.654E-77,499e+70,689.892e+08], number JmG)	begin
            continue
        end

    func xp (number y5[8.856,71,3.802], string rIZ, bool U9tX)	
    string xMs[9] <- false
    ''', '''Program([VarDecl(Id(A_f), NumberType, None, None), VarDecl(Id(XgMv), ArrayType([4.2783e+77, 3.418], StringType), None, Id(ej)), FuncDecl(Id(pgWK), [VarDecl(Id(OI), NumberType, None, None), VarDecl(Id(GX), ArrayType([4.8654e-76, 4.99e+72, 68989200000.0], NumberType), None, None), VarDecl(Id(JmG), NumberType, None, None)], Block([Continue])), FuncDecl(Id(xp), [VarDecl(Id(y5), ArrayType([8.856, 71.0, 3.802], NumberType), None, None), VarDecl(Id(rIZ), StringType, None, None), VarDecl(Id(U9tX), BoolType, None, None)], None), VarDecl(Id(xMs), ArrayType([9.0], StringType), None, BooleanLit(False))])''', 694))


    def test_695(self):
        self.assertTrue(TestAST.test('''
    func aaa ()	
        begin
            pW("D,\\'\\\\", 359, false)
        end
    number bbb[339,4,0]
    number ccc ## ddd
    string YBj[85.902E+67,1E-45,52.542]
    
    ''', '''Program([FuncDecl(Id(aaa), [], Block([CallStmt(Id(pW), [StringLit(D,\\\'\\\\), NumLit(359.0), BooleanLit(False)])])), VarDecl(Id(bbb), ArrayType([339.0, 4.0, 0.0], NumberType), None, None), VarDecl(Id(ccc), NumberType, None, None), VarDecl(Id(YBj), ArrayType([8.5902e+68, 1e-45, 52.542], StringType), None, None)])''', 695))


    def test_696(self):
        self.assertTrue(TestAST.test('''
    func w1 (number CItc)
        begin
            continue
        end

    func UO (bool isGH[8,985], bool Le)	return
    
    ''', '''Program([FuncDecl(Id(w1), [VarDecl(Id(CItc), NumberType, None, None)], Block([Continue])), FuncDecl(Id(UO), [VarDecl(Id(isGH), ArrayType([8.0, 985.0], BoolType), None, None), VarDecl(Id(Le), BoolType, None, None)], Return())])''', 696))


    def test_697(self):
        self.assertTrue(TestAST.test('''
    ## JtA{OX
    func hN (bool SB7o, number IT)	

    func d2N (string MIXf)
    
        
    ''', '''Program([FuncDecl(Id(hN), [VarDecl(Id(SB7o), BoolType, None, None), VarDecl(Id(IT), NumberType, None, None)], None), FuncDecl(Id(d2N), [VarDecl(Id(MIXf), StringType, None, None)], None)])''', 697))


    def test_698(self):
        self.assertTrue(TestAST.test('''
    number M6 <- Ne
    ## 1=
    func aE (number E_[43,93], bool Fv_, number sA[7])
        begin
            begin
                continue
            end
        end
        

    ''', '''Program([VarDecl(Id(M6), NumberType, None, Id(Ne)), FuncDecl(Id(aE), [VarDecl(Id(E_), ArrayType([43.0, 93.0], NumberType), None, None), VarDecl(Id(Fv_), BoolType, None, None), VarDecl(Id(sA), ArrayType([7.0], NumberType), None, None)], Block([Block([Continue])]))])''', 698))


    def test_699(self):
        self.assertTrue(TestAST.test('''
    number rW[82E+82] ##  |
    string xl[96e+1233,5E+60,5.205E+85]
    string uflK[465e+08] <- true
    func c5 ()

    bool asc[1298,40.12367,4.338] ## MV>%eWlh:6+
    clear
    
    ''', '''Program([VarDecl(Id(rW), ArrayType([8.2e+83], NumberType), None, None), VarDecl(Id(xl), ArrayType([inf, 5e+60, 5.205e+85], StringType), None, None), VarDecl(Id(uflK), ArrayType([46500000000.0], StringType), None, BooleanLit(True)), FuncDecl(Id(c5), [], None), VarDecl(Id(asc), ArrayType([1298.0, 40.12367, 4.338], BoolType), None, None)])''', 699))


    def test_700(self):
        self.assertTrue(TestAST.test('''
    string ttt[1,155E+91]
    func lVL (bool bbb[13.178E+06,0.12345], string bbb[4,3,69])	return
    
    ''', '''Program([VarDecl(Id(ttt), ArrayType([1.0, 1.55e+93], StringType), None, None), FuncDecl(Id(lVL), [VarDecl(Id(bbb), ArrayType([13178000.0, 0.12345], BoolType), None, None), VarDecl(Id(bbb), ArrayType([4.0, 3.0, 69.0], StringType), None, None)], Return())])''', 700))


    def test_701(self):
        self.assertTrue(TestAST.test('''
    var x <- 1+2+3*4-5
    func main()
    begin
    if (1) return 1
    elif (2) 
        if (3) return 2
        elif (4) return 3
        elif (5) return 4
        elif (a) 
            if (c) return 2
            elif(5) call()
            else return
        elif (6) return 5
        elif (7) return 8
        else return 6
    else return
    end
    ''', '''Program([VarDecl(Id(x), None, var, BinaryOp(-, BinaryOp(+, BinaryOp(+, NumLit(1.0), NumLit(2.0)), BinaryOp(*, NumLit(3.0), NumLit(4.0))), NumLit(5.0))), FuncDecl(Id(main), [], Block([If((NumLit(1.0), Return(NumLit(1.0))), [(NumLit(2.0), If((NumLit(3.0), Return(NumLit(2.0))), [(NumLit(4.0), Return(NumLit(3.0))), (NumLit(5.0), Return(NumLit(4.0))), (Id(a), If((Id(c), Return(NumLit(2.0))), [(NumLit(5.0), CallStmt(Id(call), []))], Return())), (NumLit(6.0), Return(NumLit(5.0))), (NumLit(7.0), Return(NumLit(8.0)))], Return(NumLit(6.0))))], Return())]))])''', 701))

