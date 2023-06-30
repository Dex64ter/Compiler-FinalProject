grammar Compiler;

prog: decFuncao* main;

decFuncao: NAME '(' (VARTYPE VARNAME ','?)* ')' ':' ( 'void' | VARTYPE ) 'end';

main: 'main' ':' decVar* comandos* 'end';

// Declaração de variável
decVar: 'var' ':' varlist+;
varlist: (VARNAME ','?)+ ':' VARTYPE ';' | consts ';';
consts: 'const' ((VARNAME '=' ('"'VARNAME'"' | VALINT | VALFLOAT ))','?)+;

comandos: 'COMANDO';


VARTYPE: 'int'
        | 'str'
        | 'float'
        ;

VARNAME: ([a-zA-Z]+([0-9]+)*);
NAME: [a-zA-Z]+;
VALFLOAT: ([0-9]+'.'[0-9]+);
VALINT: [0-9]+;

WS: [ \t\r\n] -> skip;