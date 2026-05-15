// ============================================================
//  RobotLang — Gramática ANTLR4
//  Mini-compilador para configuración de robots
//  Universidad Cooperativa de Colombia — Compiladores 2026
// ============================================================

grammar RobotLang;

// ─── Regla de inicio ────────────────────────────────────────
program
    : (declaration | routine | statement)+ EOF
    ;

// ─── Declaraciones ──────────────────────────────────────────
declaration
    : SENSOR ID ';'
    ;

// ─── Rutinas ────────────────────────────────────────────────
routine
    : RUTINA ID '(' ')' '{' statement+ '}'
    ;

// ─── Sentencias ─────────────────────────────────────────────
statement : control | action | call ;

control
    : SI expr ':' statement (SINO ':' statement)?
    ;

action : EJECUTAR ID '(' ')' ';' ;
call   : ID '(' ')' ';' ;

// ─── Expresiones ────────────────────────────────────────────
expr       : ID comparator NUMBER ;
comparator : LT | GT | EQ ;

// ─── Keywords ───────────────────────────────────────────────
SENSOR   : 'sensor'   ;
RUTINA   : 'rutina'   ;
SI       : 'si'       ;
SINO     : 'sino'     ;
EJECUTAR : 'ejecutar' ;

// ─── Comparadores ───────────────────────────────────────────
LT : '<'  ;
GT : '>'  ;
EQ : '==' ;

// ─── Identificadores y números ──────────────────────────────
ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER : [0-9]+ ('.' [0-9]+)?   ;

// ─── Ignorar ────────────────────────────────────────────────
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
