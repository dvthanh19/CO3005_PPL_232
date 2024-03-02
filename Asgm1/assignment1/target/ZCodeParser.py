# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63")
        buf.write("\u019c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\7\2d\n\2\f\2\16\2g\13\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3p\n\3\3\4\3\4\3\4\3\4\5")
        buf.write("\4v\n\4\3\5\3\5\3\5\5\5{\n\5\3\6\3\6\3\6\5\6\u0080\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u008d")
        buf.write("\n\b\3\b\3\b\5\b\u0091\n\b\3\t\3\t\3\t\3\t\5\t\u0097\n")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\5\13\u00a2\n")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\5\f\u00a9\n\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\5\r\u00b1\n\r\3\16\5\16\u00b4\n\16\3\16\3\16")
        buf.write("\5\16\u00b8\n\16\3\16\5\16\u00bb\n\16\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\5\20\u00c4\n\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\5\21\u00cb\n\21\3\22\3\22\3\22\3\22\3\22\3\22\7")
        buf.write("\22\u00d3\n\22\f\22\16\22\u00d6\13\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\7\23\u00de\n\23\f\23\16\23\u00e1\13\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\7\24\u00e9\n\24\f\24\16\24")
        buf.write("\u00ec\13\24\3\25\3\25\3\25\5\25\u00f1\n\25\3\26\3\26")
        buf.write("\3\26\5\26\u00f6\n\26\3\27\3\27\5\27\u00fa\n\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\5\27\u0101\n\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\5\30\u010a\n\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\5\32\u0115\n\32\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u0124\n\34\3\35\3\35\3\35\3\35\3\35\5\35\u012b\n\35\3")
        buf.write("\35\3\35\3\35\5\35\u0130\n\35\3\35\5\35\u0133\n\35\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u0139\n\36\3\37\3\37\3\37\3\37\3")
        buf.write("\37\5\37\u0140\n\37\3\37\3\37\3 \3 \5 \u0146\n \3 \3 ")
        buf.write("\3!\3!\3!\3!\3!\3!\3!\5!\u0151\n!\3!\3!\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3#\3$\3$\3$\3$\3$\5$\u0162\n$\3%\3%\3%\3&\3")
        buf.write("&\3&\3\'\3\'\5\'\u016c\n\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3")
        buf.write(")\3)\3)\3*\3*\5*\u017b\n*\3+\3+\3+\3+\5+\u0181\n+\3,\3")
        buf.write(",\3-\3-\5-\u0187\n-\3.\3.\3.\3.\3.\5.\u018e\n.\3/\3/\5")
        buf.write("/\u0192\n/\3\60\3\60\3\60\3\60\5\60\u0198\n\60\3\61\3")
        buf.write("\61\3\61\2\5\"$&\62\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`\2\7\3\2")
        buf.write(" &\3\2\30\31\3\2\32\33\3\2\34\36\5\2\'\'))++\2\u01a0\2")
        buf.write("e\3\2\2\2\4o\3\2\2\2\6u\3\2\2\2\bz\3\2\2\2\n\177\3\2\2")
        buf.write("\2\f\u0081\3\2\2\2\16\u0086\3\2\2\2\20\u0092\3\2\2\2\22")
        buf.write("\u0098\3\2\2\2\24\u00a1\3\2\2\2\26\u00a8\3\2\2\2\30\u00aa")
        buf.write("\3\2\2\2\32\u00ba\3\2\2\2\34\u00bc\3\2\2\2\36\u00c3\3")
        buf.write("\2\2\2 \u00ca\3\2\2\2\"\u00cc\3\2\2\2$\u00d7\3\2\2\2&")
        buf.write("\u00e2\3\2\2\2(\u00f0\3\2\2\2*\u00f5\3\2\2\2,\u0100\3")
        buf.write("\2\2\2.\u0109\3\2\2\2\60\u010b\3\2\2\2\62\u0114\3\2\2")
        buf.write("\2\64\u0116\3\2\2\2\66\u0123\3\2\2\28\u0125\3\2\2\2:\u0138")
        buf.write("\3\2\2\2<\u013a\3\2\2\2>\u0143\3\2\2\2@\u0149\3\2\2\2")
        buf.write("B\u0154\3\2\2\2D\u0157\3\2\2\2F\u015c\3\2\2\2H\u0163\3")
        buf.write("\2\2\2J\u0166\3\2\2\2L\u0169\3\2\2\2N\u016f\3\2\2\2P\u0172")
        buf.write("\3\2\2\2R\u017a\3\2\2\2T\u0180\3\2\2\2V\u0182\3\2\2\2")
        buf.write("X\u0186\3\2\2\2Z\u018d\3\2\2\2\\\u0191\3\2\2\2^\u0197")
        buf.write("\3\2\2\2`\u0199\3\2\2\2bd\7.\2\2cb\3\2\2\2dg\3\2\2\2e")
        buf.write("c\3\2\2\2ef\3\2\2\2fh\3\2\2\2ge\3\2\2\2hi\5\4\3\2ij\7")
        buf.write("\2\2\3j\3\3\2\2\2kl\5\6\4\2lm\5\4\3\2mp\3\2\2\2np\5\6")
        buf.write("\4\2ok\3\2\2\2on\3\2\2\2p\5\3\2\2\2qr\5\n\6\2rs\5\b\5")
        buf.write("\2sv\3\2\2\2tv\5\22\n\2uq\3\2\2\2ut\3\2\2\2v\7\3\2\2\2")
        buf.write("wx\7.\2\2x{\5\b\5\2y{\7.\2\2zw\3\2\2\2zy\3\2\2\2{\t\3")
        buf.write("\2\2\2|\u0080\5\f\7\2}\u0080\5\16\b\2~\u0080\5\20\t\2")
        buf.write("\177|\3\2\2\2\177}\3\2\2\2\177~\3\2\2\2\u0080\13\3\2\2")
        buf.write("\2\u0081\u0082\7\3\2\2\u0082\u0083\7-\2\2\u0083\u0084")
        buf.write("\7\5\2\2\u0084\u0085\5\34\17\2\u0085\r\3\2\2\2\u0086\u0087")
        buf.write("\5`\61\2\u0087\u008c\7-\2\2\u0088\u0089\7\24\2\2\u0089")
        buf.write("\u008a\5T+\2\u008a\u008b\7\25\2\2\u008b\u008d\3\2\2\2")
        buf.write("\u008c\u0088\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u0090\3")
        buf.write("\2\2\2\u008e\u008f\7\5\2\2\u008f\u0091\5\34\17\2\u0090")
        buf.write("\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\17\3\2\2\2\u0092")
        buf.write("\u0093\7\4\2\2\u0093\u0096\7-\2\2\u0094\u0095\7\5\2\2")
        buf.write("\u0095\u0097\5\34\17\2\u0096\u0094\3\2\2\2\u0096\u0097")
        buf.write("\3\2\2\2\u0097\21\3\2\2\2\u0098\u0099\7\6\2\2\u0099\u009a")
        buf.write("\7-\2\2\u009a\u009b\7\22\2\2\u009b\u009c\5\24\13\2\u009c")
        buf.write("\u009d\7\23\2\2\u009d\u009e\5\32\16\2\u009e\23\3\2\2\2")
        buf.write("\u009f\u00a2\5\26\f\2\u00a0\u00a2\3\2\2\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\25\3\2\2\2\u00a3\u00a4")
        buf.write("\5\30\r\2\u00a4\u00a5\7\26\2\2\u00a5\u00a6\5\26\f\2\u00a6")
        buf.write("\u00a9\3\2\2\2\u00a7\u00a9\5\30\r\2\u00a8\u00a3\3\2\2")
        buf.write("\2\u00a8\u00a7\3\2\2\2\u00a9\27\3\2\2\2\u00aa\u00ab\5")
        buf.write("`\61\2\u00ab\u00b0\7-\2\2\u00ac\u00ad\7\24\2\2\u00ad\u00ae")
        buf.write("\5T+\2\u00ae\u00af\7\25\2\2\u00af\u00b1\3\2\2\2\u00b0")
        buf.write("\u00ac\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\31\3\2\2\2\u00b2")
        buf.write("\u00b4\5\b\5\2\u00b3\u00b2\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\u00b7\3\2\2\2\u00b5\u00b8\5L\'\2\u00b6\u00b8\5")
        buf.write("P)\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00bb")
        buf.write("\3\2\2\2\u00b9\u00bb\5\b\5\2\u00ba\u00b3\3\2\2\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00bb\33\3\2\2\2\u00bc\u00bd\5\36\20\2")
        buf.write("\u00bd\35\3\2\2\2\u00be\u00bf\5 \21\2\u00bf\u00c0\7\37")
        buf.write("\2\2\u00c0\u00c1\5 \21\2\u00c1\u00c4\3\2\2\2\u00c2\u00c4")
        buf.write("\5 \21\2\u00c3\u00be\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4")
        buf.write("\37\3\2\2\2\u00c5\u00c6\5\"\22\2\u00c6\u00c7\t\2\2\2\u00c7")
        buf.write("\u00c8\5\"\22\2\u00c8\u00cb\3\2\2\2\u00c9\u00cb\5\"\22")
        buf.write("\2\u00ca\u00c5\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb!\3\2")
        buf.write("\2\2\u00cc\u00cd\b\22\1\2\u00cd\u00ce\5$\23\2\u00ce\u00d4")
        buf.write("\3\2\2\2\u00cf\u00d0\f\4\2\2\u00d0\u00d1\t\3\2\2\u00d1")
        buf.write("\u00d3\5$\23\2\u00d2\u00cf\3\2\2\2\u00d3\u00d6\3\2\2\2")
        buf.write("\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5#\3\2\2")
        buf.write("\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8\b\23\1\2\u00d8\u00d9")
        buf.write("\5&\24\2\u00d9\u00df\3\2\2\2\u00da\u00db\f\4\2\2\u00db")
        buf.write("\u00dc\t\4\2\2\u00dc\u00de\5&\24\2\u00dd\u00da\3\2\2\2")
        buf.write("\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3")
        buf.write("\2\2\2\u00e0%\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e3")
        buf.write("\b\24\1\2\u00e3\u00e4\5(\25\2\u00e4\u00ea\3\2\2\2\u00e5")
        buf.write("\u00e6\f\4\2\2\u00e6\u00e7\t\5\2\2\u00e7\u00e9\5(\25\2")
        buf.write("\u00e8\u00e5\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3")
        buf.write("\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\'\3\2\2\2\u00ec\u00ea")
        buf.write("\3\2\2\2\u00ed\u00ee\7\27\2\2\u00ee\u00f1\5(\25\2\u00ef")
        buf.write("\u00f1\5*\26\2\u00f0\u00ed\3\2\2\2\u00f0\u00ef\3\2\2\2")
        buf.write("\u00f1)\3\2\2\2\u00f2\u00f3\7\33\2\2\u00f3\u00f6\5*\26")
        buf.write("\2\u00f4\u00f6\5,\27\2\u00f5\u00f2\3\2\2\2\u00f5\u00f4")
        buf.write("\3\2\2\2\u00f6+\3\2\2\2\u00f7\u00fa\7-\2\2\u00f8\u00fa")
        buf.write("\5\60\31\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa")
        buf.write("\u00fb\3\2\2\2\u00fb\u00fc\7\24\2\2\u00fc\u00fd\5Z.\2")
        buf.write("\u00fd\u00fe\7\25\2\2\u00fe\u0101\3\2\2\2\u00ff\u0101")
        buf.write("\5.\30\2\u0100\u00f9\3\2\2\2\u0100\u00ff\3\2\2\2\u0101")
        buf.write("-\3\2\2\2\u0102\u010a\7-\2\2\u0103\u010a\5\62\32\2\u0104")
        buf.write("\u0105\7\22\2\2\u0105\u0106\5\34\17\2\u0106\u0107\7\23")
        buf.write("\2\2\u0107\u010a\3\2\2\2\u0108\u010a\5\60\31\2\u0109\u0102")
        buf.write("\3\2\2\2\u0109\u0103\3\2\2\2\u0109\u0104\3\2\2\2\u0109")
        buf.write("\u0108\3\2\2\2\u010a/\3\2\2\2\u010b\u010c\7-\2\2\u010c")
        buf.write("\u010d\7\22\2\2\u010d\u010e\5V,\2\u010e\u010f\7\23\2\2")
        buf.write("\u010f\61\3\2\2\2\u0110\u0115\7*\2\2\u0111\u0115\7,\2")
        buf.write("\2\u0112\u0115\7(\2\2\u0113\u0115\5\64\33\2\u0114\u0110")
        buf.write("\3\2\2\2\u0114\u0111\3\2\2\2\u0114\u0112\3\2\2\2\u0114")
        buf.write("\u0113\3\2\2\2\u0115\63\3\2\2\2\u0116\u0117\7\24\2\2\u0117")
        buf.write("\u0118\5Z.\2\u0118\u0119\7\25\2\2\u0119\65\3\2\2\2\u011a")
        buf.write("\u0124\58\35\2\u011b\u0124\5@!\2\u011c\u0124\5B\"\2\u011d")
        buf.write("\u0124\5D#\2\u011e\u0124\5H%\2\u011f\u0124\5J&\2\u0120")
        buf.write("\u0124\5L\'\2\u0121\u0124\5N(\2\u0122\u0124\5P)\2\u0123")
        buf.write("\u011a\3\2\2\2\u0123\u011b\3\2\2\2\u0123\u011c\3\2\2\2")
        buf.write("\u0123\u011d\3\2\2\2\u0123\u011e\3\2\2\2\u0123\u011f\3")
        buf.write("\2\2\2\u0123\u0120\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0122")
        buf.write("\3\2\2\2\u0124\67\3\2\2\2\u0125\u0126\7\17\2\2\u0126\u0127")
        buf.write("\7\22\2\2\u0127\u0128\5\34\17\2\u0128\u012a\7\23\2\2\u0129")
        buf.write("\u012b\5\b\5\2\u012a\u0129\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\u012c\3\2\2\2\u012c\u012d\5\66\34\2\u012d\u012f")
        buf.write("\3\2\2\2\u012e\u0130\5:\36\2\u012f\u012e\3\2\2\2\u012f")
        buf.write("\u0130\3\2\2\2\u0130\u0132\3\2\2\2\u0131\u0133\5> \2\u0132")
        buf.write("\u0131\3\2\2\2\u0132\u0133\3\2\2\2\u01339\3\2\2\2\u0134")
        buf.write("\u0135\5<\37\2\u0135\u0136\5:\36\2\u0136\u0139\3\2\2\2")
        buf.write("\u0137\u0139\5<\37\2\u0138\u0134\3\2\2\2\u0138\u0137\3")
        buf.write("\2\2\2\u0139;\3\2\2\2\u013a\u013b\7\20\2\2\u013b\u013c")
        buf.write("\7\22\2\2\u013c\u013d\5\34\17\2\u013d\u013f\7\23\2\2\u013e")
        buf.write("\u0140\5\b\5\2\u013f\u013e\3\2\2\2\u013f\u0140\3\2\2\2")
        buf.write("\u0140\u0141\3\2\2\2\u0141\u0142\5\66\34\2\u0142=\3\2")
        buf.write("\2\2\u0143\u0145\7\21\2\2\u0144\u0146\5\b\5\2\u0145\u0144")
        buf.write("\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0147\3\2\2\2\u0147")
        buf.write("\u0148\5\66\34\2\u0148?\3\2\2\2\u0149\u014a\7\n\2\2\u014a")
        buf.write("\u014b\7-\2\2\u014b\u014c\7\13\2\2\u014c\u014d\5\34\17")
        buf.write("\2\u014d\u014e\7\f\2\2\u014e\u0150\5\34\17\2\u014f\u0151")
        buf.write("\5\b\5\2\u0150\u014f\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write("\u0152\3\2\2\2\u0152\u0153\5\66\34\2\u0153A\3\2\2\2\u0154")
        buf.write("\u0155\5\n\6\2\u0155\u0156\5\b\5\2\u0156C\3\2\2\2\u0157")
        buf.write("\u0158\5F$\2\u0158\u0159\7\5\2\2\u0159\u015a\5\34\17\2")
        buf.write("\u015a\u015b\5\b\5\2\u015bE\3\2\2\2\u015c\u0161\7-\2\2")
        buf.write("\u015d\u015e\7\24\2\2\u015e\u015f\5Z.\2\u015f\u0160\7")
        buf.write("\25\2\2\u0160\u0162\3\2\2\2\u0161\u015d\3\2\2\2\u0161")
        buf.write("\u0162\3\2\2\2\u0162G\3\2\2\2\u0163\u0164\7\r\2\2\u0164")
        buf.write("\u0165\5\b\5\2\u0165I\3\2\2\2\u0166\u0167\7\16\2\2\u0167")
        buf.write("\u0168\5\b\5\2\u0168K\3\2\2\2\u0169\u016b\7\t\2\2\u016a")
        buf.write("\u016c\5\34\17\2\u016b\u016a\3\2\2\2\u016b\u016c\3\2\2")
        buf.write("\2\u016c\u016d\3\2\2\2\u016d\u016e\5\b\5\2\u016eM\3\2")
        buf.write("\2\2\u016f\u0170\5\60\31\2\u0170\u0171\5\b\5\2\u0171O")
        buf.write("\3\2\2\2\u0172\u0173\7\7\2\2\u0173\u0174\5\b\5\2\u0174")
        buf.write("\u0175\5\\/\2\u0175\u0176\7\b\2\2\u0176\u0177\5\b\5\2")
        buf.write("\u0177Q\3\2\2\2\u0178\u017b\5T+\2\u0179\u017b\3\2\2\2")
        buf.write("\u017a\u0178\3\2\2\2\u017a\u0179\3\2\2\2\u017bS\3\2\2")
        buf.write("\2\u017c\u017d\7*\2\2\u017d\u017e\7\26\2\2\u017e\u0181")
        buf.write("\5T+\2\u017f\u0181\7*\2\2\u0180\u017c\3\2\2\2\u0180\u017f")
        buf.write("\3\2\2\2\u0181U\3\2\2\2\u0182\u0183\5X-\2\u0183W\3\2\2")
        buf.write("\2\u0184\u0187\5Z.\2\u0185\u0187\3\2\2\2\u0186\u0184\3")
        buf.write("\2\2\2\u0186\u0185\3\2\2\2\u0187Y\3\2\2\2\u0188\u0189")
        buf.write("\5\34\17\2\u0189\u018a\7\26\2\2\u018a\u018b\5Z.\2\u018b")
        buf.write("\u018e\3\2\2\2\u018c\u018e\5\34\17\2\u018d\u0188\3\2\2")
        buf.write("\2\u018d\u018c\3\2\2\2\u018e[\3\2\2\2\u018f\u0192\5^\60")
        buf.write("\2\u0190\u0192\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0190")
        buf.write("\3\2\2\2\u0192]\3\2\2\2\u0193\u0194\5\66\34\2\u0194\u0195")
        buf.write("\5^\60\2\u0195\u0198\3\2\2\2\u0196\u0198\5\66\34\2\u0197")
        buf.write("\u0193\3\2\2\2\u0197\u0196\3\2\2\2\u0198_\3\2\2\2\u0199")
        buf.write("\u019a\t\6\2\2\u019aa\3\2\2\2+eouz\177\u008c\u0090\u0096")
        buf.write("\u00a1\u00a8\u00b0\u00b3\u00b7\u00ba\u00c3\u00ca\u00d4")
        buf.write("\u00df\u00ea\u00f0\u00f5\u00f9\u0100\u0109\u0114\u0123")
        buf.write("\u012a\u012f\u0132\u0138\u013f\u0145\u0150\u0161\u016b")
        buf.write("\u017a\u0180\u0186\u018d\u0191\u0197")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_list" ):
                return visitor.visitDeclare_list(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare" ):
                return visitor.visitDeclare(self)
            else:
                return visitor.visitChildren(self)




    def declare(self):

        localctx = ZCodeParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BOOL_TYP, ZCodeParser.NUM_TYP, ZCodeParser.STR_TYP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.var_declare()
                self.state = 112
                self.newlines()
                pass
            elif token in [ZCodeParser.FUNC]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlines" ):
                return visitor.visitNewlines(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = ZCodeParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_declare)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.implicit_var()
                pass
            elif token in [ZCodeParser.BOOL_TYP, ZCodeParser.NUM_TYP, ZCodeParser.STR_TYP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.keyword_var()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_var" ):
                return visitor.visitImplicit_var(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_var" ):
                return visitor.visitKeyword_var(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==ZCodeParser.LSB:
                self.state = 134
                self.match(ZCodeParser.LSB)
                self.state = 135
                self.numList_prime()
                self.state = 136
                self.match(ZCodeParser.RSB)


            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN_OPS:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamic_var" ):
                return visitor.visitDynamic_var(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==ZCodeParser.ASSIGN_OPS:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declare" ):
                return visitor.visitFunc_declare(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = ZCodeParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramList)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL_TYP, ZCodeParser.NUM_TYP, ZCodeParser.STR_TYP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.paramList_prime()
                pass
            elif token in [ZCodeParser.RB]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList_prime" ):
                return visitor.visitParamList_prime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==ZCodeParser.LSB:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




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
                if _la==ZCodeParser.NEWLINE:
                    self.state = 176
                    self.newlines()


                self.state = 181
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.RETURN]:
                    self.state = 179
                    self.return_stmt()
                    pass
                elif token in [ZCodeParser.BEGIN]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_concat" ):
                return visitor.visitExpr_concat(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_rela" ):
                return visitor.visitExpr_rela(self)
            else:
                return visitor.visitChildren(self)




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
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQS) | (1 << ZCodeParser.NEQ) | (1 << ZCodeParser.EQ) | (1 << ZCodeParser.LEQ) | (1 << ZCodeParser.GEQ) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.GT))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_logic" ):
                return visitor.visitExpr_logic(self)
            else:
                return visitor.visitChildren(self)



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
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_add" ):
                return visitor.visitExpr_add(self)
            else:
                return visitor.visitChildren(self)



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
                    if not(_la==ZCodeParser.ADD_OPS or _la==ZCodeParser.SUB_OPS):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_mul" ):
                return visitor.visitExpr_mul(self)
            else:
                return visitor.visitChildren(self)



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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL_OPS) | (1 << ZCodeParser.DIV_OPS) | (1 << ZCodeParser.MOD_OPS))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_not" ):
                return visitor.visitExpr_not(self)
            else:
                return visitor.visitChildren(self)




    def expr_not(self):

        localctx = ZCodeParser.Expr_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr_not)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(ZCodeParser.NOT)
                self.state = 236
                self.expr_not()
                pass
            elif token in [ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.SUB_OPS, ZCodeParser.BOOL_LIT, ZCodeParser.NUM_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_sign" ):
                return visitor.visitExpr_sign(self)
            else:
                return visitor.visitChildren(self)




    def expr_sign(self):

        localctx = ZCodeParser.Expr_signContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr_sign)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OPS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(ZCodeParser.SUB_OPS)
                self.state = 241
                self.expr_sign()
                pass
            elif token in [ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.BOOL_LIT, ZCodeParser.NUM_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_idx" ):
                return visitor.visitExpr_idx(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_literal)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.match(ZCodeParser.NUM_LIT)
                pass
            elif token in [ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [ZCodeParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 272
                self.match(ZCodeParser.BOOL_LIT)
                pass
            elif token in [ZCodeParser.LSB]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==ZCodeParser.NEWLINE:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmtList" ):
                return visitor.visitElif_stmtList(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmt" ):
                return visitor.visitElif_stmt(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==ZCodeParser.NEWLINE:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==ZCodeParser.NEWLINE:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==ZCodeParser.NEWLINE:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_stmt" ):
                return visitor.visitDecl_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeftSide" ):
                return visitor.visitLeftSide(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==ZCodeParser.LSB:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.LB) | (1 << ZCodeParser.LSB) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.SUB_OPS) | (1 << ZCodeParser.BOOL_LIT) | (1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.IDENTIFIER))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall_stmt" ):
                return visitor.visitFuncCall_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumList" ):
                return visitor.visitNumList(self)
            else:
                return visitor.visitChildren(self)




    def numList(self):

        localctx = ZCodeParser.NumListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_numList)
        try:
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.numList_prime()
                pass
            elif token in [ZCodeParser.EOF]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumList_prime" ):
                return visitor.visitNumList_prime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = ZCodeParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exprList)
        try:
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LB, ZCodeParser.LSB, ZCodeParser.NOT, ZCodeParser.SUB_OPS, ZCodeParser.BOOL_LIT, ZCodeParser.NUM_LIT, ZCodeParser.STRING_LIT, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.exprList_prime()
                pass
            elif token in [ZCodeParser.RB]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList_prime" ):
                return visitor.visitExprList_prime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtList" ):
                return visitor.visitStmtList(self)
            else:
                return visitor.visitChildren(self)




    def stmtList(self):

        localctx = ZCodeParser.StmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_stmtList)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BEGIN, ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BOOL_TYP, ZCodeParser.NUM_TYP, ZCodeParser.STR_TYP, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.stmtList_prime()
                pass
            elif token in [ZCodeParser.END]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtList_prime" ):
                return visitor.visitStmtList_prime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.BOOL_TYP) | (1 << ZCodeParser.NUM_TYP) | (1 << ZCodeParser.STR_TYP))) != 0)):
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
         




