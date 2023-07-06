# Generated from C:/Users/davij/PycharmProjects/Compiler-FinalProject\Compiler.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CompilerParser import CompilerParser
else:
    from CompilerParser import CompilerParser

# This class defines a complete listener for a parse tree produced by CompilerParser.
class CompilerListener(ParseTreeListener):

    # Enter a parse tree produced by CompilerParser#prog.
    def enterProg(self, ctx:CompilerParser.ProgContext):
        pass

    # Exit a parse tree produced by CompilerParser#prog.
    def exitProg(self, ctx:CompilerParser.ProgContext):
        pass


    # Enter a parse tree produced by CompilerParser#decFuncao.
    def enterDecFuncao(self, ctx:CompilerParser.DecFuncaoContext):
        pass

    # Exit a parse tree produced by CompilerParser#decFuncao.
    def exitDecFuncao(self, ctx:CompilerParser.DecFuncaoContext):
        pass


    # Enter a parse tree produced by CompilerParser#argsFunc.
    def enterArgsFunc(self, ctx:CompilerParser.ArgsFuncContext):
        pass

    # Exit a parse tree produced by CompilerParser#argsFunc.
    def exitArgsFunc(self, ctx:CompilerParser.ArgsFuncContext):
        pass


    # Enter a parse tree produced by CompilerParser#main.
    def enterMain(self, ctx:CompilerParser.MainContext):
        pass

    # Exit a parse tree produced by CompilerParser#main.
    def exitMain(self, ctx:CompilerParser.MainContext):
        pass


    # Enter a parse tree produced by CompilerParser#decVar.
    def enterDecVar(self, ctx:CompilerParser.DecVarContext):
        pass

    # Exit a parse tree produced by CompilerParser#decVar.
    def exitDecVar(self, ctx:CompilerParser.DecVarContext):
        pass


    # Enter a parse tree produced by CompilerParser#varlist.
    def enterVarlist(self, ctx:CompilerParser.VarlistContext):
        pass

    # Exit a parse tree produced by CompilerParser#varlist.
    def exitVarlist(self, ctx:CompilerParser.VarlistContext):
        pass


    # Enter a parse tree produced by CompilerParser#consts.
    def enterConsts(self, ctx:CompilerParser.ConstsContext):
        pass

    # Exit a parse tree produced by CompilerParser#consts.
    def exitConsts(self, ctx:CompilerParser.ConstsContext):
        pass


    # Enter a parse tree produced by CompilerParser#comandos.
    def enterComandos(self, ctx:CompilerParser.ComandosContext):
        pass

    # Exit a parse tree produced by CompilerParser#comandos.
    def exitComandos(self, ctx:CompilerParser.ComandosContext):
        pass



del CompilerParser