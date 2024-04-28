grammar ZCode;

@lexer::header {
from lexererr import *
# Trần Nguyễn Thái Bình - 2110051
}

options {
	language=Python3;
}


// ============================ PARSER ============================ TESTCASE 287, 289
program: null_newline declist EOF;
declist: decl declist | decl;
decl: (variabledec | funcdecl) newlines;

/* Variable Declaration */
variabledec: typedecl 
           | vardecl 
	   | arrdecl
           | dyndecl;

dyndecl: DYNAMIC ID
       | DYNAMIC ID ASSIGN expr;

typedecl: typ ID 
	| typ ID ASSIGN expr;

vardecl: VAR ID ASSIGN expr;

arrdecl: typ ID dimension
       | typ ID dimension ASSIGN expr;

dimension: SQ_OPEN numlitlist SQ_CLOSE;

numlitlist: NUMLIT COMMA numlitlist 
          | NUMLIT;

array: SQ_OPEN vallist SQ_CLOSE;

vallist: expr COMMA vallist
       | expr;

typ: NUMBER 
   | BOOL 
   | STRING;

/* Funcion Declaration */
funcdecl: FUNC ID R_OPEN paramlist R_CLOSE null_newline funcstmt;
funcstmt: funcprime 
        | ;

funcprime: returnstmt 
         | blockstmt;

paramlist: paramprime 
         | ;

paramprime: paramdecl COMMA paramprime 
          | paramdecl;

paramdecl: typ ID 
         | typ ID dimension;

/* Statements */
stmt: normalstmt | condstmt;

condstmt: ifstmt 
        | forstmt;

normalstmt: (varstmt 
          | assignstmt 
          | callstmt 
          | breakstmt 
          | contstmt 
          | returnstmt
          | blockstmt) newlines;


ifstmt: IF R_OPEN expr R_CLOSE null_newline stmt eliflist elsepart;

eliflist: elifpart eliflist 
        | ;

elifpart: ELIF R_OPEN expr R_CLOSE null_newline stmt;

elsepart: ELSE null_newline stmt 
        | ;

varstmt: variabledec;

assignstmt: lhs ASSIGN expr;
lhs: ID indexop 
   | ID;


forstmt: FOR ID UNTIL expr BY expr null_newline stmt;

breakstmt: BREAK;

contstmt: CONTINUE;

returnstmt: RETURN expr
          | RETURN;

callstmt: ID R_OPEN exprlist R_CLOSE;

exprlist: exprparam 
        | ;

exprparam: expr COMMA exprparam 
	 | expr;

blockstmt: BEGIN newlines stmtlist END;

stmtlist: stmt stmtlist 
        | ;

newlines: NEWLINE newlines
        | NEWLINE;

null_newline: newlines 
            | ;

/* Expression */
expr: expr1 CONCAT expr1 | expr1;
expr1: expr2 rel_op expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: (ID | callexpr) indexop | expr8;
indexop: SQ_OPEN exprparam SQ_CLOSE;
expr8: const | array | callexpr | subexpr;
subexpr: R_OPEN expr R_CLOSE;

callexpr: ID R_OPEN exprlist R_CLOSE;

rel_op: NUMEQ | STREQ | NEQ | LT | GT | LEQ | GEQ;
const: NUMLIT | TRUE | FALSE | STRINGLIT | ID;

// ================ LEXER ==============
/* Comment */
CMT: '##' CMTCHAR* -> skip;
fragment CMTCHAR: ~[\n];

/* Keywords For Boolean */
TRUE: 'true';
FALSE: 'false';

/* Keywords For Data Type */
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';

/* Keywords For Logic Operators */
NOT: 'not';
AND: 'and';
OR: 'or';

/* Keywords For Operators */
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NUMEQ: '=';
NEQ: '!=';
ASSIGN: '<-';
LT: '<';
LEQ: '<=';
GT: '>';
GEQ: '>=';
CONCAT: '...';
STREQ: '==';

/* Keywords For Seperators */
R_OPEN: '('; R_CLOSE: ')';
SQ_OPEN: '['; SQ_CLOSE: ']';
COMMA: ',';

/* Other Keywords */
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';

/* Number Literals */
NUMLIT: INTPART DECPART? EXPPART?;
fragment INTPART: [0-9]+;
fragment DECPART: '.'([0-9]+)?;
fragment EXPPART: [eE]('+'|'-')?[0-9]+;

/* Boolean Literals */
BOOLLIT: TRUE | FALSE;
/* String Literals */
STRINGLIT: ["] CHAR* ["]{
	temp = self.text
	self.text = temp[1:-1]
};
fragment ESC_STR: ('\\' [bnfrt'\\]);
fragment DQ_STR: '\'"';
fragment CHAR: (DQ_STR| ESC_STR | ~[\\\r\n"]);
fragment INVALID_ESC: ('\\' ~[btnfr'\\]);

/* Identifier */
ID: [A-Za-z_][A-Za-z0-9_]*;
NEWLINE: '\n' | '\r\n' {self.text = '\n'};
WS : [\t\f\b ]+  -> skip ; // skip spaces, tabs, newlines
/*Handling Error*/

UNCLOSE_STRING: '"' CHAR* ([\n\r] | EOF) {
    ESC = ['\r', '\n']
    text = str(self.text)
    if text[-1] in ESC:
	    raise UncloseString(text[1:-1])
    else: 
        raise UncloseString(text[1:]) 
};
ILLEGAL_ESCAPE: '"' CHAR* INVALID_ESC {
	raise IllegalEscape(self.text[1:])
};
ERROR_TOKEN: . {raise ErrorToken(self.text)};



