# Generated from d://_ACADEMIC//HCMUT//Term232//PPL//Assignment//Asgm3//assignment3//assignment3-initial//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,49,410,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,1,0,5,0,98,8,0,10,0,12,0,101,9,0,1,0,1,0,1,0,1,1,
        1,1,1,1,1,1,3,1,110,8,1,1,2,1,2,1,2,1,2,3,2,116,8,2,1,3,1,3,1,3,
        3,3,121,8,3,1,4,1,4,1,4,3,4,126,8,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,139,8,6,1,6,1,6,3,6,143,8,6,1,7,1,7,1,7,1,7,
        3,7,149,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,3,9,160,8,9,1,10,
        1,10,1,10,1,10,1,10,3,10,167,8,10,1,11,1,11,1,11,1,11,1,11,1,11,
        3,11,175,8,11,1,12,3,12,178,8,12,1,12,1,12,3,12,182,8,12,1,12,3,
        12,185,8,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,14,194,8,14,1,15,
        1,15,1,15,1,15,1,15,3,15,201,8,15,1,16,1,16,1,16,1,16,1,16,1,16,
        5,16,209,8,16,10,16,12,16,212,9,16,1,17,1,17,1,17,1,17,1,17,1,17,
        5,17,220,8,17,10,17,12,17,223,9,17,1,18,1,18,1,18,1,18,1,18,1,18,
        5,18,231,8,18,10,18,12,18,234,9,18,1,19,1,19,1,19,3,19,239,8,19,
        1,20,1,20,1,20,3,20,244,8,20,1,21,1,21,3,21,248,8,21,1,21,1,21,1,
        21,1,21,1,21,3,21,255,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,
        22,264,8,22,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,3,24,275,
        8,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,3,26,290,8,26,1,27,1,27,1,27,1,27,1,27,3,27,297,8,27,1,27,1,
        27,1,27,3,27,302,8,27,1,27,3,27,305,8,27,1,28,1,28,1,28,1,28,3,28,
        311,8,28,1,29,1,29,1,29,1,29,1,29,3,29,318,8,29,1,29,1,29,1,30,1,
        30,3,30,324,8,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,
        31,335,8,31,1,31,1,31,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,
        34,1,34,1,34,1,34,1,34,3,34,352,8,34,1,35,1,35,1,35,1,36,1,36,1,
        36,1,37,1,37,3,37,362,8,37,1,37,1,37,1,38,1,38,1,38,1,39,1,39,1,
        39,1,39,1,39,1,39,1,40,1,40,3,40,377,8,40,1,41,1,41,1,41,1,41,3,
        41,383,8,41,1,42,1,42,1,43,1,43,3,43,389,8,43,1,44,1,44,1,44,1,44,
        1,44,3,44,396,8,44,1,45,1,45,3,45,400,8,45,1,46,1,46,1,46,1,46,3,
        46,406,8,46,1,47,1,47,1,47,0,3,32,34,36,48,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,0,5,1,0,30,36,
        1,0,22,23,1,0,24,25,1,0,26,28,3,0,37,37,39,39,41,41,414,0,99,1,0,
        0,0,2,109,1,0,0,0,4,115,1,0,0,0,6,120,1,0,0,0,8,125,1,0,0,0,10,127,
        1,0,0,0,12,132,1,0,0,0,14,144,1,0,0,0,16,150,1,0,0,0,18,159,1,0,
        0,0,20,166,1,0,0,0,22,168,1,0,0,0,24,184,1,0,0,0,26,186,1,0,0,0,
        28,193,1,0,0,0,30,200,1,0,0,0,32,202,1,0,0,0,34,213,1,0,0,0,36,224,
        1,0,0,0,38,238,1,0,0,0,40,243,1,0,0,0,42,254,1,0,0,0,44,263,1,0,
        0,0,46,265,1,0,0,0,48,274,1,0,0,0,50,276,1,0,0,0,52,289,1,0,0,0,
        54,291,1,0,0,0,56,310,1,0,0,0,58,312,1,0,0,0,60,321,1,0,0,0,62,327,
        1,0,0,0,64,338,1,0,0,0,66,341,1,0,0,0,68,346,1,0,0,0,70,353,1,0,
        0,0,72,356,1,0,0,0,74,359,1,0,0,0,76,365,1,0,0,0,78,368,1,0,0,0,
        80,376,1,0,0,0,82,382,1,0,0,0,84,384,1,0,0,0,86,388,1,0,0,0,88,395,
        1,0,0,0,90,399,1,0,0,0,92,405,1,0,0,0,94,407,1,0,0,0,96,98,5,44,
        0,0,97,96,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,
        102,1,0,0,0,101,99,1,0,0,0,102,103,3,2,1,0,103,104,5,0,0,1,104,1,
        1,0,0,0,105,106,3,4,2,0,106,107,3,2,1,0,107,110,1,0,0,0,108,110,
        3,4,2,0,109,105,1,0,0,0,109,108,1,0,0,0,110,3,1,0,0,0,111,112,3,
        8,4,0,112,113,3,6,3,0,113,116,1,0,0,0,114,116,3,16,8,0,115,111,1,
        0,0,0,115,114,1,0,0,0,116,5,1,0,0,0,117,118,5,44,0,0,118,121,3,6,
        3,0,119,121,5,44,0,0,120,117,1,0,0,0,120,119,1,0,0,0,121,7,1,0,0,
        0,122,126,3,10,5,0,123,126,3,12,6,0,124,126,3,14,7,0,125,122,1,0,
        0,0,125,123,1,0,0,0,125,124,1,0,0,0,126,9,1,0,0,0,127,128,5,1,0,
        0,128,129,5,43,0,0,129,130,5,3,0,0,130,131,3,26,13,0,131,11,1,0,
        0,0,132,133,3,94,47,0,133,138,5,43,0,0,134,135,5,18,0,0,135,136,
        3,82,41,0,136,137,5,19,0,0,137,139,1,0,0,0,138,134,1,0,0,0,138,139,
        1,0,0,0,139,142,1,0,0,0,140,141,5,3,0,0,141,143,3,26,13,0,142,140,
        1,0,0,0,142,143,1,0,0,0,143,13,1,0,0,0,144,145,5,2,0,0,145,148,5,
        43,0,0,146,147,5,3,0,0,147,149,3,26,13,0,148,146,1,0,0,0,148,149,
        1,0,0,0,149,15,1,0,0,0,150,151,5,4,0,0,151,152,5,43,0,0,152,153,
        5,16,0,0,153,154,3,18,9,0,154,155,5,17,0,0,155,156,3,24,12,0,156,
        17,1,0,0,0,157,160,3,20,10,0,158,160,1,0,0,0,159,157,1,0,0,0,159,
        158,1,0,0,0,160,19,1,0,0,0,161,162,3,22,11,0,162,163,5,20,0,0,163,
        164,3,20,10,0,164,167,1,0,0,0,165,167,3,22,11,0,166,161,1,0,0,0,
        166,165,1,0,0,0,167,21,1,0,0,0,168,169,3,94,47,0,169,174,5,43,0,
        0,170,171,5,18,0,0,171,172,3,82,41,0,172,173,5,19,0,0,173,175,1,
        0,0,0,174,170,1,0,0,0,174,175,1,0,0,0,175,23,1,0,0,0,176,178,3,6,
        3,0,177,176,1,0,0,0,177,178,1,0,0,0,178,181,1,0,0,0,179,182,3,74,
        37,0,180,182,3,78,39,0,181,179,1,0,0,0,181,180,1,0,0,0,182,185,1,
        0,0,0,183,185,3,6,3,0,184,177,1,0,0,0,184,183,1,0,0,0,185,25,1,0,
        0,0,186,187,3,28,14,0,187,27,1,0,0,0,188,189,3,30,15,0,189,190,5,
        29,0,0,190,191,3,30,15,0,191,194,1,0,0,0,192,194,3,30,15,0,193,188,
        1,0,0,0,193,192,1,0,0,0,194,29,1,0,0,0,195,196,3,32,16,0,196,197,
        7,0,0,0,197,198,3,32,16,0,198,201,1,0,0,0,199,201,3,32,16,0,200,
        195,1,0,0,0,200,199,1,0,0,0,201,31,1,0,0,0,202,203,6,16,-1,0,203,
        204,3,34,17,0,204,210,1,0,0,0,205,206,10,2,0,0,206,207,7,1,0,0,207,
        209,3,34,17,0,208,205,1,0,0,0,209,212,1,0,0,0,210,208,1,0,0,0,210,
        211,1,0,0,0,211,33,1,0,0,0,212,210,1,0,0,0,213,214,6,17,-1,0,214,
        215,3,36,18,0,215,221,1,0,0,0,216,217,10,2,0,0,217,218,7,2,0,0,218,
        220,3,36,18,0,219,216,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,
        222,1,0,0,0,222,35,1,0,0,0,223,221,1,0,0,0,224,225,6,18,-1,0,225,
        226,3,38,19,0,226,232,1,0,0,0,227,228,10,2,0,0,228,229,7,3,0,0,229,
        231,3,38,19,0,230,227,1,0,0,0,231,234,1,0,0,0,232,230,1,0,0,0,232,
        233,1,0,0,0,233,37,1,0,0,0,234,232,1,0,0,0,235,236,5,21,0,0,236,
        239,3,38,19,0,237,239,3,40,20,0,238,235,1,0,0,0,238,237,1,0,0,0,
        239,39,1,0,0,0,240,241,5,25,0,0,241,244,3,40,20,0,242,244,3,42,21,
        0,243,240,1,0,0,0,243,242,1,0,0,0,244,41,1,0,0,0,245,248,5,43,0,
        0,246,248,3,46,23,0,247,245,1,0,0,0,247,246,1,0,0,0,248,249,1,0,
        0,0,249,250,5,18,0,0,250,251,3,88,44,0,251,252,5,19,0,0,252,255,
        1,0,0,0,253,255,3,44,22,0,254,247,1,0,0,0,254,253,1,0,0,0,255,43,
        1,0,0,0,256,264,5,43,0,0,257,264,3,48,24,0,258,259,5,16,0,0,259,
        260,3,26,13,0,260,261,5,17,0,0,261,264,1,0,0,0,262,264,3,46,23,0,
        263,256,1,0,0,0,263,257,1,0,0,0,263,258,1,0,0,0,263,262,1,0,0,0,
        264,45,1,0,0,0,265,266,5,43,0,0,266,267,5,16,0,0,267,268,3,84,42,
        0,268,269,5,17,0,0,269,47,1,0,0,0,270,275,5,40,0,0,271,275,5,42,
        0,0,272,275,5,38,0,0,273,275,3,50,25,0,274,270,1,0,0,0,274,271,1,
        0,0,0,274,272,1,0,0,0,274,273,1,0,0,0,275,49,1,0,0,0,276,277,5,18,
        0,0,277,278,3,88,44,0,278,279,5,19,0,0,279,51,1,0,0,0,280,290,3,
        54,27,0,281,290,3,62,31,0,282,290,3,64,32,0,283,290,3,66,33,0,284,
        290,3,70,35,0,285,290,3,72,36,0,286,290,3,74,37,0,287,290,3,76,38,
        0,288,290,3,78,39,0,289,280,1,0,0,0,289,281,1,0,0,0,289,282,1,0,
        0,0,289,283,1,0,0,0,289,284,1,0,0,0,289,285,1,0,0,0,289,286,1,0,
        0,0,289,287,1,0,0,0,289,288,1,0,0,0,290,53,1,0,0,0,291,292,5,13,
        0,0,292,293,5,16,0,0,293,294,3,26,13,0,294,296,5,17,0,0,295,297,
        3,6,3,0,296,295,1,0,0,0,296,297,1,0,0,0,297,298,1,0,0,0,298,299,
        3,52,26,0,299,301,1,0,0,0,300,302,3,56,28,0,301,300,1,0,0,0,301,
        302,1,0,0,0,302,304,1,0,0,0,303,305,3,60,30,0,304,303,1,0,0,0,304,
        305,1,0,0,0,305,55,1,0,0,0,306,307,3,58,29,0,307,308,3,56,28,0,308,
        311,1,0,0,0,309,311,3,58,29,0,310,306,1,0,0,0,310,309,1,0,0,0,311,
        57,1,0,0,0,312,313,5,14,0,0,313,314,5,16,0,0,314,315,3,26,13,0,315,
        317,5,17,0,0,316,318,3,6,3,0,317,316,1,0,0,0,317,318,1,0,0,0,318,
        319,1,0,0,0,319,320,3,52,26,0,320,59,1,0,0,0,321,323,5,15,0,0,322,
        324,3,6,3,0,323,322,1,0,0,0,323,324,1,0,0,0,324,325,1,0,0,0,325,
        326,3,52,26,0,326,61,1,0,0,0,327,328,5,8,0,0,328,329,5,43,0,0,329,
        330,5,9,0,0,330,331,3,26,13,0,331,332,5,10,0,0,332,334,3,26,13,0,
        333,335,3,6,3,0,334,333,1,0,0,0,334,335,1,0,0,0,335,336,1,0,0,0,
        336,337,3,52,26,0,337,63,1,0,0,0,338,339,3,8,4,0,339,340,3,6,3,0,
        340,65,1,0,0,0,341,342,3,68,34,0,342,343,5,3,0,0,343,344,3,26,13,
        0,344,345,3,6,3,0,345,67,1,0,0,0,346,351,5,43,0,0,347,348,5,18,0,
        0,348,349,3,88,44,0,349,350,5,19,0,0,350,352,1,0,0,0,351,347,1,0,
        0,0,351,352,1,0,0,0,352,69,1,0,0,0,353,354,5,11,0,0,354,355,3,6,
        3,0,355,71,1,0,0,0,356,357,5,12,0,0,357,358,3,6,3,0,358,73,1,0,0,
        0,359,361,5,7,0,0,360,362,3,26,13,0,361,360,1,0,0,0,361,362,1,0,
        0,0,362,363,1,0,0,0,363,364,3,6,3,0,364,75,1,0,0,0,365,366,3,46,
        23,0,366,367,3,6,3,0,367,77,1,0,0,0,368,369,5,5,0,0,369,370,3,6,
        3,0,370,371,3,90,45,0,371,372,5,6,0,0,372,373,3,6,3,0,373,79,1,0,
        0,0,374,377,3,82,41,0,375,377,1,0,0,0,376,374,1,0,0,0,376,375,1,
        0,0,0,377,81,1,0,0,0,378,379,5,40,0,0,379,380,5,20,0,0,380,383,3,
        82,41,0,381,383,5,40,0,0,382,378,1,0,0,0,382,381,1,0,0,0,383,83,
        1,0,0,0,384,385,3,86,43,0,385,85,1,0,0,0,386,389,3,88,44,0,387,389,
        1,0,0,0,388,386,1,0,0,0,388,387,1,0,0,0,389,87,1,0,0,0,390,391,3,
        26,13,0,391,392,5,20,0,0,392,393,3,88,44,0,393,396,1,0,0,0,394,396,
        3,26,13,0,395,390,1,0,0,0,395,394,1,0,0,0,396,89,1,0,0,0,397,400,
        3,92,46,0,398,400,1,0,0,0,399,397,1,0,0,0,399,398,1,0,0,0,400,91,
        1,0,0,0,401,402,3,52,26,0,402,403,3,92,46,0,403,406,1,0,0,0,404,
        406,3,52,26,0,405,401,1,0,0,0,405,404,1,0,0,0,406,93,1,0,0,0,407,
        408,7,4,0,0,408,95,1,0,0,0,41,99,109,115,120,125,138,142,148,159,
        166,174,177,181,184,193,200,210,221,232,238,243,247,254,263,274,
        289,296,301,304,310,317,323,334,351,361,376,382,388,395,399,405
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'dynamic'", "'<-'", "'func'", 
                     "'begin'", "'end'", "'return'", "'for'", "'until'", 
                     "'by'", "'break'", "'continue'", "'if'", "'elif'", 
                     "'else'", "'('", "')'", "'['", "']'", "','", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'...'", "'=='", "'!='", "'='", "'<='", "'>='", "'<'", 
                     "'>'", "'bool'", "<INVALID>", "'number'", "<INVALID>", 
                     "'string'" ]

    symbolicNames = [ "<INVALID>", "VAR", "DYNAMIC", "ASSIGN_OPS", "FUNC", 
                      "BEGIN", "END", "RETURN", "FOR", "UNTIL", "BY", "BREAK", 
                      "CONTINUE", "IF", "ELIF", "ELSE", "LB", "RB", "LSB", 
                      "RSB", "COMMA", "NOT", "AND", "OR", "ADD_OPS", "SUB_OPS", 
                      "MUL_OPS", "DIV_OPS", "MOD_OPS", "CONCAT_OPS", "EQS", 
                      "NEQ", "EQ", "LEQ", "GEQ", "LT", "GT", "BOOL_TYP", 
                      "BOOL_LIT", "NUM_TYP", "NUM_LIT", "STR_TYP", "STRING_LIT", 
                      "IDENTIFIER", "NEWLINE", "COMMENT", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declare_list = 1
    RULE_declare = 2
    RULE_newlines = 3
    RULE_var_declare = 4
    RULE_implicit_var = 5
    RULE_keyword_var = 6
    RULE_dynamic_var = 7
    RULE_func_declare = 8
    RULE_paramList = 9
    RULE_paramList_prime = 10
    RULE_param = 11
    RULE_body = 12
    RULE_expr = 13
    RULE_expr_concat = 14
    RULE_expr_rela = 15
    RULE_expr_logic = 16
    RULE_expr_add = 17
    RULE_expr_mul = 18
    RULE_expr_not = 19
    RULE_expr_sign = 20
    RULE_expr_idx = 21
    RULE_operand = 22
    RULE_funcCall = 23
    RULE_literal = 24
    RULE_array_lit = 25
    RULE_stmt = 26
    RULE_if_stmt = 27
    RULE_elif_stmtList = 28
    RULE_elif_stmt = 29
    RULE_else_stmt = 30
    RULE_for_stmt = 31
    RULE_decl_stmt = 32
    RULE_assign_stmt = 33
    RULE_leftSide = 34
    RULE_break_stmt = 35
    RULE_continue_stmt = 36
    RULE_return_stmt = 37
    RULE_funcCall_stmt = 38
    RULE_block_stmt = 39
    RULE_numList = 40
    RULE_numList_prime = 41
    RULE_argList = 42
    RULE_exprList = 43
    RULE_exprList_prime = 44
    RULE_stmtList = 45
    RULE_stmtList_prime = 46
    RULE_typ = 47

    ruleNames =  [ "program", "declare_list", "declare", "newlines", "var_declare", 
                   "implicit_var", "keyword_var", "dynamic_var", "func_declare", 
                   "paramList", "paramList_prime", "param", "body", "expr", 
                   "expr_concat", "expr_rela", "expr_logic", "expr_add", 
                   "expr_mul", "expr_not", "expr_sign", "expr_idx", "operand", 
                   "funcCall", "literal", "array_lit", "stmt", "if_stmt", 
                   "elif_stmtList", "elif_stmt", "else_stmt", "for_stmt", 
                   "decl_stmt", "assign_stmt", "leftSide", "break_stmt", 
                   "continue_stmt", "return_stmt", "funcCall_stmt", "block_stmt", 
                   "numList", "numList_prime", "argList", "exprList", "exprList_prime", 
                   "stmtList", "stmtList_prime", "typ" ]

    EOF = Token.EOF
    VAR=1
    DYNAMIC=2
    ASSIGN_OPS=3
    FUNC=4
    BEGIN=5
    END=6
    RETURN=7
    FOR=8
    UNTIL=9
    BY=10
    BREAK=11
    CONTINUE=12
    IF=13
    ELIF=14
    ELSE=15
    LB=16
    RB=17
    LSB=18
    RSB=19
    COMMA=20
    NOT=21
    AND=22
    OR=23
    ADD_OPS=24
    SUB_OPS=25
    MUL_OPS=26
    DIV_OPS=27
    MOD_OPS=28
    CONCAT_OPS=29
    EQS=30
    NEQ=31
    EQ=32
    LEQ=33
    GEQ=34
    LT=35
    GT=36
    BOOL_TYP=37
    BOOL_LIT=38
    NUM_TYP=39
    NUM_LIT=40
    STR_TYP=41
    STRING_LIT=42
    IDENTIFIER=43
    NEWLINE=44
    COMMENT=45
    WS=46
    UNCLOSE_STRING=47
    ILLEGAL_ESCAPE=48
    ERROR_CHAR=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declare_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 96
                self.match(ZCodeParser.NEWLINE)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
            self.declare_list()
            self.state = 103
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare(self):
            return self.getTypedRuleContext(ZCodeParser.DeclareContext,0)


        def declare_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declare_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declare_list




    def declare_list(self):

        localctx = ZCodeParser.Declare_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declare_list)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.declare()
                self.state = 106
                self.declare_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declareContext,0)


        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def func_declare(self):
            return self.getTypedRuleContext(ZCodeParser.Func_declareContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declare




    def declare(self):

        localctx = ZCodeParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 37, 39, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.var_declare()
                self.state = 112
                self.newlines()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.func_declare()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlinesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlines




    def newlines(self):

        localctx = ZCodeParser.NewlinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_newlines)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(ZCodeParser.NEWLINE)
                self.state = 118
                self.newlines()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicit_var(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_varContext,0)


        def keyword_var(self):
            return self.getTypedRuleContext(ZCodeParser.Keyword_varContext,0)


        def dynamic_var(self):
            return self.getTypedRuleContext(ZCodeParser.Dynamic_varContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_declare




    def var_declare(self):

        localctx = ZCodeParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_declare)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.implicit_var()
                pass
            elif token in [37, 39, 41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.keyword_var()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.dynamic_var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN_OPS(self):
            return self.getToken(ZCodeParser.ASSIGN_OPS, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_var




    def implicit_var(self):

        localctx = ZCodeParser.Implicit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_implicit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(ZCodeParser.VAR)
            self.state = 128
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 129
            self.match(ZCodeParser.ASSIGN_OPS)
            self.state = 130
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def numList_prime(self):
            return self.getTypedRuleContext(ZCodeParser.NumList_primeContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def ASSIGN_OPS(self):
            return self.getToken(ZCodeParser.ASSIGN_OPS, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_keyword_var




    def keyword_var(self):

        localctx = ZCodeParser.Keyword_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_keyword_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.typ()
            self.state = 133
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 134
                self.match(ZCodeParser.LSB)
                self.state = 135
                self.numList_prime()
                self.state = 136
                self.match(ZCodeParser.RSB)


            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 140
                self.match(ZCodeParser.ASSIGN_OPS)
                self.state = 141
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dynamic_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN_OPS(self):
            return self.getToken(ZCodeParser.ASSIGN_OPS, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamic_var




    def dynamic_var(self):

        localctx = ZCodeParser.Dynamic_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dynamic_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(ZCodeParser.DYNAMIC)
            self.state = 145
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 146
                self.match(ZCodeParser.ASSIGN_OPS)
                self.state = 147
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def paramList(self):
            return self.getTypedRuleContext(ZCodeParser.ParamListContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def body(self):
            return self.getTypedRuleContext(ZCodeParser.BodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_declare




    def func_declare(self):

        localctx = ZCodeParser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(ZCodeParser.FUNC)
            self.state = 151
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 152
            self.match(ZCodeParser.LB)
            self.state = 153
            self.paramList()
            self.state = 154
            self.match(ZCodeParser.RB)
            self.state = 155
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramList_prime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamList_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramList




    def paramList(self):

        localctx = ZCodeParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramList)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37, 39, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.paramList_prime()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamList_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramList_prime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamList_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramList_prime




    def paramList_prime(self):

        localctx = ZCodeParser.ParamList_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramList_prime)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.param()
                self.state = 162
                self.match(ZCodeParser.COMMA)
                self.state = 163
                self.paramList_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def numList_prime(self):
            return self.getTypedRuleContext(ZCodeParser.NumList_primeContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.typ()
            self.state = 169
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 170
                self.match(ZCodeParser.LSB)
                self.state = 171
                self.numList_prime()
                self.state = 172
                self.match(ZCodeParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_body




    def body(self):

        localctx = ZCodeParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==44:
                    self.state = 176
                    self.newlines()


                self.state = 181
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 179
                    self.return_stmt()
                    pass
                elif token in [5]:
                    self.state = 180
                    self.block_stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.newlines()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_concat(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_concatContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.expr_concat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_concatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_rela(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_relaContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_relaContext,i)


        def CONCAT_OPS(self):
            return self.getToken(ZCodeParser.CONCAT_OPS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_concat




    def expr_concat(self):

        localctx = ZCodeParser.Expr_concatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr_concat)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.expr_rela()
                self.state = 189
                self.match(ZCodeParser.CONCAT_OPS)
                self.state = 190
                self.expr_rela()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.expr_rela()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_relaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_logic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_logicContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_logicContext,i)


        def EQS(self):
            return self.getToken(ZCodeParser.EQS, 0)

        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def NEQ(self):
            return self.getToken(ZCodeParser.NEQ, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def LEQ(self):
            return self.getToken(ZCodeParser.LEQ, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def GEQ(self):
            return self.getToken(ZCodeParser.GEQ, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_rela




    def expr_rela(self):

        localctx = ZCodeParser.Expr_relaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr_rela)
        self._la = 0 # Token type
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.expr_logic(0)
                self.state = 196
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 136365211648) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 197
                self.expr_logic(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.expr_logic(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_logicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_add(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_addContext,0)


        def expr_logic(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_logicContext,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_logic



    def expr_logic(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_logicContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr_logic, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.expr_add(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_logicContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_logic)
                    self.state = 205
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 206
                    _la = self._input.LA(1)
                    if not(_la==22 or _la==23):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 207
                    self.expr_add(0) 
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_addContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_mul(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_mulContext,0)


        def expr_add(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_addContext,0)


        def ADD_OPS(self):
            return self.getToken(ZCodeParser.ADD_OPS, 0)

        def SUB_OPS(self):
            return self.getToken(ZCodeParser.SUB_OPS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_add



    def expr_add(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_addContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr_add, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.expr_mul(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_addContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_add)
                    self.state = 216
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 217
                    _la = self._input.LA(1)
                    if not(_la==24 or _la==25):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 218
                    self.expr_mul(0) 
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_mulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_not(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_notContext,0)


        def expr_mul(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_mulContext,0)


        def MUL_OPS(self):
            return self.getToken(ZCodeParser.MUL_OPS, 0)

        def DIV_OPS(self):
            return self.getToken(ZCodeParser.DIV_OPS, 0)

        def MOD_OPS(self):
            return self.getToken(ZCodeParser.MOD_OPS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_mul



    def expr_mul(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_mulContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr_mul, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.expr_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_mulContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_mul)
                    self.state = 227
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 228
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 229
                    self.expr_not() 
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_notContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr_not(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_notContext,0)


        def expr_sign(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_signContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_not




    def expr_not(self):

        localctx = ZCodeParser.Expr_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr_not)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(ZCodeParser.NOT)
                self.state = 236
                self.expr_not()
                pass
            elif token in [16, 18, 25, 38, 40, 42, 43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.expr_sign()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_signContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OPS(self):
            return self.getToken(ZCodeParser.SUB_OPS, 0)

        def expr_sign(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_signContext,0)


        def expr_idx(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_idxContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_sign




    def expr_sign(self):

        localctx = ZCodeParser.Expr_signContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr_sign)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(ZCodeParser.SUB_OPS)
                self.state = 241
                self.expr_sign()
                pass
            elif token in [16, 18, 38, 40, 42, 43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.expr_idx()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_idxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def exprList_prime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprList_primeContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def funcCall(self):
            return self.getTypedRuleContext(ZCodeParser.FuncCallContext,0)


        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_idx




    def expr_idx(self):

        localctx = ZCodeParser.Expr_idxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr_idx)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 245
                    self.match(ZCodeParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 246
                    self.funcCall()
                    pass


                self.state = 249
                self.match(ZCodeParser.LSB)
                self.state = 250
                self.exprList_prime()
                self.state = 251
                self.match(ZCodeParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def funcCall(self):
            return self.getTypedRuleContext(ZCodeParser.FuncCallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_operand)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.match(ZCodeParser.LB)
                self.state = 259
                self.expr()
                self.state = 260
                self.match(ZCodeParser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 262
                self.funcCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def argList(self):
            return self.getTypedRuleContext(ZCodeParser.ArgListContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_funcCall




    def funcCall(self):

        localctx = ZCodeParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_funcCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 266
            self.match(ZCodeParser.LB)
            self.state = 267
            self.argList()
            self.state = 268
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(ZCodeParser.BOOL_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Array_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_literal)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.match(ZCodeParser.NUM_LIT)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 272
                self.match(ZCodeParser.BOOL_LIT)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 273
                self.array_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def exprList_prime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprList_primeContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_lit




    def array_lit(self):

        localctx = ZCodeParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(ZCodeParser.LSB)
            self.state = 277
            self.exprList_prime()
            self.state = 278
            self.match(ZCodeParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def decl_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def funcCall_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.FuncCall_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stmt)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.for_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 282
                self.decl_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 283
                self.assign_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 284
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 285
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 286
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 287
                self.funcCall_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 288
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def elif_stmtList(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtListContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Else_stmtContext,0)


        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(ZCodeParser.IF)
            self.state = 292
            self.match(ZCodeParser.LB)
            self.state = 293
            self.expr()
            self.state = 294
            self.match(ZCodeParser.RB)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 295
                self.newlines()


            self.state = 298
            self.stmt()
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 300
                self.elif_stmtList()


            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 303
                self.else_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmtListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtContext,0)


        def elif_stmtList(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmtList




    def elif_stmtList(self):

        localctx = ZCodeParser.Elif_stmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_elif_stmtList)
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.elif_stmt()
                self.state = 307
                self.elif_stmtList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.elif_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt




    def elif_stmt(self):

        localctx = ZCodeParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_elif_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(ZCodeParser.ELIF)
            self.state = 313
            self.match(ZCodeParser.LB)
            self.state = 314
            self.expr()
            self.state = 315
            self.match(ZCodeParser.RB)
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 316
                self.newlines()


            self.state = 319
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_stmt




    def else_stmt(self):

        localctx = ZCodeParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_else_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(ZCodeParser.ELSE)
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 322
                self.newlines()


            self.state = 325
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(ZCodeParser.FOR)
            self.state = 328
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 329
            self.match(ZCodeParser.UNTIL)
            self.state = 330
            self.expr()
            self.state = 331
            self.match(ZCodeParser.BY)
            self.state = 332
            self.expr()
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 333
                self.newlines()


            self.state = 336
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declareContext,0)


        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_stmt




    def decl_stmt(self):

        localctx = ZCodeParser.Decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_decl_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.var_declare()
            self.state = 339
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def leftSide(self):
            return self.getTypedRuleContext(ZCodeParser.LeftSideContext,0)


        def ASSIGN_OPS(self):
            return self.getToken(ZCodeParser.ASSIGN_OPS, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = ZCodeParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.leftSide()
            self.state = 342
            self.match(ZCodeParser.ASSIGN_OPS)
            self.state = 343
            self.expr()
            self.state = 344
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeftSideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(ZCodeParser.LSB, 0)

        def exprList_prime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprList_primeContext,0)


        def RSB(self):
            return self.getToken(ZCodeParser.RSB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_leftSide




    def leftSide(self):

        localctx = ZCodeParser.LeftSideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_leftSide)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 347
                self.match(ZCodeParser.LSB)
                self.state = 348
                self.exprList_prime()
                self.state = 349
                self.match(ZCodeParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(ZCodeParser.BREAK)
            self.state = 354
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(ZCodeParser.CONTINUE)
            self.state = 357
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(ZCodeParser.RETURN)
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14568565047296) != 0):
                self.state = 360
                self.expr()


            self.state = 363
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCall_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcCall(self):
            return self.getTypedRuleContext(ZCodeParser.FuncCallContext,0)


        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcCall_stmt




    def funcCall_stmt(self):

        localctx = ZCodeParser.FuncCall_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_funcCall_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.funcCall()
            self.state = 366
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def newlines(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NewlinesContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NewlinesContext,i)


        def stmtList(self):
            return self.getTypedRuleContext(ZCodeParser.StmtListContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(ZCodeParser.BEGIN)
            self.state = 369
            self.newlines()
            self.state = 370
            self.stmtList()
            self.state = 371
            self.match(ZCodeParser.END)
            self.state = 372
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numList_prime(self):
            return self.getTypedRuleContext(ZCodeParser.NumList_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numList




    def numList(self):

        localctx = ZCodeParser.NumListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_numList)
        try:
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.numList_prime()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumList_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def numList_prime(self):
            return self.getTypedRuleContext(ZCodeParser.NumList_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numList_prime




    def numList_prime(self):

        localctx = ZCodeParser.NumList_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_numList_prime)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.match(ZCodeParser.NUM_LIT)
                self.state = 379
                self.match(ZCodeParser.COMMA)
                self.state = 380
                self.numList_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.match(ZCodeParser.NUM_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprList(self):
            return self.getTypedRuleContext(ZCodeParser.ExprListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argList




    def argList(self):

        localctx = ZCodeParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_argList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.exprList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprList_prime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprList_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprList




    def exprList(self):

        localctx = ZCodeParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exprList)
        try:
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 18, 21, 25, 38, 40, 42, 43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.exprList_prime()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprList_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def exprList_prime(self):
            return self.getTypedRuleContext(ZCodeParser.ExprList_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprList_prime




    def exprList_prime(self):

        localctx = ZCodeParser.ExprList_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_exprList_prime)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.expr()
                self.state = 391
                self.match(ZCodeParser.COMMA)
                self.state = 392
                self.exprList_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtList_prime(self):
            return self.getTypedRuleContext(ZCodeParser.StmtList_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtList




    def stmtList(self):

        localctx = ZCodeParser.StmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_stmtList)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 5, 7, 8, 11, 12, 13, 37, 39, 41, 43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.stmtList_prime()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtList_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def stmtList_prime(self):
            return self.getTypedRuleContext(ZCodeParser.StmtList_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtList_prime




    def stmtList_prime(self):

        localctx = ZCodeParser.StmtList_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stmtList_prime)
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.stmt()
                self.state = 402
                self.stmtList_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_TYP(self):
            return self.getToken(ZCodeParser.NUM_TYP, 0)

        def BOOL_TYP(self):
            return self.getToken(ZCodeParser.BOOL_TYP, 0)

        def STR_TYP(self):
            return self.getToken(ZCodeParser.STR_TYP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2886218022912) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expr_logic_sempred
        self._predicates[17] = self.expr_add_sempred
        self._predicates[18] = self.expr_mul_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_logic_sempred(self, localctx:Expr_logicContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_add_sempred(self, localctx:Expr_addContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_mul_sempred(self, localctx:Expr_mulContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




