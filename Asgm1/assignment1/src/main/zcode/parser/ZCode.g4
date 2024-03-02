// Student ID: 2152966

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// PARSER ////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////


program:		NEWLINE* declare_list EOF;
declare_list: 	declare declare_list | declare;
declare:		var_declare newlines | func_declare;

newlines:			NEWLINE newlines | NEWLINE;



// 7.1 Variable declaration -------------------------------------------------
var_declare: 	implicit_var | keyword_var | dynamic_var;

implicit_var:	VAR IDENTIFIER ASSIGN_OPS expr;
keyword_var:	typ IDENTIFIER (LSB numList_prime RSB)? (ASSIGN_OPS expr)?;
dynamic_var:	DYNAMIC IDENTIFIER (ASSIGN_OPS expr)?;


// Function declaration -----------------------------------------------------
func_declare:	FUNC IDENTIFIER LB paramList RB body;

paramList:		paramList_prime | ;
paramList_prime:param COMMA paramList_prime | param;
param:			typ IDENTIFIER (LSB numList_prime RSB)?;

body:			newlines? (return_stmt | block_stmt) | newlines;



// Expression ===================================================================================================
expr: 			expr_concat;

expr_concat:	expr_rela CONCAT_OPS expr_rela | expr_rela; 								// (1)
expr_rela:		expr_logic (EQS | EQ | NEQ | LT | LEQ | GT | GEQ) expr_logic | expr_logic;	// (2)
expr_logic: 	expr_logic (AND | OR) expr_add | expr_add;									// (3)

expr_add:		expr_add (ADD_OPS | SUB_OPS) expr_mul | expr_mul;							// (4)
expr_mul:		expr_mul (MUL_OPS | DIV_OPS | MOD_OPS) expr_not | expr_not;					// (5)

expr_not:  		NOT expr_not | expr_sign;											// (6)
expr_sign:		SUB_OPS expr_sign | expr_idx;												// (7)

expr_idx:		(IDENTIFIER | funcCall) LSB exprList_prime RSB | operand;					// (8) Index


operand: 		IDENTIFIER | literal | LB expr RB | funcCall;								// (9) Operands
funcCall:		IDENTIFIER LB argList RB;
literal:		NUM_LIT | STRING_LIT | BOOL_LIT | array_lit;

array_lit:		LSB exprList_prime RSB;




// 7 Statement --------------------------------------------------------------
stmt:			if_stmt
				|for_stmt
				| decl_stmt
				| assign_stmt
                | break_stmt
                | continue_stmt
				| return_stmt
                | funcCall_stmt
				| block_stmt
                ;



// 7.3 If statement
if_stmt:		(IF LB expr RB newlines? stmt) (elif_stmtList)? (else_stmt)?;

elif_stmtList:	elif_stmt elif_stmtList | elif_stmt;
elif_stmt:		ELIF LB expr RB newlines? stmt;

else_stmt:		ELSE newlines? stmt;


// 7.4 For statement
for_stmt:		FOR IDENTIFIER UNTIL expr BY expr newlines? stmt;


// 7.1 Variable  declaration statement
decl_stmt:		var_declare newlines;


// 7.2 Assignment statement
assign_stmt:	leftSide ASSIGN_OPS expr newlines;
leftSide:		IDENTIFIER (LSB exprList_prime RSB)?;


// 7.5 Break statement
break_stmt:		BREAK newlines;


// 7.6 Continue statement
continue_stmt:	CONTINUE newlines;


// 7.7 Return statement
return_stmt:	RETURN expr? newlines;


// 7.8 Function call statement
funcCall_stmt:	funcCall newlines;


// 7.9 Block statement
block_stmt: 	BEGIN newlines stmtList END newlines;




// Common syntax ================================================================================================
numList:		numList_prime | ;
numList_prime:	NUM_LIT COMMA numList_prime| NUM_LIT;

argList:		exprList;
exprList:		exprList_prime | ;
exprList_prime: expr COMMA exprList_prime | expr;

stmtList: 		stmtList_prime | ;
stmtList_prime:	stmt stmtList_prime | stmt;

// litList:		litList_prime | ;
// litList_prime:	literal COMMA litList_prime | literal;







//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// LEXER /////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// 4.0 Data Type
typ:			NUM_TYP | BOOL_TYP | STR_TYP;


// Declare
VAR: 			'var';
DYNAMIC: 		'dynamic';
ASSIGN_OPS: 	'<-';


// Function
FUNC:			'func';

// Statement
BEGIN:			'begin';
END:			'end';

RETURN:			'return';

FOR:			'for';
UNTIL:			'until';
BY:				'by';

BREAK:			'break';
CONTINUE:		'continue';

IF:				'if';
ELIF:			'elif';
ELSE:			'else';


// 3.6 Seperators
LB:				'(';
RB:				')';
LSB:			'[';
RSB:			']';
COMMA:			',';


// 4.1 Boolean Type Operators -----------------------------------------------
NOT:			'not';
AND:			'and';
OR:				'or';


// 4.2 Operators ------------------------------------------------------------
ADD_OPS: 		'+';
SUB_OPS:		'-';
MUL_OPS:		'*';
DIV_OPS:		'/';
MOD_OPS:     	'%';

CONCAT_OPS:		'...';

// 4.3 Relational Operators -------------------------------------------------
EQS:			'==';				// Equal string
NEQ:			'!=';				// Not Equal number
EQ:				'=';				// Equal number
LEQ:			'<=';				// Less or equal
GEQ:			'>=';				// Greater or equal
LT:				'<';				// Less than
GT:				'>';				// Greater than



// Boolean ------------------------------------------------------------------
BOOL_TYP:		'bool';				// Primitive
BOOL_LIT:		ZTrue | ZFalse;

fragment ZTrue:		'true';
fragment ZFalse:	'false';


// 3.7.1 Number -------------------------------------------------------------
NUM_TYP:		'number';			// Primitive
NUM_LIT:		Int Dec? Exp?;

fragment Int:	[0-9]+;
fragment Dec:	[.] [0-9]*;
fragment Exp:	[eE] [+-]? [0-9]+;


// 3.7.3 String -------------------------------------------------------------
STR_TYP:		'string';			// Primitive
STRING_LIT:		["] Str_Char* ["]  {self.text = self.text[1:-1]};

fragment Str_Char:	~[\r\n\\"] | Esc_Seq | [']["];
fragment Esc_Seq:	[\\] ['bfrnt\\];


// 3.3 Identifiers ----------------------------------------------------------
IDENTIFIER:		[a-zA-Z_][a-zA-Z0-9_]*;




// Special Charaters ============================================================================================
// Newline ------------------------------------------------------------------
NEWLINE:		[\n];

// Comments -----------------------------------------------------------------
COMMENT: 		'##' ~[\n\r]* -> skip;

// White space
WS: 			[ \f\b\t\r]+ -> skip;



// Error --------------------------------------------------------------------
UNCLOSE_STRING:	'"' Str_Char* ('\r\n' | '\n' | EOF)
{
	if(len(self.text) > 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
		raise UncloseString(self.text[1:-2])
	elif (self.text[-1] == '\n'):
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE:	'"' Str_Char* Illegal_Char {raise IllegalEscape(self.text[1:])};
fragment Illegal_Char:	[\r] | [\\] ~['bfrnt\\];

ERROR_CHAR:		. {raise ErrorToken(self.text)};


