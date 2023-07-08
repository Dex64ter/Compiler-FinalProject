grammar Compiler;

prog: decFuncao* main;

// Declaração de função
decFuncao: NAMEFUNCTION argsFunc ':' ( 'void' | VARTYPE ) decVar* comandos* 'end';
argsFunc: (VARTYPE VARNAME (',' VARTYPE VARNAME)*)? ')';

//Função principal
main: 'main' ':' decVar* comandos* 'end';

// Declaração de variável
decVar: 'var' ':' varlist+;
varlist: (VARNAME ','?)+ ':' VARTYPE ';' | consts ';';
consts: 'const' ((VARNAME '=' (STRING | VALINT | VALFLOAT | VALBOOL ))','?)+;

// Tipos de comandos existentes
// a fazer
comandos: funcinput+
    | funcprint+
    | condicional+
    | cmdWhile+
    ;

// Estrutura de impressão
funcprint: PRINT ( VARNAME (',' (VARNAME | STRING) )* | STRING (',' (VARNAME | STRING) )* ) ');';

// Estrutura de entrada
funcinput: SCAN VARNAME (',' VARNAME)* ');';

// Estrutura condicional
condicional: CMDIF '<teste logico>' '):' comandos+ (CMDELSE comandos+)? 'end';

// Estrutura de repetição
cmdWhile: CMDWHILE '(' '<condição>' '):' comandos+ 'end';

// A Fazer:
// regra para operações
// regra para operadores lógicos


CMDWHILE: 'while';
CMDIF: 'if (';
CMDELSE: 'else:';
PRINT: 'print (';
SCAN: 'scanf(';
VARTYPE: 'int' | 'str' | 'float' | 'bool'; // Tipo de variável
VALBOOL: 'true' | 'false' ;     // Valor de variável booleana
NAMEFUNCTION: [a-zA-Z]+ ('('|' ''(');    // início do escopo de uma função
VARNAME: ([a-zA-Z]+([0-9]+)*);    // declaração de nome de função
STRING: '"'([ áâàêéíóúãa-zÁÂÀÃÊÉÍÓÚA-Z]*[ 0-9]*)'"';  // identificador de strings
VALFLOAT: ([0-9]+'.'[0-9]+);     // identificador de números do tipo float
VALINT: [0-9]+;       // identificador de números do tipo int

WS: [ \t\r\n] -> skip;