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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u01ac\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3w\n\3\3\4\3\4\5\4{\n\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\5\5\u0083\n\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u008b\n")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0095\n\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\5\t\u00a6\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u00b0\n\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\5\r\u00bb")
        buf.write("\n\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\5\20\u00c9\n\20\3\21\3\21\5\21\u00cd\n\21\3")
        buf.write("\22\3\22\5\22\u00d1\n\22\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00d8\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00e1")
        buf.write("\n\24\3\25\3\25\5\25\u00e5\n\25\3\26\3\26\5\26\u00e9\n")
        buf.write("\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u00f2\n\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\5\31\u0103\n\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\5\33\u0111")
        buf.write("\n\33\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\5\36")
        buf.write("\u011c\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3 \3 \3!\3!\3\"\3\"\3\"\5\"\u012e\n\"\3#\3#\3#\3#")
        buf.write("\3#\3$\3$\5$\u0137\n$\3%\3%\3%\3%\3%\5%\u013e\n%\3&\3")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\3\'\5\'\u0149\n\'\3(\3(\3(\5(\u014e")
        buf.write("\n(\3)\3)\5)\u0152\n)\3*\3*\3*\3*\3*\5*\u0159\n*\3+\3")
        buf.write("+\3+\3+\3+\5+\u0160\n+\3,\3,\3,\3,\3,\3,\7,\u0168\n,\f")
        buf.write(",\16,\u016b\13,\3-\3-\3-\3-\3-\3-\7-\u0173\n-\f-\16-\u0176")
        buf.write("\13-\3.\3.\3.\3.\3.\3.\7.\u017e\n.\f.\16.\u0181\13.\3")
        buf.write("/\3/\3/\5/\u0186\n/\3\60\3\60\3\60\5\60\u018b\n\60\3\61")
        buf.write("\3\61\5\61\u018f\n\61\3\61\3\61\5\61\u0193\n\61\3\62\3")
        buf.write("\62\3\62\3\62\3\63\3\63\3\63\3\63\5\63\u019d\n\63\3\64")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\3\67\2\5VXZ8\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjl\2")
        buf.write("\b\3\2\6\b\3\2\n\13\3\2\f\r\3\2\16\20\5\2\21\22\24\27")
        buf.write("\31\31\5\2\4\5--/\60\2\u01a1\2n\3\2\2\2\4v\3\2\2\2\6z")
        buf.write("\3\2\2\2\b\u0082\3\2\2\2\n\u008a\3\2\2\2\f\u0094\3\2\2")
        buf.write("\2\16\u0096\3\2\2\2\20\u00a5\3\2\2\2\22\u00a7\3\2\2\2")
        buf.write("\24\u00af\3\2\2\2\26\u00b1\3\2\2\2\30\u00ba\3\2\2\2\32")
        buf.write("\u00bc\3\2\2\2\34\u00be\3\2\2\2\36\u00c8\3\2\2\2 \u00cc")
        buf.write("\3\2\2\2\"\u00d0\3\2\2\2$\u00d7\3\2\2\2&\u00e0\3\2\2\2")
        buf.write("(\u00e4\3\2\2\2*\u00e8\3\2\2\2,\u00f1\3\2\2\2.\u00f5\3")
        buf.write("\2\2\2\60\u0102\3\2\2\2\62\u0104\3\2\2\2\64\u0110\3\2")
        buf.write("\2\2\66\u0112\3\2\2\28\u0114\3\2\2\2:\u011b\3\2\2\2<\u011d")
        buf.write("\3\2\2\2>\u0126\3\2\2\2@\u0128\3\2\2\2B\u012d\3\2\2\2")
        buf.write("D\u012f\3\2\2\2F\u0136\3\2\2\2H\u013d\3\2\2\2J\u013f\3")
        buf.write("\2\2\2L\u0148\3\2\2\2N\u014d\3\2\2\2P\u0151\3\2\2\2R\u0158")
        buf.write("\3\2\2\2T\u015f\3\2\2\2V\u0161\3\2\2\2X\u016c\3\2\2\2")
        buf.write("Z\u0177\3\2\2\2\\\u0185\3\2\2\2^\u018a\3\2\2\2`\u0192")
        buf.write("\3\2\2\2b\u0194\3\2\2\2d\u019c\3\2\2\2f\u019e\3\2\2\2")
        buf.write("h\u01a2\3\2\2\2j\u01a7\3\2\2\2l\u01a9\3\2\2\2no\5P)\2")
        buf.write("op\5\4\3\2pq\7\2\2\3q\3\3\2\2\2rs\5\6\4\2st\5\4\3\2tw")
        buf.write("\3\2\2\2uw\5\6\4\2vr\3\2\2\2vu\3\2\2\2w\5\3\2\2\2x{\5")
        buf.write("\b\5\2y{\5\34\17\2zx\3\2\2\2zy\3\2\2\2{|\3\2\2\2|}\5N")
        buf.write("(\2}\7\3\2\2\2~\u0083\5\f\7\2\177\u0083\5\16\b\2\u0080")
        buf.write("\u0083\5\20\t\2\u0081\u0083\5\n\6\2\u0082~\3\2\2\2\u0082")
        buf.write("\177\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2\2\2\u0083")
        buf.write("\t\3\2\2\2\u0084\u0085\7!\2\2\u0085\u008b\7\60\2\2\u0086")
        buf.write("\u0087\7!\2\2\u0087\u0088\7\60\2\2\u0088\u0089\7\23\2")
        buf.write("\2\u0089\u008b\5R*\2\u008a\u0084\3\2\2\2\u008a\u0086\3")
        buf.write("\2\2\2\u008b\13\3\2\2\2\u008c\u008d\5\32\16\2\u008d\u008e")
        buf.write("\7\60\2\2\u008e\u0095\3\2\2\2\u008f\u0090\5\32\16\2\u0090")
        buf.write("\u0091\7\60\2\2\u0091\u0092\7\23\2\2\u0092\u0093\5R*\2")
        buf.write("\u0093\u0095\3\2\2\2\u0094\u008c\3\2\2\2\u0094\u008f\3")
        buf.write("\2\2\2\u0095\r\3\2\2\2\u0096\u0097\7 \2\2\u0097\u0098")
        buf.write("\7\60\2\2\u0098\u0099\7\23\2\2\u0099\u009a\5R*\2\u009a")
        buf.write("\17\3\2\2\2\u009b\u009c\5\32\16\2\u009c\u009d\7\60\2\2")
        buf.write("\u009d\u009e\5\22\n\2\u009e\u00a6\3\2\2\2\u009f\u00a0")
        buf.write("\5\32\16\2\u00a0\u00a1\7\60\2\2\u00a1\u00a2\5\22\n\2\u00a2")
        buf.write("\u00a3\7\23\2\2\u00a3\u00a4\5R*\2\u00a4\u00a6\3\2\2\2")
        buf.write("\u00a5\u009b\3\2\2\2\u00a5\u009f\3\2\2\2\u00a6\21\3\2")
        buf.write("\2\2\u00a7\u00a8\7\34\2\2\u00a8\u00a9\5\24\13\2\u00a9")
        buf.write("\u00aa\7\35\2\2\u00aa\23\3\2\2\2\u00ab\u00ac\7-\2\2\u00ac")
        buf.write("\u00ad\7\36\2\2\u00ad\u00b0\5\24\13\2\u00ae\u00b0\7-\2")
        buf.write("\2\u00af\u00ab\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0\25\3")
        buf.write("\2\2\2\u00b1\u00b2\7\34\2\2\u00b2\u00b3\5\30\r\2\u00b3")
        buf.write("\u00b4\7\35\2\2\u00b4\27\3\2\2\2\u00b5\u00b6\5R*\2\u00b6")
        buf.write("\u00b7\7\36\2\2\u00b7\u00b8\5\30\r\2\u00b8\u00bb\3\2\2")
        buf.write("\2\u00b9\u00bb\5R*\2\u00ba\u00b5\3\2\2\2\u00ba\u00b9\3")
        buf.write("\2\2\2\u00bb\31\3\2\2\2\u00bc\u00bd\t\2\2\2\u00bd\33\3")
        buf.write("\2\2\2\u00be\u00bf\7\"\2\2\u00bf\u00c0\7\60\2\2\u00c0")
        buf.write("\u00c1\7\32\2\2\u00c1\u00c2\5\"\22\2\u00c2\u00c3\7\33")
        buf.write("\2\2\u00c3\u00c4\5P)\2\u00c4\u00c5\5\36\20\2\u00c5\35")
        buf.write("\3\2\2\2\u00c6\u00c9\5 \21\2\u00c7\u00c9\3\2\2\2\u00c8")
        buf.write("\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9\37\3\2\2\2\u00ca")
        buf.write("\u00cd\5B\"\2\u00cb\u00cd\5J&\2\u00cc\u00ca\3\2\2\2\u00cc")
        buf.write("\u00cb\3\2\2\2\u00cd!\3\2\2\2\u00ce\u00d1\5$\23\2\u00cf")
        buf.write("\u00d1\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00cf\3\2\2\2")
        buf.write("\u00d1#\3\2\2\2\u00d2\u00d3\5&\24\2\u00d3\u00d4\7\36\2")
        buf.write("\2\u00d4\u00d5\5$\23\2\u00d5\u00d8\3\2\2\2\u00d6\u00d8")
        buf.write("\5&\24\2\u00d7\u00d2\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8")
        buf.write("%\3\2\2\2\u00d9\u00da\5\32\16\2\u00da\u00db\7\60\2\2\u00db")
        buf.write("\u00e1\3\2\2\2\u00dc\u00dd\5\32\16\2\u00dd\u00de\7\60")
        buf.write("\2\2\u00de\u00df\5\22\n\2\u00df\u00e1\3\2\2\2\u00e0\u00d9")
        buf.write("\3\2\2\2\u00e0\u00dc\3\2\2\2\u00e1\'\3\2\2\2\u00e2\u00e5")
        buf.write("\5,\27\2\u00e3\u00e5\5*\26\2\u00e4\u00e2\3\2\2\2\u00e4")
        buf.write("\u00e3\3\2\2\2\u00e5)\3\2\2\2\u00e6\u00e9\5.\30\2\u00e7")
        buf.write("\u00e9\5<\37\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3\2\2\2")
        buf.write("\u00e9+\3\2\2\2\u00ea\u00f2\5\66\34\2\u00eb\u00f2\58\35")
        buf.write("\2\u00ec\u00f2\5D#\2\u00ed\u00f2\5> \2\u00ee\u00f2\5@")
        buf.write("!\2\u00ef\u00f2\5B\"\2\u00f0\u00f2\5J&\2\u00f1\u00ea\3")
        buf.write("\2\2\2\u00f1\u00eb\3\2\2\2\u00f1\u00ec\3\2\2\2\u00f1\u00ed")
        buf.write("\3\2\2\2\u00f1\u00ee\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\5N(\2\u00f4")
        buf.write("-\3\2\2\2\u00f5\u00f6\7(\2\2\u00f6\u00f7\7\32\2\2\u00f7")
        buf.write("\u00f8\5R*\2\u00f8\u00f9\7\33\2\2\u00f9\u00fa\5P)\2\u00fa")
        buf.write("\u00fb\5(\25\2\u00fb\u00fc\5\60\31\2\u00fc\u00fd\5\64")
        buf.write("\33\2\u00fd/\3\2\2\2\u00fe\u00ff\5\62\32\2\u00ff\u0100")
        buf.write("\5\60\31\2\u0100\u0103\3\2\2\2\u0101\u0103\3\2\2\2\u0102")
        buf.write("\u00fe\3\2\2\2\u0102\u0101\3\2\2\2\u0103\61\3\2\2\2\u0104")
        buf.write("\u0105\7*\2\2\u0105\u0106\7\32\2\2\u0106\u0107\5R*\2\u0107")
        buf.write("\u0108\7\33\2\2\u0108\u0109\5P)\2\u0109\u010a\5(\25\2")
        buf.write("\u010a\63\3\2\2\2\u010b\u010c\7)\2\2\u010c\u010d\5P)\2")
        buf.write("\u010d\u010e\5(\25\2\u010e\u0111\3\2\2\2\u010f\u0111\3")
        buf.write("\2\2\2\u0110\u010b\3\2\2\2\u0110\u010f\3\2\2\2\u0111\65")
        buf.write("\3\2\2\2\u0112\u0113\5\b\5\2\u0113\67\3\2\2\2\u0114\u0115")
        buf.write("\5:\36\2\u0115\u0116\7\23\2\2\u0116\u0117\5R*\2\u0117")
        buf.write("9\3\2\2\2\u0118\u0119\7\60\2\2\u0119\u011c\5b\62\2\u011a")
        buf.write("\u011c\7\60\2\2\u011b\u0118\3\2\2\2\u011b\u011a\3\2\2")
        buf.write("\2\u011c;\3\2\2\2\u011d\u011e\7#\2\2\u011e\u011f\7\60")
        buf.write("\2\2\u011f\u0120\7$\2\2\u0120\u0121\5R*\2\u0121\u0122")
        buf.write("\7%\2\2\u0122\u0123\5R*\2\u0123\u0124\5P)\2\u0124\u0125")
        buf.write("\5(\25\2\u0125=\3\2\2\2\u0126\u0127\7&\2\2\u0127?\3\2")
        buf.write("\2\2\u0128\u0129\7\'\2\2\u0129A\3\2\2\2\u012a\u012b\7")
        buf.write("\37\2\2\u012b\u012e\5R*\2\u012c\u012e\7\37\2\2\u012d\u012a")
        buf.write("\3\2\2\2\u012d\u012c\3\2\2\2\u012eC\3\2\2\2\u012f\u0130")
        buf.write("\7\60\2\2\u0130\u0131\7\32\2\2\u0131\u0132\5F$\2\u0132")
        buf.write("\u0133\7\33\2\2\u0133E\3\2\2\2\u0134\u0137\5H%\2\u0135")
        buf.write("\u0137\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0135\3\2\2\2")
        buf.write("\u0137G\3\2\2\2\u0138\u0139\5R*\2\u0139\u013a\7\36\2\2")
        buf.write("\u013a\u013b\5H%\2\u013b\u013e\3\2\2\2\u013c\u013e\5R")
        buf.write("*\2\u013d\u0138\3\2\2\2\u013d\u013c\3\2\2\2\u013eI\3\2")
        buf.write("\2\2\u013f\u0140\7+\2\2\u0140\u0141\5N(\2\u0141\u0142")
        buf.write("\5L\'\2\u0142\u0143\7,\2\2\u0143K\3\2\2\2\u0144\u0145")
        buf.write("\5(\25\2\u0145\u0146\5L\'\2\u0146\u0149\3\2\2\2\u0147")
        buf.write("\u0149\3\2\2\2\u0148\u0144\3\2\2\2\u0148\u0147\3\2\2\2")
        buf.write("\u0149M\3\2\2\2\u014a\u014b\7\61\2\2\u014b\u014e\5N(\2")
        buf.write("\u014c\u014e\7\61\2\2\u014d\u014a\3\2\2\2\u014d\u014c")
        buf.write("\3\2\2\2\u014eO\3\2\2\2\u014f\u0152\5N(\2\u0150\u0152")
        buf.write("\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0150\3\2\2\2\u0152")
        buf.write("Q\3\2\2\2\u0153\u0154\5T+\2\u0154\u0155\7\30\2\2\u0155")
        buf.write("\u0156\5T+\2\u0156\u0159\3\2\2\2\u0157\u0159\5T+\2\u0158")
        buf.write("\u0153\3\2\2\2\u0158\u0157\3\2\2\2\u0159S\3\2\2\2\u015a")
        buf.write("\u015b\5V,\2\u015b\u015c\5j\66\2\u015c\u015d\5V,\2\u015d")
        buf.write("\u0160\3\2\2\2\u015e\u0160\5V,\2\u015f\u015a\3\2\2\2\u015f")
        buf.write("\u015e\3\2\2\2\u0160U\3\2\2\2\u0161\u0162\b,\1\2\u0162")
        buf.write("\u0163\5X-\2\u0163\u0169\3\2\2\2\u0164\u0165\f\4\2\2\u0165")
        buf.write("\u0166\t\3\2\2\u0166\u0168\5X-\2\u0167\u0164\3\2\2\2\u0168")
        buf.write("\u016b\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2")
        buf.write("\u016aW\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u016d\b-\1\2")
        buf.write("\u016d\u016e\5Z.\2\u016e\u0174\3\2\2\2\u016f\u0170\f\4")
        buf.write("\2\2\u0170\u0171\t\4\2\2\u0171\u0173\5Z.\2\u0172\u016f")
        buf.write("\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175Y\3\2\2\2\u0176\u0174\3\2\2\2\u0177")
        buf.write("\u0178\b.\1\2\u0178\u0179\5\\/\2\u0179\u017f\3\2\2\2\u017a")
        buf.write("\u017b\f\4\2\2\u017b\u017c\t\5\2\2\u017c\u017e\5\\/\2")
        buf.write("\u017d\u017a\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3")
        buf.write("\2\2\2\u017f\u0180\3\2\2\2\u0180[\3\2\2\2\u0181\u017f")
        buf.write("\3\2\2\2\u0182\u0183\7\t\2\2\u0183\u0186\5\\/\2\u0184")
        buf.write("\u0186\5^\60\2\u0185\u0182\3\2\2\2\u0185\u0184\3\2\2\2")
        buf.write("\u0186]\3\2\2\2\u0187\u0188\7\r\2\2\u0188\u018b\5^\60")
        buf.write("\2\u0189\u018b\5`\61\2\u018a\u0187\3\2\2\2\u018a\u0189")
        buf.write("\3\2\2\2\u018b_\3\2\2\2\u018c\u018f\7\60\2\2\u018d\u018f")
        buf.write("\5h\65\2\u018e\u018c\3\2\2\2\u018e\u018d\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190\u0193\5b\62\2\u0191\u0193\5d\63\2")
        buf.write("\u0192\u018e\3\2\2\2\u0192\u0191\3\2\2\2\u0193a\3\2\2")
        buf.write("\2\u0194\u0195\7\34\2\2\u0195\u0196\5H%\2\u0196\u0197")
        buf.write("\7\35\2\2\u0197c\3\2\2\2\u0198\u019d\5l\67\2\u0199\u019d")
        buf.write("\5\26\f\2\u019a\u019d\5h\65\2\u019b\u019d\5f\64\2\u019c")
        buf.write("\u0198\3\2\2\2\u019c\u0199\3\2\2\2\u019c\u019a\3\2\2\2")
        buf.write("\u019c\u019b\3\2\2\2\u019de\3\2\2\2\u019e\u019f\7\32\2")
        buf.write("\2\u019f\u01a0\5R*\2\u01a0\u01a1\7\33\2\2\u01a1g\3\2\2")
        buf.write("\2\u01a2\u01a3\7\60\2\2\u01a3\u01a4\7\32\2\2\u01a4\u01a5")
        buf.write("\5F$\2\u01a5\u01a6\7\33\2\2\u01a6i\3\2\2\2\u01a7\u01a8")
        buf.write("\t\6\2\2\u01a8k\3\2\2\2\u01a9\u01aa\t\7\2\2\u01aam\3\2")
        buf.write("\2\2%vz\u0082\u008a\u0094\u00a5\u00af\u00ba\u00c8\u00cc")
        buf.write("\u00d0\u00d7\u00e0\u00e4\u00e8\u00f1\u0102\u0110\u011b")
        buf.write("\u012d\u0136\u013d\u0148\u014d\u0151\u0158\u015f\u0169")
        buf.write("\u0174\u017f\u0185\u018a\u018e\u0192\u019c")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'true'", "'false'", "'number'", 
                     "'bool'", "'string'", "'not'", "'and'", "'or'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'='", "'!='", "'<-'", 
                     "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'('", 
                     "')'", "'['", "']'", "','", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'" ]

    symbolicNames = [ "<INVALID>", "CMT", "TRUE", "FALSE", "NUMBER", "BOOL", 
                      "STRING", "NOT", "AND", "OR", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "NUMEQ", "NEQ", "ASSIGN", "LT", "LEQ", 
                      "GT", "GEQ", "CONCAT", "STREQ", "R_OPEN", "R_CLOSE", 
                      "SQ_OPEN", "SQ_CLOSE", "COMMA", "RETURN", "VAR", "DYNAMIC", 
                      "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "ELIF", "BEGIN", "END", "NUMLIT", "BOOLLIT", 
                      "STRINGLIT", "ID", "NEWLINE", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_declist = 1
    RULE_decl = 2
    RULE_variabledec = 3
    RULE_dyndecl = 4
    RULE_typedecl = 5
    RULE_vardecl = 6
    RULE_arrdecl = 7
    RULE_dimension = 8
    RULE_numlitlist = 9
    RULE_array = 10
    RULE_vallist = 11
    RULE_typ = 12
    RULE_funcdecl = 13
    RULE_funcstmt = 14
    RULE_funcprime = 15
    RULE_paramlist = 16
    RULE_paramprime = 17
    RULE_paramdecl = 18
    RULE_stmt = 19
    RULE_condstmt = 20
    RULE_normalstmt = 21
    RULE_ifstmt = 22
    RULE_eliflist = 23
    RULE_elifpart = 24
    RULE_elsepart = 25
    RULE_varstmt = 26
    RULE_assignstmt = 27
    RULE_lhs = 28
    RULE_forstmt = 29
    RULE_breakstmt = 30
    RULE_contstmt = 31
    RULE_returnstmt = 32
    RULE_callstmt = 33
    RULE_exprlist = 34
    RULE_exprparam = 35
    RULE_blockstmt = 36
    RULE_stmtlist = 37
    RULE_newlines = 38
    RULE_null_newline = 39
    RULE_expr = 40
    RULE_expr1 = 41
    RULE_expr2 = 42
    RULE_expr3 = 43
    RULE_expr4 = 44
    RULE_expr5 = 45
    RULE_expr6 = 46
    RULE_expr7 = 47
    RULE_indexop = 48
    RULE_expr8 = 49
    RULE_subexpr = 50
    RULE_callexpr = 51
    RULE_rel_op = 52
    RULE_const = 53

    ruleNames =  [ "program", "declist", "decl", "variabledec", "dyndecl", 
                   "typedecl", "vardecl", "arrdecl", "dimension", "numlitlist", 
                   "array", "vallist", "typ", "funcdecl", "funcstmt", "funcprime", 
                   "paramlist", "paramprime", "paramdecl", "stmt", "condstmt", 
                   "normalstmt", "ifstmt", "eliflist", "elifpart", "elsepart", 
                   "varstmt", "assignstmt", "lhs", "forstmt", "breakstmt", 
                   "contstmt", "returnstmt", "callstmt", "exprlist", "exprparam", 
                   "blockstmt", "stmtlist", "newlines", "null_newline", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "indexop", "expr8", "subexpr", "callexpr", 
                   "rel_op", "const" ]

    EOF = Token.EOF
    CMT=1
    TRUE=2
    FALSE=3
    NUMBER=4
    BOOL=5
    STRING=6
    NOT=7
    AND=8
    OR=9
    ADD=10
    SUB=11
    MUL=12
    DIV=13
    MOD=14
    NUMEQ=15
    NEQ=16
    ASSIGN=17
    LT=18
    LEQ=19
    GT=20
    GEQ=21
    CONCAT=22
    STREQ=23
    R_OPEN=24
    R_CLOSE=25
    SQ_OPEN=26
    SQ_CLOSE=27
    COMMA=28
    RETURN=29
    VAR=30
    DYNAMIC=31
    FUNC=32
    FOR=33
    UNTIL=34
    BY=35
    BREAK=36
    CONTINUE=37
    IF=38
    ELSE=39
    ELIF=40
    BEGIN=41
    END=42
    NUMLIT=43
    BOOLLIT=44
    STRINGLIT=45
    ID=46
    NEWLINE=47
    WS=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50
    ERROR_TOKEN=51

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

        def null_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Null_newlineContext,0)


        def declist(self):
            return self.getTypedRuleContext(ZCodeParser.DeclistContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.null_newline()
            self.state = 109
            self.declist()
            self.state = 110
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def declist(self):
            return self.getTypedRuleContext(ZCodeParser.DeclistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclist" ):
                return visitor.visitDeclist(self)
            else:
                return visitor.visitChildren(self)




    def declist(self):

        localctx = ZCodeParser.DeclistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declist)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.decl()
                self.state = 113
                self.declist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def variabledec(self):
            return self.getTypedRuleContext(ZCodeParser.VariabledecContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.state = 118
                self.variabledec()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.state = 119
                self.funcdecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 122
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariabledecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typedecl(self):
            return self.getTypedRuleContext(ZCodeParser.TypedeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def arrdecl(self):
            return self.getTypedRuleContext(ZCodeParser.ArrdeclContext,0)


        def dyndecl(self):
            return self.getTypedRuleContext(ZCodeParser.DyndeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variabledec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariabledec" ):
                return visitor.visitVariabledec(self)
            else:
                return visitor.visitChildren(self)




    def variabledec(self):

        localctx = ZCodeParser.VariabledecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variabledec)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.typedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.arrdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.dyndecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DyndeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dyndecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDyndecl" ):
                return visitor.visitDyndecl(self)
            else:
                return visitor.visitChildren(self)




    def dyndecl(self):

        localctx = ZCodeParser.DyndeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dyndecl)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(ZCodeParser.DYNAMIC)
                self.state = 131
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(ZCodeParser.DYNAMIC)
                self.state = 133
                self.match(ZCodeParser.ID)
                self.state = 134
                self.match(ZCodeParser.ASSIGN)
                self.state = 135
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_typedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedecl" ):
                return visitor.visitTypedecl(self)
            else:
                return visitor.visitChildren(self)




    def typedecl(self):

        localctx = ZCodeParser.TypedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typedecl)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.typ()
                self.state = 139
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.typ()
                self.state = 142
                self.match(ZCodeParser.ID)
                self.state = 143
                self.match(ZCodeParser.ASSIGN)
                self.state = 144
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(ZCodeParser.VAR)
            self.state = 149
            self.match(ZCodeParser.ID)
            self.state = 150
            self.match(ZCodeParser.ASSIGN)
            self.state = 151
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def dimension(self):
            return self.getTypedRuleContext(ZCodeParser.DimensionContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrdecl" ):
                return visitor.visitArrdecl(self)
            else:
                return visitor.visitChildren(self)




    def arrdecl(self):

        localctx = ZCodeParser.ArrdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arrdecl)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.typ()
                self.state = 154
                self.match(ZCodeParser.ID)
                self.state = 155
                self.dimension()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.typ()
                self.state = 158
                self.match(ZCodeParser.ID)
                self.state = 159
                self.dimension()
                self.state = 160
                self.match(ZCodeParser.ASSIGN)
                self.state = 161
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ_OPEN(self):
            return self.getToken(ZCodeParser.SQ_OPEN, 0)

        def numlitlist(self):
            return self.getTypedRuleContext(ZCodeParser.NumlitlistContext,0)


        def SQ_CLOSE(self):
            return self.getToken(ZCodeParser.SQ_CLOSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = ZCodeParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(ZCodeParser.SQ_OPEN)
            self.state = 166
            self.numlitlist()
            self.state = 167
            self.match(ZCodeParser.SQ_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumlitlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def numlitlist(self):
            return self.getTypedRuleContext(ZCodeParser.NumlitlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numlitlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumlitlist" ):
                return visitor.visitNumlitlist(self)
            else:
                return visitor.visitChildren(self)




    def numlitlist(self):

        localctx = ZCodeParser.NumlitlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_numlitlist)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(ZCodeParser.NUMLIT)
                self.state = 170
                self.match(ZCodeParser.COMMA)
                self.state = 171
                self.numlitlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(ZCodeParser.NUMLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ_OPEN(self):
            return self.getToken(ZCodeParser.SQ_OPEN, 0)

        def vallist(self):
            return self.getTypedRuleContext(ZCodeParser.VallistContext,0)


        def SQ_CLOSE(self):
            return self.getToken(ZCodeParser.SQ_CLOSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(ZCodeParser.SQ_OPEN)
            self.state = 176
            self.vallist()
            self.state = 177
            self.match(ZCodeParser.SQ_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VallistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def vallist(self):
            return self.getTypedRuleContext(ZCodeParser.VallistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vallist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVallist" ):
                return visitor.visitVallist(self)
            else:
                return visitor.visitChildren(self)




    def vallist(self):

        localctx = ZCodeParser.VallistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_vallist)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.expr()
                self.state = 180
                self.match(ZCodeParser.COMMA)
                self.state = 181
                self.vallist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.expr()
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

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
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


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def R_OPEN(self):
            return self.getToken(ZCodeParser.R_OPEN, 0)

        def paramlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlistContext,0)


        def R_CLOSE(self):
            return self.getToken(ZCodeParser.R_CLOSE, 0)

        def null_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Null_newlineContext,0)


        def funcstmt(self):
            return self.getTypedRuleContext(ZCodeParser.FuncstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(ZCodeParser.FUNC)
            self.state = 189
            self.match(ZCodeParser.ID)
            self.state = 190
            self.match(ZCodeParser.R_OPEN)
            self.state = 191
            self.paramlist()
            self.state = 192
            self.match(ZCodeParser.R_CLOSE)
            self.state = 193
            self.null_newline()
            self.state = 194
            self.funcstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcprime(self):
            return self.getTypedRuleContext(ZCodeParser.FuncprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncstmt" ):
                return visitor.visitFuncstmt(self)
            else:
                return visitor.visitChildren(self)




    def funcstmt(self):

        localctx = ZCodeParser.FuncstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_funcstmt)
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.funcprime()
                pass
            elif token in [ZCodeParser.NEWLINE]:
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


    class FuncprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncprime" ):
                return visitor.visitFuncprime(self)
            else:
                return visitor.visitChildren(self)




    def funcprime(self):

        localctx = ZCodeParser.FuncprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_funcprime)
        try:
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.returnstmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.blockstmt()
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


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_paramlist)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.paramprime()
                pass
            elif token in [ZCodeParser.R_CLOSE]:
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


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramdecl(self):
            return self.getTypedRuleContext(ZCodeParser.ParamdeclContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = ZCodeParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_paramprime)
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.paramdecl()
                self.state = 209
                self.match(ZCodeParser.COMMA)
                self.state = 210
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.paramdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def dimension(self):
            return self.getTypedRuleContext(ZCodeParser.DimensionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdecl" ):
                return visitor.visitParamdecl(self)
            else:
                return visitor.visitChildren(self)




    def paramdecl(self):

        localctx = ZCodeParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_paramdecl)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.typ()
                self.state = 216
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.typ()
                self.state = 219
                self.match(ZCodeParser.ID)
                self.state = 220
                self.dimension()
                pass


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

        def normalstmt(self):
            return self.getTypedRuleContext(ZCodeParser.NormalstmtContext,0)


        def condstmt(self):
            return self.getTypedRuleContext(ZCodeParser.CondstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmt)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.normalstmt()
                pass
            elif token in [ZCodeParser.FOR, ZCodeParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.condstmt()
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


    class CondstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_condstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondstmt" ):
                return visitor.visitCondstmt(self)
            else:
                return visitor.visitChildren(self)




    def condstmt(self):

        localctx = ZCodeParser.CondstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_condstmt)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.ifstmt()
                pass
            elif token in [ZCodeParser.FOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.forstmt()
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


    class NormalstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def varstmt(self):
            return self.getTypedRuleContext(ZCodeParser.VarstmtContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(ZCodeParser.CallstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BreakstmtContext,0)


        def contstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_normalstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalstmt" ):
                return visitor.visitNormalstmt(self)
            else:
                return visitor.visitChildren(self)




    def normalstmt(self):

        localctx = ZCodeParser.NormalstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_normalstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 232
                self.varstmt()
                pass

            elif la_ == 2:
                self.state = 233
                self.assignstmt()
                pass

            elif la_ == 3:
                self.state = 234
                self.callstmt()
                pass

            elif la_ == 4:
                self.state = 235
                self.breakstmt()
                pass

            elif la_ == 5:
                self.state = 236
                self.contstmt()
                pass

            elif la_ == 6:
                self.state = 237
                self.returnstmt()
                pass

            elif la_ == 7:
                self.state = 238
                self.blockstmt()
                pass


            self.state = 241
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def R_OPEN(self):
            return self.getToken(ZCodeParser.R_OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def R_CLOSE(self):
            return self.getToken(ZCodeParser.R_CLOSE, 0)

        def null_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Null_newlineContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def elsepart(self):
            return self.getTypedRuleContext(ZCodeParser.ElsepartContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = ZCodeParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(ZCodeParser.IF)
            self.state = 244
            self.match(ZCodeParser.R_OPEN)
            self.state = 245
            self.expr()
            self.state = 246
            self.match(ZCodeParser.R_CLOSE)
            self.state = 247
            self.null_newline()
            self.state = 248
            self.stmt()
            self.state = 249
            self.eliflist()
            self.state = 250
            self.elsepart()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliflistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifpart(self):
            return self.getTypedRuleContext(ZCodeParser.ElifpartContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_eliflist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEliflist" ):
                return visitor.visitEliflist(self)
            else:
                return visitor.visitChildren(self)




    def eliflist(self):

        localctx = ZCodeParser.EliflistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_eliflist)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.elifpart()
                self.state = 253
                self.eliflist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifpartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def R_OPEN(self):
            return self.getToken(ZCodeParser.R_OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def R_CLOSE(self):
            return self.getToken(ZCodeParser.R_CLOSE, 0)

        def null_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Null_newlineContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifpart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifpart" ):
                return visitor.visitElifpart(self)
            else:
                return visitor.visitChildren(self)




    def elifpart(self):

        localctx = ZCodeParser.ElifpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elifpart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(ZCodeParser.ELIF)
            self.state = 259
            self.match(ZCodeParser.R_OPEN)
            self.state = 260
            self.expr()
            self.state = 261
            self.match(ZCodeParser.R_CLOSE)
            self.state = 262
            self.null_newline()
            self.state = 263
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsepartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def null_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Null_newlineContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elsepart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsepart" ):
                return visitor.visitElsepart(self)
            else:
                return visitor.visitChildren(self)




    def elsepart(self):

        localctx = ZCodeParser.ElsepartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elsepart)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(ZCodeParser.ELSE)
                self.state = 266
                self.null_newline()
                self.state = 267
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variabledec(self):
            return self.getTypedRuleContext(ZCodeParser.VariabledecContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_varstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarstmt" ):
                return visitor.visitVarstmt(self)
            else:
                return visitor.visitChildren(self)




    def varstmt(self):

        localctx = ZCodeParser.VarstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_varstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.variabledec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.lhs()
            self.state = 275
            self.match(ZCodeParser.ASSIGN)
            self.state = 276
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def indexop(self):
            return self.getTypedRuleContext(ZCodeParser.IndexopContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_lhs)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(ZCodeParser.ID)
                self.state = 279
                self.indexop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(ZCodeParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def null_newline(self):
            return self.getTypedRuleContext(ZCodeParser.Null_newlineContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(ZCodeParser.FOR)
            self.state = 284
            self.match(ZCodeParser.ID)
            self.state = 285
            self.match(ZCodeParser.UNTIL)
            self.state = 286
            self.expr()
            self.state = 287
            self.match(ZCodeParser.BY)
            self.state = 288
            self.expr()
            self.state = 289
            self.null_newline()
            self.state = 290
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_contstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContstmt" ):
                return visitor.visitContstmt(self)
            else:
                return visitor.visitChildren(self)




    def contstmt(self):

        localctx = ZCodeParser.ContstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_contstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = ZCodeParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_returnstmt)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(ZCodeParser.RETURN)
                self.state = 297
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.match(ZCodeParser.RETURN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def R_OPEN(self):
            return self.getToken(ZCodeParser.R_OPEN, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def R_CLOSE(self):
            return self.getToken(ZCodeParser.R_CLOSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = ZCodeParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(ZCodeParser.ID)
            self.state = 302
            self.match(ZCodeParser.R_OPEN)
            self.state = 303
            self.exprlist()
            self.state = 304
            self.match(ZCodeParser.R_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprparam(self):
            return self.getTypedRuleContext(ZCodeParser.ExprparamContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = ZCodeParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exprlist)
        try:
            self.state = 308
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.R_OPEN, ZCodeParser.SQ_OPEN, ZCodeParser.NUMLIT, ZCodeParser.STRINGLIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.exprparam()
                pass
            elif token in [ZCodeParser.R_CLOSE]:
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


    class ExprparamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def exprparam(self):
            return self.getTypedRuleContext(ZCodeParser.ExprparamContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprparam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprparam" ):
                return visitor.visitExprparam(self)
            else:
                return visitor.visitChildren(self)




    def exprparam(self):

        localctx = ZCodeParser.ExprparamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exprparam)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.expr()
                self.state = 311
                self.match(ZCodeParser.COMMA)
                self.state = 312
                self.exprparam()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = ZCodeParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(ZCodeParser.BEGIN)
            self.state = 318
            self.newlines()
            self.state = 319
            self.stmtlist()
            self.state = 320
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_stmtlist)
        try:
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.stmt()
                self.state = 323
                self.stmtlist()
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
        self.enterRule(localctx, 76, self.RULE_newlines)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.match(ZCodeParser.NEWLINE)
                self.state = 329
                self.newlines()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Null_newlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_null_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNull_newline" ):
                return visitor.visitNull_newline(self)
            else:
                return visitor.visitChildren(self)




    def null_newline(self):

        localctx = ZCodeParser.Null_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_null_newline)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.newlines()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

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

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.expr1()
                self.state = 338
                self.match(ZCodeParser.CONCAT)
                self.state = 339
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def rel_op(self):
            return self.getTypedRuleContext(ZCodeParser.Rel_opContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr1)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.expr2(0)
                self.state = 345
                self.rel_op()
                self.state = 346
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 359
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 354
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 355
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 356
                    self.expr3(0) 
                self.state = 361
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 365
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 366
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 367
                    self.expr4(0) 
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 376
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 377
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 378
                    self.expr5() 
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr5)
        try:
            self.state = 387
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.match(ZCodeParser.NOT)
                self.state = 385
                self.expr5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.R_OPEN, ZCodeParser.SQ_OPEN, ZCodeParser.NUMLIT, ZCodeParser.STRINGLIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.expr6()
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr6)
        try:
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.match(ZCodeParser.SUB)
                self.state = 390
                self.expr6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.R_OPEN, ZCodeParser.SQ_OPEN, ZCodeParser.NUMLIT, ZCodeParser.STRINGLIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.expr7()
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexop(self):
            return self.getTypedRuleContext(ZCodeParser.IndexopContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def callexpr(self):
            return self.getTypedRuleContext(ZCodeParser.CallexprContext,0)


        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr7)
        try:
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 394
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 395
                    self.callexpr()
                    pass


                self.state = 398
                self.indexop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                self.expr8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ_OPEN(self):
            return self.getToken(ZCodeParser.SQ_OPEN, 0)

        def exprparam(self):
            return self.getTypedRuleContext(ZCodeParser.ExprparamContext,0)


        def SQ_CLOSE(self):
            return self.getToken(ZCodeParser.SQ_CLOSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_indexop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexop" ):
                return visitor.visitIndexop(self)
            else:
                return visitor.visitChildren(self)




    def indexop(self):

        localctx = ZCodeParser.IndexopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_indexop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(ZCodeParser.SQ_OPEN)
            self.state = 403
            self.exprparam()
            self.state = 404
            self.match(ZCodeParser.SQ_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const(self):
            return self.getTypedRuleContext(ZCodeParser.ConstContext,0)


        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def callexpr(self):
            return self.getTypedRuleContext(ZCodeParser.CallexprContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(ZCodeParser.SubexprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr8)
        try:
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.const()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.array()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 408
                self.callexpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 409
                self.subexpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def R_OPEN(self):
            return self.getToken(ZCodeParser.R_OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def R_CLOSE(self):
            return self.getToken(ZCodeParser.R_CLOSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_subexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = ZCodeParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(ZCodeParser.R_OPEN)
            self.state = 413
            self.expr()
            self.state = 414
            self.match(ZCodeParser.R_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def R_OPEN(self):
            return self.getToken(ZCodeParser.R_OPEN, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def R_CLOSE(self):
            return self.getToken(ZCodeParser.R_CLOSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_callexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallexpr" ):
                return visitor.visitCallexpr(self)
            else:
                return visitor.visitChildren(self)




    def callexpr(self):

        localctx = ZCodeParser.CallexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_callexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(ZCodeParser.ID)
            self.state = 417
            self.match(ZCodeParser.R_OPEN)
            self.state = 418
            self.exprlist()
            self.state = 419
            self.match(ZCodeParser.R_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMEQ(self):
            return self.getToken(ZCodeParser.NUMEQ, 0)

        def STREQ(self):
            return self.getToken(ZCodeParser.STREQ, 0)

        def NEQ(self):
            return self.getToken(ZCodeParser.NEQ, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LEQ(self):
            return self.getToken(ZCodeParser.LEQ, 0)

        def GEQ(self):
            return self.getToken(ZCodeParser.GEQ, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_rel_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_op" ):
                return visitor.visitRel_op(self)
            else:
                return visitor.visitChildren(self)




    def rel_op(self):

        localctx = ZCodeParser.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMEQ) | (1 << ZCodeParser.NEQ) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LEQ) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GEQ) | (1 << ZCodeParser.STREQ))) != 0)):
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


    class ConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_const

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst" ):
                return visitor.visitConst(self)
            else:
                return visitor.visitChildren(self)




    def const(self):

        localctx = ZCodeParser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.STRINGLIT) | (1 << ZCodeParser.ID))) != 0)):
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
        self._predicates[42] = self.expr2_sempred
        self._predicates[43] = self.expr3_sempred
        self._predicates[44] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




