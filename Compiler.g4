grammar Compiler;

prog: decFuncao* main;

// Declaração de função
decFuncao: VARNAME '(' argsFunc ')' ':' ( 'void' | VARTYPE ) decVar* comandos* return* 'end';
argsFunc: (VARTYPE VARNAME (',' VARTYPE VARNAME)*)? ;    // argumentos da função
call: callFunction';' ;      // chamada de função com ;
callFunction returns [type]: VARNAME '(' valsCallFunc? ')'; // (')'|');')
valsCallFunc: (expressaoAritmetica) ((',' expressaoAritmetica)*)?;      // valores da chamada de função
return: RETORNO opMathR;      // função de retorno


// Tipos de comandos existentes
comandos: funcinput
    | funcprint
    | opMath
    | opMathR
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
opMath returns [type, isBool, val]: VARNAME ('=') ( expressaoAritmetica | expressaoBooleana )';';
opMathR returns [type, isBool, val]: (  expressaoAritmetica | expressaoBooleana )';';//-

expressaoAritmetica returns [type, isBool, val]: termo #e_termo
    |expressaoAritmetica op=('+' | '-') termo   #sum_minus
    ;

termo returns [type, val]: fator    #e_factor
    | termo op=('*' | '/') fator    #time_div
    ;

fator returns [type, val]: VARNAME   #var_name
    | VALFLOAT  #float_value
    | VALINT    #int_value
    | STRING    #str_val
    | callFunction #func_call
    | '('expressaoAritmetica')' #expr
    ;

// Operações lógicas
expressaoBooleana returns [type, inh_type, isBool, val]: condicao         // Lógica para expressões booleanas
    | '(' expressaoBooleana ')'
    ;
condicao returns [type, isBool, val]: valorBool
    | expressaoRelacional
    ;
expressaoRelacional returns [type, isBool, val]
    : expressaoAritmetica op=
    ( '=='
    | '!='
    | '<'
    | '<='
    | '>'
    | '>='
    )
    expressaoAritmetica;
valorBool returns [type, isBool, val]: VALBOOL
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