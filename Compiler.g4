grammar Compiler;

prog: decFuncao* main;

// Declaração de função
decFuncao: NAMEFUNCTION argsFunc ':' ( 'void' | VARTYPE ) decVar* comandos* 'end';
argsFunc: (VARTYPE VARNAME(',')?)* ')';

//Função principal
main: 'main' ':' decVar* comandos* 'end';

// Declaração de variável
decVar: 'var' ':' varlist+;
varlist: (VARNAME ','?)+ ':' VARTYPE ';' | consts ';';
consts: 'const' ((VARNAME '=' (STRING | VALINT | VALFLOAT | VALBOOL ))','?)+;

// Tipos de comandos existentes
// a fazer
comandos: 'COMANDO';

VARTYPE: 'int' | 'str' | 'float' | 'bool'; // Tipo de variável
VALBOOL: 'true' | 'false' ;     // Valor de variável booleana
NAMEFUNCTION: [a-zA-Z]+ ('('|' ''(');
VARNAME: ([a-zA-Z]+([0-9]+)*);
STRING: '"'([a-zA-Z]*[0-9]*)'"';
VALFLOAT: ([0-9]+'.'[0-9]+);
VALINT: [0-9]+;

WS: [ \t\r\n] -> skip;