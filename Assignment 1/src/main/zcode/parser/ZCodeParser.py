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
        buf.write("\u01e2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\7\2j\n\2\f\2\16\2m\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\5\3v\n\3\3\4\3\4\5\4z\n\4\3\4\6\4}\n\4\r\4\16\4~\3")
        buf.write("\5\3\5\3\5\3\5\5\5\u0085\n\5\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6\u008d\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0097")
        buf.write("\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\5\t\u00a8\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u00b2\n\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u00bd\n\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\7\17\u00c7\n\17\f\17\16\17\u00ca\13\17\3\17\3\17")
        buf.write("\3\20\3\20\5\20\u00d0\n\20\3\21\3\21\5\21\u00d4\n\21\3")
        buf.write("\22\3\22\5\22\u00d8\n\22\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00df\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00e8")
        buf.write("\n\24\3\25\3\25\5\25\u00ec\n\25\3\26\3\26\3\26\3\26\3")
        buf.write("\26\7\26\u00f3\n\26\f\26\16\26\u00f6\13\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\7\26\u0100\n\26\f\26\16\26")
        buf.write("\u0103\13\26\3\26\3\26\3\26\3\26\7\26\u0109\n\26\f\26")
        buf.write("\16\26\u010c\13\26\3\26\3\26\5\26\u0110\n\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\7\27\u0117\n\27\f\27\16\27\u011a\13\27")
        buf.write("\3\27\3\27\3\27\3\27\7\27\u0120\n\27\f\27\16\27\u0123")
        buf.write("\13\27\3\27\3\27\3\27\5\27\u0128\n\27\3\30\3\30\5\30\u012c")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0135\n")
        buf.write("\31\3\31\6\31\u0138\n\31\r\31\16\31\u0139\3\32\3\32\3")
        buf.write("\32\3\32\5\32\u0140\n\32\3\33\3\33\3\33\3\33\3\33\7\33")
        buf.write("\u0147\n\33\f\33\16\33\u014a\13\33\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\5\36\u0157\n\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0160\n\37\f\37")
        buf.write("\16\37\u0163\13\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\5")
        buf.write("\"\u016e\n\"\3#\3#\3#\3#\3#\3$\3$\5$\u0177\n$\3%\3%\3")
        buf.write("%\3%\3%\5%\u017e\n%\3&\3&\6&\u0182\n&\r&\16&\u0183\3&")
        buf.write("\3&\3&\3\'\3\'\3\'\3\'\5\'\u018d\n\'\3(\3(\3(\3(\3(\5")
        buf.write("(\u0194\n(\3)\3)\3)\3)\3)\5)\u019b\n)\3*\3*\3*\3*\3*\3")
        buf.write("*\7*\u01a3\n*\f*\16*\u01a6\13*\3+\3+\3+\3+\3+\3+\7+\u01ae")
        buf.write("\n+\f+\16+\u01b1\13+\3,\3,\3,\3,\3,\3,\7,\u01b9\n,\f,")
        buf.write("\16,\u01bc\13,\3-\3-\3-\5-\u01c1\n-\3.\3.\3.\5.\u01c6")
        buf.write("\n.\3/\3/\5/\u01ca\n/\3/\3/\5/\u01ce\n/\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\5\61\u01d8\n\61\3\62\3\62\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\64\2\5RTV\65\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\^`bdf\2\b\3\2\6\b\3\2\n\13\3\2\f\r\3")
        buf.write("\2\16\20\5\2\21\22\24\27\31\31\5\2\4\5--/\60\2\u01e5\2")
        buf.write("k\3\2\2\2\4u\3\2\2\2\6y\3\2\2\2\b\u0084\3\2\2\2\n\u008c")
        buf.write("\3\2\2\2\f\u0096\3\2\2\2\16\u0098\3\2\2\2\20\u00a7\3\2")
        buf.write("\2\2\22\u00a9\3\2\2\2\24\u00b1\3\2\2\2\26\u00b3\3\2\2")
        buf.write("\2\30\u00bc\3\2\2\2\32\u00be\3\2\2\2\34\u00c0\3\2\2\2")
        buf.write("\36\u00cf\3\2\2\2 \u00d3\3\2\2\2\"\u00d7\3\2\2\2$\u00de")
        buf.write("\3\2\2\2&\u00e7\3\2\2\2(\u00eb\3\2\2\2*\u010f\3\2\2\2")
        buf.write(",\u0127\3\2\2\2.\u012b\3\2\2\2\60\u0134\3\2\2\2\62\u013f")
        buf.write("\3\2\2\2\64\u0141\3\2\2\2\66\u014d\3\2\2\28\u014f\3\2")
        buf.write("\2\2:\u0156\3\2\2\2<\u0158\3\2\2\2>\u0166\3\2\2\2@\u0168")
        buf.write("\3\2\2\2B\u016d\3\2\2\2D\u016f\3\2\2\2F\u0176\3\2\2\2")
        buf.write("H\u017d\3\2\2\2J\u017f\3\2\2\2L\u018c\3\2\2\2N\u0193\3")
        buf.write("\2\2\2P\u019a\3\2\2\2R\u019c\3\2\2\2T\u01a7\3\2\2\2V\u01b2")
        buf.write("\3\2\2\2X\u01c0\3\2\2\2Z\u01c5\3\2\2\2\\\u01cd\3\2\2\2")
        buf.write("^\u01cf\3\2\2\2`\u01d7\3\2\2\2b\u01d9\3\2\2\2d\u01dd\3")
        buf.write("\2\2\2f\u01df\3\2\2\2hj\7\61\2\2ih\3\2\2\2jm\3\2\2\2k")
        buf.write("i\3\2\2\2kl\3\2\2\2ln\3\2\2\2mk\3\2\2\2no\5\4\3\2op\7")
        buf.write("\2\2\3p\3\3\2\2\2qr\5\6\4\2rs\5\4\3\2sv\3\2\2\2tv\5\6")
        buf.write("\4\2uq\3\2\2\2ut\3\2\2\2v\5\3\2\2\2wz\5\b\5\2xz\5\34\17")
        buf.write("\2yw\3\2\2\2yx\3\2\2\2z|\3\2\2\2{}\7\61\2\2|{\3\2\2\2")
        buf.write("}~\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\7\3\2\2\2\u0080")
        buf.write("\u0085\5\f\7\2\u0081\u0085\5\16\b\2\u0082\u0085\5\20\t")
        buf.write("\2\u0083\u0085\5\n\6\2\u0084\u0080\3\2\2\2\u0084\u0081")
        buf.write("\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085")
        buf.write("\t\3\2\2\2\u0086\u0087\7!\2\2\u0087\u008d\7\60\2\2\u0088")
        buf.write("\u0089\7!\2\2\u0089\u008a\7\60\2\2\u008a\u008b\7\23\2")
        buf.write("\2\u008b\u008d\5N(\2\u008c\u0086\3\2\2\2\u008c\u0088\3")
        buf.write("\2\2\2\u008d\13\3\2\2\2\u008e\u008f\5\32\16\2\u008f\u0090")
        buf.write("\7\60\2\2\u0090\u0097\3\2\2\2\u0091\u0092\5\32\16\2\u0092")
        buf.write("\u0093\7\60\2\2\u0093\u0094\7\23\2\2\u0094\u0095\5N(\2")
        buf.write("\u0095\u0097\3\2\2\2\u0096\u008e\3\2\2\2\u0096\u0091\3")
        buf.write("\2\2\2\u0097\r\3\2\2\2\u0098\u0099\7 \2\2\u0099\u009a")
        buf.write("\7\60\2\2\u009a\u009b\7\23\2\2\u009b\u009c\5N(\2\u009c")
        buf.write("\17\3\2\2\2\u009d\u009e\5\32\16\2\u009e\u009f\7\60\2\2")
        buf.write("\u009f\u00a0\5\22\n\2\u00a0\u00a8\3\2\2\2\u00a1\u00a2")
        buf.write("\5\32\16\2\u00a2\u00a3\7\60\2\2\u00a3\u00a4\5\22\n\2\u00a4")
        buf.write("\u00a5\7\23\2\2\u00a5\u00a6\5N(\2\u00a6\u00a8\3\2\2\2")
        buf.write("\u00a7\u009d\3\2\2\2\u00a7\u00a1\3\2\2\2\u00a8\21\3\2")
        buf.write("\2\2\u00a9\u00aa\7\34\2\2\u00aa\u00ab\5\24\13\2\u00ab")
        buf.write("\u00ac\7\35\2\2\u00ac\23\3\2\2\2\u00ad\u00ae\7-\2\2\u00ae")
        buf.write("\u00af\7\36\2\2\u00af\u00b2\5\24\13\2\u00b0\u00b2\7-\2")
        buf.write("\2\u00b1\u00ad\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\25\3")
        buf.write("\2\2\2\u00b3\u00b4\7\34\2\2\u00b4\u00b5\5\30\r\2\u00b5")
        buf.write("\u00b6\7\35\2\2\u00b6\27\3\2\2\2\u00b7\u00b8\5N(\2\u00b8")
        buf.write("\u00b9\7\36\2\2\u00b9\u00ba\5\30\r\2\u00ba\u00bd\3\2\2")
        buf.write("\2\u00bb\u00bd\5N(\2\u00bc\u00b7\3\2\2\2\u00bc\u00bb\3")
        buf.write("\2\2\2\u00bd\31\3\2\2\2\u00be\u00bf\t\2\2\2\u00bf\33\3")
        buf.write("\2\2\2\u00c0\u00c1\7\"\2\2\u00c1\u00c2\7\60\2\2\u00c2")
        buf.write("\u00c3\7\32\2\2\u00c3\u00c4\5\"\22\2\u00c4\u00c8\7\33")
        buf.write("\2\2\u00c5\u00c7\7\61\2\2\u00c6\u00c5\3\2\2\2\u00c7\u00ca")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("\u00cb\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00cc\5\36\20")
        buf.write("\2\u00cc\35\3\2\2\2\u00cd\u00d0\5 \21\2\u00ce\u00d0\3")
        buf.write("\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\37")
        buf.write("\3\2\2\2\u00d1\u00d4\5B\"\2\u00d2\u00d4\5J&\2\u00d3\u00d1")
        buf.write("\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4!\3\2\2\2\u00d5\u00d8")
        buf.write("\5$\23\2\u00d6\u00d8\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7")
        buf.write("\u00d6\3\2\2\2\u00d8#\3\2\2\2\u00d9\u00da\5&\24\2\u00da")
        buf.write("\u00db\7\36\2\2\u00db\u00dc\5$\23\2\u00dc\u00df\3\2\2")
        buf.write("\2\u00dd\u00df\5&\24\2\u00de\u00d9\3\2\2\2\u00de\u00dd")
        buf.write("\3\2\2\2\u00df%\3\2\2\2\u00e0\u00e1\5\32\16\2\u00e1\u00e2")
        buf.write("\7\60\2\2\u00e2\u00e8\3\2\2\2\u00e3\u00e4\5\32\16\2\u00e4")
        buf.write("\u00e5\7\60\2\2\u00e5\u00e6\5\22\n\2\u00e6\u00e8\3\2\2")
        buf.write("\2\u00e7\u00e0\3\2\2\2\u00e7\u00e3\3\2\2\2\u00e8\'\3\2")
        buf.write("\2\2\u00e9\u00ec\5,\27\2\u00ea\u00ec\5*\26\2\u00eb\u00e9")
        buf.write("\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec)\3\2\2\2\u00ed\u00ee")
        buf.write("\7(\2\2\u00ee\u00ef\7\32\2\2\u00ef\u00f0\5N(\2\u00f0\u00f4")
        buf.write("\7\33\2\2\u00f1\u00f3\7\61\2\2\u00f2\u00f1\3\2\2\2\u00f3")
        buf.write("\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2")
        buf.write("\u00f5\u00f7\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f8\5")
        buf.write("(\25\2\u00f8\u00f9\5\62\32\2\u00f9\u0110\3\2\2\2\u00fa")
        buf.write("\u00fb\7(\2\2\u00fb\u00fc\7\32\2\2\u00fc\u00fd\5N(\2\u00fd")
        buf.write("\u0101\7\33\2\2\u00fe\u0100\7\61\2\2\u00ff\u00fe\3\2\2")
        buf.write("\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102")
        buf.write("\3\2\2\2\u0102\u0104\3\2\2\2\u0103\u0101\3\2\2\2\u0104")
        buf.write("\u0105\5,\27\2\u0105\u0106\5\62\32\2\u0106\u010a\7)\2")
        buf.write("\2\u0107\u0109\7\61\2\2\u0108\u0107\3\2\2\2\u0109\u010c")
        buf.write("\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write("\u010d\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010e\5*\26\2")
        buf.write("\u010e\u0110\3\2\2\2\u010f\u00ed\3\2\2\2\u010f\u00fa\3")
        buf.write("\2\2\2\u0110+\3\2\2\2\u0111\u0112\7(\2\2\u0112\u0113\7")
        buf.write("\32\2\2\u0113\u0114\5N(\2\u0114\u0118\7\33\2\2\u0115\u0117")
        buf.write("\7\61\2\2\u0116\u0115\3\2\2\2\u0117\u011a\3\2\2\2\u0118")
        buf.write("\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011b\3\2\2\2")
        buf.write("\u011a\u0118\3\2\2\2\u011b\u011c\5,\27\2\u011c\u011d\5")
        buf.write("\62\32\2\u011d\u0121\7)\2\2\u011e\u0120\7\61\2\2\u011f")
        buf.write("\u011e\3\2\2\2\u0120\u0123\3\2\2\2\u0121\u011f\3\2\2\2")
        buf.write("\u0121\u0122\3\2\2\2\u0122\u0124\3\2\2\2\u0123\u0121\3")
        buf.write("\2\2\2\u0124\u0125\5,\27\2\u0125\u0128\3\2\2\2\u0126\u0128")
        buf.write("\5.\30\2\u0127\u0111\3\2\2\2\u0127\u0126\3\2\2\2\u0128")
        buf.write("-\3\2\2\2\u0129\u012c\5\60\31\2\u012a\u012c\5<\37\2\u012b")
        buf.write("\u0129\3\2\2\2\u012b\u012a\3\2\2\2\u012c/\3\2\2\2\u012d")
        buf.write("\u0135\5\66\34\2\u012e\u0135\58\35\2\u012f\u0135\5> \2")
        buf.write("\u0130\u0135\5@!\2\u0131\u0135\5B\"\2\u0132\u0135\5J&")
        buf.write("\2\u0133\u0135\5D#\2\u0134\u012d\3\2\2\2\u0134\u012e\3")
        buf.write("\2\2\2\u0134\u012f\3\2\2\2\u0134\u0130\3\2\2\2\u0134\u0131")
        buf.write("\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0133\3\2\2\2\u0135")
        buf.write("\u0137\3\2\2\2\u0136\u0138\7\61\2\2\u0137\u0136\3\2\2")
        buf.write("\2\u0138\u0139\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a")
        buf.write("\3\2\2\2\u013a\61\3\2\2\2\u013b\u013c\5\64\33\2\u013c")
        buf.write("\u013d\5\62\32\2\u013d\u0140\3\2\2\2\u013e\u0140\3\2\2")
        buf.write("\2\u013f\u013b\3\2\2\2\u013f\u013e\3\2\2\2\u0140\63\3")
        buf.write("\2\2\2\u0141\u0142\7*\2\2\u0142\u0143\7\32\2\2\u0143\u0144")
        buf.write("\5N(\2\u0144\u0148\7\33\2\2\u0145\u0147\7\61\2\2\u0146")
        buf.write("\u0145\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2")
        buf.write("\u0148\u0149\3\2\2\2\u0149\u014b\3\2\2\2\u014a\u0148\3")
        buf.write("\2\2\2\u014b\u014c\5(\25\2\u014c\65\3\2\2\2\u014d\u014e")
        buf.write("\5\b\5\2\u014e\67\3\2\2\2\u014f\u0150\5:\36\2\u0150\u0151")
        buf.write("\7\23\2\2\u0151\u0152\5N(\2\u01529\3\2\2\2\u0153\u0154")
        buf.write("\7\60\2\2\u0154\u0157\5^\60\2\u0155\u0157\7\60\2\2\u0156")
        buf.write("\u0153\3\2\2\2\u0156\u0155\3\2\2\2\u0157;\3\2\2\2\u0158")
        buf.write("\u0159\7#\2\2\u0159\u015a\7\60\2\2\u015a\u015b\7$\2\2")
        buf.write("\u015b\u015c\5N(\2\u015c\u015d\7%\2\2\u015d\u0161\5N(")
        buf.write("\2\u015e\u0160\7\61\2\2\u015f\u015e\3\2\2\2\u0160\u0163")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0164\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0165\5(\25\2")
        buf.write("\u0165=\3\2\2\2\u0166\u0167\7&\2\2\u0167?\3\2\2\2\u0168")
        buf.write("\u0169\7\'\2\2\u0169A\3\2\2\2\u016a\u016b\7\37\2\2\u016b")
        buf.write("\u016e\5N(\2\u016c\u016e\7\37\2\2\u016d\u016a\3\2\2\2")
        buf.write("\u016d\u016c\3\2\2\2\u016eC\3\2\2\2\u016f\u0170\7\60\2")
        buf.write("\2\u0170\u0171\7\32\2\2\u0171\u0172\5F$\2\u0172\u0173")
        buf.write("\7\33\2\2\u0173E\3\2\2\2\u0174\u0177\5H%\2\u0175\u0177")
        buf.write("\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0175\3\2\2\2\u0177")
        buf.write("G\3\2\2\2\u0178\u0179\5N(\2\u0179\u017a\7\36\2\2\u017a")
        buf.write("\u017b\5H%\2\u017b\u017e\3\2\2\2\u017c\u017e\5N(\2\u017d")
        buf.write("\u0178\3\2\2\2\u017d\u017c\3\2\2\2\u017eI\3\2\2\2\u017f")
        buf.write("\u0181\7+\2\2\u0180\u0182\7\61\2\2\u0181\u0180\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3")
        buf.write("\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\5L\'\2\u0186\u0187")
        buf.write("\7,\2\2\u0187K\3\2\2\2\u0188\u0189\5(\25\2\u0189\u018a")
        buf.write("\5L\'\2\u018a\u018d\3\2\2\2\u018b\u018d\3\2\2\2\u018c")
        buf.write("\u0188\3\2\2\2\u018c\u018b\3\2\2\2\u018dM\3\2\2\2\u018e")
        buf.write("\u018f\5P)\2\u018f\u0190\7\30\2\2\u0190\u0191\5P)\2\u0191")
        buf.write("\u0194\3\2\2\2\u0192\u0194\5P)\2\u0193\u018e\3\2\2\2\u0193")
        buf.write("\u0192\3\2\2\2\u0194O\3\2\2\2\u0195\u0196\5R*\2\u0196")
        buf.write("\u0197\5d\63\2\u0197\u0198\5R*\2\u0198\u019b\3\2\2\2\u0199")
        buf.write("\u019b\5R*\2\u019a\u0195\3\2\2\2\u019a\u0199\3\2\2\2\u019b")
        buf.write("Q\3\2\2\2\u019c\u019d\b*\1\2\u019d\u019e\5T+\2\u019e\u01a4")
        buf.write("\3\2\2\2\u019f\u01a0\f\4\2\2\u01a0\u01a1\t\3\2\2\u01a1")
        buf.write("\u01a3\5T+\2\u01a2\u019f\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5S\3\2\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a7\u01a8\b+\1\2\u01a8\u01a9\5V,\2\u01a9")
        buf.write("\u01af\3\2\2\2\u01aa\u01ab\f\4\2\2\u01ab\u01ac\t\4\2\2")
        buf.write("\u01ac\u01ae\5V,\2\u01ad\u01aa\3\2\2\2\u01ae\u01b1\3\2")
        buf.write("\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0U\3")
        buf.write("\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b3\b,\1\2\u01b3\u01b4")
        buf.write("\5X-\2\u01b4\u01ba\3\2\2\2\u01b5\u01b6\f\4\2\2\u01b6\u01b7")
        buf.write("\t\5\2\2\u01b7\u01b9\5X-\2\u01b8\u01b5\3\2\2\2\u01b9\u01bc")
        buf.write("\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb")
        buf.write("W\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01be\7\t\2\2\u01be")
        buf.write("\u01c1\5X-\2\u01bf\u01c1\5Z.\2\u01c0\u01bd\3\2\2\2\u01c0")
        buf.write("\u01bf\3\2\2\2\u01c1Y\3\2\2\2\u01c2\u01c3\7\r\2\2\u01c3")
        buf.write("\u01c6\5Z.\2\u01c4\u01c6\5\\/\2\u01c5\u01c2\3\2\2\2\u01c5")
        buf.write("\u01c4\3\2\2\2\u01c6[\3\2\2\2\u01c7\u01ca\7\60\2\2\u01c8")
        buf.write("\u01ca\5D#\2\u01c9\u01c7\3\2\2\2\u01c9\u01c8\3\2\2\2\u01ca")
        buf.write("\u01cb\3\2\2\2\u01cb\u01ce\5^\60\2\u01cc\u01ce\5`\61\2")
        buf.write("\u01cd\u01c9\3\2\2\2\u01cd\u01cc\3\2\2\2\u01ce]\3\2\2")
        buf.write("\2\u01cf\u01d0\7\34\2\2\u01d0\u01d1\5H%\2\u01d1\u01d2")
        buf.write("\7\35\2\2\u01d2_\3\2\2\2\u01d3\u01d8\5f\64\2\u01d4\u01d8")
        buf.write("\5\26\f\2\u01d5\u01d8\5D#\2\u01d6\u01d8\5b\62\2\u01d7")
        buf.write("\u01d3\3\2\2\2\u01d7\u01d4\3\2\2\2\u01d7\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d6\3\2\2\2\u01d8a\3\2\2\2\u01d9\u01da\7\32\2")
        buf.write("\2\u01da\u01db\5N(\2\u01db\u01dc\7\33\2\2\u01dcc\3\2\2")
        buf.write("\2\u01dd\u01de\t\6\2\2\u01dee\3\2\2\2\u01df\u01e0\t\7")
        buf.write("\2\2\u01e0g\3\2\2\2\60kuy~\u0084\u008c\u0096\u00a7\u00b1")
        buf.write("\u00bc\u00c8\u00cf\u00d3\u00d7\u00de\u00e7\u00eb\u00f4")
        buf.write("\u0101\u010a\u010f\u0118\u0121\u0127\u012b\u0134\u0139")
        buf.write("\u013f\u0148\u0156\u0161\u016d\u0176\u017d\u0183\u018c")
        buf.write("\u0193\u019a\u01a4\u01af\u01ba\u01c0\u01c5\u01c9\u01cd")
        buf.write("\u01d7")
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
    RULE_unmatchifstmt = 20
    RULE_matchifstmt = 21
    RULE_otherstmt = 22
    RULE_noncondstmt = 23
    RULE_eliflist = 24
    RULE_elifpart = 25
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
    RULE_expr = 38
    RULE_expr1 = 39
    RULE_expr2 = 40
    RULE_expr3 = 41
    RULE_expr4 = 42
    RULE_expr5 = 43
    RULE_expr6 = 44
    RULE_expr7 = 45
    RULE_indexop = 46
    RULE_expr8 = 47
    RULE_subexpr = 48
    RULE_rel_op = 49
    RULE_const = 50

    ruleNames =  [ "program", "declist", "decl", "variabledec", "dyndecl", 
                   "typedecl", "vardecl", "arrdecl", "dimension", "numlitlist", 
                   "array", "vallist", "typ", "funcdecl", "funcstmt", "funcprime", 
                   "paramlist", "paramprime", "paramdecl", "stmt", "unmatchifstmt", 
                   "matchifstmt", "otherstmt", "noncondstmt", "eliflist", 
                   "elifpart", "varstmt", "assignstmt", "lhs", "forstmt", 
                   "breakstmt", "contstmt", "returnstmt", "callstmt", "exprlist", 
                   "exprparam", "blockstmt", "stmtlist", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "indexop", "expr8", "subexpr", "rel_op", "const" ]

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

        def declist(self):
            return self.getTypedRuleContext(ZCodeParser.DeclistContext,0)


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
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 102
                self.match(ZCodeParser.NEWLINE)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.declist()
            self.state = 109
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
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.decl()
                self.state = 112
                self.declist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
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

        def variabledec(self):
            return self.getTypedRuleContext(ZCodeParser.VariabledecContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.state = 117
                self.variabledec()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.state = 118
                self.funcdecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 122 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 121
                self.match(ZCodeParser.NEWLINE)
                self.state = 124 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

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
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.typedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.arrdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
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
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(ZCodeParser.DYNAMIC)
                self.state = 133
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(ZCodeParser.DYNAMIC)
                self.state = 135
                self.match(ZCodeParser.ID)
                self.state = 136
                self.match(ZCodeParser.ASSIGN)
                self.state = 137
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
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.typ()
                self.state = 141
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.typ()
                self.state = 144
                self.match(ZCodeParser.ID)
                self.state = 145
                self.match(ZCodeParser.ASSIGN)
                self.state = 146
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
            self.state = 150
            self.match(ZCodeParser.VAR)
            self.state = 151
            self.match(ZCodeParser.ID)
            self.state = 152
            self.match(ZCodeParser.ASSIGN)
            self.state = 153
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
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.typ()
                self.state = 156
                self.match(ZCodeParser.ID)
                self.state = 157
                self.dimension()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.typ()
                self.state = 160
                self.match(ZCodeParser.ID)
                self.state = 161
                self.dimension()
                self.state = 162
                self.match(ZCodeParser.ASSIGN)
                self.state = 163
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
            self.state = 167
            self.match(ZCodeParser.SQ_OPEN)
            self.state = 168
            self.numlitlist()
            self.state = 169
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
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(ZCodeParser.NUMLIT)
                self.state = 172
                self.match(ZCodeParser.COMMA)
                self.state = 173
                self.numlitlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
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
            self.state = 177
            self.match(ZCodeParser.SQ_OPEN)
            self.state = 178
            self.vallist()
            self.state = 179
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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.expr()
                self.state = 182
                self.match(ZCodeParser.COMMA)
                self.state = 183
                self.vallist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
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
            self.state = 188
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

        def funcstmt(self):
            return self.getTypedRuleContext(ZCodeParser.FuncstmtContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

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
            self.state = 190
            self.match(ZCodeParser.FUNC)
            self.state = 191
            self.match(ZCodeParser.ID)
            self.state = 192
            self.match(ZCodeParser.R_OPEN)
            self.state = 193
            self.paramlist()
            self.state = 194
            self.match(ZCodeParser.R_CLOSE)
            self.state = 198
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 195
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 200
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 201
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
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
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
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.returnstmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
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
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
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
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.paramdecl()
                self.state = 216
                self.match(ZCodeParser.COMMA)
                self.state = 217
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
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
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.typ()
                self.state = 223
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.typ()
                self.state = 226
                self.match(ZCodeParser.ID)
                self.state = 227
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

        def matchifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.MatchifstmtContext,0)


        def unmatchifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.UnmatchifstmtContext,0)


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
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.matchifstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.unmatchifstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnmatchifstmtContext(ParserRuleContext):
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

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def matchifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.MatchifstmtContext,0)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def unmatchifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.UnmatchifstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_unmatchifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnmatchifstmt" ):
                return visitor.visitUnmatchifstmt(self)
            else:
                return visitor.visitChildren(self)




    def unmatchifstmt(self):

        localctx = ZCodeParser.UnmatchifstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_unmatchifstmt)
        self._la = 0 # Token type
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(ZCodeParser.IF)
                self.state = 236
                self.match(ZCodeParser.R_OPEN)
                self.state = 237
                self.expr()
                self.state = 238
                self.match(ZCodeParser.R_CLOSE)
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 239
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 244
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 245
                self.stmt()
                self.state = 246
                self.eliflist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(ZCodeParser.IF)
                self.state = 249
                self.match(ZCodeParser.R_OPEN)
                self.state = 250
                self.expr()
                self.state = 251
                self.match(ZCodeParser.R_CLOSE)
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 252
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 257
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 258
                self.matchifstmt()
                self.state = 259
                self.eliflist()
                self.state = 260
                self.match(ZCodeParser.ELSE)
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 261
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 266
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 267
                self.unmatchifstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchifstmtContext(ParserRuleContext):
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

        def matchifstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.MatchifstmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.MatchifstmtContext,i)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def otherstmt(self):
            return self.getTypedRuleContext(ZCodeParser.OtherstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_matchifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchifstmt" ):
                return visitor.visitMatchifstmt(self)
            else:
                return visitor.visitChildren(self)




    def matchifstmt(self):

        localctx = ZCodeParser.MatchifstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_matchifstmt)
        self._la = 0 # Token type
        try:
            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(ZCodeParser.IF)
                self.state = 272
                self.match(ZCodeParser.R_OPEN)
                self.state = 273
                self.expr()
                self.state = 274
                self.match(ZCodeParser.R_CLOSE)
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 275
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 280
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 281
                self.matchifstmt()
                self.state = 282
                self.eliflist()
                self.state = 283
                self.match(ZCodeParser.ELSE)
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 284
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 289
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 290
                self.matchifstmt()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.otherstmt()
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


    class OtherstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noncondstmt(self):
            return self.getTypedRuleContext(ZCodeParser.NoncondstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_otherstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOtherstmt" ):
                return visitor.visitOtherstmt(self)
            else:
                return visitor.visitChildren(self)




    def otherstmt(self):

        localctx = ZCodeParser.OtherstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_otherstmt)
        try:
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.noncondstmt()
                pass
            elif token in [ZCodeParser.FOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
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


    class NoncondstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varstmt(self):
            return self.getTypedRuleContext(ZCodeParser.VarstmtContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BreakstmtContext,0)


        def contstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(ZCodeParser.CallstmtContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_noncondstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoncondstmt" ):
                return visitor.visitNoncondstmt(self)
            else:
                return visitor.visitChildren(self)




    def noncondstmt(self):

        localctx = ZCodeParser.NoncondstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_noncondstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 299
                self.varstmt()
                pass

            elif la_ == 2:
                self.state = 300
                self.assignstmt()
                pass

            elif la_ == 3:
                self.state = 301
                self.breakstmt()
                pass

            elif la_ == 4:
                self.state = 302
                self.contstmt()
                pass

            elif la_ == 5:
                self.state = 303
                self.returnstmt()
                pass

            elif la_ == 6:
                self.state = 304
                self.blockstmt()
                pass

            elif la_ == 7:
                self.state = 305
                self.callstmt()
                pass


            self.state = 309 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 308
                self.match(ZCodeParser.NEWLINE)
                self.state = 311 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

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
        self.enterRule(localctx, 48, self.RULE_eliflist)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.elifpart()
                self.state = 314
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

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elifpart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifpart" ):
                return visitor.visitElifpart(self)
            else:
                return visitor.visitChildren(self)




    def elifpart(self):

        localctx = ZCodeParser.ElifpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elifpart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(ZCodeParser.ELIF)
            self.state = 320
            self.match(ZCodeParser.R_OPEN)
            self.state = 321
            self.expr()
            self.state = 322
            self.match(ZCodeParser.R_CLOSE)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 323
                self.match(ZCodeParser.NEWLINE)
                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 329
            self.stmt()
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
            self.state = 331
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
            self.state = 333
            self.lhs()
            self.state = 334
            self.match(ZCodeParser.ASSIGN)
            self.state = 335
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
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(ZCodeParser.ID)
                self.state = 338
                self.indexop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
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

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(ZCodeParser.FOR)
            self.state = 343
            self.match(ZCodeParser.ID)
            self.state = 344
            self.match(ZCodeParser.UNTIL)
            self.state = 345
            self.expr()
            self.state = 346
            self.match(ZCodeParser.BY)
            self.state = 347
            self.expr()
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 348
                self.match(ZCodeParser.NEWLINE)
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 354
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
            self.state = 356
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
            self.state = 358
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
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(ZCodeParser.RETURN)
                self.state = 361
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
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
            self.state = 365
            self.match(ZCodeParser.ID)
            self.state = 366
            self.match(ZCodeParser.R_OPEN)
            self.state = 367
            self.exprlist()
            self.state = 368
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
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.R_OPEN, ZCodeParser.SQ_OPEN, ZCodeParser.NUMLIT, ZCodeParser.STRINGLIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
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
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.expr()
                self.state = 375
                self.match(ZCodeParser.COMMA)
                self.state = 376
                self.exprparam()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
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

        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(ZCodeParser.BEGIN)
            self.state = 383 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 382
                self.match(ZCodeParser.NEWLINE)
                self.state = 385 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

            self.state = 387
            self.stmtlist()
            self.state = 388
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
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.stmt()
                self.state = 391
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
        self.enterRule(localctx, 76, self.RULE_expr)
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.expr1()
                self.state = 397
                self.match(ZCodeParser.CONCAT)
                self.state = 398
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
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
        self.enterRule(localctx, 78, self.RULE_expr1)
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.expr2(0)
                self.state = 404
                self.rel_op()
                self.state = 405
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 413
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 414
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 415
                    self.expr3(0) 
                self.state = 420
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 424
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 425
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 426
                    self.expr4(0) 
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 440
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 435
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 436
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 437
                    self.expr5() 
                self.state = 442
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        self.enterRule(localctx, 86, self.RULE_expr5)
        try:
            self.state = 446
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.match(ZCodeParser.NOT)
                self.state = 444
                self.expr5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.R_OPEN, ZCodeParser.SQ_OPEN, ZCodeParser.NUMLIT, ZCodeParser.STRINGLIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
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
        self.enterRule(localctx, 88, self.RULE_expr6)
        try:
            self.state = 451
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.match(ZCodeParser.SUB)
                self.state = 449
                self.expr6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.R_OPEN, ZCodeParser.SQ_OPEN, ZCodeParser.NUMLIT, ZCodeParser.STRINGLIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
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

        def callstmt(self):
            return self.getTypedRuleContext(ZCodeParser.CallstmtContext,0)


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
        self.enterRule(localctx, 90, self.RULE_expr7)
        try:
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                if la_ == 1:
                    self.state = 453
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 454
                    self.callstmt()
                    pass


                self.state = 457
                self.indexop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 458
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
        self.enterRule(localctx, 92, self.RULE_indexop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(ZCodeParser.SQ_OPEN)
            self.state = 462
            self.exprparam()
            self.state = 463
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


        def callstmt(self):
            return self.getTypedRuleContext(ZCodeParser.CallstmtContext,0)


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
        self.enterRule(localctx, 94, self.RULE_expr8)
        try:
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.const()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.array()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 467
                self.callstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 468
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
        self.enterRule(localctx, 96, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(ZCodeParser.R_OPEN)
            self.state = 472
            self.expr()
            self.state = 473
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
        self.enterRule(localctx, 98, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
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
        self.enterRule(localctx, 100, self.RULE_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
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
        self._predicates[40] = self.expr2_sempred
        self._predicates[41] = self.expr3_sempred
        self._predicates[42] = self.expr4_sempred
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
         




