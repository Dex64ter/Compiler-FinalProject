from antlr4 import *

from gen.CompilerLexer import CompilerLexer
from gen.CompilerParser import CompilerParser

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dados = FileStream('input.txt')
    # dados = InputStream("hello Raimundo, Santos, Moura.")
    lexer = CompilerLexer(dados)
    output = ""
    for tok in lexer.getAllTokens():    # Ajeitando a string para saída adequada no arquivo
        output += '<'+str(tok.type) + ',' + str(tok.text) +'>'+ '\n'
    lexer.reset()
    stream = CommonTokenStream(lexer)
    parser = CompilerParser(stream)
    tree = parser.prog()
    with open('output.txt', 'w+') as saida:     # Imprimindo os tokens e os tipos dos tokens no arquivo
        saida.write(output)