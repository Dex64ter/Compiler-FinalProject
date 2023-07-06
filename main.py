from antlr4 import *

from gen.CompilerLexer import CompilerLexer
from gen.CompilerParser import CompilerParser

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dados = FileStream('input.txt')
    # dados = InputStream("hello Raimundo, Santos, Moura.")
    lexer = CompilerLexer(dados)
    output = ''
    for tok in lexer.getAllTokens():
        output += str(tok.text) + ' ' + '-'*(10-len(str(tok.text))) + ' ' + str(tok.type) + '\n'
    lexer.reset()
    stream = CommonTokenStream(lexer)
    parser = CompilerParser(stream)
    tree = parser.prog()
    with open('output.txt', 'w+') as saida:
        saida.write(output)