import unittest
from TestUtils import TestLexer



class LexerSuite(unittest.TestCase):
    def test0(self):
        input = """true abc=== ... """
        expect = """true,abc,==,=,...,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 100))


    def test1(self):
        input = """...     ==         +-*/%= <= > >= ... """
        expect = """...,==,+,-,*,/,%,=,<=,>,>=,...,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 101))


    def test2(self):
        input = """bool  return string      var dynamic func for until by break continue if else"""
        expect = """bool,return,string,var,dynamic,func,for,until,by,break,continue,if,else,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 102))


    def test3(self):
        input = """&"""
        expect = """Error Token &"""
        self.assertTrue(TestLexer.test(input, expect, 103))


    def test4(self):
        input = """#"""
        expect = """Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 104))


    def test5(self):
        input = """[(,,)]"""
        expect = """[,(,,,,,),],<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 105))


    def test6(self):
        input = """A _ a az AZ a_ a1 _1 A1"""
        expect = """A,_,a,az,AZ,a_,a1,_1,A1,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 106))


    def test7(self):
        input = """87128.94E + 215.14E16"""
        expect = """87128.94,E,+,215.14E16,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 107))


    def test8(self):
        input = """87128.94E+215.14E16"""
        expect = """87128.94E+215,Error Token ."""
        self.assertTrue(TestLexer.test(input, expect, 108))


    def test9(self):
        input = "0 -4 999 003 089. 89. 89.4 89.4e3 89.4e-15 89.e3 0.e-17 89e+3 72e-3 0e+2 0e-2"
        expect = "0,-,4,999,003,089.,89.,89.4,89.4e3,89.4e-15,89.e3,0.e-17,89e+3,72e-3,0e+2,0e-2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 109))


    def test10(self):
        input = ".34e-3"
        expect = "Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 110))


    def test11(self):
        input = "48.7h-4"
        expect = "48.7,h,-,4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 111))


    def test12(self):
        input = """----10. - ----0.25""" 
        expect = "-,-,-,-,10.,-,-,-,-,-,0.25,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 112))


    def test13(self):
        input = """ "" """
        expect = ",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 113))


    def test14(self):
        input = """ "'  PPL \\b \\f \\r \\n \\t \\\\ PPL  " """
        expect = """'  PPL \\b \\f \\r \\n \\t \\\\ PPL  ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 114))


    def test15(self):
        input = """ "'"S1mple '" Niko '' '"" """
        expect = "'\"S1mple '\" Niko '' '\",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 115))


    def test16(self):
        input = """ "PPL \n" """
        expect = "Unclosed String: PPL "
        self.assertTrue(TestLexer.test(input, expect, 116))


    def test17(self):
        input = """ "CS - PPL \n" """
        expect = "Unclosed String: CS - PPL "
        self.assertTrue(TestLexer.test(input, expect, 117))


    def test18(self):
        input = """ "CS-PPL !'"!'"!'"!'"! '' """
        expect = """Unclosed String: CS-PPL !'"!'"!'"!'"! '' """
        self.assertTrue(TestLexer.test(input, expect, 118))


    def test19(self):
        input = """ "CS \\n \n """
        expect = "Unclosed String: CS \\n "
        self.assertTrue(TestLexer.test(input, expect, 119))
        

    def test20(self):
        input = """ "CS ' \\n \\b """
        expect = "Unclosed String: CS ' \\n \\b "
        self.assertTrue(TestLexer.test(input, expect, 120))


    def test21(self):
        input = """123.45u6"""
        expect = """123.45,u6,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 121))


    def test22(self):
        input = """true false false true"""
        expect = """true,false,false,true,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 122))


    def test23(self):
        input = """ "PPL ' \\2  """
        expect = "Illegal Escape In String: PPL ' \\2"
        self.assertTrue(TestLexer.test(input, expect, 123))


    def test24(self):
        input = """ "PPL \\n \n """
        expect = """Unclosed String: PPL \\n """
        self.assertTrue(TestLexer.test(input, expect, 124))


    def test25(self):
        input = """ print(a, 123, "PPL'''"'''PPL") """
        expect = """print,(,a,,,123,,,PPL'''"'''PPL,),<EOF>"""   
        self.assertTrue(TestLexer.test(input, expect, 125))


    def test26(self):
        input = """ func foo(a[1,2,3,[1 + 2],1.2e+3]) """
        expect = "func,foo,(,a,[,1,,,2,,,3,,,[,1,+,2,],,,1.2e+3,],),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 126))


    def test27(self):
        input = """ var i <- 12.3e-4 """
        expect = "var,i,<-,12.3e-4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 127))


    def test28(self):
        input = """ "Go ' '" \\" """
        expect = "Illegal Escape In String: Go ' '\" \\\""
        self.assertTrue(TestLexer.test(input, expect, 128))


    def test29(self):
        input = """ "Go \\' ""1 """
        expect = "Go \\' ,Unclosed String: 1 "
        self.assertTrue(TestLexer.test(input, expect, 129))


    def test30(self):
        input = """\t\f\b\r## CS PPL"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 130))


    def test31(self):
        input = """###"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 131))


    def test32(self):
        input = """b##1"""
        expect = """b,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 132))


    def test33(self):
        input = """c#"""
        expect = """c,Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 133))


    def test34(self):
        input = """a\n##1\nb"""
        expect = """a,\n,\n,b,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 134))


    def test35(self):
        input = """a\n\n\n#"""
        expect = """a,\n,\n,\n,Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 135))


    def test36(self):
        input = """a
                    ## comment
                """
        expect = """a,
,
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 136))


    def test37(self):
        input = """ppl_nhp ppl_tnbd#"""
        expect = """ppl_nhp,ppl_tnbd,Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 137))


    def test38(self):
        input = """bv\n##1234\nb"""
        expect = """bv,\n,\n,b,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 138))


    def test39(self):
        input = """PpL\n\n#"""
        expect = """PpL,\n,\n,Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 139))


    def test40(self):
        input = """."""
        expect = """Error Token ."""
        self.assertTrue(TestLexer.test(input, expect, 140))


    def test41(self):
        input = """;"""
        expect = """Error Token ;"""
        self.assertTrue(TestLexer.test(input, expect, 141))


    def test42(self):
        input = """{"""
        expect = """Error Token {"""
        self.assertTrue(TestLexer.test(input, expect, 142))


    def test43(self):
        input = """+1-2"""
        expect = """+,1,-,2,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 143))


    def test44(self):
        input = """ "Start \t \n" """
        expect = """Unclosed String: Start 	 """
        self.assertTrue(TestLexer.test(input, expect, 144))


    def test45(self):
        input = """ "Start \\" """
        expect = "Illegal Escape In String: Start \\\""
        self.assertTrue(TestLexer.test(input, expect, 145))


    def test46(self):
        input = """ "Start \\\n """
        expect = """Illegal Escape In String: Start \\\n"""
        self.assertTrue(TestLexer.test(input, expect, 146))


    def test47(self):
        input = """ "Start '\\ """
        expect = """Illegal Escape In String: Start '\\ """
        self.assertTrue(TestLexer.test(input, expect, 147))


    def test48(self):
        input = """ "Start \'" " """
        expect = """Start '\" ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 148))


    def test49(self):
        input = """ "Start \\\'" " """
        expect = """Start \\',Unclosed String:  """
        self.assertTrue(TestLexer.test(input, expect, 149))


    def test50(self):
        input = """ "Start 
                                       " """
        expect = """Unclosed String: Start """
        self.assertTrue(TestLexer.test(input, expect, 150))


    def test51(self):
        self.assertTrue(TestLexer.test(
""" ##PPL Go
##PPL Go\n
##PPL Go """,
"""
,
,
,<EOF>""", 151))
        # self.assertTrue(TestLexer.test(input, expect, 151))


    def test52(self):
        input = """ ##PPL Go "123" ## 12 \n"""
        expect = """
,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 152))


    def test53(self):
        input = """ "\\a" """
        expect = """Illegal Escape In String: \\a"""
        self.assertTrue(TestLexer.test(input, expect, 153))


    def test54(self):
        input = """ "\\:" """
        expect = """Illegal Escape In String: \\:"""
        self.assertTrue(TestLexer.test(input, expect, 154))


    def test55(self):
        input = """ "\\\\1 \\z" """
        expect = """Illegal Escape In String: \\\\1 \z"""
        self.assertTrue(TestLexer.test(input, expect, 155))


    def test56(self):
        input = """ "'y \\y" """
        expect = """Illegal Escape In String: 'y \\y"""
        self.assertTrue(TestLexer.test(input, expect, 156))


    def test57(self):
        input = """ "'PPL \f \t \\a" """
        expect = """Illegal Escape In String: 'PPL \f \t \\a"""
        self.assertTrue(TestLexer.test(input, expect, 157))


    def test58(self):
        input = """1.1/3"""
        expect = """1.1,/,3,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 158))


    def test59(self):
        input = """ "'"'"'" """
        expect = """Unclosed String: '"'"'" """
        self.assertTrue(TestLexer.test(input, expect, 159))


    def test_60(self):
            self.assertTrue(TestLexer.test(''' "7'"
    '"9'" ''', '''Unclosed String: 7'"''', 160))

    def test61(self):
        input = """= != <"""
        expect = """=,!=,<,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 161))

    
    def test62(self):
        input = """+"""
        expect = """+,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 162))

    
    def test63(self):
        input = """-"""
        expect = """-,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 163))

    
    def test64(self):
        input = """*"""
        expect = """*,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 164))
    
    
    def test65(self):
        input = """/"""
        expect = """/,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 165))
        

    def test66(self):
        input = "for i until i < 100 by 1 \n a <- 1"
        expect = "for,i,until,i,<,100,by,1,\n,a,<-,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect,166))
    
    
    def test67(self):
        input = """if (a) if (b) if (c) return -1 elif (d) return 1 """
        expect = """if,(,a,),if,(,b,),if,(,c,),return,-,1,elif,(,d,),return,1,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect,167))
    
    
    def test68(self):
        input = """PPL Sem232"""
        expect = """PPL,Sem232,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 168))

    def test69(self):
        input = """abc"""
        expect = """abc,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect,169))


    def test70(self):
        input = """Z 181"""
        expect = """Z,181,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 170))


    def test71(self):
        input = """S 1 M P L E"""
        expect = """S,1,M,P,L,E,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 171))


    def test72(self):
        input = """1GUCCI"""
        expect = """1,GUCCI,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 172))


    def test73(self):
        input = """xyz2"""
        expect = """xyz2,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 173))


    def test74(self):
        input = """08072003"""
        expect = """08072003,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 174))


    def test75(self):
        input = """5.5"""
        expect = """5.5,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 175))


    def test76(self):
        input = """7e9"""
        expect = """7e9,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 176))


    def test77(self):
        input = """12e-1"""
        expect = "12e-1,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 177))


    def test78(self):
        input = """1.1.1.1"""
        expect = """1.1,Error Token ."""
        self.assertTrue(TestLexer.test(input, expect, 178))


    def test79(self):
        input = """909.909e-1"""
        expect = """909.909e-1,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 179))


    def test80(self):
        input = """6.9 + 9.6"""
        expect = """6.9,+,9.6,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 180))


    def test81(self):
        input = "6.9+9.6"
        expect = """6.9,+,9.6,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 181))


    def test82(self):
        input = """ "S1mple eX^Mp13" """ 
        expect = """S1mple eX^Mp13,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 182))


    def test83(self):
        input = """ "Tien '\\ """
        expect = """Illegal Escape In String: Tien '\ """
        self.assertTrue(TestLexer.test(input, expect, 183))


    def test84(self):
        input = """string str <- "_" bool b <- trueFalsetrue number num <- <-5.2 .3e+10  """ 
        expect = """string,str,<-,_,bool,b,<-,trueFalsetrue,number,num,<-,<-,5.2,Error Token ."""
        self.assertTrue(TestLexer.test(input, expect, 184))


    def test85(self):
        input = """ "Try hard \n" """
        expect = "Unclosed String: Try hard "
        self.assertTrue(TestLexer.test(input, expect, 185))


    def test86(self):
        input = """ "PPL \n Go" """
        expect = "Unclosed String: PPL "
        self.assertTrue(TestLexer.test(input, expect, 186))


    def test87(self):
        input = """ "97865  """
        expect = "Unclosed String: 97865  "
        self.assertTrue(TestLexer.test(input, expect, 187))


    def test88(self):
        input = """ "xyx121 \\n \n """
        expect = "Unclosed String: xyx121 \\n "
        self.assertTrue(TestLexer.test(input, expect, 188))


    def test89(self):
        input = """ "abcd '' \\n \\b """
        expect = "Unclosed String: abcd '' \\n \\b "
        self.assertTrue(TestLexer.test(input, expect, 189))
    
    
    def test90(self):
        input = """\f\b## PPL Go"""
        expect = """<EOF>"""  
        self.assertTrue(TestLexer.test(input, expect, 190))


    def test91(self):
        input = """##"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 191))


    def test92(self):
        input = """b##1"""
        expect = """b,<EOF>""" 
        self.assertTrue(TestLexer.test(input, expect, 192))


    def test93(self):
        input = """counter#"""
        expect = """counter,Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 193))


    def test94(self):
        input = """a\n##1b"""
        expect = """a,\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 194))


    def test95(self):
        input = """n\n#"""
        expect = """n,\n,Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 195))


    def test96(self):
        input = """++2 - 2"""
        expect = """+,+,2,-,2,<EOF>""" 
        self.assertTrue(TestLexer.test(input, expect, 196))


    def test97(self):
        input = """number a[1] <- [["str"],[1,2,3], 1 + 2 + 5]"""
        expect = """number,a,[,1,],<-,[,[,str,],,,[,1,,,2,,,3,],,,1,+,2,+,5,],<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 197))


    def test98(self):
        input = """5 % 2 + 2"""
        expect = """5,%,2,+,2,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 198))


    def test99(self):
        input = """var a1, a2, a3, a4 a5 <- 6/1 ... 9"""
        expect = """var,a1,,,a2,,,a3,,,a4,a5,<-,6,/,1,...,9,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 199))
    
    
    
    
    