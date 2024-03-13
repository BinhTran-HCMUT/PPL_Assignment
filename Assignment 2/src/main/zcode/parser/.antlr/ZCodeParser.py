# Generated from d:/ASM 2/assignment2-initial/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
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
        4,1,51,438,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,115,8,1,1,2,1,2,3,2,119,8,2,
        1,2,1,2,1,3,1,3,1,3,1,3,3,3,127,8,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
        135,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,145,8,5,1,6,1,6,1,6,
        1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,162,8,7,1,8,
        1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,172,8,9,1,10,1,10,1,10,1,10,1,11,
        1,11,1,11,1,11,1,11,3,11,183,8,11,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,14,1,14,3,14,197,8,14,1,15,1,15,3,15,201,8,
        15,1,16,1,16,3,16,205,8,16,1,17,1,17,1,17,1,17,1,17,3,17,212,8,17,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,221,8,18,1,19,1,19,3,19,
        225,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,246,8,20,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,260,8,21,
        1,22,1,22,3,22,264,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,
        273,8,23,1,23,1,23,1,24,1,24,1,24,1,24,3,24,281,8,24,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,26,1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,
        28,3,28,299,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,
        30,1,30,1,31,1,31,1,32,1,32,1,32,3,32,317,8,32,1,33,1,33,1,33,1,
        33,1,33,1,34,1,34,3,34,326,8,34,1,35,1,35,1,35,1,35,1,35,3,35,333,
        8,35,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,3,37,344,8,37,
        1,38,1,38,1,38,3,38,349,8,38,1,39,1,39,3,39,353,8,39,1,40,1,40,1,
        40,1,40,1,40,3,40,360,8,40,1,41,1,41,1,41,1,41,1,41,3,41,367,8,41,
        1,42,1,42,1,42,1,42,1,42,1,42,5,42,375,8,42,10,42,12,42,378,9,42,
        1,43,1,43,1,43,1,43,1,43,1,43,5,43,386,8,43,10,43,12,43,389,9,43,
        1,44,1,44,1,44,1,44,1,44,1,44,5,44,397,8,44,10,44,12,44,400,9,44,
        1,45,1,45,1,45,3,45,405,8,45,1,46,1,46,1,46,3,46,410,8,46,1,47,1,
        47,3,47,414,8,47,1,47,1,47,3,47,418,8,47,1,48,1,48,1,48,1,48,1,49,
        1,49,1,49,1,49,3,49,428,8,49,1,50,1,50,1,50,1,50,1,51,1,51,1,52,
        1,52,1,52,0,3,84,86,88,53,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,0,6,1,0,4,6,1,
        0,8,9,1,0,10,11,1,0,12,14,3,0,15,16,18,21,23,23,3,0,2,3,43,43,45,
        46,429,0,106,1,0,0,0,2,114,1,0,0,0,4,118,1,0,0,0,6,126,1,0,0,0,8,
        134,1,0,0,0,10,144,1,0,0,0,12,146,1,0,0,0,14,161,1,0,0,0,16,163,
        1,0,0,0,18,171,1,0,0,0,20,173,1,0,0,0,22,182,1,0,0,0,24,184,1,0,
        0,0,26,186,1,0,0,0,28,196,1,0,0,0,30,200,1,0,0,0,32,204,1,0,0,0,
        34,211,1,0,0,0,36,220,1,0,0,0,38,224,1,0,0,0,40,245,1,0,0,0,42,259,
        1,0,0,0,44,263,1,0,0,0,46,272,1,0,0,0,48,280,1,0,0,0,50,282,1,0,
        0,0,52,289,1,0,0,0,54,291,1,0,0,0,56,298,1,0,0,0,58,300,1,0,0,0,
        60,309,1,0,0,0,62,311,1,0,0,0,64,316,1,0,0,0,66,318,1,0,0,0,68,325,
        1,0,0,0,70,332,1,0,0,0,72,334,1,0,0,0,74,343,1,0,0,0,76,348,1,0,
        0,0,78,352,1,0,0,0,80,359,1,0,0,0,82,366,1,0,0,0,84,368,1,0,0,0,
        86,379,1,0,0,0,88,390,1,0,0,0,90,404,1,0,0,0,92,409,1,0,0,0,94,417,
        1,0,0,0,96,419,1,0,0,0,98,427,1,0,0,0,100,429,1,0,0,0,102,433,1,
        0,0,0,104,435,1,0,0,0,106,107,3,78,39,0,107,108,3,2,1,0,108,109,
        5,0,0,1,109,1,1,0,0,0,110,111,3,4,2,0,111,112,3,2,1,0,112,115,1,
        0,0,0,113,115,3,4,2,0,114,110,1,0,0,0,114,113,1,0,0,0,115,3,1,0,
        0,0,116,119,3,6,3,0,117,119,3,26,13,0,118,116,1,0,0,0,118,117,1,
        0,0,0,119,120,1,0,0,0,120,121,3,76,38,0,121,5,1,0,0,0,122,127,3,
        10,5,0,123,127,3,12,6,0,124,127,3,14,7,0,125,127,3,8,4,0,126,122,
        1,0,0,0,126,123,1,0,0,0,126,124,1,0,0,0,126,125,1,0,0,0,127,7,1,
        0,0,0,128,129,5,31,0,0,129,135,5,46,0,0,130,131,5,31,0,0,131,132,
        5,46,0,0,132,133,5,17,0,0,133,135,3,80,40,0,134,128,1,0,0,0,134,
        130,1,0,0,0,135,9,1,0,0,0,136,137,3,24,12,0,137,138,5,46,0,0,138,
        145,1,0,0,0,139,140,3,24,12,0,140,141,5,46,0,0,141,142,5,17,0,0,
        142,143,3,80,40,0,143,145,1,0,0,0,144,136,1,0,0,0,144,139,1,0,0,
        0,145,11,1,0,0,0,146,147,5,30,0,0,147,148,5,46,0,0,148,149,5,17,
        0,0,149,150,3,80,40,0,150,13,1,0,0,0,151,152,3,24,12,0,152,153,5,
        46,0,0,153,154,3,16,8,0,154,162,1,0,0,0,155,156,3,24,12,0,156,157,
        5,46,0,0,157,158,3,16,8,0,158,159,5,17,0,0,159,160,3,80,40,0,160,
        162,1,0,0,0,161,151,1,0,0,0,161,155,1,0,0,0,162,15,1,0,0,0,163,164,
        5,26,0,0,164,165,3,18,9,0,165,166,5,27,0,0,166,17,1,0,0,0,167,168,
        5,43,0,0,168,169,5,28,0,0,169,172,3,18,9,0,170,172,5,43,0,0,171,
        167,1,0,0,0,171,170,1,0,0,0,172,19,1,0,0,0,173,174,5,26,0,0,174,
        175,3,22,11,0,175,176,5,27,0,0,176,21,1,0,0,0,177,178,3,80,40,0,
        178,179,5,28,0,0,179,180,3,22,11,0,180,183,1,0,0,0,181,183,3,80,
        40,0,182,177,1,0,0,0,182,181,1,0,0,0,183,23,1,0,0,0,184,185,7,0,
        0,0,185,25,1,0,0,0,186,187,5,32,0,0,187,188,5,46,0,0,188,189,5,24,
        0,0,189,190,3,32,16,0,190,191,5,25,0,0,191,192,3,78,39,0,192,193,
        3,28,14,0,193,27,1,0,0,0,194,197,3,30,15,0,195,197,1,0,0,0,196,194,
        1,0,0,0,196,195,1,0,0,0,197,29,1,0,0,0,198,201,3,64,32,0,199,201,
        3,72,36,0,200,198,1,0,0,0,200,199,1,0,0,0,201,31,1,0,0,0,202,205,
        3,34,17,0,203,205,1,0,0,0,204,202,1,0,0,0,204,203,1,0,0,0,205,33,
        1,0,0,0,206,207,3,36,18,0,207,208,5,28,0,0,208,209,3,34,17,0,209,
        212,1,0,0,0,210,212,3,36,18,0,211,206,1,0,0,0,211,210,1,0,0,0,212,
        35,1,0,0,0,213,214,3,24,12,0,214,215,5,46,0,0,215,221,1,0,0,0,216,
        217,3,24,12,0,217,218,5,46,0,0,218,219,3,16,8,0,219,221,1,0,0,0,
        220,213,1,0,0,0,220,216,1,0,0,0,221,37,1,0,0,0,222,225,3,42,21,0,
        223,225,3,40,20,0,224,222,1,0,0,0,224,223,1,0,0,0,225,39,1,0,0,0,
        226,227,5,38,0,0,227,228,5,24,0,0,228,229,3,80,40,0,229,230,5,25,
        0,0,230,231,3,78,39,0,231,232,3,38,19,0,232,233,3,48,24,0,233,246,
        1,0,0,0,234,235,5,38,0,0,235,236,5,24,0,0,236,237,3,80,40,0,237,
        238,5,25,0,0,238,239,3,78,39,0,239,240,3,42,21,0,240,241,3,48,24,
        0,241,242,5,39,0,0,242,243,3,78,39,0,243,244,3,40,20,0,244,246,1,
        0,0,0,245,226,1,0,0,0,245,234,1,0,0,0,246,41,1,0,0,0,247,248,5,38,
        0,0,248,249,5,24,0,0,249,250,3,80,40,0,250,251,5,25,0,0,251,252,
        3,78,39,0,252,253,3,42,21,0,253,254,3,48,24,0,254,255,5,39,0,0,255,
        256,3,78,39,0,256,257,3,42,21,0,257,260,1,0,0,0,258,260,3,44,22,
        0,259,247,1,0,0,0,259,258,1,0,0,0,260,43,1,0,0,0,261,264,3,46,23,
        0,262,264,3,58,29,0,263,261,1,0,0,0,263,262,1,0,0,0,264,45,1,0,0,
        0,265,273,3,52,26,0,266,273,3,54,27,0,267,273,3,60,30,0,268,273,
        3,62,31,0,269,273,3,64,32,0,270,273,3,72,36,0,271,273,3,66,33,0,
        272,265,1,0,0,0,272,266,1,0,0,0,272,267,1,0,0,0,272,268,1,0,0,0,
        272,269,1,0,0,0,272,270,1,0,0,0,272,271,1,0,0,0,273,274,1,0,0,0,
        274,275,3,76,38,0,275,47,1,0,0,0,276,277,3,50,25,0,277,278,3,48,
        24,0,278,281,1,0,0,0,279,281,1,0,0,0,280,276,1,0,0,0,280,279,1,0,
        0,0,281,49,1,0,0,0,282,283,5,40,0,0,283,284,5,24,0,0,284,285,3,80,
        40,0,285,286,5,25,0,0,286,287,3,78,39,0,287,288,3,38,19,0,288,51,
        1,0,0,0,289,290,3,6,3,0,290,53,1,0,0,0,291,292,3,56,28,0,292,293,
        5,17,0,0,293,294,3,80,40,0,294,55,1,0,0,0,295,296,5,46,0,0,296,299,
        3,96,48,0,297,299,5,46,0,0,298,295,1,0,0,0,298,297,1,0,0,0,299,57,
        1,0,0,0,300,301,5,33,0,0,301,302,5,46,0,0,302,303,5,34,0,0,303,304,
        3,80,40,0,304,305,5,35,0,0,305,306,3,80,40,0,306,307,3,78,39,0,307,
        308,3,38,19,0,308,59,1,0,0,0,309,310,5,36,0,0,310,61,1,0,0,0,311,
        312,5,37,0,0,312,63,1,0,0,0,313,314,5,29,0,0,314,317,3,80,40,0,315,
        317,5,29,0,0,316,313,1,0,0,0,316,315,1,0,0,0,317,65,1,0,0,0,318,
        319,5,46,0,0,319,320,5,24,0,0,320,321,3,68,34,0,321,322,5,25,0,0,
        322,67,1,0,0,0,323,326,3,70,35,0,324,326,1,0,0,0,325,323,1,0,0,0,
        325,324,1,0,0,0,326,69,1,0,0,0,327,328,3,80,40,0,328,329,5,28,0,
        0,329,330,3,70,35,0,330,333,1,0,0,0,331,333,3,80,40,0,332,327,1,
        0,0,0,332,331,1,0,0,0,333,71,1,0,0,0,334,335,5,41,0,0,335,336,3,
        76,38,0,336,337,3,74,37,0,337,338,5,42,0,0,338,73,1,0,0,0,339,340,
        3,38,19,0,340,341,3,74,37,0,341,344,1,0,0,0,342,344,1,0,0,0,343,
        339,1,0,0,0,343,342,1,0,0,0,344,75,1,0,0,0,345,346,5,47,0,0,346,
        349,3,76,38,0,347,349,5,47,0,0,348,345,1,0,0,0,348,347,1,0,0,0,349,
        77,1,0,0,0,350,353,3,76,38,0,351,353,1,0,0,0,352,350,1,0,0,0,352,
        351,1,0,0,0,353,79,1,0,0,0,354,355,3,82,41,0,355,356,5,22,0,0,356,
        357,3,82,41,0,357,360,1,0,0,0,358,360,3,82,41,0,359,354,1,0,0,0,
        359,358,1,0,0,0,360,81,1,0,0,0,361,362,3,84,42,0,362,363,3,102,51,
        0,363,364,3,84,42,0,364,367,1,0,0,0,365,367,3,84,42,0,366,361,1,
        0,0,0,366,365,1,0,0,0,367,83,1,0,0,0,368,369,6,42,-1,0,369,370,3,
        86,43,0,370,376,1,0,0,0,371,372,10,2,0,0,372,373,7,1,0,0,373,375,
        3,86,43,0,374,371,1,0,0,0,375,378,1,0,0,0,376,374,1,0,0,0,376,377,
        1,0,0,0,377,85,1,0,0,0,378,376,1,0,0,0,379,380,6,43,-1,0,380,381,
        3,88,44,0,381,387,1,0,0,0,382,383,10,2,0,0,383,384,7,2,0,0,384,386,
        3,88,44,0,385,382,1,0,0,0,386,389,1,0,0,0,387,385,1,0,0,0,387,388,
        1,0,0,0,388,87,1,0,0,0,389,387,1,0,0,0,390,391,6,44,-1,0,391,392,
        3,90,45,0,392,398,1,0,0,0,393,394,10,2,0,0,394,395,7,3,0,0,395,397,
        3,90,45,0,396,393,1,0,0,0,397,400,1,0,0,0,398,396,1,0,0,0,398,399,
        1,0,0,0,399,89,1,0,0,0,400,398,1,0,0,0,401,402,5,7,0,0,402,405,3,
        90,45,0,403,405,3,92,46,0,404,401,1,0,0,0,404,403,1,0,0,0,405,91,
        1,0,0,0,406,407,5,11,0,0,407,410,3,92,46,0,408,410,3,94,47,0,409,
        406,1,0,0,0,409,408,1,0,0,0,410,93,1,0,0,0,411,414,5,46,0,0,412,
        414,3,66,33,0,413,411,1,0,0,0,413,412,1,0,0,0,414,415,1,0,0,0,415,
        418,3,96,48,0,416,418,3,98,49,0,417,413,1,0,0,0,417,416,1,0,0,0,
        418,95,1,0,0,0,419,420,5,26,0,0,420,421,3,70,35,0,421,422,5,27,0,
        0,422,97,1,0,0,0,423,428,3,104,52,0,424,428,3,20,10,0,425,428,3,
        66,33,0,426,428,3,100,50,0,427,423,1,0,0,0,427,424,1,0,0,0,427,425,
        1,0,0,0,427,426,1,0,0,0,428,99,1,0,0,0,429,430,5,24,0,0,430,431,
        3,80,40,0,431,432,5,25,0,0,432,101,1,0,0,0,433,434,7,4,0,0,434,103,
        1,0,0,0,435,436,7,5,0,0,436,105,1,0,0,0,36,114,118,126,134,144,161,
        171,182,196,200,204,211,220,224,245,259,263,272,280,298,316,325,
        332,343,348,352,359,366,376,387,398,404,409,413,417,427
    ]

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
    RULE_rel_op = 51
    RULE_const = 52

    ruleNames =  [ "program", "declist", "decl", "variabledec", "dyndecl", 
                   "typedecl", "vardecl", "arrdecl", "dimension", "numlitlist", 
                   "array", "vallist", "typ", "funcdecl", "funcstmt", "funcprime", 
                   "paramlist", "paramprime", "paramdecl", "stmt", "unmatchifstmt", 
                   "matchifstmt", "otherstmt", "noncondstmt", "eliflist", 
                   "elifpart", "varstmt", "assignstmt", "lhs", "forstmt", 
                   "breakstmt", "contstmt", "returnstmt", "callstmt", "exprlist", 
                   "exprparam", "blockstmt", "stmtlist", "newlines", "null_newline", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "indexop", "expr8", "subexpr", "rel_op", 
                   "const" ]

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
        self.checkVersion("4.13.1")
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




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.null_newline()
            self.state = 107
            self.declist()
            self.state = 108
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




    def declist(self):

        localctx = ZCodeParser.DeclistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declist)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.decl()
                self.state = 111
                self.declist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
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




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 30, 31]:
                self.state = 116
                self.variabledec()
                pass
            elif token in [32]:
                self.state = 117
                self.funcdecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 120
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




    def variabledec(self):

        localctx = ZCodeParser.VariabledecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variabledec)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.typedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.arrdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
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




    def dyndecl(self):

        localctx = ZCodeParser.DyndeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dyndecl)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(ZCodeParser.DYNAMIC)
                self.state = 129
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.match(ZCodeParser.DYNAMIC)
                self.state = 131
                self.match(ZCodeParser.ID)
                self.state = 132
                self.match(ZCodeParser.ASSIGN)
                self.state = 133
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




    def typedecl(self):

        localctx = ZCodeParser.TypedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typedecl)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.typ()
                self.state = 137
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.typ()
                self.state = 140
                self.match(ZCodeParser.ID)
                self.state = 141
                self.match(ZCodeParser.ASSIGN)
                self.state = 142
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




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(ZCodeParser.VAR)
            self.state = 147
            self.match(ZCodeParser.ID)
            self.state = 148
            self.match(ZCodeParser.ASSIGN)
            self.state = 149
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




    def arrdecl(self):

        localctx = ZCodeParser.ArrdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arrdecl)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.typ()
                self.state = 152
                self.match(ZCodeParser.ID)
                self.state = 153
                self.dimension()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.typ()
                self.state = 156
                self.match(ZCodeParser.ID)
                self.state = 157
                self.dimension()
                self.state = 158
                self.match(ZCodeParser.ASSIGN)
                self.state = 159
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




    def dimension(self):

        localctx = ZCodeParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(ZCodeParser.SQ_OPEN)
            self.state = 164
            self.numlitlist()
            self.state = 165
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




    def numlitlist(self):

        localctx = ZCodeParser.NumlitlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_numlitlist)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(ZCodeParser.NUMLIT)
                self.state = 168
                self.match(ZCodeParser.COMMA)
                self.state = 169
                self.numlitlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
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




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(ZCodeParser.SQ_OPEN)
            self.state = 174
            self.vallist()
            self.state = 175
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




    def vallist(self):

        localctx = ZCodeParser.VallistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_vallist)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.expr()
                self.state = 178
                self.match(ZCodeParser.COMMA)
                self.state = 179
                self.vallist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
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




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
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




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(ZCodeParser.FUNC)
            self.state = 187
            self.match(ZCodeParser.ID)
            self.state = 188
            self.match(ZCodeParser.R_OPEN)
            self.state = 189
            self.paramlist()
            self.state = 190
            self.match(ZCodeParser.R_CLOSE)
            self.state = 191
            self.null_newline()
            self.state = 192
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




    def funcstmt(self):

        localctx = ZCodeParser.FuncstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_funcstmt)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.funcprime()
                pass
            elif token in [47]:
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




    def funcprime(self):

        localctx = ZCodeParser.FuncprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_funcprime)
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.returnstmt()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
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




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_paramlist)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.paramprime()
                pass
            elif token in [25]:
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




    def paramprime(self):

        localctx = ZCodeParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_paramprime)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.paramdecl()
                self.state = 207
                self.match(ZCodeParser.COMMA)
                self.state = 208
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
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




    def paramdecl(self):

        localctx = ZCodeParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_paramdecl)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.typ()
                self.state = 214
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.typ()
                self.state = 217
                self.match(ZCodeParser.ID)
                self.state = 218
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




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmt)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.matchifstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
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

        def null_newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Null_newlineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Null_newlineContext,i)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def matchifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.MatchifstmtContext,0)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def unmatchifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.UnmatchifstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_unmatchifstmt




    def unmatchifstmt(self):

        localctx = ZCodeParser.UnmatchifstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_unmatchifstmt)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(ZCodeParser.IF)
                self.state = 227
                self.match(ZCodeParser.R_OPEN)
                self.state = 228
                self.expr()
                self.state = 229
                self.match(ZCodeParser.R_CLOSE)
                self.state = 230
                self.null_newline()
                self.state = 231
                self.stmt()
                self.state = 232
                self.eliflist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(ZCodeParser.IF)
                self.state = 235
                self.match(ZCodeParser.R_OPEN)
                self.state = 236
                self.expr()
                self.state = 237
                self.match(ZCodeParser.R_CLOSE)
                self.state = 238
                self.null_newline()
                self.state = 239
                self.matchifstmt()
                self.state = 240
                self.eliflist()
                self.state = 241
                self.match(ZCodeParser.ELSE)
                self.state = 242
                self.null_newline()
                self.state = 243
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

        def null_newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Null_newlineContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Null_newlineContext,i)


        def matchifstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.MatchifstmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.MatchifstmtContext,i)


        def eliflist(self):
            return self.getTypedRuleContext(ZCodeParser.EliflistContext,0)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def otherstmt(self):
            return self.getTypedRuleContext(ZCodeParser.OtherstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_matchifstmt




    def matchifstmt(self):

        localctx = ZCodeParser.MatchifstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_matchifstmt)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(ZCodeParser.IF)
                self.state = 248
                self.match(ZCodeParser.R_OPEN)
                self.state = 249
                self.expr()
                self.state = 250
                self.match(ZCodeParser.R_CLOSE)
                self.state = 251
                self.null_newline()
                self.state = 252
                self.matchifstmt()
                self.state = 253
                self.eliflist()
                self.state = 254
                self.match(ZCodeParser.ELSE)
                self.state = 255
                self.null_newline()
                self.state = 256
                self.matchifstmt()
                pass
            elif token in [4, 5, 6, 29, 30, 31, 33, 36, 37, 41, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
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




    def otherstmt(self):

        localctx = ZCodeParser.OtherstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_otherstmt)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 29, 30, 31, 36, 37, 41, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.noncondstmt()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
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

        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


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


        def getRuleIndex(self):
            return ZCodeParser.RULE_noncondstmt




    def noncondstmt(self):

        localctx = ZCodeParser.NoncondstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_noncondstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 265
                self.varstmt()
                pass

            elif la_ == 2:
                self.state = 266
                self.assignstmt()
                pass

            elif la_ == 3:
                self.state = 267
                self.breakstmt()
                pass

            elif la_ == 4:
                self.state = 268
                self.contstmt()
                pass

            elif la_ == 5:
                self.state = 269
                self.returnstmt()
                pass

            elif la_ == 6:
                self.state = 270
                self.blockstmt()
                pass

            elif la_ == 7:
                self.state = 271
                self.callstmt()
                pass


            self.state = 274
            self.newlines()
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




    def eliflist(self):

        localctx = ZCodeParser.EliflistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_eliflist)
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.elifpart()
                self.state = 277
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




    def elifpart(self):

        localctx = ZCodeParser.ElifpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elifpart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(ZCodeParser.ELIF)
            self.state = 283
            self.match(ZCodeParser.R_OPEN)
            self.state = 284
            self.expr()
            self.state = 285
            self.match(ZCodeParser.R_CLOSE)
            self.state = 286
            self.null_newline()
            self.state = 287
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




    def varstmt(self):

        localctx = ZCodeParser.VarstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_varstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
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




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.lhs()
            self.state = 292
            self.match(ZCodeParser.ASSIGN)
            self.state = 293
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




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_lhs)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.match(ZCodeParser.ID)
                self.state = 296
                self.indexop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
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




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ZCodeParser.FOR)
            self.state = 301
            self.match(ZCodeParser.ID)
            self.state = 302
            self.match(ZCodeParser.UNTIL)
            self.state = 303
            self.expr()
            self.state = 304
            self.match(ZCodeParser.BY)
            self.state = 305
            self.expr()
            self.state = 306
            self.null_newline()
            self.state = 307
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




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
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




    def contstmt(self):

        localctx = ZCodeParser.ContstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_contstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
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




    def returnstmt(self):

        localctx = ZCodeParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_returnstmt)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.match(ZCodeParser.RETURN)
                self.state = 314
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
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




    def callstmt(self):

        localctx = ZCodeParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(ZCodeParser.ID)
            self.state = 319
            self.match(ZCodeParser.R_OPEN)
            self.state = 320
            self.exprlist()
            self.state = 321
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




    def exprlist(self):

        localctx = ZCodeParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exprlist)
        try:
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 7, 11, 24, 26, 43, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.exprparam()
                pass
            elif token in [25]:
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




    def exprparam(self):

        localctx = ZCodeParser.ExprparamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exprparam)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.expr()
                self.state = 328
                self.match(ZCodeParser.COMMA)
                self.state = 329
                self.exprparam()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
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




    def blockstmt(self):

        localctx = ZCodeParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(ZCodeParser.BEGIN)
            self.state = 335
            self.newlines()
            self.state = 336
            self.stmtlist()
            self.state = 337
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




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_stmtlist)
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 29, 30, 31, 33, 36, 37, 38, 41, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.stmt()
                self.state = 340
                self.stmtlist()
                pass
            elif token in [42]:
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




    def newlines(self):

        localctx = ZCodeParser.NewlinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_newlines)
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(ZCodeParser.NEWLINE)
                self.state = 346
                self.newlines()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
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




    def null_newline(self):

        localctx = ZCodeParser.Null_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_null_newline)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
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




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.expr1()
                self.state = 355
                self.match(ZCodeParser.CONCAT)
                self.state = 356
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
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




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr1)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.expr2(0)
                self.state = 362
                self.rel_op()
                self.state = 363
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
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
            self.state = 369
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 371
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 372
                    _la = self._input.LA(1)
                    if not(_la==8 or _la==9):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 373
                    self.expr3(0) 
                self.state = 378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
            self.state = 380
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 387
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 382
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 383
                    _la = self._input.LA(1)
                    if not(_la==10 or _la==11):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 384
                    self.expr4(0) 
                self.state = 389
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
            self.state = 391
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 398
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 393
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 394
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 395
                    self.expr5() 
                self.state = 400
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr5)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(ZCodeParser.NOT)
                self.state = 402
                self.expr5()
                pass
            elif token in [2, 3, 11, 24, 26, 43, 45, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
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




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr6)
        try:
            self.state = 409
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.match(ZCodeParser.SUB)
                self.state = 407
                self.expr6()
                pass
            elif token in [2, 3, 24, 26, 43, 45, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
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




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr7)
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 411
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 412
                    self.callstmt()
                    pass


                self.state = 415
                self.indexop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
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




    def indexop(self):

        localctx = ZCodeParser.IndexopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_indexop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(ZCodeParser.SQ_OPEN)
            self.state = 420
            self.exprparam()
            self.state = 421
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




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr8)
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.const()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.array()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 425
                self.callstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 426
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




    def subexpr(self):

        localctx = ZCodeParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(ZCodeParser.R_OPEN)
            self.state = 430
            self.expr()
            self.state = 431
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




    def rel_op(self):

        localctx = ZCodeParser.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 12419072) != 0)):
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




    def const(self):

        localctx = ZCodeParser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114349209288716) != 0)):
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
         




