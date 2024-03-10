import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
	def test_301(self):
		input = """number a
		"""
		expect = str(Program([VarDecl(Id("a"), NumberType())]))
		self.assertTrue(TestAST.test(input, expect, 301))
	def test_302(self):
		input = """
		func main()
begin
	var a <- 2
	return 1
end
		"""
		expect=str(Program(
			[FuncDecl(Id("main"), [], 
					Block([VarDecl(Id("a"), None, "var", NumberLiteral(2.0)), Return(NumberLiteral(1.0))]))]))
		#expect = str(Program([VarDecl(Id("a"), NumberType())]))
		self.assertTrue(TestAST.test(input, expect, 302))
	def test_303(self):
		input = """
		func main()
begin
	if (a<2)
	if (a<3) return 1
	else return 3
end
		"""
		expect=str(Program([
			FuncDecl(Id("main"), [], Block([If(BinaryOp("<", Id("a"), NumberLiteral(2.0)), 
												If(BinaryOp("<", Id("a"), NumberLiteral(3.0)), Return(NumberLiteral(1.0)), [], 
												   Return(NumberLiteral(3.0))), 
											[], None),
											]))
			]))
	# Program([FuncDecl(Id(main), [], Block([If((BinaryOp(<, Id(a), NumLit(2.0)),
	#                                       If((BinaryOp(<, Id(a), NumLit(3.0)), Return(NumLit(1.0))), [], Return(NumLit(3.0)))), [], None)]))])
		self.assertTrue(TestAST.test(input, expect, 303))
	def test_304(self):
		input = """
		number arr[2,3] <- [1,2,3,[4,5]]
		func main()
begin
	if (a<2) return 1
	if (a<3) return 2
	elif (b == 3) return 4
	elif (c / 3 == 1) return 5
	else return 3
end
		"""
		expect=str(Program([VarDecl(Id("arr"),ArrayType([2.0,3.0],NumberType()),None,ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0),ArrayLiteral([NumberLiteral(4.0),NumberLiteral(5.0)])])),
							FuncDecl(Id("main"),[],Block([
								If(BinaryOp("<",Id("a"),NumberLiteral(2.0)),Return(NumberLiteral(1.0))),
								If(BinaryOp("<",Id("a"),NumberLiteral(3.0)),Return(NumberLiteral(2.0)),
								   [(BinaryOp("==",Id("b"),NumberLiteral(3.0)),Return(NumberLiteral(4.0))),
									(BinaryOp("==",BinaryOp("/",Id("c"),NumberLiteral(3.0)),NumberLiteral(1.0)),Return(NumberLiteral(5.0)))],
								   Return(NumberLiteral(3.0)))]))]))
		#Program([VarDecl(Id(arr), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), ArrayLit(NumLit(4.0), NumLit(5.0)))), FuncDecl(Id(main), [], Block([If((BinaryOp(<, Id(a), NumLit(2.0)), Return(NumLit(1.0))), [], None), If((BinaryOp(<, Id(a), NumLit(3.0)), Return(NumLit(2.0))), [(BinaryOp(==, Id(b), NumLit(3.0)), Return(NumLit(4.0))), (BinaryOp(==, BinaryOp(/, Id(c), NumLit(3.0)), NumLit(1.0)), Return(NumLit(5.0)))], Return(NumLit(3.0)))]))])
		self.assertTrue(TestAST.test(input, expect, 304))
	def test_305(self):
		input = """
		number arr[2,3] <- [1,2,3,[4,5]]
		func main()
begin
	if (a<2) return true
	else return false
end
		"""
		
		expect = str(Program([
			VarDecl(Id("arr"),ArrayType([2.0,3.0],NumberType()),None,ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0),ArrayLiteral([NumberLiteral(4.0),NumberLiteral(5.0)])])),
			FuncDecl(Id("main"), [], Block([If(BinaryOp("<", Id("a"), NumberLiteral(2.0)),Return(BooleanLiteral(True)), [], 
											   Return(BooleanLiteral(False)))
											]))
			]))
		self.assertTrue(TestAST.test(input, expect, 305))
	def test_306(self):
		input = """
		bool a[0] <- [[2,3],[4,5],1+2] 
		"""
		
		expect = str(Program(
		   [VarDecl(Id("a"),ArrayType([0.0],BoolType()),None,
					ArrayLiteral([ArrayLiteral([NumberLiteral(2.0),NumberLiteral(3.0)]),ArrayLiteral([NumberLiteral(4.0),NumberLiteral(5.0)]),BinaryOp("+",NumberLiteral(1.0),NumberLiteral(2.0))]))]
		   )
			)
		self.assertTrue(TestAST.test(input, expect, 306))
	def test_307(self):
		input = """
		bool hello <- [123] 
		"""
		
		expect = str(Program(
		   [VarDecl(Id("hello"),BoolType(),None,ArrayLiteral([NumberLiteral(123.0)]))]
		   )
			)
		self.assertTrue(TestAST.test(input, expect, 307))
	def test_308(self):
		input = """
		bool a[1,2,3] <- [[true, false, true],["true","false",true]]
		"""
		
		expect = str(Program(
		   [VarDecl(Id("a"),ArrayType([1.0,2.0,3.0],BoolType()),None,ArrayLiteral([ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True)]),ArrayLiteral([StringLiteral("true"),StringLiteral("false"),BooleanLiteral(True)])]))]
		   )
			)
		self.assertTrue(TestAST.test(input, expect, 308))
	def test_309(self):
		input = """
		func main()
begin
	 x[1] <- y(1)[1,2,3]
end
		"""
		
		expect ="""Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(x), [NumLit(1.0)]), ArrayCell(CallExpr(Id(y), [NumLit(1.0)]), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]))]))])"""
		self.assertTrue(TestAST.test(input, expect, 309))
	def test_310(self):
		input = """
		func main()
					begin
						a <- main()[1+2,3] / a[2,3,4,5,6,7] + func_call(func_call[1,2])[1,2]
					end
		"""
		
		expect ="""Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), BinaryOp(+, BinaryOp(/, ArrayCell(CallExpr(Id(main), []), [BinaryOp(+, NumLit(1.0), NumLit(2.0)), NumLit(3.0)]), ArrayCell(Id(a), [NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0), NumLit(6.0), NumLit(7.0)])), ArrayCell(CallExpr(Id(func_call), [ArrayCell(Id(func_call), [NumLit(1.0), NumLit(2.0)])]), [NumLit(1.0), NumLit(2.0)])))]))])"""
			
		self.assertTrue(TestAST.test(input, expect, 310))
	def test_311(self):
		input = """
		func main()
					begin
						a[2,3] <- 2<a ... b > 2
					end
		"""
		
		expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(2.0), NumLit(3.0)]), BinaryOp(..., BinaryOp(<, NumLit(2.0), Id(a)), BinaryOp(>, Id(b), NumLit(2.0))))]))])"""
					 
					 
			
		self.assertTrue(TestAST.test(input, expect, 311))
	def test_312(self):
		input = """
		func main()
					begin
						a <- (function()[2,3] ... true) + 2 > (123 ... a[1+2,4/2])
					end
		"""
		
		expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), BinaryOp(>, BinaryOp(+, BinaryOp(..., ArrayCell(CallExpr(Id(function), []), [NumLit(2.0), NumLit(3.0)]), BooleanLit(True)), NumLit(2.0)), BinaryOp(..., NumLit(123.0), ArrayCell(Id(a), [BinaryOp(+, NumLit(1.0), NumLit(2.0)), BinaryOp(/, NumLit(4.0), NumLit(2.0))]))))]))])"""
		self.assertTrue(TestAST.test(input, expect, 312))
	def test_313(self):
		input = """
		func main()
					begin
						a <- ( "hello" > 3 ) - (a <= 2) - (true == 3)
						a[3] <- hehe[1,2] + - "happy" + not true 
						var a <- [1,2,3] + - [a+1,3>2] - [[1-2%3,a > a], [true, false]]
					end 
		"""
		
		expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), BinaryOp(-, BinaryOp(-, BinaryOp(>, StringLit(hello), NumLit(3.0)), BinaryOp(<=, Id(a), NumLit(2.0))), BinaryOp(==, BooleanLit(True), NumLit(3.0)))), AssignStmt(ArrayCell(Id(a), [NumLit(3.0)]), BinaryOp(+, BinaryOp(+, ArrayCell(Id(hehe), [NumLit(1.0), NumLit(2.0)]), UnaryOp(-, StringLit(happy))), UnaryOp(not, BooleanLit(True)))), VarDecl(Id(a), None, var, BinaryOp(-, BinaryOp(+, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), UnaryOp(-, ArrayLit(BinaryOp(+, Id(a), NumLit(1.0)), BinaryOp(>, NumLit(3.0), NumLit(2.0))))), ArrayLit(ArrayLit(BinaryOp(-, NumLit(1.0), BinaryOp(%, NumLit(2.0), NumLit(3.0))), BinaryOp(>, Id(a), Id(a))), ArrayLit(BooleanLit(True), BooleanLit(False)))))]))])"""
		self.assertTrue(TestAST.test(input, expect, 313))
	def test_314(self):
		input = """
		func main()
					begin
						a[2]<- isOdd(a,true,1)
					end
		"""
		
		expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), CallExpr(Id(isOdd), [Id(a), BooleanLit(True), NumLit(1.0)]))]))])"""
		self.assertTrue(TestAST.test(input, expect, 314))
	def test_315(self):
		input = """
		func main()
					begin
						 a[2]<- isOdd(a,true,isEven())
					end   
		"""
		
		expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), CallExpr(Id(isOdd), [Id(a), BooleanLit(True), CallExpr(Id(isEven), [])]))]))])"""
		self.assertTrue(TestAST.test(input, expect, 315))
	def test_316(self):
		input = """func oddOneOut(number a[2], bool d) return "happy birthday"
					func main()
					begin
						a <- odd() + even() % even()[oddOneOut(odd(),even())[odd(),even()]]
					end 
		"""
		expect = """Program([FuncDecl(Id(oddOneOut), [VarDecl(Id(a), ArrayType([2.0], NumberType), None, None), VarDecl(Id(d), BoolType, None, None)], Return(StringLit(happy birthday))), FuncDecl(Id(main), [], Block([AssignStmt(Id(a), BinaryOp(+, CallExpr(Id(odd), []), BinaryOp(%, CallExpr(Id(even), []), ArrayCell(CallExpr(Id(even), []), [ArrayCell(CallExpr(Id(oddOneOut), [CallExpr(Id(odd), []), CallExpr(Id(even), [])]), [CallExpr(Id(odd), []), CallExpr(Id(even), [])])]))))]))])"""
		self.assertTrue(TestAST.test(input, expect, 316))
	def test_317(self):
		input = """
		var assignment <- a()
			var assignment <- a(1,2)
			dynamic b <- [a,a<3,3]
			var assignment <- a(x,b[2])[2]
			var assignment <- a(x,y[3] ... z)[1,2]
			   
		"""
		expect="""Program([VarDecl(Id(assignment), None, var, CallExpr(Id(a), [])), VarDecl(Id(assignment), None, var, CallExpr(Id(a), [NumLit(1.0), NumLit(2.0)])), VarDecl(Id(b), None, dynamic, ArrayLit(Id(a), BinaryOp(<, Id(a), NumLit(3.0)), NumLit(3.0))), VarDecl(Id(assignment), None, var, ArrayCell(CallExpr(Id(a), [Id(x), ArrayCell(Id(b), [NumLit(2.0)])]), [NumLit(2.0)])), VarDecl(Id(assignment), None, var, ArrayCell(CallExpr(Id(a), [Id(x), BinaryOp(..., ArrayCell(Id(y), [NumLit(3.0)]), Id(z))]), [NumLit(1.0), NumLit(2.0)]))])"""
	# Program([FuncDecl(Id(main), [], Block([If((BinaryOp(<, Id(a), NumLit(2.0)),
	#                                       If((BinaryOp(<, Id(a), NumLit(3.0)), Return(NumLit(1.0))), [], Return(NumLit(3.0)))), [], None)]))])
		self.assertTrue(TestAST.test(input, expect, 317))
	def test_318(self):
		input =""" ## knight's tour problem
  

func solveKTUtil(number x,number y,number move_i,number sol,number moveX,number moveY) begin
    if (move_i == N * N) begin
        return true
    end

    for k until 0 by 8 begin
        var next_x <- x + moveX[k]
        var next_y <- y + moveY[k]
        if (isSafe(next_x, next_y, sol)) begin
            sol[next_x,next_y] <- move_i
            if (solveKTUtil(next_x, next_y, move_i + 1, sol, moveX, moveY)) begin
                return true
            end
            else begin
                sol[next_x,next_y] <- -1  ## backtracking
            end
        end
    end

    return false
end

func solveKT() begin
    var sol <- [N,N]

    for x until 0 by N begin
        for y until 0 by N begin
            sol[x,y] <- -1
        end
    end

    var moveX <- [2, 1, -1, -2, -2, -1, 1, 2]
    var moveY <- [1, 2, 2, 1, -1, -2, -2, -1]

    sol[0,0] <- 0

    if (not(solveKTUtil(0, 0, 1, sol, moveX, moveY))) begin
        print("Solution does not exist")
        return false
    end
    else begin
        printSolution(sol)
    end

    return true
end

"""
		expect = """Program([FuncDecl(Id(solveKTUtil), [VarDecl(Id(x), NumberType, None, None), VarDecl(Id(y), NumberType, None, None), VarDecl(Id(move_i), NumberType, None, None), VarDecl(Id(sol), NumberType, None, None), VarDecl(Id(moveX), NumberType, None, None), VarDecl(Id(moveY), NumberType, None, None)], Block([If((BinaryOp(==, Id(move_i), BinaryOp(*, Id(N), Id(N))), Block([Return(BooleanLit(True))])), [], None), For(Id(k), NumLit(0.0), NumLit(8.0), Block([VarDecl(Id(next_x), None, var, BinaryOp(+, Id(x), ArrayCell(Id(moveX), [Id(k)]))), VarDecl(Id(next_y), None, var, BinaryOp(+, Id(y), ArrayCell(Id(moveY), [Id(k)]))), If((CallExpr(Id(isSafe), [Id(next_x), Id(next_y), Id(sol)]), Block([AssignStmt(ArrayCell(Id(sol), [Id(next_x), Id(next_y)]), Id(move_i)), If((CallExpr(Id(solveKTUtil), [Id(next_x), Id(next_y), BinaryOp(+, Id(move_i), NumLit(1.0)), Id(sol), Id(moveX), Id(moveY)]), Block([Return(BooleanLit(True))])), [], Block([AssignStmt(ArrayCell(Id(sol), [Id(next_x), Id(next_y)]), UnaryOp(-, NumLit(1.0)))]))])), [], None)])), Return(BooleanLit(False))])), FuncDecl(Id(solveKT), [], Block([VarDecl(Id(sol), None, var, ArrayLit(Id(N), Id(N))), For(Id(x), NumLit(0.0), Id(N), Block([For(Id(y), NumLit(0.0), Id(N), Block([AssignStmt(ArrayCell(Id(sol), [Id(x), Id(y)]), UnaryOp(-, NumLit(1.0)))]))])), VarDecl(Id(moveX), None, var, ArrayLit(NumLit(2.0), NumLit(1.0), UnaryOp(-, NumLit(1.0)), UnaryOp(-, NumLit(2.0)), UnaryOp(-, NumLit(2.0)), UnaryOp(-, NumLit(1.0)), NumLit(1.0), NumLit(2.0))), VarDecl(Id(moveY), None, var, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(2.0), NumLit(1.0), UnaryOp(-, NumLit(1.0)), UnaryOp(-, NumLit(2.0)), UnaryOp(-, NumLit(2.0)), UnaryOp(-, NumLit(1.0)))), AssignStmt(ArrayCell(Id(sol), [NumLit(0.0), NumLit(0.0)]), NumLit(0.0)), If((UnaryOp(not, CallExpr(Id(solveKTUtil), [NumLit(0.0), NumLit(0.0), NumLit(1.0), Id(sol), Id(moveX), Id(moveY)])), Block([CallStmt(Id(print), [StringLit(Solution does not exist)]), Return(BooleanLit(False))])), [], Block([CallStmt(Id(printSolution), [Id(sol)])])), Return(BooleanLit(True))]))])"""
		self.assertTrue(TestAST.test(input, expect, 318))
	def test_319(self):
		input = """
		func areDivisors(number num1, number num2)
 return ((num1 % num2 = 0) or (num2 % num1 = 0))
 func main()
 begin
 var num1 <- readNumber()
 var num2 <- readNumber()
 if (areDivisors(num1, num2)) writeString("Yes")
 else writeString("No")
 end  
		"""
		expect="""Program([FuncDecl(Id(areDivisors), [VarDecl(Id(num1), NumberType, None, None), VarDecl(Id(num2), NumberType, None, None)], Return(BinaryOp(or, BinaryOp(=, BinaryOp(%, Id(num1), Id(num2)), NumLit(0.0)), BinaryOp(=, BinaryOp(%, Id(num2), Id(num1)), NumLit(0.0))))), FuncDecl(Id(main), [], Block([VarDecl(Id(num1), None, var, CallExpr(Id(readNumber), [])), VarDecl(Id(num2), None, var, CallExpr(Id(readNumber), [])), If((CallExpr(Id(areDivisors), [Id(num1), Id(num2)]), CallStmt(Id(writeString), [StringLit(Yes)])), [], CallStmt(Id(writeString), [StringLit(No)]))]))])"""#Program([VarDecl(Id(arr), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), ArrayLit(NumLit(4.0), NumLit(5.0)))), FuncDecl(Id(main), [], Block([If((BinaryOp(<, Id(a), NumLit(2.0)), Return(NumLit(1.0))), [], None), If((BinaryOp(<, Id(a), NumLit(3.0)), Return(NumLit(2.0))), [(BinaryOp(==, Id(b), NumLit(3.0)), Return(NumLit(4.0))), (BinaryOp(==, BinaryOp(/, Id(c), NumLit(3.0)), NumLit(1.0)), Return(NumLit(5.0)))], Return(NumLit(3.0)))]))])
		self.assertTrue(TestAST.test(input, expect, 319))
	def test_320(self):
		input = """
		func isPrime(number x)
 func main()
 begin
 number x <- readNumber()
 if (isPrime(x)) writeString("Yes")
 else writeString("No")
 end
		
		"""
		
		expect = """Program([FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], None), FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, CallExpr(Id(readNumber), [])), If((CallExpr(Id(isPrime), [Id(x)]), CallStmt(Id(writeString), [StringLit(Yes)])), [], CallStmt(Id(writeString), [StringLit(No)]))]))])"""
		self.assertTrue(TestAST.test(input, expect, 320))
	def test_321(self):
		input = """
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
		
		expect = """Program([FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], Block([If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None), VarDecl(Id(i), None, var, NumLit(2.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), Block([If((BinaryOp(=, BinaryOp(%, Id(x), Id(i)), NumLit(0.0)), Return(BooleanLit(False))), [], None)])), Return(BooleanLit(True))]))])"""
		self.assertTrue(TestAST.test(input, expect, 321))
	def test_322(self):
		input = """
		func isPrime()
 begin
 if (x <= 1) return false
 var i <- 2
 for i until (i > x / 2) by 1
 begin
 if (x % i = 0) return false
 end
 return true
 end
		"""
		
		expect = """Program([FuncDecl(Id(isPrime), [], Block([If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None), VarDecl(Id(i), None, var, NumLit(2.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), Block([If((BinaryOp(=, BinaryOp(%, Id(x), Id(i)), NumLit(0.0)), Return(BooleanLit(False))), [], None)])), Return(BooleanLit(True))]))])"""
		self.assertTrue(TestAST.test(input, expect, 322))
	def test_323(self):
		input = """
		func foo(number a[5], string b)
 begin
 var i <- 0
 for i until i >= 5 by 1
 begin
 a[i] <- i * i + 5
 end
 return-1
 end
		"""
		
		expect = """Program([FuncDecl(Id(foo), [VarDecl(Id(a), ArrayType([5.0], NumberType), None, None), VarDecl(Id(b), StringType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), NumLit(5.0)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(a), [Id(i)]), BinaryOp(+, BinaryOp(*, Id(i), Id(i)), NumLit(5.0)))])), Return(UnaryOp(-, NumLit(1.0)))]))])"""
		self.assertTrue(TestAST.test(input, expect, 323))
	def test_324(self):
		input = """
		 func main()
		begin
			var i <- foo(2+5)
			begin
				continue
				begin
					break
					begin
						for a until a >= i by 1 + 1
							if (a > i * i) return true
							else return false
					end
				end
			end
		end
		"""
		
		expect ="""Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, CallExpr(Id(foo), [BinaryOp(+, NumLit(2.0), NumLit(5.0))])), Block([Continue, Block([Break, Block([For(Id(a), BinaryOp(>=, Id(a), Id(i)), BinaryOp(+, NumLit(1.0), NumLit(1.0)), If((BinaryOp(>, Id(a), BinaryOp(*, Id(i), Id(i))), Return(BooleanLit(True))), [], Return(BooleanLit(False))))])])])]))])"""
		self.assertTrue(TestAST.test(input, expect, 324))
	def test_325(self):
		input = """
		func main()
begin
dynamic a <- readNumber()
if ((a>0) and (a<10))
	a<-a*2
else if ((a>10) and (a<20) )
a<-a*3
else a <- a*4
return
end
		"""
		
		expect ="""Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, dynamic, CallExpr(Id(readNumber), [])), If((BinaryOp(and, BinaryOp(>, Id(a), NumLit(0.0)), BinaryOp(<, Id(a), NumLit(10.0))), AssignStmt(Id(a), BinaryOp(*, Id(a), NumLit(2.0)))), [], If((BinaryOp(and, BinaryOp(>, Id(a), NumLit(10.0)), BinaryOp(<, Id(a), NumLit(20.0))), AssignStmt(Id(a), BinaryOp(*, Id(a), NumLit(3.0)))), [], AssignStmt(Id(a), BinaryOp(*, Id(a), NumLit(4.0))))), Return()]))])"""
		self.assertTrue(TestAST.test(input, expect, 325))
	def test_326(self):
		input = """
		dynamic a
var b<-2
func main()
	begin
if (b=2)
	a <- b
elif (b=3)
	a <- b*2 + 1
else a <- -1
return
end
		"""
		
		expect = """Program([VarDecl(Id(a), None, dynamic, None), VarDecl(Id(b), None, var, NumLit(2.0)), FuncDecl(Id(main), [], Block([If((BinaryOp(=, Id(b), NumLit(2.0)), AssignStmt(Id(a), Id(b))), [(BinaryOp(=, Id(b), NumLit(3.0)), AssignStmt(Id(a), BinaryOp(+, BinaryOp(*, Id(b), NumLit(2.0)), NumLit(1.0))))], AssignStmt(Id(a), UnaryOp(-, NumLit(1.0)))), Return()]))])"""    
					 
			
		self.assertTrue(TestAST.test(input, expect, 326))
	def test_327(self):
		input = """
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
		
		expect ="""Program([FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], Block([If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None), VarDecl(Id(i), None, var, NumLit(2.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), Block([If((BinaryOp(=, BinaryOp(%, Id(x), Id(i)), NumLit(0.0)), Return(BooleanLit(False))), [], None)])), Return(BooleanLit(True))]))])"""
		self.assertTrue(TestAST.test(input, expect, 327))
	def test_328(self):
		input = """
		func main()
		begin
		return
		end 
		"""
		
		expect = """Program([FuncDecl(Id(main), [], Block([Return()]))])"""
		self.assertTrue(TestAST.test(input, expect, 328))
	def test_329(self):
		input = """
		func main()
		begin
		return (false)
		end
		"""
		
		expect = """Program([FuncDecl(Id(main), [], Block([Return(BooleanLit(False))]))])"""
		self.assertTrue(TestAST.test(input, expect, 329))
	def test_330(self):
		input = """
		 func main()
		begin
			begin
				begin
					return "I <3 PPL"
				end
			end
		end
		"""
		
		expect = """Program([FuncDecl(Id(main), [], Block([Block([Block([Return(StringLit(I <3 PPL))])])]))])"""
		self.assertTrue(TestAST.test(input, expect, 330))
	def test_331(self):
		input = """
				 func main()
		begin 
			return ([1,2,3]) + 1
			return main()
			main(1,2)
			fun()
			main([1,2,3], 1+2, a, c ... e)
		end
		"""
		
		expect = """Program([FuncDecl(Id(main), [], Block([Return(BinaryOp(+, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), NumLit(1.0))), Return(CallExpr(Id(main), [])), CallStmt(Id(main), [NumLit(1.0), NumLit(2.0)]), CallStmt(Id(fun), []), CallStmt(Id(main), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), BinaryOp(+, NumLit(1.0), NumLit(2.0)), Id(a), BinaryOp(..., Id(c), Id(e))])]))])"""
		self.assertTrue(TestAST.test(input, expect, 331))
	
	def test_332(self):
		input = """func main()
		"""
		expect = """Program([FuncDecl(Id(main), [], None)])"""
		self.assertTrue(TestAST.test(input, expect, 332))
	def test_333(self):
		input = """
		  var _globalVar <- -1e-9
number pi <- 3.1415926535897
dynamic e <- 2.71828182846
func exp(number n)
begin
var ans <- 1
var i<-0
for i until i=n by 1
return ans
end
func main()
begin
	var a<-exp(10)
end
		"""
		expect="""Program([VarDecl(Id(_globalVar), None, var, UnaryOp(-, NumLit(1e-09))), VarDecl(Id(pi), NumberType, None, NumLit(3.1415926535897)), VarDecl(Id(e), None, dynamic, NumLit(2.71828182846)), FuncDecl(Id(exp), [VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(ans), None, var, NumLit(1.0)), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(=, Id(i), Id(n)), NumLit(1.0), Return(Id(ans)))])), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, CallExpr(Id(exp), [NumLit(10.0)]))]))])"""
		self.assertTrue(TestAST.test(input, expect, 333))
	def test_334(self):
		input = """
		func main()
begin
	if (a<2)
	if (a<3) return 1
	else return 3
end
		"""
		expect="""Program([FuncDecl(Id(main), [], Block([If((BinaryOp(<, Id(a), NumLit(2.0)), If((BinaryOp(<, Id(a), NumLit(3.0)), Return(NumLit(1.0))), [], Return(NumLit(3.0)))), [], None)]))])"""
	# Program([FuncDecl(Id(main), [], Block([If((BinaryOp(<, Id(a), NumLit(2.0)),
	#                                       If((BinaryOp(<, Id(a), NumLit(3.0)), Return(NumLit(1.0))), [], Return(NumLit(3.0)))), [], None)]))])
		self.assertTrue(TestAST.test(input, expect, 334))
	def test_335(self):
		input = """
		 func main()
		begin 
			bool a <- not not - - (a[a[a[a[a[a[0]]]]]])
		end
		"""
		expect="""Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), BoolType, None, UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(-, ArrayCell(Id(a), [ArrayCell(Id(a), [ArrayCell(Id(a), [ArrayCell(Id(a), [ArrayCell(Id(a), [ArrayCell(Id(a), [NumLit(0.0)])])])])])]))))))]))])"""
		#Program([VarDecl(Id(arr), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), ArrayLit(NumLit(4.0), NumLit(5.0)))), FuncDecl(Id(main), [], Block([If((BinaryOp(<, Id(a), NumLit(2.0)), Return(NumLit(1.0))), [], None), If((BinaryOp(<, Id(a), NumLit(3.0)), Return(NumLit(2.0))), [(BinaryOp(==, Id(b), NumLit(3.0)), Return(NumLit(4.0))), (BinaryOp(==, BinaryOp(/, Id(c), NumLit(3.0)), NumLit(1.0)), Return(NumLit(5.0)))], Return(NumLit(3.0)))]))])
		self.assertTrue(TestAST.test(input, expect, 335))
	def test_336(self):
		input = """
		func interface()
		begin
			newline()
			newline()
		end
		"""
		
		expect = """Program([FuncDecl(Id(interface), [], Block([CallStmt(Id(newline), []), CallStmt(Id(newline), [])]))])"""
		self.assertTrue(TestAST.test(input, expect, 336))
	def test_337(self):
		input = """
		func main()
begin
var i<-0
var j<-0
var k<-0
number x<-readNumber()
for i until i<x by 5
for j until j<x by a
for k until k<x by 1 var a <- "Dung noi hai chu '" Gia nhu '""
end 
		"""
		
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), None, var, NumLit(0.0)), VarDecl(Id(k), None, var, NumLit(0.0)), VarDecl(Id(x), NumberType, None, CallExpr(Id(readNumber), [])), For(Id(i), BinaryOp(<, Id(i), Id(x)), NumLit(5.0), For(Id(j), BinaryOp(<, Id(j), Id(x)), Id(a), For(Id(k), BinaryOp(<, Id(k), Id(x)), NumLit(1.0), VarDecl(Id(a), None, var, StringLit(Dung noi hai chu '" Gia nhu '")))))]))])"""
		self.assertTrue(TestAST.test(input, expect, 337))
	def test_338(self):
		input = """
		func main()
		begin 
			bool a <- a[not not - - (a[a[a[a[a[a[0]]]]]]), 2+3/4,[1,2,3,4]]
		end
		var b <- a(1,2)[1,2,3 ... 2] + false + true
		
		
		"""
		
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), BoolType, None, ArrayCell(Id(a), [UnaryOp(not, UnaryOp(not, UnaryOp(-, UnaryOp(-, ArrayCell(Id(a), [ArrayCell(Id(a), [ArrayCell(Id(a), [ArrayCell(Id(a), [ArrayCell(Id(a), [ArrayCell(Id(a), [NumLit(0.0)])])])])])]))))), BinaryOp(+, NumLit(2.0), BinaryOp(/, NumLit(3.0), NumLit(4.0))), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0))]))])), VarDecl(Id(b), None, var, BinaryOp(+, BinaryOp(+, ArrayCell(CallExpr(Id(a), [NumLit(1.0), NumLit(2.0)]), [NumLit(1.0), NumLit(2.0), BinaryOp(..., NumLit(3.0), NumLit(2.0))]), BooleanLit(False)), BooleanLit(True)))])"""
		self.assertTrue(TestAST.test(input, expect, 338))
	def test_339(self):
		input = """
		func main()
			begin
				for i until i<2 by a%2+5-4 
					for j until i by a[5] 
						for k until j by fun()[a] return
			end 
		"""
		
		expect ="""Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(<, Id(i), NumLit(2.0)), BinaryOp(-, BinaryOp(+, BinaryOp(%, Id(a), NumLit(2.0)), NumLit(5.0)), NumLit(4.0)), For(Id(j), Id(i), ArrayCell(Id(a), [NumLit(5.0)]), For(Id(k), Id(j), ArrayCell(CallExpr(Id(fun), []), [Id(a)]), Return())))]))])"""
		self.assertTrue(TestAST.test(input, expect, 339))
	def test_340(self):
		input = """
		func a() ##HAPPY NEW YEAR
		begin
			a[_3 + foo(_2)] <- a[_b[_2, _3]] + _4 
		end
		
		"""
		
		expect ="""Program([FuncDecl(Id(a), [], Block([AssignStmt(ArrayCell(Id(a), [BinaryOp(+, Id(_3), CallExpr(Id(foo), [Id(_2)]))]), BinaryOp(+, ArrayCell(Id(a), [ArrayCell(Id(_b), [Id(_2), Id(_3)])]), Id(_4)))]))])"""
		self.assertTrue(TestAST.test(input, expect, 340))
	def test_341(self):
		input = """
		string a <- "despacito"
		bool a <- true
		func main()
		func isOdd()
		"""
		
		expect ="""Program([VarDecl(Id(a), StringType, None, StringLit(despacito)), VarDecl(Id(a), BoolType, None, BooleanLit(True)), FuncDecl(Id(main), [], None), FuncDecl(Id(isOdd), [], None)])"""
			
		self.assertTrue(TestAST.test(input, expect, 341))
	def test_342(self):
		input = """
		func foo(number a[5], string b)
		begin
			var i <- 0
			for i until i >= 5 by 1
				begin
					a[i] <- i * i + 5
				end
			return -1
		end
		"""
		
		expect = """Program([FuncDecl(Id(foo), [VarDecl(Id(a), ArrayType([5.0], NumberType), None, None), VarDecl(Id(b), StringType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), NumLit(5.0)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(a), [Id(i)]), BinaryOp(+, BinaryOp(*, Id(i), Id(i)), NumLit(5.0)))])), Return(UnaryOp(-, NumLit(1.0)))]))])"""
					 
					 
			
		self.assertTrue(TestAST.test(input, expect, 342))
	def test_343(self):
		input = """
		func main() begin
		number x <- readNumber()
		var y <- 0.
		dynamic z
end
		"""
		
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, CallExpr(Id(readNumber), [])), VarDecl(Id(y), None, var, NumLit(0.0)), VarDecl(Id(z), None, dynamic, None)]))])"""
		self.assertTrue(TestAST.test(input, expect, 343))
	def test_344(self):
		input = """
		func main() begin
		bool _b[1] <- [true]
		number a[2,2] <- [[1,2],[3,4]]
		a[1,1] <- a[1,2]
end
		"""
		
		expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(_b), ArrayType([1.0], BoolType), None, ArrayLit(BooleanLit(True))), VarDecl(Id(a), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0)))), AssignStmt(ArrayCell(Id(a), [NumLit(1.0), NumLit(1.0)]), ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0)]))]))])"""
		self.assertTrue(TestAST.test(input, expect, 344))
	def test_345(self):
		input = """
		func main()
		begin
			a[_3 + foo(_2)] <- a[_b[_2, _3]] + _4 
		end
		func a() ##HAPPY NEW YEAR
		"""
		
		expect = """Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [BinaryOp(+, Id(_3), CallExpr(Id(foo), [Id(_2)]))]), BinaryOp(+, ArrayCell(Id(a), [ArrayCell(Id(_b), [Id(_2), Id(_3)])]), Id(_4)))])), FuncDecl(Id(a), [], None)])"""
		self.assertTrue(TestAST.test(input, expect, 345))
	def test_346(self):
		input = """ ## dfs
			func dfs(number node,number visited) begin
		## Mark the current node as visited
		visited[node] <- true

		## Print the node
		print(node)

		## Recur for all the vertices adjacent to this vertex
		for i until 0 by size(adj[node]) begin
			if (not visited[adj[node,i]]) begin
				dfs(adj[node,i], visited)
			end
		end
	end

	func main() begin
		## Number of nodes
		var n <- 5

		## Adjacency list
		var adj <- [n]

		## Visited array
		var visited <- [n]

		## Initialize visited array
		for i until 0 by n begin
			visited[i] <- false
		end

		## Add edges to the graph (adjacency list)
		## Note: Add your own edges here

		## Call DFS
		dfs(0, visited)
	end

		"""
		expect = """Program([FuncDecl(Id(dfs), [VarDecl(Id(node), NumberType, None, None), VarDecl(Id(visited), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(visited), [Id(node)]), BooleanLit(True)), CallStmt(Id(print), [Id(node)]), For(Id(i), NumLit(0.0), CallExpr(Id(size), [ArrayCell(Id(adj), [Id(node)])]), Block([If((UnaryOp(not, ArrayCell(Id(visited), [ArrayCell(Id(adj), [Id(node), Id(i)])])), Block([CallStmt(Id(dfs), [ArrayCell(Id(adj), [Id(node), Id(i)]), Id(visited)])])), [], None)]))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n), None, var, NumLit(5.0)), VarDecl(Id(adj), None, var, ArrayLit(Id(n))), VarDecl(Id(visited), None, var, ArrayLit(Id(n))), For(Id(i), NumLit(0.0), Id(n), Block([AssignStmt(ArrayCell(Id(visited), [Id(i)]), BooleanLit(False))])), CallStmt(Id(dfs), [NumLit(0.0), Id(visited)])]))])"""
		self.assertTrue(TestAST.test(input, expect, 346))
	def test_347(self):
		input = """
		number a[2] <- [1,2]
		func main (number _1[2], string _2) begin
		print("Hello, world!")	
		end

	"""
		expect = """Program([VarDecl(Id(a), ArrayType([2.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0))), FuncDecl(Id(main), [VarDecl(Id(_1), ArrayType([2.0], NumberType), None, None), VarDecl(Id(_2), StringType, None, None)], Block([CallStmt(Id(print), [StringLit(Hello, world!)])]))])"""
	def test_348(self):
		input = """
		func bfs(number node,number visited,number queue) begin
    ## Mark the current node as visited and enqueue it
    visited[node] <- true
    enqueue(queue, node)

    ## Loop until the queue is empty
    for i until 0 by size(queue) begin
        ## Dequeue a vertex from queue and print it
        var s <- dequeue(queue)
        print(s)

        ## Get all adjacent vertices of the dequeued vertex s
        ## If an adjacent has not been visited, then mark it visited and enqueue it
        for j until 0 by size(adj[s]) begin
            if (not visited[adj[s,j]]) begin
                visited[adj[s,j]] <- true
                enqueue(queue, adj[s,j])
            end
        end
    end
end

func main() begin
    ## Number of nodes
    var n <- 5

    ## Adjacency list
    var adj <- [n]

    ## Visited array
    var visited <- [n]

    ## Queue for BFS
    var queue <- [None]

    ## Initialize visited array
    for i until 0 by n begin
        visited[i] <- false
    end

    ## Add edges to the graph (adjacency list)
    ## Note: Add your own edges here

    ## Call BFS
    bfs(0, visited, queue)
end

 """
		expect = """Program([FuncDecl(Id(bfs), [VarDecl(Id(node), NumberType, None, None), VarDecl(Id(visited), NumberType, None, None), VarDecl(Id(queue), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(visited), [Id(node)]), BooleanLit(True)), CallStmt(Id(enqueue), [Id(queue), Id(node)]), For(Id(i), NumLit(0.0), CallExpr(Id(size), [Id(queue)]), Block([VarDecl(Id(s), None, var, CallExpr(Id(dequeue), [Id(queue)])), CallStmt(Id(print), [Id(s)]), For(Id(j), NumLit(0.0), CallExpr(Id(size), [ArrayCell(Id(adj), [Id(s)])]), Block([If((UnaryOp(not, ArrayCell(Id(visited), [ArrayCell(Id(adj), [Id(s), Id(j)])])), Block([AssignStmt(ArrayCell(Id(visited), [ArrayCell(Id(adj), [Id(s), Id(j)])]), BooleanLit(True)), CallStmt(Id(enqueue), [Id(queue), ArrayCell(Id(adj), [Id(s), Id(j)])])])), [], None)]))]))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n), None, var, NumLit(5.0)), VarDecl(Id(adj), None, var, ArrayLit(Id(n))), VarDecl(Id(visited), None, var, ArrayLit(Id(n))), VarDecl(Id(queue), None, var, ArrayLit(Id(None))), For(Id(i), NumLit(0.0), Id(n), Block([AssignStmt(ArrayCell(Id(visited), [Id(i)]), BooleanLit(False))])), CallStmt(Id(bfs), [NumLit(0.0), Id(visited), Id(queue)])]))])"""
		self.assertTrue(TestAST.test(input, expect, 348))
	def test_349(self):
		input = """
		func partition(number arr [1000],number low ,number high) begin
    var pivot <- arr[high]
    var i <- (low - 1)

    for j until low by high begin
        if (arr[j] <= pivot) begin
            i <- i + 1
            var temp <- arr[i]
            arr[i] <- arr[j]
            arr[j] <- temp
        end
    end

    var temp <- arr[i + 1]
    arr[i + 1] <- arr[high]
    arr[high] <- temp

    return (i + 1)
end

func quickSort(number arr[1000], number low,number high) begin
    if (low < high) begin
        var pi <- partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    end
end

"""
		expect = """Program([FuncDecl(Id(partition), [VarDecl(Id(arr), ArrayType([1000.0], NumberType), None, None), VarDecl(Id(low), NumberType, None, None), VarDecl(Id(high), NumberType, None, None)], Block([VarDecl(Id(pivot), None, var, ArrayCell(Id(arr), [Id(high)])), VarDecl(Id(i), None, var, BinaryOp(-, Id(low), NumLit(1.0))), For(Id(j), Id(low), Id(high), Block([If((BinaryOp(<=, ArrayCell(Id(arr), [Id(j)]), Id(pivot)), Block([AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0))), VarDecl(Id(temp), None, var, ArrayCell(Id(arr), [Id(i)])), AssignStmt(ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [Id(j)])), AssignStmt(ArrayCell(Id(arr), [Id(j)]), Id(temp))])), [], None)])), VarDecl(Id(temp), None, var, ArrayCell(Id(arr), [BinaryOp(+, Id(i), NumLit(1.0))])), AssignStmt(ArrayCell(Id(arr), [BinaryOp(+, Id(i), NumLit(1.0))]), ArrayCell(Id(arr), [Id(high)])), AssignStmt(ArrayCell(Id(arr), [Id(high)]), Id(temp)), Return(BinaryOp(+, Id(i), NumLit(1.0)))])), FuncDecl(Id(quickSort), [VarDecl(Id(arr), ArrayType([1000.0], NumberType), None, None), VarDecl(Id(low), NumberType, None, None), VarDecl(Id(high), NumberType, None, None)], Block([If((BinaryOp(<, Id(low), Id(high)), Block([VarDecl(Id(pi), None, var, CallExpr(Id(partition), [Id(arr), Id(low), Id(high)])), CallStmt(Id(quickSort), [Id(arr), Id(low), BinaryOp(-, Id(pi), NumLit(1.0))]), CallStmt(Id(quickSort), [Id(arr), BinaryOp(+, Id(pi), NumLit(1.0)), Id(high)])])), [], None)]))])"""
		self.assertTrue(TestAST.test(input, expect, 349))
	def test_350(self):
		input = """
  func binaryToDecimal(number binary) begin
    var decimal <- 0
    var base <- 1  ## 2^0 = 1

    for i until 0 by size(binary) begin
        if (binary[size(binary) - i - 1] == "1") begin
            decimal <- decimal + base
        end
        base <- base * 2
    end

    return decimal
end

func main() begin
    var binary <- "1011"  ## Binary number
    var decimal <- binaryToDecimal(binary)
    print(decimal)
end
	
   """
		expect = """Program([FuncDecl(Id(binaryToDecimal), [VarDecl(Id(binary), NumberType, None, None)], Block([VarDecl(Id(decimal), None, var, NumLit(0.0)), VarDecl(Id(base), None, var, NumLit(1.0)), For(Id(i), NumLit(0.0), CallExpr(Id(size), [Id(binary)]), Block([If((BinaryOp(==, ArrayCell(Id(binary), [BinaryOp(-, BinaryOp(-, CallExpr(Id(size), [Id(binary)]), Id(i)), NumLit(1.0))]), StringLit(1)), Block([AssignStmt(Id(decimal), BinaryOp(+, Id(decimal), Id(base)))])), [], None), AssignStmt(Id(base), BinaryOp(*, Id(base), NumLit(2.0)))])), Return(Id(decimal))])), FuncDecl(Id(main), [], Block([VarDecl(Id(binary), None, var, StringLit(1011)), VarDecl(Id(decimal), None, var, CallExpr(Id(binaryToDecimal), [Id(binary)])), CallStmt(Id(print), [Id(decimal)])]))])"""
		self.assertTrue(TestAST.test(input, expect, 350))
	def test_351(self):
		input = """
    func decimalToBinary( number n)begin
    if (n == 0) begin
        return "0"
    end

    var binary <- ""
    var temp <- n
    var i <- 0

    for i until 0 by size(n) begin
        if (temp % 2 == 1) begin
            binary <- "1" + binary
        end
        else begin
            binary <- "0" + binary
        end
        temp <- temp / 2
        if (temp == 0) begin
            break
        end
    end

    return binary
end

"""
		expect = """Program([FuncDecl(Id(decimalToBinary), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(==, Id(n), NumLit(0.0)), Block([Return(StringLit(0))])), [], None), VarDecl(Id(binary), None, var, StringLit()), VarDecl(Id(temp), None, var, Id(n)), VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), NumLit(0.0), CallExpr(Id(size), [Id(n)]), Block([If((BinaryOp(==, BinaryOp(%, Id(temp), NumLit(2.0)), NumLit(1.0)), Block([AssignStmt(Id(binary), BinaryOp(+, StringLit(1), Id(binary)))])), [], Block([AssignStmt(Id(binary), BinaryOp(+, StringLit(0), Id(binary)))])), AssignStmt(Id(temp), BinaryOp(/, Id(temp), NumLit(2.0))), If((BinaryOp(==, Id(temp), NumLit(0.0)), Block([Break])), [], None)])), Return(Id(binary))]))])"""
		self.assertTrue(TestAST.test(input, expect, 351))
	def test_352(self):
		input = """### prime check
  		func isPrime(number n) begin
    if (n <= 1) begin
        return false
    end
    for i until 2 by sqrt(n) + 1 begin
        if (n % i == 0) begin
            return false
        end
    end
    return true
end
"""
		expect = """Program([FuncDecl(Id(isPrime), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(<=, Id(n), NumLit(1.0)), Block([Return(BooleanLit(False))])), [], None), For(Id(i), NumLit(2.0), BinaryOp(+, CallExpr(Id(sqrt), [Id(n)]), NumLit(1.0)), Block([If((BinaryOp(==, BinaryOp(%, Id(n), Id(i)), NumLit(0.0)), Block([Return(BooleanLit(False))])), [], None)])), Return(BooleanLit(True))]))])"""
		self.assertTrue(TestAST.test(input, expect, 352))
	def test_353(self):
		input = """## find GCD
  func gcd(number a,number b) begin
    if (b == 0) begin
        return a
    end
    else begin
        return gcd(b, a % b)
    end
end
"""
		expect = """Program([FuncDecl(Id(gcd), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(==, Id(b), NumLit(0.0)), Block([Return(Id(a))])), [], Block([Return(CallExpr(Id(gcd), [Id(b), BinaryOp(%, Id(a), Id(b))]))]))]))])"""
		self.assertTrue(TestAST.test(input, expect, 353))
	def test_354(self):
		input = """## find LCM
  func lcm(number a,number b) begin
    return (a * b) / gcd(a, b)
end
"""
		expect = """Program([FuncDecl(Id(lcm), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(BinaryOp(/, BinaryOp(*, Id(a), Id(b)), CallExpr(Id(gcd), [Id(a), Id(b)])))]))])"""
		self.assertTrue(TestAST.test(input, expect, 354))
	def test_355(self):
		input = """ ### fibonacci
  		func fibonacci(number n) begin
    if (n <= 1) begin
        return n
    end
    else begin
        return fibonacci(n - 1) + fibonacci(n - 2)
    end
end
"""
		expect = """Program([FuncDecl(Id(fibonacci), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(<=, Id(n), NumLit(1.0)), Block([Return(Id(n))])), [], Block([Return(BinaryOp(+, CallExpr(Id(fibonacci), [BinaryOp(-, Id(n), NumLit(1.0))]), CallExpr(Id(fibonacci), [BinaryOp(-, Id(n), NumLit(2.0))])))]))]))])"""
		self.assertTrue(TestAST.test(input, expect,355))	
	def test_356(self):
		input = """## factorial
  		func factorial(number n) begin
    if (n == 0) begin
        return 1
    end
    else begin
        return n * factorial(n - 1)
    end
end
"""
		expect = """Program([FuncDecl(Id(factorial), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(==, Id(n), NumLit(0.0)), Block([Return(NumLit(1.0))])), [], Block([Return(BinaryOp(*, Id(n), CallExpr(Id(factorial), [BinaryOp(-, Id(n), NumLit(1.0))])))]))]))])"""
		self.assertTrue(TestAST.test(input, expect,356))
	def test_357(self):
		input = """## power 
  		func factorial(number n) begin
    if (n == 0) begin
        return 1
    end
    else begin
        return n * factorial(n - 1)
    end
end
"""
		expect = """Program([FuncDecl(Id(factorial), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(==, Id(n), NumLit(0.0)), Block([Return(NumLit(1.0))])), [], Block([Return(BinaryOp(*, Id(n), CallExpr(Id(factorial), [BinaryOp(-, Id(n), NumLit(1.0))])))]))]))])"""
		self.assertTrue(TestAST.test(input, expect, 357))
	def test_358(self):
		input = """ ## modulo
  		func modulus(number a,number b) begin
    if (b != 0) begin
        return a % b
    end
    else begin
        print("Error: Division by zero is not allowed.")
    end
end
"""
		expect = """Program([FuncDecl(Id(modulus), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(!=, Id(b), NumLit(0.0)), Block([Return(BinaryOp(%, Id(a), Id(b)))])), [], Block([CallStmt(Id(print), [StringLit(Error: Division by zero is not allowed.)])]))]))])"""
		self.assertTrue(TestAST.test(input, expect, 358))
	def test_359(self):
		input = """ ## divide
  		func divide(number a, number b) begin
    if (b != 0) begin
        return a / b
    end
    else begin
        print("Error: Division by zero is not allowed.")
    end
end
"""
		expect = """Program([FuncDecl(Id(divide), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(!=, Id(b), NumLit(0.0)), Block([Return(BinaryOp(/, Id(a), Id(b)))])), [], Block([CallStmt(Id(print), [StringLit(Error: Division by zero is not allowed.)])]))]))])"""
		self.assertTrue(TestAST.test(input, expect, 359))
	def test_360(self):
		input = """### dijikstra
  		## Note: This is a simplified version of Dijkstra's algorithm for demonstration purposes.
## It assumes that the graph is represented as an adjacency matrix 'graph' and that
## all edges have positive weights. The function returns the shortest path from the
## source node to all other nodes in the graph.

func dijkstra(number graph,number src) begin
    var n <- size(graph)
    var dist <- [n]
    var visited <- [n]

    for i until 0 by n begin
        dist[i] <- INF
        visited[i] <- false
    end

    dist[src] <- 0

    for i until 0 by n begin
        var u <- minDistance(dist, visited)

        visited[u] <- true

        for v until 0 by n begin
            if (not(visited[v] and graph[u,v] and dist[u] != INF and (dist[u] + graph[u,v] < dist[v]))) begin
                dist[v] <- dist[u] + graph[u,v]
            end
        end
    end

    printSolution(dist)
end
"""
		expect = """Program([FuncDecl(Id(dijkstra), [VarDecl(Id(graph), NumberType, None, None), VarDecl(Id(src), NumberType, None, None)], Block([VarDecl(Id(n), None, var, CallExpr(Id(size), [Id(graph)])), VarDecl(Id(dist), None, var, ArrayLit(Id(n))), VarDecl(Id(visited), None, var, ArrayLit(Id(n))), For(Id(i), NumLit(0.0), Id(n), Block([AssignStmt(ArrayCell(Id(dist), [Id(i)]), Id(INF)), AssignStmt(ArrayCell(Id(visited), [Id(i)]), BooleanLit(False))])), AssignStmt(ArrayCell(Id(dist), [Id(src)]), NumLit(0.0)), For(Id(i), NumLit(0.0), Id(n), Block([VarDecl(Id(u), None, var, CallExpr(Id(minDistance), [Id(dist), Id(visited)])), AssignStmt(ArrayCell(Id(visited), [Id(u)]), BooleanLit(True)), For(Id(v), NumLit(0.0), Id(n), Block([If((UnaryOp(not, BinaryOp(!=, BinaryOp(and, BinaryOp(and, ArrayCell(Id(visited), [Id(v)]), ArrayCell(Id(graph), [Id(u), Id(v)])), ArrayCell(Id(dist), [Id(u)])), BinaryOp(and, Id(INF), BinaryOp(<, BinaryOp(+, ArrayCell(Id(dist), [Id(u)]), ArrayCell(Id(graph), [Id(u), Id(v)])), ArrayCell(Id(dist), [Id(v)]))))), Block([AssignStmt(ArrayCell(Id(dist), [Id(v)]), BinaryOp(+, ArrayCell(Id(dist), [Id(u)]), ArrayCell(Id(graph), [Id(u), Id(v)])))])), [], None)]))])), CallStmt(Id(printSolution), [Id(dist)])]))])"""
		self.assertTrue(TestAST.test(input, expect, 360))
	def test_361(self):
		input = """## bellman-ford
  		## Note: This is a simplified version of the Bellman-Ford algorithm for demonstration purposes.
## It assumes that the graph is represented as an adjacency matrix 'graph' and that
## all edges have positive weights. The function returns the shortest path from the
## source node to all other nodes in the graph.

func bellmanFord(number graph,number src) begin
    var n <- size(graph)
    var dist <- [n]

    for i until 0 by n begin
        dist[i] <- INF
    end

    dist[src] <- 0

    for i until 0 by n - 1 begin
        for u until 0 by n begin
            for v until 0 by n begin
                if (dist[u] != INF and graph[u,v] and (dist[u] + graph[u,v] < dist[v])) begin
                    dist[v] <- dist[u] + graph[u,v]
                end
            end
        end
    end

    for u until 0 by n begin
        for v until 0 by n begin
            if (dist[u] != INF and graph[u,v] and (dist[u] + graph[u,v] < dist[v])) begin
                print("Graph contains a negative weight cycle")
                return
            end
        end
    end

    printSolution(dist)
end

"""
		expect = """Program([FuncDecl(Id(bellmanFord), [VarDecl(Id(graph), NumberType, None, None), VarDecl(Id(src), NumberType, None, None)], Block([VarDecl(Id(n), None, var, CallExpr(Id(size), [Id(graph)])), VarDecl(Id(dist), None, var, ArrayLit(Id(n))), For(Id(i), NumLit(0.0), Id(n), Block([AssignStmt(ArrayCell(Id(dist), [Id(i)]), Id(INF))])), AssignStmt(ArrayCell(Id(dist), [Id(src)]), NumLit(0.0)), For(Id(i), NumLit(0.0), BinaryOp(-, Id(n), NumLit(1.0)), Block([For(Id(u), NumLit(0.0), Id(n), Block([For(Id(v), NumLit(0.0), Id(n), Block([If((BinaryOp(!=, ArrayCell(Id(dist), [Id(u)]), BinaryOp(and, BinaryOp(and, Id(INF), ArrayCell(Id(graph), [Id(u), Id(v)])), BinaryOp(<, BinaryOp(+, ArrayCell(Id(dist), [Id(u)]), ArrayCell(Id(graph), [Id(u), Id(v)])), ArrayCell(Id(dist), [Id(v)])))), Block([AssignStmt(ArrayCell(Id(dist), [Id(v)]), BinaryOp(+, ArrayCell(Id(dist), [Id(u)]), ArrayCell(Id(graph), [Id(u), Id(v)])))])), [], None)]))]))])), For(Id(u), NumLit(0.0), Id(n), Block([For(Id(v), NumLit(0.0), Id(n), Block([If((BinaryOp(!=, ArrayCell(Id(dist), [Id(u)]), BinaryOp(and, BinaryOp(and, Id(INF), ArrayCell(Id(graph), [Id(u), Id(v)])), BinaryOp(<, BinaryOp(+, ArrayCell(Id(dist), [Id(u)]), ArrayCell(Id(graph), [Id(u), Id(v)])), ArrayCell(Id(dist), [Id(v)])))), Block([CallStmt(Id(print), [StringLit(Graph contains a negative weight cycle)]), Return()])), [], None)]))])), CallStmt(Id(printSolution), [Id(dist)])]))])"""
		self.assertTrue(TestAST.test(input, expect, 361))
	def test_362(self):
		input = """### vetex coloring
  		## Note: This is a simplified version of a vertex coloring algorithm for demonstration purposes.
## It assigns colors to vertices of a graph such that no two adjacent vertices share the same color.

func coloring(number graph) begin
    var n <- size(graph)
    var color <- [n]

    for i until 0 by n begin
        color[i] <- -1
    end

    color[0] <- 0

    for u until 1 by n begin
        for v until 0 by u begin
            if (graph[u,v] and color[u] == color[v]) begin
                color[u] <- color[u] + 1
            end
        end
    end

    printSolution(color)
end

"""
		expect = """Program([FuncDecl(Id(coloring), [VarDecl(Id(graph), NumberType, None, None)], Block([VarDecl(Id(n), None, var, CallExpr(Id(size), [Id(graph)])), VarDecl(Id(color), None, var, ArrayLit(Id(n))), For(Id(i), NumLit(0.0), Id(n), Block([AssignStmt(ArrayCell(Id(color), [Id(i)]), UnaryOp(-, NumLit(1.0)))])), AssignStmt(ArrayCell(Id(color), [NumLit(0.0)]), NumLit(0.0)), For(Id(u), NumLit(1.0), Id(n), Block([For(Id(v), NumLit(0.0), Id(u), Block([If((BinaryOp(==, BinaryOp(and, ArrayCell(Id(graph), [Id(u), Id(v)]), ArrayCell(Id(color), [Id(u)])), ArrayCell(Id(color), [Id(v)])), Block([AssignStmt(ArrayCell(Id(color), [Id(u)]), BinaryOp(+, ArrayCell(Id(color), [Id(u)]), NumLit(1.0)))])), [], None)]))])), CallStmt(Id(printSolution), [Id(color)])]))])"""
		self.assertTrue(TestAST.test(input, expect, 362))
	def test_363(self):
		input = """### interpolation sort
  ## Note: This is a simplified version of the interpolation sort algorithm for demonstration purposes.
## It assumes that the input is an array 'arr' of n uniformly distributed values.

func interpolationSort(number arr) begin
    var n <- size(arr)

    for i until 0 by n - 1 begin
        var key <- arr[i]
        var j <- i - 1

        

        arr[j + 1] <- key
    end

    printSolution(arr)
end
"""
		expect = """Program([FuncDecl(Id(interpolationSort), [VarDecl(Id(arr), NumberType, None, None)], Block([VarDecl(Id(n), None, var, CallExpr(Id(size), [Id(arr)])), For(Id(i), NumLit(0.0), BinaryOp(-, Id(n), NumLit(1.0)), Block([VarDecl(Id(key), None, var, ArrayCell(Id(arr), [Id(i)])), VarDecl(Id(j), None, var, BinaryOp(-, Id(i), NumLit(1.0))), AssignStmt(ArrayCell(Id(arr), [BinaryOp(+, Id(j), NumLit(1.0))]), Id(key))])), CallStmt(Id(printSolution), [Id(arr)])]))])"""
		self.assertTrue(TestAST.test(input, expect,363))
	def test_364(self):
		input = """### radix sort
		## Note: This is a simplified version of the radix sort algorithm for demonstration purposes.
## It assumes that the input is an array 'arr' of n integers.

func radixsort(number arr) begin
    var n <- size(arr)
    var m <- getMax(arr, n)

    for exp until 1 by m / exp > 0 begin
        countSort(arr, n, exp)
    end

    printSolution(arr)
end

  		"""
		expect = """Program([FuncDecl(Id(radixsort), [VarDecl(Id(arr), NumberType, None, None)], Block([VarDecl(Id(n), None, var, CallExpr(Id(size), [Id(arr)])), VarDecl(Id(m), None, var, CallExpr(Id(getMax), [Id(arr), Id(n)])), For(Id(exp), NumLit(1.0), BinaryOp(>, BinaryOp(/, Id(m), Id(exp)), NumLit(0.0)), Block([CallStmt(Id(countSort), [Id(arr), Id(n), Id(exp)])])), CallStmt(Id(printSolution), [Id(arr)])]))])"""
		self.assertTrue(TestAST.test(input, expect, 364))

	def test_365(self):
		input = '''
func deM0 (number t2[4.64], string pkJ[24.64])
	return true

number zJ6 <- "kraVT"
'''
		expect = '''Program([FuncDecl(Id(deM0), [VarDecl(Id(t2), ArrayType([4.64], NumberType), None, None), VarDecl(Id(pkJ), ArrayType([24.64], StringType), None, None)], Return(BooleanLit(True))), VarDecl(Id(zJ6), NumberType, None, StringLit(kraVT))])'''
		self.assertTrue(TestAST.test(input, expect, 365))

	def test_366(self):
		input = '''
func IYB (number VOhK[23.59,13.82])
	return "pGAha"

string d9
func TgA (bool mp)	begin
		begin
			if (false) if (true) if ("wIZg") if (true)
			f1N4(true, pfsO, "uEu")
			elif ("NIp") dynamic fk
			elif (uo2)
			for wmBT until 92.11 by true
				if (false) break
				elif (55.28) As("vl", true)
				elif ("vxYJO")
				break
				elif (false) if ("m")
				for im1 until 60.89 by "nqLwc"
					begin
					end
				elif (false)
				for mHD until false by 38.01
					TY <- "XeUS"
				elif ("TtPPA")
				continue
				elif (true) continue
				elif ("ZFzN") break
				elif (true) for yag until false by sBe
					begin
					end
			elif ("N")
			continue
			elif (false)
			break
			elif (true) begin
				if (zN)
				mYro <- false
				elif (51.14) ODSj()
				elif (false) if (SdCf) break
				elif ("bMhR")
				continue
				elif (true)
				if (true)
				ngP2(true)
				elif (27.35) if (ZZ)
				return "IsRIw"
				elif (true)
				begin
					Qy[95.6, false] <- true
				end
				elif (Dip)
				continue
				elif ("a")
				return false
				elif (67.76) for Dc until 69.71 by 63.42
					Bgr <- "qX"
				elif (false) break
				else break
				else break
				else string B_ <- true
				bool Zo5[26.39,17.71,18.61]
			end
			elif (false)
			begin
				return
			end
			elif (false) return
			elif ("i")
			if ("SEtS")
			begin
				C02(pjg4, 67.7)
				kZXB(PhX)
				QuL2(false, "dfN")
			end
			elif (true) break
			else dynamic ndjB
			elif (82.45)
			break
			else string b0W
		end
		return true
		bool m_[48.45]
	end
string YNa7
'''
		expect = '''Program([FuncDecl(Id(IYB), [VarDecl(Id(VOhK), ArrayType([23.59, 13.82], NumberType), None, None)], Return(StringLit(pGAha))), VarDecl(Id(d9), StringType, None, None), FuncDecl(Id(TgA), [VarDecl(Id(mp), BoolType, None, None)], Block([Block([If((BooleanLit(False), If((BooleanLit(True), If((StringLit(wIZg), If((BooleanLit(True), CallStmt(Id(f1N4), [BooleanLit(True), Id(pfsO), StringLit(uEu)])), [(StringLit(NIp), VarDecl(Id(fk), None, dynamic, None)), (Id(uo2), For(Id(wmBT), NumLit(92.11), BooleanLit(True), If((BooleanLit(False), Break), [(NumLit(55.28), CallStmt(Id(As), [StringLit(vl), BooleanLit(True)])), (StringLit(vxYJO), Break), (BooleanLit(False), If((StringLit(m), For(Id(im1), NumLit(60.89), StringLit(nqLwc), Block([]))), [(BooleanLit(False), For(Id(mHD), BooleanLit(False), NumLit(38.01), AssignStmt(Id(TY), StringLit(XeUS)))), (StringLit(TtPPA), Continue), (BooleanLit(True), Continue), (StringLit(ZFzN), Break), (BooleanLit(True), For(Id(yag), BooleanLit(False), Id(sBe), Block([]))), (StringLit(N), Continue), (BooleanLit(False), Break), (BooleanLit(True), Block([If((Id(zN), AssignStmt(Id(mYro), BooleanLit(False))), [(NumLit(51.14), CallStmt(Id(ODSj), [])), (BooleanLit(False), If((Id(SdCf), Break), [(StringLit(bMhR), Continue), (BooleanLit(True), If((BooleanLit(True), CallStmt(Id(ngP2), [BooleanLit(True)])), [(NumLit(27.35), If((Id(ZZ), Return(StringLit(IsRIw))), [(BooleanLit(True), Block([AssignStmt(ArrayCell(Id(Qy), [NumLit(95.6), BooleanLit(False)]), BooleanLit(True))])), (Id(Dip), Continue), (StringLit(a), Return(BooleanLit(False))), (NumLit(67.76), For(Id(Dc), NumLit(69.71), NumLit(63.42), AssignStmt(Id(Bgr), StringLit(qX)))), (BooleanLit(False), Break)], Break))], Break))], VarDecl(Id(B_), StringType, None, BooleanLit(True))))], None), VarDecl(Id(Zo5), ArrayType([26.39, 17.71, 18.61], BoolType), None, None)])), (BooleanLit(False), Block([Return()])), (BooleanLit(False), Return()), (StringLit(i), If((StringLit(SEtS), Block([CallStmt(Id(C02), [Id(pjg4), NumLit(67.7)]), CallStmt(Id(kZXB), [Id(PhX)]), CallStmt(Id(QuL2), [BooleanLit(False), StringLit(dfN)])])), [(BooleanLit(True), Break)], VarDecl(Id(ndjB), None, dynamic, None))), (NumLit(82.45), Break)], VarDecl(Id(b0W), StringType, None, None)))], None)))], None)), [], None)), [], None)), [], None)]), Return(BooleanLit(True)), VarDecl(Id(m_), ArrayType([48.45], BoolType), None, None)])), VarDecl(Id(YNa7), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 366))

	def test_367(self):
		input = '''
func ve ()	return SI6

func wm (number pMp)
	begin
	end

string Mpv
func pl05 (bool D3_)	return

'''
		expect = '''Program([FuncDecl(Id(ve), [], Return(Id(SI6))), FuncDecl(Id(wm), [VarDecl(Id(pMp), NumberType, None, None)], Block([])), VarDecl(Id(Mpv), StringType, None, None), FuncDecl(Id(pl05), [VarDecl(Id(D3_), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 367))

	def test_368(self):
		input = '''
func c_ (bool b_oW[94.1])	begin
		for qBXN until 20.52 by "vNO"
			return 40.56
		continue
	end
string fvk[29.58,54.34,46.9]
'''
		expect = '''Program([FuncDecl(Id(c_), [VarDecl(Id(b_oW), ArrayType([94.1], BoolType), None, None)], Block([For(Id(qBXN), NumLit(20.52), StringLit(vNO), Return(NumLit(40.56))), Continue])), VarDecl(Id(fvk), ArrayType([29.58, 54.34, 46.9], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 368))

	def test_369(self):
		input = '''
func ws (bool tyhO[29.98,50.47])
	begin
		return
		UUfd(bBU)
		begin
		end
	end
func Pj (number waa[74.92])
	return
func DU ()
	begin
		string DiW[66.3,4.28]
	end

number d4 <- DvGy
func G7H (string NP3[77.98,82.98,23.87], number eHZ)	begin
	end

'''
		expect = '''Program([FuncDecl(Id(ws), [VarDecl(Id(tyhO), ArrayType([29.98, 50.47], BoolType), None, None)], Block([Return(), CallStmt(Id(UUfd), [Id(bBU)]), Block([])])), FuncDecl(Id(Pj), [VarDecl(Id(waa), ArrayType([74.92], NumberType), None, None)], Return()), FuncDecl(Id(DU), [], Block([VarDecl(Id(DiW), ArrayType([66.3, 4.28], StringType), None, None)])), VarDecl(Id(d4), NumberType, None, Id(DvGy)), FuncDecl(Id(G7H), [VarDecl(Id(NP3), ArrayType([77.98, 82.98, 23.87], StringType), None, None), VarDecl(Id(eHZ), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 369))

	def test_370(self):
		input = '''
func L9 (string p0[31.86])
	return

func WY (number Vgce[54.96,51.09,73.79], number lseH, bool Neyb[70.64])	return Lta
'''
		expect = '''Program([FuncDecl(Id(L9), [VarDecl(Id(p0), ArrayType([31.86], StringType), None, None)], Return()), FuncDecl(Id(WY), [VarDecl(Id(Vgce), ArrayType([54.96, 51.09, 73.79], NumberType), None, None), VarDecl(Id(lseH), NumberType, None, None), VarDecl(Id(Neyb), ArrayType([70.64], BoolType), None, None)], Return(Id(Lta)))])'''
		self.assertTrue(TestAST.test(input, expect, 370))

	def test_371(self):
		input = '''
string Mw <- Urzm
number Jj[36.37,55.72]
'''
		expect = '''Program([VarDecl(Id(Mw), StringType, None, Id(Urzm)), VarDecl(Id(Jj), ArrayType([36.37, 55.72], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 371))

	def test_372(self):
		input = '''
dynamic XRKi
'''
		expect = '''Program([VarDecl(Id(XRKi), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 372))

	def test_373(self):
		input = '''
number sQK4 <- "OPpPH"
func XKbn (string xBZF[8.23,62.09,11.41], number Wo_[86.66])	return

string nN_p[35.4]
string ag8i <- false
number tlkY[5.83,95.14,10.19] <- "cwZ"
'''
		expect = '''Program([VarDecl(Id(sQK4), NumberType, None, StringLit(OPpPH)), FuncDecl(Id(XKbn), [VarDecl(Id(xBZF), ArrayType([8.23, 62.09, 11.41], StringType), None, None), VarDecl(Id(Wo_), ArrayType([86.66], NumberType), None, None)], Return()), VarDecl(Id(nN_p), ArrayType([35.4], StringType), None, None), VarDecl(Id(ag8i), StringType, None, BooleanLit(False)), VarDecl(Id(tlkY), ArrayType([5.83, 95.14, 10.19], NumberType), None, StringLit(cwZ))])'''
		self.assertTrue(TestAST.test(input, expect, 373))

	def test_374(self):
		input = '''
string WxX <- 4.89
string MlAV[82.26,35.05]
bool aZd
'''
		expect = '''Program([VarDecl(Id(WxX), StringType, None, NumLit(4.89)), VarDecl(Id(MlAV), ArrayType([82.26, 35.05], StringType), None, None), VarDecl(Id(aZd), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 374))

	def test_375(self):
		input = '''
func BPKm ()
	begin
		if (false)
		FQSH()
		elif (true) continue
		elif (false)
		for ip until 47.28 by 6.76
			return 62.38
		else for NJW until "Y" by 42.0
			hl6[true, 50.94, Zh] <- C7vH
		string ADh
		for oO_7 until false by y5Yt
			l_b <- "Q"
	end
func Zicy (number Aata)	begin
		dynamic RuA <- "Ob"
		AI9K(true, wE, 9.66)
		kMDg("bS")
	end

func F_s (number Mc1B[36.82])	begin
	end

string oM
'''
		expect = '''Program([FuncDecl(Id(BPKm), [], Block([If((BooleanLit(False), CallStmt(Id(FQSH), [])), [(BooleanLit(True), Continue), (BooleanLit(False), For(Id(ip), NumLit(47.28), NumLit(6.76), Return(NumLit(62.38))))], For(Id(NJW), StringLit(Y), NumLit(42.0), AssignStmt(ArrayCell(Id(hl6), [BooleanLit(True), NumLit(50.94), Id(Zh)]), Id(C7vH)))), VarDecl(Id(ADh), StringType, None, None), For(Id(oO_7), BooleanLit(False), Id(y5Yt), AssignStmt(Id(l_b), StringLit(Q)))])), FuncDecl(Id(Zicy), [VarDecl(Id(Aata), NumberType, None, None)], Block([VarDecl(Id(RuA), None, dynamic, StringLit(Ob)), CallStmt(Id(AI9K), [BooleanLit(True), Id(wE), NumLit(9.66)]), CallStmt(Id(kMDg), [StringLit(bS)])])), FuncDecl(Id(F_s), [VarDecl(Id(Mc1B), ArrayType([36.82], NumberType), None, None)], Block([])), VarDecl(Id(oM), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 375))

	def test_376(self):
		input = '''
bool uhqU[1.91] <- true
bool JB
number fjA[95.94]
func LGi (string OH[79.52], bool rpsQ, string Nmg[18.3])	return
'''
		expect = '''Program([VarDecl(Id(uhqU), ArrayType([1.91], BoolType), None, BooleanLit(True)), VarDecl(Id(JB), BoolType, None, None), VarDecl(Id(fjA), ArrayType([95.94], NumberType), None, None), FuncDecl(Id(LGi), [VarDecl(Id(OH), ArrayType([79.52], StringType), None, None), VarDecl(Id(rpsQ), BoolType, None, None), VarDecl(Id(Nmg), ArrayType([18.3], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 376))

	def test_377(self):
		input = '''
func kg1 (bool KJ4[38.65,17.0], string oKDU)	return 33.2

func Q9b (number qcw[79.03,23.03,4.59], bool MZ6[64.11,51.25,65.24], string r3d1[63.46,37.26])
	return "ps"

func uq5h (number gKDy)
	return true
bool pq <- 95.78
number czD
'''
		expect = '''Program([FuncDecl(Id(kg1), [VarDecl(Id(KJ4), ArrayType([38.65, 17.0], BoolType), None, None), VarDecl(Id(oKDU), StringType, None, None)], Return(NumLit(33.2))), FuncDecl(Id(Q9b), [VarDecl(Id(qcw), ArrayType([79.03, 23.03, 4.59], NumberType), None, None), VarDecl(Id(MZ6), ArrayType([64.11, 51.25, 65.24], BoolType), None, None), VarDecl(Id(r3d1), ArrayType([63.46, 37.26], StringType), None, None)], Return(StringLit(ps))), FuncDecl(Id(uq5h), [VarDecl(Id(gKDy), NumberType, None, None)], Return(BooleanLit(True))), VarDecl(Id(pq), BoolType, None, NumLit(95.78)), VarDecl(Id(czD), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 377))

	def test_378(self):
		input = '''
func nD (bool Xs[18.75,73.83,53.11])
	begin
	end
func JX1 (string NnK, number xrtk, number wd[13.33,61.42,40.63])
	begin
		if (VP) DPA2(NA0, 20.77, true)
		else zbbW()
	end

string PlT[58.11,98.6,53.91] <- false
'''
		expect = '''Program([FuncDecl(Id(nD), [VarDecl(Id(Xs), ArrayType([18.75, 73.83, 53.11], BoolType), None, None)], Block([])), FuncDecl(Id(JX1), [VarDecl(Id(NnK), StringType, None, None), VarDecl(Id(xrtk), NumberType, None, None), VarDecl(Id(wd), ArrayType([13.33, 61.42, 40.63], NumberType), None, None)], Block([If((Id(VP), CallStmt(Id(DPA2), [Id(NA0), NumLit(20.77), BooleanLit(True)])), [], CallStmt(Id(zbbW), []))])), VarDecl(Id(PlT), ArrayType([58.11, 98.6, 53.91], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 378))

	def test_379(self):
		input = '''
func qMG (string Sd, string zTu[57.95,41.88,23.7], string OsnQ)	return 37.14

'''
		expect = '''Program([FuncDecl(Id(qMG), [VarDecl(Id(Sd), StringType, None, None), VarDecl(Id(zTu), ArrayType([57.95, 41.88, 23.7], StringType), None, None), VarDecl(Id(OsnQ), StringType, None, None)], Return(NumLit(37.14)))])'''
		self.assertTrue(TestAST.test(input, expect, 379))

	def test_380(self):
		input = '''
dynamic r_
'''
		expect = '''Program([VarDecl(Id(r_), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 380))

	def test_381(self):
		input = '''
func gN4 (string p6, number X2, string QT)	return

number I9a[12.02,2.28,21.09] <- true
func VYg (bool mD[37.16])
	return
'''
		expect = '''Program([FuncDecl(Id(gN4), [VarDecl(Id(p6), StringType, None, None), VarDecl(Id(X2), NumberType, None, None), VarDecl(Id(QT), StringType, None, None)], Return()), VarDecl(Id(I9a), ArrayType([12.02, 2.28, 21.09], NumberType), None, BooleanLit(True)), FuncDecl(Id(VYg), [VarDecl(Id(mD), ArrayType([37.16], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 381))

	def test_382(self):
		input = '''
func FyCf (bool eO, number oMSj)	return true

func LGJ (string pcKx[5.33,68.0,2.49])	return Yx
'''
		expect = '''Program([FuncDecl(Id(FyCf), [VarDecl(Id(eO), BoolType, None, None), VarDecl(Id(oMSj), NumberType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(LGJ), [VarDecl(Id(pcKx), ArrayType([5.33, 68.0, 2.49], StringType), None, None)], Return(Id(Yx)))])'''
		self.assertTrue(TestAST.test(input, expect, 382))

	def test_383(self):
		input = '''
string wlj
number uHaX[36.22]
'''
		expect = '''Program([VarDecl(Id(wlj), StringType, None, None), VarDecl(Id(uHaX), ArrayType([36.22], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 383))

	def test_384(self):
		input = '''
string yU9[52.15] <- "ld"
func jRKu (number JF[70.09,42.6], number pA[5.69,28.44])	begin
		qp0v()
		if (hz)
		Qr9(78.45, "FauNH")
		elif ("YOxXn") U6("foOC", 70.32, 84.89)
		elif ("omGl")
		bool M5EK
		elif (56.34)
		dynamic HWhJ
		else begin
			bool L7
			return
			for aat until true by "nAY"
				X42[Tc] <- d7tf
		end
	end
string efB
func ZTnV (number N5vK)	begin
		ZtI("OfERc", "Ag")
		begin
			number Qf[68.54,10.5,20.75] <- 97.81
			for QRYe until false by false
				mf("u")
		end
		break
	end

string w9p <- RYm
'''
		expect = '''Program([VarDecl(Id(yU9), ArrayType([52.15], StringType), None, StringLit(ld)), FuncDecl(Id(jRKu), [VarDecl(Id(JF), ArrayType([70.09, 42.6], NumberType), None, None), VarDecl(Id(pA), ArrayType([5.69, 28.44], NumberType), None, None)], Block([CallStmt(Id(qp0v), []), If((Id(hz), CallStmt(Id(Qr9), [NumLit(78.45), StringLit(FauNH)])), [(StringLit(YOxXn), CallStmt(Id(U6), [StringLit(foOC), NumLit(70.32), NumLit(84.89)])), (StringLit(omGl), VarDecl(Id(M5EK), BoolType, None, None)), (NumLit(56.34), VarDecl(Id(HWhJ), None, dynamic, None))], Block([VarDecl(Id(L7), BoolType, None, None), Return(), For(Id(aat), BooleanLit(True), StringLit(nAY), AssignStmt(ArrayCell(Id(X42), [Id(Tc)]), Id(d7tf)))]))])), VarDecl(Id(efB), StringType, None, None), FuncDecl(Id(ZTnV), [VarDecl(Id(N5vK), NumberType, None, None)], Block([CallStmt(Id(ZtI), [StringLit(OfERc), StringLit(Ag)]), Block([VarDecl(Id(Qf), ArrayType([68.54, 10.5, 20.75], NumberType), None, NumLit(97.81)), For(Id(QRYe), BooleanLit(False), BooleanLit(False), CallStmt(Id(mf), [StringLit(u)]))]), Break])), VarDecl(Id(w9p), StringType, None, Id(RYm))])'''
		self.assertTrue(TestAST.test(input, expect, 384))

	def test_385(self):
		input = '''
func sD6 (number pbGY, bool ge)	begin
		bool WHtu[44.78,3.43]
		for XM until true by 26.89
			string Hf
	end

func FNeX (string Yib[55.03,3.34], number jD)	return
func RB_ (bool k9X)
	begin
		BJ <- rKQV
		continue
		continue
	end

bool wFA <- true
var zrw <- 61.64
'''
		expect = '''Program([FuncDecl(Id(sD6), [VarDecl(Id(pbGY), NumberType, None, None), VarDecl(Id(ge), BoolType, None, None)], Block([VarDecl(Id(WHtu), ArrayType([44.78, 3.43], BoolType), None, None), For(Id(XM), BooleanLit(True), NumLit(26.89), VarDecl(Id(Hf), StringType, None, None))])), FuncDecl(Id(FNeX), [VarDecl(Id(Yib), ArrayType([55.03, 3.34], StringType), None, None), VarDecl(Id(jD), NumberType, None, None)], Return()), FuncDecl(Id(RB_), [VarDecl(Id(k9X), BoolType, None, None)], Block([AssignStmt(Id(BJ), Id(rKQV)), Continue, Continue])), VarDecl(Id(wFA), BoolType, None, BooleanLit(True)), VarDecl(Id(zrw), None, var, NumLit(61.64))])'''
		self.assertTrue(TestAST.test(input, expect, 385))

	def test_386(self):
		input = '''
func cR ()
	return 58.21

number Yecv <- "NBn"
func Qn6 ()	return

func oVv (number vLnr[38.28], number IO[66.6,66.27,28.83])	return 47.88

func mU4 (bool Swh, bool OT0, number tcY[0.91])
	return "GfBp"

'''
		expect = '''Program([FuncDecl(Id(cR), [], Return(NumLit(58.21))), VarDecl(Id(Yecv), NumberType, None, StringLit(NBn)), FuncDecl(Id(Qn6), [], Return()), FuncDecl(Id(oVv), [VarDecl(Id(vLnr), ArrayType([38.28], NumberType), None, None), VarDecl(Id(IO), ArrayType([66.6, 66.27, 28.83], NumberType), None, None)], Return(NumLit(47.88))), FuncDecl(Id(mU4), [VarDecl(Id(Swh), BoolType, None, None), VarDecl(Id(OT0), BoolType, None, None), VarDecl(Id(tcY), ArrayType([0.91], NumberType), None, None)], Return(StringLit(GfBp)))])'''
		self.assertTrue(TestAST.test(input, expect, 386))

	def test_387(self):
		input = '''
bool NKJ[44.43,1.37] <- ocK9
string DWP[29.73] <- 49.25
string iU74[78.29,92.04]
'''
		expect = '''Program([VarDecl(Id(NKJ), ArrayType([44.43, 1.37], BoolType), None, Id(ocK9)), VarDecl(Id(DWP), ArrayType([29.73], StringType), None, NumLit(49.25)), VarDecl(Id(iU74), ArrayType([78.29, 92.04], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 387))

	def test_388(self):
		input = '''
func uWG (string LmL[62.38,30.26,47.2])	return true
func N7 (string BLj)
	return
number P5
dynamic QZ <- LZG
func se (string Gw8w[85.11,36.47])	begin
		begin
			Vqt()
			string HsbK[60.49,82.43]
		end
	end
'''
		expect = '''Program([FuncDecl(Id(uWG), [VarDecl(Id(LmL), ArrayType([62.38, 30.26, 47.2], StringType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(N7), [VarDecl(Id(BLj), StringType, None, None)], Return()), VarDecl(Id(P5), NumberType, None, None), VarDecl(Id(QZ), None, dynamic, Id(LZG)), FuncDecl(Id(se), [VarDecl(Id(Gw8w), ArrayType([85.11, 36.47], StringType), None, None)], Block([Block([CallStmt(Id(Vqt), []), VarDecl(Id(HsbK), ArrayType([60.49, 82.43], StringType), None, None)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 388))

	def test_389(self):
		input = '''
number Xq[57.55,42.74]
bool jG[34.27,63.93,27.55] <- "aq"
func Pz (string GqE, bool nQ, number X3[42.31])
	return
'''
		expect = '''Program([VarDecl(Id(Xq), ArrayType([57.55, 42.74], NumberType), None, None), VarDecl(Id(jG), ArrayType([34.27, 63.93, 27.55], BoolType), None, StringLit(aq)), FuncDecl(Id(Pz), [VarDecl(Id(GqE), StringType, None, None), VarDecl(Id(nQ), BoolType, None, None), VarDecl(Id(X3), ArrayType([42.31], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 389))

	def test_390(self):
		input = '''
bool Bi[11.84,21.66,87.57] <- o2
number C3xU[45.45] <- true
func mEai (number Yyv_, bool ZE[76.55,28.61], number c5[20.41,18.17])	begin
	end

func xmdp ()
	begin
		for FbLf until 55.13 by false
			return "o"
		string Asq[96.25]
		ELF5[28.56, false] <- 96.74
	end
'''
		expect = '''Program([VarDecl(Id(Bi), ArrayType([11.84, 21.66, 87.57], BoolType), None, Id(o2)), VarDecl(Id(C3xU), ArrayType([45.45], NumberType), None, BooleanLit(True)), FuncDecl(Id(mEai), [VarDecl(Id(Yyv_), NumberType, None, None), VarDecl(Id(ZE), ArrayType([76.55, 28.61], BoolType), None, None), VarDecl(Id(c5), ArrayType([20.41, 18.17], NumberType), None, None)], Block([])), FuncDecl(Id(xmdp), [], Block([For(Id(FbLf), NumLit(55.13), BooleanLit(False), Return(StringLit(o))), VarDecl(Id(Asq), ArrayType([96.25], StringType), None, None), AssignStmt(ArrayCell(Id(ELF5), [NumLit(28.56), BooleanLit(False)]), NumLit(96.74))]))])'''
		self.assertTrue(TestAST.test(input, expect, 390))

	def test_391(self):
		input = '''
func z8r (bool JV, bool LhlT[39.83,71.01])	return XBYr

func JtfO (string ssd[73.64], number ODaE, number u6)
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(z8r), [VarDecl(Id(JV), BoolType, None, None), VarDecl(Id(LhlT), ArrayType([39.83, 71.01], BoolType), None, None)], Return(Id(XBYr))), FuncDecl(Id(JtfO), [VarDecl(Id(ssd), ArrayType([73.64], StringType), None, None), VarDecl(Id(ODaE), NumberType, None, None), VarDecl(Id(u6), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 391))

	def test_392(self):
		input = '''
dynamic F_0b
func kHN (number g9, number na[69.03], string Yk[80.8,47.73])	return B0

'''
		expect = '''Program([VarDecl(Id(F_0b), None, dynamic, None), FuncDecl(Id(kHN), [VarDecl(Id(g9), NumberType, None, None), VarDecl(Id(na), ArrayType([69.03], NumberType), None, None), VarDecl(Id(Yk), ArrayType([80.8, 47.73], StringType), None, None)], Return(Id(B0)))])'''
		self.assertTrue(TestAST.test(input, expect, 392))

	def test_393(self):
		input = '''
number ez[6.36] <- Cu
bool MET[58.38]
dynamic vTBf <- false
number KA[33.96]
'''
		expect = '''Program([VarDecl(Id(ez), ArrayType([6.36], NumberType), None, Id(Cu)), VarDecl(Id(MET), ArrayType([58.38], BoolType), None, None), VarDecl(Id(vTBf), None, dynamic, BooleanLit(False)), VarDecl(Id(KA), ArrayType([33.96], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 393))

	def test_394(self):
		input = '''
func IRxe (number o_1[79.02,53.42])	begin
	end

string wAz[28.39] <- 94.39
func q3 (bool IqAt, number R2Z[4.81,99.81])
	return

bool wWh[24.33] <- false
bool ayF[26.01] <- "cdvQ"
'''
		expect = '''Program([FuncDecl(Id(IRxe), [VarDecl(Id(o_1), ArrayType([79.02, 53.42], NumberType), None, None)], Block([])), VarDecl(Id(wAz), ArrayType([28.39], StringType), None, NumLit(94.39)), FuncDecl(Id(q3), [VarDecl(Id(IqAt), BoolType, None, None), VarDecl(Id(R2Z), ArrayType([4.81, 99.81], NumberType), None, None)], Return()), VarDecl(Id(wWh), ArrayType([24.33], BoolType), None, BooleanLit(False)), VarDecl(Id(ayF), ArrayType([26.01], BoolType), None, StringLit(cdvQ))])'''
		self.assertTrue(TestAST.test(input, expect, 394))

	def test_395(self):
		input = '''
func sd3 (number fY)	return
'''
		expect = '''Program([FuncDecl(Id(sd3), [VarDecl(Id(fY), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 395))

	def test_396(self):
		input = '''
func SE ()	begin
	end
func ju (number mywf[71.3,50.96], number pUXx[3.81], string GfC[93.32,8.58])
	return 96.1

func ngKb (bool IlM[73.44,27.92,86.86], number tC[37.27,43.19,87.39], bool Lj[19.35,13.68,84.9])
	begin
		if ("na") bool dj0 <- fO
		elif (false) continue
		elif (89.88)
		ZZE <- 57.0
		elif (wJiD) bool A4vc[13.17,52.1]
		else break
	end
string oZ <- lks
number jfr[31.68,83.4]
'''
		expect = '''Program([FuncDecl(Id(SE), [], Block([])), FuncDecl(Id(ju), [VarDecl(Id(mywf), ArrayType([71.3, 50.96], NumberType), None, None), VarDecl(Id(pUXx), ArrayType([3.81], NumberType), None, None), VarDecl(Id(GfC), ArrayType([93.32, 8.58], StringType), None, None)], Return(NumLit(96.1))), FuncDecl(Id(ngKb), [VarDecl(Id(IlM), ArrayType([73.44, 27.92, 86.86], BoolType), None, None), VarDecl(Id(tC), ArrayType([37.27, 43.19, 87.39], NumberType), None, None), VarDecl(Id(Lj), ArrayType([19.35, 13.68, 84.9], BoolType), None, None)], Block([If((StringLit(na), VarDecl(Id(dj0), BoolType, None, Id(fO))), [(BooleanLit(False), Continue), (NumLit(89.88), AssignStmt(Id(ZZE), NumLit(57.0))), (Id(wJiD), VarDecl(Id(A4vc), ArrayType([13.17, 52.1], BoolType), None, None))], Break)])), VarDecl(Id(oZ), StringType, None, Id(lks)), VarDecl(Id(jfr), ArrayType([31.68, 83.4], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 396))

	def test_397(self):
		input = '''
number UZw6[31.14]
number gsD[89.46,15.75,75.86] <- "LX"
func mvYm (number XNl)
	begin
		vnQ(false, false, 27.97)
		kSzK <- 13.56
		continue
	end

func xJds (number cz[92.33], string Nlxa[64.77], number BpF)
	begin
		continue
	end

'''
		expect = '''Program([VarDecl(Id(UZw6), ArrayType([31.14], NumberType), None, None), VarDecl(Id(gsD), ArrayType([89.46, 15.75, 75.86], NumberType), None, StringLit(LX)), FuncDecl(Id(mvYm), [VarDecl(Id(XNl), NumberType, None, None)], Block([CallStmt(Id(vnQ), [BooleanLit(False), BooleanLit(False), NumLit(27.97)]), AssignStmt(Id(kSzK), NumLit(13.56)), Continue])), FuncDecl(Id(xJds), [VarDecl(Id(cz), ArrayType([92.33], NumberType), None, None), VarDecl(Id(Nlxa), ArrayType([64.77], StringType), None, None), VarDecl(Id(BpF), NumberType, None, None)], Block([Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 397))

	def test_398(self):
		input = '''
string iJ_A <- 81.16
'''
		expect = '''Program([VarDecl(Id(iJ_A), StringType, None, NumLit(81.16))])'''
		self.assertTrue(TestAST.test(input, expect, 398))

	def test_399(self):
		input = '''
bool bX
bool fvaj[36.82,73.67] <- "WpS"
'''
		expect = '''Program([VarDecl(Id(bX), BoolType, None, None), VarDecl(Id(fvaj), ArrayType([36.82, 73.67], BoolType), None, StringLit(WpS))])'''
		self.assertTrue(TestAST.test(input, expect, 399))

	def test_400(self):
		input = '''
number FVg6[13.77,78.96,61.95]
'''
		expect = '''Program([VarDecl(Id(FVg6), ArrayType([13.77, 78.96, 61.95], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 400))
