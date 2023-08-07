grammar Compiler;

prog: decFuncao* main;

// Declaração de função
decFuncao: VARNAME '(' argsFunc ')' ':' ( 'void' | VARTYPE ) decVar* comandos* return* 'end';
argsFunc: (VARTYPE VARNAME (',' VARTYPE VARNAME)*)? ;    // argumentos da função
call: callFunction';' ;      // chamada de função com ;
callFunction: VARNAME '(' valsCallFunc? ')'; // (')'|');')
valsCallFunc: (expressaoAritmetica) ((',' expressaoAritmetica)*)?;      // valores da chamada de função
return: RETORNO (expressaoBooleana | expressaoAritmetica) ';';      // função de retorno


// Tipos de comandos existentes
comandos: funcinput
    | funcprint
    | opMath
    | condicional
    | cmdWhile
    | call
    | return
    ;

//Função principal
main: 'main' ':' decVar* comandos* 'end';

// Declaração de variável
decVar: 'var' ':' varlist+;
varlist: (VARNAME ','?)+ ':' VARTYPE ';' | consts ';';
consts: 'const' ((VARNAME ('=') (STRING | VALINT | VALFLOAT | VALBOOL | VARNAME ))','?)+;//--

// Estrutura de impressão
funcprint: PRINT '(' (expressaoAritmetica) (',' (expressaoAritmetica ) )* ')'';';

// Estrutura de entrada
funcinput: SCAN '(' VARNAME (',' VARNAME)* ')'';';

// Estrutura condicional
condicional: CMDIF '(' expressaoBooleana ')'':' comandos+ ((condElse) | 'end');
condElse: CMDELSE ':' comandos+;

// Estrutura de repetição
cmdWhile: CMDWHILE '(' expressaoBooleana ')' ':' comandos+ ('break;')* 'end';

// Operações matemáticas
opMath: VARNAME ('=') expressaoAritmetica';'; //-
expressaoAritmetica: termo
    | termo '+' expressaoAritmetica
    | termo '-' expressaoAritmetica
    ;
termo: fator
    | fator '*' termo
    | fator '/' termo
    ;
fator: VARNAME
    | VALFLOAT
    | VALINT
    | VALBOOL
    | STRING
    | callFunction
    | '('expressaoAritmetica')'
    ;

// Operações lógicas
expressaoBooleana: condicao         // Lógica para expressões booleanas
    | '(' expressaoBooleana ')'
    ;
condicao: valorBool
    | expressaoRelacional
    ;
expressaoRelacional: expressaoAritmetica operadorRelacional expressaoAritmetica;
operadorRelacional: '=='
    | '!='
    | '<'
    | '<='
    | '>'
    | '>='
    ;
valorBool: VALBOOL
    ;
// Funções nativas
CMDWHILE: 'while';
CMDIF: 'if';
CMDELSE: 'else';
PRINT: 'print';
SCAN: 'scanf';

// Igualdade e retorno
RETORNO: 'return';

// Valores, tipos, tokens, etc
VARTYPE: 'int' | 'str' | 'float' | 'bool'; // Tipo de variável
VALBOOL: 'true' | 'false' ;     // Valor de variável booleana
VARNAME: ([a-zA-Z]+([0-9]+)*);    // declaração de nome de função
STRING: '"'([ çáâàêéíóúãa-zÇÁÂÀÃÊÉÍÓÚA-Z0-9.,;:!?]* PONTUACAO?)'"';  // identificador de strings
VALFLOAT: ([0-9]+'.'[0-9]+);     // identificador de números do tipo float
VALINT: [0-9]+;       // identificador de números do tipo int
PONTUACAO: [.,;:!?];

COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

WS: [ \t\r\n] -> skip;