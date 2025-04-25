grammar Calculator;

// --- MAIN PROGRAM ---

program 
    : statement+ 
    ;

statement 
    : expression NEWLINE
    | ID '=' expression NEWLINE
    | NEWLINE
    ;

// --- EXPRESSIONS ---

expression
    : expression op=(MUL | DIV) expression    # MulDivExpr
    | expression op=(ADD | SUB) expression    # AddSubExpr
    | expression op=(GT | LT) expression       # CompareExpr
    | function '(' expression ')'             # FunctionExpr
    | INT                                     # IntExpr
    | ID                                      # IdExpr
    | '(' expression ')'                      # ParensExpr
    ;

// --- FUNCTIONS ---

function 
    : 'cos'
    | 'sin'
    | 'tan'
    | 'acos'
    | 'asin'
    | 'atan'
    | 'sqrt'
    | 'log'
    | 'ln'
    ;

// --- TOKENS ---

ID : [a-zA-Z]+ ;
INT : [0-9]+ ;
NEWLINE : '\r'? '\n' ;
WS : [ \t]+ -> skip ;

ADD : '+' ;
SUB : '-' ;
MUL : '*' ;
DIV : '/' ;
GT  : '>' ;
LT  : '<' ;
