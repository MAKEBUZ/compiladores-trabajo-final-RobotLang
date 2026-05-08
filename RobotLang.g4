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
    : 'sensor' ID ';'
    ;

// ─── Rutinas ────────────────────────────────────────────────
routine
    : 'rutina' ID '(' ')' '{' statement+ '}'
    ;

// ─── Sentencias ─────────────────────────────────────────────
statement
    : control
    | action
    | call
    ;

control
    : 'si' expr ':' statement ('sino' ':' statement)?
    ;

action
    : 'ejecutar' ID '(' ')' ';'
    ;

call
    : ID '(' ')' ';'
    ;

// ─── Expresiones ────────────────────────────────────────────
expr
    : ID comparator NUMBER
    ;

comparator
    : '<'
    | '>'
    | '=='
    ;

// ─── Tokens léxicos ─────────────────────────────────────────
// Palabras reservadas
SENSOR   : 'sensor'   ;
RUTINA   : 'rutina'   ;
SI       : 'si'       ;
SINO     : 'sino'     ;
EJECUTAR : 'ejecutar' ;

// Identificadores y números
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER  : [0-9]+ ('.' [0-9]+)?   ;

// Ignorar espacios y comentarios
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
