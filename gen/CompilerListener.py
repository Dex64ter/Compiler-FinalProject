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


    # Enter a parse tree produced by CompilerParser#call.
    def enterCall(self, ctx:CompilerParser.CallContext):
        pass

    # Exit a parse tree produced by CompilerParser#call.
    def exitCall(self, ctx:CompilerParser.CallContext):
        pass


    # Enter a parse tree produced by CompilerParser#callFunction.
    def enterCallFunction(self, ctx:CompilerParser.CallFunctionContext):
        pass

    # Exit a parse tree produced by CompilerParser#callFunction.
    def exitCallFunction(self, ctx:CompilerParser.CallFunctionContext):
        pass


    # Enter a parse tree produced by CompilerParser#valsCallFunc.
    def enterValsCallFunc(self, ctx:CompilerParser.ValsCallFuncContext):
        pass

    # Exit a parse tree produced by CompilerParser#valsCallFunc.
    def exitValsCallFunc(self, ctx:CompilerParser.ValsCallFuncContext):
        pass


    # Enter a parse tree produced by CompilerParser#return.
    def enterReturn(self, ctx:CompilerParser.ReturnContext):
        pass

    # Exit a parse tree produced by CompilerParser#return.
    def exitReturn(self, ctx:CompilerParser.ReturnContext):
        pass


    # Enter a parse tree produced by CompilerParser#comandos.
    def enterComandos(self, ctx:CompilerParser.ComandosContext):
        pass

    # Exit a parse tree produced by CompilerParser#comandos.
    def exitComandos(self, ctx:CompilerParser.ComandosContext):
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


    # Enter a parse tree produced by CompilerParser#funcprint.
    def enterFuncprint(self, ctx:CompilerParser.FuncprintContext):
        pass

    # Exit a parse tree produced by CompilerParser#funcprint.
    def exitFuncprint(self, ctx:CompilerParser.FuncprintContext):
        pass


    # Enter a parse tree produced by CompilerParser#funcinput.
    def enterFuncinput(self, ctx:CompilerParser.FuncinputContext):
        pass

    # Exit a parse tree produced by CompilerParser#funcinput.
    def exitFuncinput(self, ctx:CompilerParser.FuncinputContext):
        pass


    # Enter a parse tree produced by CompilerParser#condicional.
    def enterCondicional(self, ctx:CompilerParser.CondicionalContext):
        pass

    # Exit a parse tree produced by CompilerParser#condicional.
    def exitCondicional(self, ctx:CompilerParser.CondicionalContext):
        pass


    # Enter a parse tree produced by CompilerParser#condElse.
    def enterCondElse(self, ctx:CompilerParser.CondElseContext):
        pass

    # Exit a parse tree produced by CompilerParser#condElse.
    def exitCondElse(self, ctx:CompilerParser.CondElseContext):
        pass


    # Enter a parse tree produced by CompilerParser#cmdWhile.
    def enterCmdWhile(self, ctx:CompilerParser.CmdWhileContext):
        pass

    # Exit a parse tree produced by CompilerParser#cmdWhile.
    def exitCmdWhile(self, ctx:CompilerParser.CmdWhileContext):
        pass


    # Enter a parse tree produced by CompilerParser#opMath.
    def enterOpMath(self, ctx:CompilerParser.OpMathContext):
        pass

    # Exit a parse tree produced by CompilerParser#opMath.
    def exitOpMath(self, ctx:CompilerParser.OpMathContext):
        pass


    # Enter a parse tree produced by CompilerParser#expressaoAritmetica.
    def enterExpressaoAritmetica(self, ctx:CompilerParser.ExpressaoAritmeticaContext):
        pass

    # Exit a parse tree produced by CompilerParser#expressaoAritmetica.
    def exitExpressaoAritmetica(self, ctx:CompilerParser.ExpressaoAritmeticaContext):
        pass


    # Enter a parse tree produced by CompilerParser#termo.
    def enterTermo(self, ctx:CompilerParser.TermoContext):
        pass

    # Exit a parse tree produced by CompilerParser#termo.
    def exitTermo(self, ctx:CompilerParser.TermoContext):
        pass


    # Enter a parse tree produced by CompilerParser#fator.
    def enterFator(self, ctx:CompilerParser.FatorContext):
        pass

    # Exit a parse tree produced by CompilerParser#fator.
    def exitFator(self, ctx:CompilerParser.FatorContext):
        pass


    # Enter a parse tree produced by CompilerParser#expressaoBooleana.
    def enterExpressaoBooleana(self, ctx:CompilerParser.ExpressaoBooleanaContext):
        pass

    # Exit a parse tree produced by CompilerParser#expressaoBooleana.
    def exitExpressaoBooleana(self, ctx:CompilerParser.ExpressaoBooleanaContext):
        pass


    # Enter a parse tree produced by CompilerParser#condicao.
    def enterCondicao(self, ctx:CompilerParser.CondicaoContext):
        pass

    # Exit a parse tree produced by CompilerParser#condicao.
    def exitCondicao(self, ctx:CompilerParser.CondicaoContext):
        pass


    # Enter a parse tree produced by CompilerParser#expressaoRelacional.
    def enterExpressaoRelacional(self, ctx:CompilerParser.ExpressaoRelacionalContext):
        pass

    # Exit a parse tree produced by CompilerParser#expressaoRelacional.
    def exitExpressaoRelacional(self, ctx:CompilerParser.ExpressaoRelacionalContext):
        pass


    # Enter a parse tree produced by CompilerParser#operadorRelacional.
    def enterOperadorRelacional(self, ctx:CompilerParser.OperadorRelacionalContext):
        pass

    # Exit a parse tree produced by CompilerParser#operadorRelacional.
    def exitOperadorRelacional(self, ctx:CompilerParser.OperadorRelacionalContext):
        pass



del CompilerParser