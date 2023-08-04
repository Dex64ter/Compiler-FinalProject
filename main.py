from antlr4 import *

from gen.CompilerLexer import CompilerLexer
from gen.CompilerParser import CompilerParser


if __name__ == '__main__':
    dados = FileStream('input.txt')
    lexer = CompilerLexer(dados)

    with open('gen/Compiler.tokens', 'r+') as tT:
        Tokens = tT.readlines()
    typeTokens = {}
    for i in Tokens:
        j = -2
        key =[]
        while i[j].isdigit():
            key.insert(0, i[j])
            j-=1
        typeTokens[''.join(key)] = i[0:len(i)+j]

    output = ""
    for tok in lexer.getAllTokens():    # Ajeitando a string para saída adequada no arquivo
        output += '<'+ typeTokens[str(tok.type)] + ',' + str(tok.text) +'>'+ '\n'
    lexer.reset()
    stream = CommonTokenStream(lexer)
    parser = CompilerParser(stream)
    tree = parser.prog()
    with open('output.txt', 'w+') as saida:     # Imprimindo os tokens e os tipos dos tokens no arquivo
        saida.write(output)