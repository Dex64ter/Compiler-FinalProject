# Generated from C:/Users/ryant/OneDrive/Área de Trabalho/2023.1/COMPILADORES/Compiler-FinalProject\Compiler.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CompilerParser import CompilerParser
else:
    from CompilerParser import CompilerParser

# This class defines a complete generic visitor for a parse tree produced by CompilerParser.

class CompilerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CompilerParser#prog.
    def visitProg(self, ctx:CompilerParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#decFuncao.
    def visitDecFuncao(self, ctx:CompilerParser.DecFuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#call.
    def visitCall(self, ctx:CompilerParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#callFunction.
    def visitCallFunction(self, ctx:CompilerParser.CallFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#valsCallFunc.
    def visitValsCallFunc(self, ctx:CompilerParser.ValsCallFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#return.
    def visitReturn(self, ctx:CompilerParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#comandos.
    def visitComandos(self, ctx:CompilerParser.ComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#main.
    def visitMain(self, ctx:CompilerParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#decVar.
    def visitDecVar(self, ctx:CompilerParser.DecVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#varlist.
    def visitVarlist(self, ctx:CompilerParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#consts.
    def visitConsts(self, ctx:CompilerParser.ConstsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#funcprint.
    def visitFuncprint(self, ctx:CompilerParser.FuncprintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#funcinput.
    def visitFuncinput(self, ctx:CompilerParser.FuncinputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#condicional.
    def visitCondicional(self, ctx:CompilerParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#condElse.
    def visitCondElse(self, ctx:CompilerParser.CondElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#cmdWhile.
    def visitCmdWhile(self, ctx:CompilerParser.CmdWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#opMath.
    def visitOpMath(self, ctx:CompilerParser.OpMathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#opMathR.
    def visitOpMathR(self, ctx:CompilerParser.OpMathRContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#sum_minus.
    def visitSum_minus(self, ctx:CompilerParser.Sum_minusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#e_termo.
    def visitE_termo(self, ctx:CompilerParser.E_termoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#e_factor.
    def visitE_factor(self, ctx:CompilerParser.E_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#time_div.
    def visitTime_div(self, ctx:CompilerParser.Time_divContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#var_name.
    def visitVar_name(self, ctx:CompilerParser.Var_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#float_value.
    def visitFloat_value(self, ctx:CompilerParser.Float_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#int_value.
    def visitInt_value(self, ctx:CompilerParser.Int_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#str_val.
    def visitStr_val(self, ctx:CompilerParser.Str_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#func_call.
    def visitFunc_call(self, ctx:CompilerParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#expr.
    def visitExpr(self, ctx:CompilerParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#expressaoBooleana.
    def visitExpressaoBooleana(self, ctx:CompilerParser.ExpressaoBooleanaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#condicao.
    def visitCondicao(self, ctx:CompilerParser.CondicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#expressaoRelacional.
    def visitExpressaoRelacional(self, ctx:CompilerParser.ExpressaoRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompilerParser#valorBool.
    def visitValorBool(self, ctx:CompilerParser.ValorBoolContext):
        return self.visitChildren(ctx)



del CompilerParser