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
        output += (tok.text, tok.type, '\n')
    with open('output.txt', 'w+', 'utf-8') as saida:
        saida.write(output)
    lexer.reset()
    stream = CommonTokenStream(lexer)
    parser = CompilerParser(stream)
    tree = parser.prog()
    # print(tree.toStringTree())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
