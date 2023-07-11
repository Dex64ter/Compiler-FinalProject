grammar Compiler;

prog: decFuncao* main;

// Declaração de função
decFuncao: NAMEFUNCTION argsFunc ':' ( 'void' | VARTYPE ) decVar* comandos* return* 'end';
argsFunc: (VARTYPE VARNAME (',' VARTYPE VARNAME)*)? ')';    // argumentos da função
call: callFunction';' ;         // chamada de função com ;
callFunction: NAMEFUNCTION valsCallFunc? ')'; // (')'|');')
valsCallFunc: (expressaoAritmetica) ((',' expressaoAritmetica)*)?;      // valores da chamada de função
return: RETORNO (expressaoBooleana | expressaoAritmetica) ';';      // função de retorno


// Tipos de comandos existentes
comandos: funcinput+
    | funcprint+
    | opMath+
    | condicional+
    | cmdWhile+
    | call+
    | return+
    ;

//Função principal
main: 'main' ':' decVar* comandos* 'end';

// Declaração de variável
decVar: 'var' ':' varlist+;
varlist: (VARNAME ','?)+ ':' VARTYPE ';' | consts ';';
consts: 'const' ((IGUALDADE (STRING | VALINT | VALFLOAT | VALBOOL | VARNAME ))','?)+;

// Estrutura de impressão
funcprint: PRINT (VARNAME | STRING | expressaoAritmetica) (',' (VARNAME | STRING | expressaoAritmetica ) )* ');';

// Estrutura de entrada
funcinput: SCAN VARNAME (',' VARNAME)* ');';

// Estrutura condicional
condicional: CMDIF expressaoBooleana '):' comandos+ ((condElse) | 'end');
condElse: CMDELSE comandos+ 'end';

// Estrutura de repetição
cmdWhile: CMDWHILE expressaoBooleana '):' comandos+ 'end';

// Operações matemáticas
opMath: IGUALDADE expressaoAritmetica';';
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
    | callFunction
    | '('expressaoAritmetica')'
    ;

// Operações lógicas
expressaoBooleana: condicao         // Lógica para expressões booleanas
    | expressaoBooleana operadorLogico expressaoBooleana
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
valorBool: 'true' | 'false' ;
operadorLogico: 'and' | 'or' | 'not';

// Funções nativas
CMDWHILE: 'while(';
CMDIF: 'if (';
CMDELSE: 'else:';
PRINT: 'print (';
SCAN: 'scanf(';

// Igualdade e retorno
IGUALDADE: VARNAME ('='|' =');
RETORNO: 'return ';

// Valores, tipos, tokens, etc
VARTYPE: 'int' | 'str' | 'float' | 'bool'; // Tipo de variável
VALBOOL: 'true' | 'false' ;     // Valor de variável booleana
NAMEFUNCTION: [a-zA-Z]+ ('('|' ''(');    // início do escopo de uma função
VARNAME: ([a-zA-Z]+([0-9]+)*);    // declaração de nome de função
STRING: '"'([ çáâàêéíóúãa-zÇÁÂÀÃÊÉÍÓÚA-Z.,;:!?]* [ 0-9]* PONTUACAO?)'"';  // identificador de strings
VALFLOAT: ([0-9]+'.'[0-9]+);     // identificador de números do tipo float
VALINT: [0-9]+;       // identificador de números do tipo int
PONTUACAO: [.,;:!?];

WS: [ \t\r\n] -> skip;