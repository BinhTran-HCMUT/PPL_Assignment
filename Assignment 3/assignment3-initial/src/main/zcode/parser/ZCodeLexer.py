# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
# Trần Nguyễn Thái Bình - 2110051



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u018e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\2\7\2~\n\2\f\2\16\2\u0081\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&")
        buf.write("\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3")
        buf.write(",\3,\3,\3,\3-\3-\5-\u012a\n-\3-\5-\u012d\n-\3.\6.\u0130")
        buf.write("\n.\r.\16.\u0131\3/\3/\6/\u0136\n/\r/\16/\u0137\5/\u013a")
        buf.write("\n/\3\60\3\60\5\60\u013e\n\60\3\60\6\60\u0141\n\60\r\60")
        buf.write("\16\60\u0142\3\61\3\61\5\61\u0147\n\61\3\62\3\62\7\62")
        buf.write("\u014b\n\62\f\62\16\62\u014e\13\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\5\65\u015c\n")
        buf.write("\65\3\66\3\66\3\66\3\67\3\67\7\67\u0163\n\67\f\67\16\67")
        buf.write("\u0166\13\67\38\38\38\38\38\58\u016d\n8\39\69\u0170\n")
        buf.write("9\r9\169\u0171\39\39\3:\3:\7:\u0178\n:\f:\16:\u017b\13")
        buf.write(":\3:\5:\u017e\n:\3:\3:\3;\3;\7;\u0184\n;\f;\16;\u0187")
        buf.write("\13;\3;\3;\3;\3<\3<\3<\2\2=\3\3\5\2\7\4\t\5\13\6\r\7\17")
        buf.write("\b\21\t\23\n\25\13\27\f\31\r\33\16\35\17\37\20!\21#\22")
        buf.write("%\23\'\24)\25+\26-\27/\30\61\31\63\32\65\33\67\349\35")
        buf.write(";\36=\37? A!C\"E#G$I%K&M\'O(Q)S*U+W,Y-[\2]\2_\2a.c/e\2")
        buf.write("g\2i\2k\2m\60o\61q\62s\63u\64w\65\3\2\r\3\2\f\f\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\3\2$$\t\2))^^ddhhppttvv\6\2\f\f\17\17")
        buf.write("$$^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\13\16\16\"\"\4\3")
        buf.write("\f\f\17\17\2\u0196\2\3\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\3y\3\2\2\2\5\u0084\3\2\2\2\7\u0086")
        buf.write("\3\2\2\2\t\u008b\3\2\2\2\13\u0091\3\2\2\2\r\u0098\3\2")
        buf.write("\2\2\17\u009d\3\2\2\2\21\u00a4\3\2\2\2\23\u00a8\3\2\2")
        buf.write("\2\25\u00ac\3\2\2\2\27\u00af\3\2\2\2\31\u00b1\3\2\2\2")
        buf.write("\33\u00b3\3\2\2\2\35\u00b5\3\2\2\2\37\u00b7\3\2\2\2!\u00b9")
        buf.write("\3\2\2\2#\u00bb\3\2\2\2%\u00be\3\2\2\2\'\u00c1\3\2\2\2")
        buf.write(")\u00c3\3\2\2\2+\u00c6\3\2\2\2-\u00c8\3\2\2\2/\u00cb\3")
        buf.write("\2\2\2\61\u00cf\3\2\2\2\63\u00d2\3\2\2\2\65\u00d4\3\2")
        buf.write("\2\2\67\u00d6\3\2\2\29\u00d8\3\2\2\2;\u00da\3\2\2\2=\u00dc")
        buf.write("\3\2\2\2?\u00e3\3\2\2\2A\u00e7\3\2\2\2C\u00ef\3\2\2\2")
        buf.write("E\u00f4\3\2\2\2G\u00f8\3\2\2\2I\u00fe\3\2\2\2K\u0101\3")
        buf.write("\2\2\2M\u0107\3\2\2\2O\u0110\3\2\2\2Q\u0113\3\2\2\2S\u0118")
        buf.write("\3\2\2\2U\u011d\3\2\2\2W\u0123\3\2\2\2Y\u0127\3\2\2\2")
        buf.write("[\u012f\3\2\2\2]\u0133\3\2\2\2_\u013b\3\2\2\2a\u0146\3")
        buf.write("\2\2\2c\u0148\3\2\2\2e\u0152\3\2\2\2g\u0155\3\2\2\2i\u015b")
        buf.write("\3\2\2\2k\u015d\3\2\2\2m\u0160\3\2\2\2o\u016c\3\2\2\2")
        buf.write("q\u016f\3\2\2\2s\u0175\3\2\2\2u\u0181\3\2\2\2w\u018b\3")
        buf.write("\2\2\2yz\7%\2\2z{\7%\2\2{\177\3\2\2\2|~\5\5\3\2}|\3\2")
        buf.write("\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080")
        buf.write("\u0082\3\2\2\2\u0081\177\3\2\2\2\u0082\u0083\b\2\2\2\u0083")
        buf.write("\4\3\2\2\2\u0084\u0085\n\2\2\2\u0085\6\3\2\2\2\u0086\u0087")
        buf.write("\7v\2\2\u0087\u0088\7t\2\2\u0088\u0089\7w\2\2\u0089\u008a")
        buf.write("\7g\2\2\u008a\b\3\2\2\2\u008b\u008c\7h\2\2\u008c\u008d")
        buf.write("\7c\2\2\u008d\u008e\7n\2\2\u008e\u008f\7u\2\2\u008f\u0090")
        buf.write("\7g\2\2\u0090\n\3\2\2\2\u0091\u0092\7p\2\2\u0092\u0093")
        buf.write("\7w\2\2\u0093\u0094\7o\2\2\u0094\u0095\7d\2\2\u0095\u0096")
        buf.write("\7g\2\2\u0096\u0097\7t\2\2\u0097\f\3\2\2\2\u0098\u0099")
        buf.write("\7d\2\2\u0099\u009a\7q\2\2\u009a\u009b\7q\2\2\u009b\u009c")
        buf.write("\7n\2\2\u009c\16\3\2\2\2\u009d\u009e\7u\2\2\u009e\u009f")
        buf.write("\7v\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1\7k\2\2\u00a1\u00a2")
        buf.write("\7p\2\2\u00a2\u00a3\7i\2\2\u00a3\20\3\2\2\2\u00a4\u00a5")
        buf.write("\7p\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7v\2\2\u00a7\22")
        buf.write("\3\2\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab")
        buf.write("\7f\2\2\u00ab\24\3\2\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae")
        buf.write("\7t\2\2\u00ae\26\3\2\2\2\u00af\u00b0\7-\2\2\u00b0\30\3")
        buf.write("\2\2\2\u00b1\u00b2\7/\2\2\u00b2\32\3\2\2\2\u00b3\u00b4")
        buf.write("\7,\2\2\u00b4\34\3\2\2\2\u00b5\u00b6\7\61\2\2\u00b6\36")
        buf.write("\3\2\2\2\u00b7\u00b8\7\'\2\2\u00b8 \3\2\2\2\u00b9\u00ba")
        buf.write("\7?\2\2\u00ba\"\3\2\2\2\u00bb\u00bc\7#\2\2\u00bc\u00bd")
        buf.write("\7?\2\2\u00bd$\3\2\2\2\u00be\u00bf\7>\2\2\u00bf\u00c0")
        buf.write("\7/\2\2\u00c0&\3\2\2\2\u00c1\u00c2\7>\2\2\u00c2(\3\2\2")
        buf.write("\2\u00c3\u00c4\7>\2\2\u00c4\u00c5\7?\2\2\u00c5*\3\2\2")
        buf.write("\2\u00c6\u00c7\7@\2\2\u00c7,\3\2\2\2\u00c8\u00c9\7@\2")
        buf.write("\2\u00c9\u00ca\7?\2\2\u00ca.\3\2\2\2\u00cb\u00cc\7\60")
        buf.write("\2\2\u00cc\u00cd\7\60\2\2\u00cd\u00ce\7\60\2\2\u00ce\60")
        buf.write("\3\2\2\2\u00cf\u00d0\7?\2\2\u00d0\u00d1\7?\2\2\u00d1\62")
        buf.write("\3\2\2\2\u00d2\u00d3\7*\2\2\u00d3\64\3\2\2\2\u00d4\u00d5")
        buf.write("\7+\2\2\u00d5\66\3\2\2\2\u00d6\u00d7\7]\2\2\u00d78\3\2")
        buf.write("\2\2\u00d8\u00d9\7_\2\2\u00d9:\3\2\2\2\u00da\u00db\7.")
        buf.write("\2\2\u00db<\3\2\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de\7g")
        buf.write("\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7w\2\2\u00e0\u00e1")
        buf.write("\7t\2\2\u00e1\u00e2\7p\2\2\u00e2>\3\2\2\2\u00e3\u00e4")
        buf.write("\7x\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7t\2\2\u00e6@\3")
        buf.write("\2\2\2\u00e7\u00e8\7f\2\2\u00e8\u00e9\7{\2\2\u00e9\u00ea")
        buf.write("\7p\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7o\2\2\u00ec\u00ed")
        buf.write("\7k\2\2\u00ed\u00ee\7e\2\2\u00eeB\3\2\2\2\u00ef\u00f0")
        buf.write("\7h\2\2\u00f0\u00f1\7w\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3")
        buf.write("\7e\2\2\u00f3D\3\2\2\2\u00f4\u00f5\7h\2\2\u00f5\u00f6")
        buf.write("\7q\2\2\u00f6\u00f7\7t\2\2\u00f7F\3\2\2\2\u00f8\u00f9")
        buf.write("\7w\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc")
        buf.write("\7k\2\2\u00fc\u00fd\7n\2\2\u00fdH\3\2\2\2\u00fe\u00ff")
        buf.write("\7d\2\2\u00ff\u0100\7{\2\2\u0100J\3\2\2\2\u0101\u0102")
        buf.write("\7d\2\2\u0102\u0103\7t\2\2\u0103\u0104\7g\2\2\u0104\u0105")
        buf.write("\7c\2\2\u0105\u0106\7m\2\2\u0106L\3\2\2\2\u0107\u0108")
        buf.write("\7e\2\2\u0108\u0109\7q\2\2\u0109\u010a\7p\2\2\u010a\u010b")
        buf.write("\7v\2\2\u010b\u010c\7k\2\2\u010c\u010d\7p\2\2\u010d\u010e")
        buf.write("\7w\2\2\u010e\u010f\7g\2\2\u010fN\3\2\2\2\u0110\u0111")
        buf.write("\7k\2\2\u0111\u0112\7h\2\2\u0112P\3\2\2\2\u0113\u0114")
        buf.write("\7g\2\2\u0114\u0115\7n\2\2\u0115\u0116\7u\2\2\u0116\u0117")
        buf.write("\7g\2\2\u0117R\3\2\2\2\u0118\u0119\7g\2\2\u0119\u011a")
        buf.write("\7n\2\2\u011a\u011b\7k\2\2\u011b\u011c\7h\2\2\u011cT\3")
        buf.write("\2\2\2\u011d\u011e\7d\2\2\u011e\u011f\7g\2\2\u011f\u0120")
        buf.write("\7i\2\2\u0120\u0121\7k\2\2\u0121\u0122\7p\2\2\u0122V\3")
        buf.write("\2\2\2\u0123\u0124\7g\2\2\u0124\u0125\7p\2\2\u0125\u0126")
        buf.write("\7f\2\2\u0126X\3\2\2\2\u0127\u0129\5[.\2\u0128\u012a\5")
        buf.write("]/\2\u0129\u0128\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012c")
        buf.write("\3\2\2\2\u012b\u012d\5_\60\2\u012c\u012b\3\2\2\2\u012c")
        buf.write("\u012d\3\2\2\2\u012dZ\3\2\2\2\u012e\u0130\t\3\2\2\u012f")
        buf.write("\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u012f\3\2\2\2")
        buf.write("\u0131\u0132\3\2\2\2\u0132\\\3\2\2\2\u0133\u0139\7\60")
        buf.write("\2\2\u0134\u0136\t\3\2\2\u0135\u0134\3\2\2\2\u0136\u0137")
        buf.write("\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138")
        buf.write("\u013a\3\2\2\2\u0139\u0135\3\2\2\2\u0139\u013a\3\2\2\2")
        buf.write("\u013a^\3\2\2\2\u013b\u013d\t\4\2\2\u013c\u013e\t\5\2")
        buf.write("\2\u013d\u013c\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0140")
        buf.write("\3\2\2\2\u013f\u0141\t\3\2\2\u0140\u013f\3\2\2\2\u0141")
        buf.write("\u0142\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2")
        buf.write("\u0143`\3\2\2\2\u0144\u0147\5\7\4\2\u0145\u0147\5\t\5")
        buf.write("\2\u0146\u0144\3\2\2\2\u0146\u0145\3\2\2\2\u0147b\3\2")
        buf.write("\2\2\u0148\u014c\t\6\2\2\u0149\u014b\5i\65\2\u014a\u0149")
        buf.write("\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c")
        buf.write("\u014d\3\2\2\2\u014d\u014f\3\2\2\2\u014e\u014c\3\2\2\2")
        buf.write("\u014f\u0150\t\6\2\2\u0150\u0151\b\62\3\2\u0151d\3\2\2")
        buf.write("\2\u0152\u0153\7^\2\2\u0153\u0154\t\7\2\2\u0154f\3\2\2")
        buf.write("\2\u0155\u0156\7)\2\2\u0156\u0157\7$\2\2\u0157h\3\2\2")
        buf.write("\2\u0158\u015c\5g\64\2\u0159\u015c\5e\63\2\u015a\u015c")
        buf.write("\n\b\2\2\u015b\u0158\3\2\2\2\u015b\u0159\3\2\2\2\u015b")
        buf.write("\u015a\3\2\2\2\u015cj\3\2\2\2\u015d\u015e\7^\2\2\u015e")
        buf.write("\u015f\n\7\2\2\u015fl\3\2\2\2\u0160\u0164\t\t\2\2\u0161")
        buf.write("\u0163\t\n\2\2\u0162\u0161\3\2\2\2\u0163\u0166\3\2\2\2")
        buf.write("\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165n\3\2\2")
        buf.write("\2\u0166\u0164\3\2\2\2\u0167\u016d\7\f\2\2\u0168\u0169")
        buf.write("\7\17\2\2\u0169\u016a\7\f\2\2\u016a\u016b\3\2\2\2\u016b")
        buf.write("\u016d\b8\4\2\u016c\u0167\3\2\2\2\u016c\u0168\3\2\2\2")
        buf.write("\u016dp\3\2\2\2\u016e\u0170\t\13\2\2\u016f\u016e\3\2\2")
        buf.write("\2\u0170\u0171\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172")
        buf.write("\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0174\b9\2\2\u0174")
        buf.write("r\3\2\2\2\u0175\u0179\7$\2\2\u0176\u0178\5i\65\2\u0177")
        buf.write("\u0176\3\2\2\2\u0178\u017b\3\2\2\2\u0179\u0177\3\2\2\2")
        buf.write("\u0179\u017a\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3")
        buf.write("\2\2\2\u017c\u017e\t\f\2\2\u017d\u017c\3\2\2\2\u017e\u017f")
        buf.write("\3\2\2\2\u017f\u0180\b:\5\2\u0180t\3\2\2\2\u0181\u0185")
        buf.write("\7$\2\2\u0182\u0184\5i\65\2\u0183\u0182\3\2\2\2\u0184")
        buf.write("\u0187\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2")
        buf.write("\u0186\u0188\3\2\2\2\u0187\u0185\3\2\2\2\u0188\u0189\5")
        buf.write("k\66\2\u0189\u018a\b;\6\2\u018av\3\2\2\2\u018b\u018c\13")
        buf.write("\2\2\2\u018c\u018d\b<\7\2\u018dx\3\2\2\2\24\2\177\u0129")
        buf.write("\u012c\u0131\u0137\u0139\u013d\u0142\u0146\u014c\u015b")
        buf.write("\u0164\u016c\u0171\u0179\u017d\u0185\b\b\2\2\3\62\2\3")
        buf.write("8\3\3:\4\3;\5\3<\6")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CMT = 1
    TRUE = 2
    FALSE = 3
    NUMBER = 4
    BOOL = 5
    STRING = 6
    NOT = 7
    AND = 8
    OR = 9
    ADD = 10
    SUB = 11
    MUL = 12
    DIV = 13
    MOD = 14
    NUMEQ = 15
    NEQ = 16
    ASSIGN = 17
    LT = 18
    LEQ = 19
    GT = 20
    GEQ = 21
    CONCAT = 22
    STREQ = 23
    R_OPEN = 24
    R_CLOSE = 25
    SQ_OPEN = 26
    SQ_CLOSE = 27
    COMMA = 28
    RETURN = 29
    VAR = 30
    DYNAMIC = 31
    FUNC = 32
    FOR = 33
    UNTIL = 34
    BY = 35
    BREAK = 36
    CONTINUE = 37
    IF = 38
    ELSE = 39
    ELIF = 40
    BEGIN = 41
    END = 42
    NUMLIT = 43
    BOOLLIT = 44
    STRINGLIT = 45
    ID = 46
    NEWLINE = 47
    WS = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50
    ERROR_TOKEN = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'not'", 
            "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'!='", 
            "'<-'", "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'('", 
            "')'", "'['", "']'", "','", "'return'", "'var'", "'dynamic'", 
            "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
            "'if'", "'else'", "'elif'", "'begin'", "'end'" ]

    symbolicNames = [ "<INVALID>",
            "CMT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "NOT", "AND", 
            "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "NUMEQ", "NEQ", "ASSIGN", 
            "LT", "LEQ", "GT", "GEQ", "CONCAT", "STREQ", "R_OPEN", "R_CLOSE", 
            "SQ_OPEN", "SQ_CLOSE", "COMMA", "RETURN", "VAR", "DYNAMIC", 
            "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
            "ELIF", "BEGIN", "END", "NUMLIT", "BOOLLIT", "STRINGLIT", "ID", 
            "NEWLINE", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    ruleNames = [ "CMT", "CMTCHAR", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                  "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "NUMEQ", "NEQ", "ASSIGN", "LT", "LEQ", "GT", "GEQ", "CONCAT", 
                  "STREQ", "R_OPEN", "R_CLOSE", "SQ_OPEN", "SQ_CLOSE", "COMMA", 
                  "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                  "NUMLIT", "INTPART", "DECPART", "EXPPART", "BOOLLIT", 
                  "STRINGLIT", "ESC_STR", "DQ_STR", "CHAR", "INVALID_ESC", 
                  "ID", "NEWLINE", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_TOKEN" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[48] = self.STRINGLIT_action 
            actions[54] = self.NEWLINE_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            actions[58] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	temp = self.text
            	self.text = temp[1:-1]

     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = '\n'
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                ESC = ['\r', '\n']
                text = str(self.text)
                if text[-1] in ESC:
            	    raise UncloseString(text[1:-1])
                else: 
                    raise UncloseString(text[1:]) 

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


