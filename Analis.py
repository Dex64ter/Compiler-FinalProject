from main import *
tokens = []
def nextToken():
    global index_token_atual,tokens
    if index_token_atual<len(tokens):
        index_token_atual +=1
        token_atual = tokens[index_token_atual]
        #print(token_atual, index_token_atual)
        return token_atual
    else:
        return ("EOF", "end of file")

def formerToken():
    global index_token_atual, tokens
    if index_token_atual<len(tokens):
        index_token_atual -=1
        token_atual = tokens[index_token_atual]
        return token_atual


def parser_prog():
    token = tokens[index_token_atual]
    while True:
        if token[0]=="VARNAME":
            token = nextToken()
            parser_decFuncao()
        elif token[1] == "main":
            break
        else:
            raise SyntaxError("expected Declaração de Função")
        token = nextToken()
    parser_main()


def parser_main():
    token = tokens[index_token_atual]
    if token[0] != "':'":
        raise SyntaxError("Expected ':'")
    token = nextToken()
    while index_token_atual<len(tokens) and token[0] != "'end'":
        print("analisar linha 25 gramatica")

    if token[0] != "'end'":
        raise SyntaxError("Expected 'end'")


def parser_decFuncao():
    token = tokens[index_token_atual]
    if token[1] != "(":
        raise SyntaxError("Expected (")
    token = nextToken()
    parser_argFunc()
    if tokens[index_token_atual][1] != ")":
        raise SyntaxError("Expected )")
    token = nextToken()
    if token[1] != ":":
        raise SyntaxError("Expected :")
    token = nextToken()
    if token[0] not in ["VARTYPE", "'void'"]:
        raise SyntaxError("Expected VARTYPE or VOID")
    token = nextToken()
    while token[0] != "'end'":
        if token[1]=="var":
            parser_decVar()
        elif token[1]=="return":
            parser_retorno()
        elif token[1] == "end":
            break
        else:
            parser_comando()
        token = nextToken()
    if token[1] != "end":
        raise SyntaxError("expected 'end'")

def parser_argFunc():
    token = tokens[index_token_atual]
    if token[0] != "VARTYPE":
        raise SyntaxError("expected 'VARTYPE'")
    token = nextToken()
    if token[0] != "VARNAME":
        raise SyntaxError("expected 'VARNAME'")
    token = nextToken()
    while token[0] == ",":
        token = nextToken()
        if token[0]!="VARTYPE":
            raise SyntaxError ("expected VARTYPE")
        token = nextToken()
        if token[0] != "VARNAME":
            raise SyntaxError("expected VARTYPE")
        token = nextToken()

def parser_call():
    parser_callFunction()
    token = nextToken()
    if token != ";":
        SyntaxError("expected ';'")

def parser_callFunction():
    token = tokens[index_token_atual]
    if token[0] != "VARNAME":
        raise SyntaxError("expected VARNAME")
    token = nextToken()
    if token[1] != "(":
        raise SyntaxError("expected '('")
    token = nextToken()
    if token[1] != ")":
        parser_valsCallFunc()
        a = nextToken()
    if token[1] != ")":
        raise SyntaxError("expected ')'")

def parser_valsCallFunc():
    parser_expressaoAritmetica()
    token = nextToken()
    while token[1] == ',':
        parser_expressaoAritmetica()
        token = nextToken()

def parser_retorno():
    token = tokens[index_token_atual]
    if token[1] != "return":
        raise SyntaxError("expected return")
    token = nextToken()
    if token[0]=="VALBOOL":
        parser_expressaoBooleana()
    elif token[0] in ["VALINT", "VALFLOAT", "STRING", "VARNAME"]:
        parser_expressaoAritmetica()
    token = nextToken()
    if token[1]!=';':
        raise SyntaxError("expected ';'")

def parser_comando():
    token = tokens[index_token_atual]
    if token[1] == "scanf":
        parser_funcInput()
    elif token[1] == "print":
        parser_funcPrint()
    elif token[0] == "VARNAME":
        token = nextToken()
        if token[1] in ['+','-','/','*']:
            token = formerToken()
            parser_opMath()
        else:
            parser_call()
    elif token[1] == "if":
        parser_condicional()
    elif token[1] == "while":
        parser_cmdWhile()
    elif token[1] == "return":
        parser_retorno()
    else:
        raise SyntaxError("Invalid Command")

def parser_decVar():
    token = tokens[index_token_atual]
    if token[1] != "var":
        raise SyntaxError ("expected var")
    if token[1] != ":":
        raise SyntaxError ("expected :")
    token = nextToken()
    parser_varList()

def parser_varList():
    token = tokens[index_token_atual]
    if token[0] == "VARNAME":
        token = nextToken()
        if token[1] == ',':
            while token[1] == ",":
                token = nextToken()
                if token[0] != "VARNAME":
                    raise SyntaxError("expected VARNAME")
                token = nextToken()
                if token[1] == ':':
                    break
                if token[1] != ',':
                    raise SyntaxError("expected ',' or ':'")
        token = nextToken()
        if token[0] != "VARTYPE":
            raise SyntaxError ("expected VARTYPE")
    elif token[0] =="const":
        parser_const()
    else:
        raise SyntaxError("expected VARNAME or CONST")
    token = nextToken()
    if token[1] != ";":
        raise SyntaxError("expected ';'")

def parser_const():
    token = tokens[index_token_atual]
    if token[1] != "const":
        raise SyntaxError("expected const")
    token = nextToken()
    if token[0] != "VARNAME":
        raise SyntaxError("expected VARNAME")
    token = nextToken()
    if token[1] != "=":
        raise SyntaxError("expected '='")
    token = nextToken()
    if token[1] not in ['STRING', 'VALINT', 'VALFLOAT', 'VALBOOL', 'VARNAME']:
        raise SyntaxError("Invalid DataType")
    token=nextToken()
    while token[1]==",":
        token = nextToken()
        if token[0] != "VARNAME":
            raise SyntaxError("expected VARNAME")
        token = nextToken()
        if token[1] != "=":
            raise SyntaxError("expected '='")
        token = nextToken()
        if token[1] not in ['STRING', 'VALINT', 'VALFLOAT', 'VALBOOL', 'VARNAME']:
            raise SyntaxError("Invalid DataType")
        token = nextToken()

def parser_funcPrint():
    token = tokens[index_token_atual]
    if token[1] != "print":
        raise SyntaxError("expected Print")
    token = nextToken()
    if token[1] != "(":
        raise SyntaxError("expected '('")
    token = nextToken()
    parser_expressaoAritmetica()
    token = nextToken()
    while token[1]==",":
        token = nextToken()
        parser_expressaoAritmetica()
        token = nextToken()
    if token[1]!=")":
        raise SyntaxError("Expected ')'")
    token = nextToken()
    if token[1] != ";":
        raise SyntaxError("Expected ';'")

def parser_funcInput():
    token = tokens[index_token_atual]
    if token[1] != "scanf":
        raise SyntaxError("expected scanf")
    token = nextToken()
    if token[1] != "(":
        raise SyntaxError("expected '('")
    token = nextToken()
    if token[0] != "VARNAME":
        raise SyntaxError("expected VARNAME")
    token = nextToken()
    while token[1]== ",":
        token = nextToken()
        if token[0] != "VARNAME":
            raise SyntaxError("expected VARNAME")
        token = nextToken()
    if token[1] != ")":
        raise SyntaxError("Expected ')'")
    token = nextToken()
    if token[1] != ";":
        raise SyntaxError("Expected ';'")

def parser_condicional():
    token=tokens[index_token_atual]
    if token[1] != "if":
        raise SyntaxError ("Expected 'if'")
    token = nextToken()
    if token[1] != "(":
        raise SyntaxError ("Expected '('")
    token = nextToken()
    parser_expressaoBooleana()
    token = tokens[index_token_atual]
    if token[1] != ")":
        raise SyntaxError ("Expected ')'")
    token = nextToken()
    if token[1] != ":":
        raise SyntaxError ("Expected ':'")
    token = nextToken()
    while True:
        parser_comando()
        token = nextToken()
        if token[1] in ["else","end"]:
            break
    if token[1] == "else":
        parser_condElse()
    if token[1] != "end":
        raise SyntaxError("Expected 'End'")

def parser_condElse():
    token = tokens[index_token_atual]
    if token[1] != "else":
        raise SyntaxError ("Expected 'else'")
    token = nextToken()
    while True:
        parser_comando()
        token = nextToken()
        if token[1] == "end":
            break

def parser_cmdWhile():
    token = tokens[index_token_atual]
    if token[1] != "while":
        raise SyntaxError ("expected 'While'")
    token = nextToken()
    if token[1] != "(":
        raise SyntaxError ("expected '('")
    token = nextToken()
    parser_expressaoBooleana()
    token = nextToken()
    if token[1] not in [')','):']:
        raise SyntaxError("expected ')' or '):'")
    token = nextToken()
    if token[1] != ":":
        raise SyntaxError ("expected ':'")
    token = nextToken()
    while True:
        if token[1]=="end":
            break
        if token[1] == "break;":
            break
        parser_comando()
        token = nextToken()
    if token.value != "end":
        raise SyntaxError("Expected 'end'")

def parser_opMath():
    token = tokens[index_token_atual]
    if token[0]!= "VARNAME":
        raise SyntaxError("Expected 'VARNAME'")
    token =nextToken()
    if token[0]!= "=":
        raise SyntaxError("Expected '='")
    token = nextToken()
    parser_expressaoAritmetica()
    token = nextToken()
    if token[0]!= ";":
        raise SyntaxError("Expected ';'")

def parser_expressaoAritmetica():
    parser_termo()
    token = nextToken()
    if token[1] in ["+","-"]:
        token = nextToken()
        parser_expressaoAritmetica()
    else:
        token = formerToken()


def parser_termo():
    parser_fator()
    if tokens[index_token_atual] in ["*","/"]:
        nextToken()
        parser_termo()
    else:
        token = formerToken()

def parser_fator():
    token = tokens[index_token_atual]
    if token[0] in ['VALFLOAT','VALINT','STRING']:
        token = nextToken()
    elif token[0] == "VARNAME":
        token = nextToken()
        if token == "(":
            token = formerToken()
            parser_callFunction()
    elif token[1] == "(":
        token = nextToken()
        parser_expressaoAritmetica()
        token = nextToken()
        if token[1] != ")":
            raise SyntaxError("expected ')'")
    else:
        raise SyntaxError("Expected VALFLOAT','VALINT','STRING' or 'VARNAME")

def parser_expressaoBooleana():
    token = tokens[index_token_atual]
    if token[1] == "(":
        token = nextToken()
        parser_expressaoBooleana()
        token = nextToken()
        if token[1] != ")":
            raise SyntaxError("expected ')'")
    else:
        parser_condicao()

def parser_condicao():
    token = tokens[index_token_atual]
    if token[1] in ['true','false']:
        parser_valorBool()
    else:
        parser_expressaoRelacional()

def parser_valorBool():
    token = tokens[index_token_atual]
    if token[0] != "VALBOL":
        raise SyntaxError("expected Boolean Value")

def parser_expressaoRelacional():
    parser_expressaoAritmetica()
    token = nextToken()
    parser_operadorRelacional()
    parser_expressaoAritmetica()
    token = nextToken()

def parser_operadorRelacional():
    token = tokens[index_token_atual]
    if token[1] not in ['==','!=','<','<=','>','>=']:
        raise SyntaxError("Expected Valid Operator")
    token = nextToken()

def parser_init():
    inicializar()
    return parser_prog()
def inicializar():
    global tokens, index_token_atual
    a = open("output.txt", "r").read().splitlines()
    for b in range(len(a)):
        s =a[b][1:-1].split(",",1)
        a[b] = tuple([s[0],s[1]])
    tokens = a
    index_token_atual = 0


parser_init()
