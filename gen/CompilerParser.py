# Generated from C:/Users/ryant/OneDrive/Área de Trabalho/2023.1/COMPILADORES/Compiler-FinalProject\Compiler.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,309,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,66,8,1,10,1,
        12,1,69,9,1,3,1,71,8,1,1,1,1,1,1,1,1,1,5,1,77,8,1,10,1,12,1,80,9,
        1,1,1,5,1,83,8,1,10,1,12,1,86,9,1,1,1,5,1,89,8,1,10,1,12,1,92,9,
        1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,3,3,102,8,3,1,3,1,3,1,4,1,4,1,
        4,5,4,109,8,4,10,4,12,4,112,9,4,3,4,114,8,4,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,3,6,127,8,6,1,7,1,7,1,7,5,7,132,8,7,10,7,
        12,7,135,9,7,1,7,5,7,138,8,7,10,7,12,7,141,9,7,1,7,1,7,1,8,1,8,1,
        8,4,8,148,8,8,11,8,12,8,149,1,9,1,9,3,9,154,8,9,4,9,156,8,9,11,9,
        12,9,157,1,9,1,9,1,9,1,9,1,9,1,9,3,9,166,8,9,1,10,1,10,1,10,1,10,
        1,10,1,10,3,10,174,8,10,4,10,176,8,10,11,10,12,10,177,1,11,1,11,
        1,11,1,11,1,11,5,11,185,8,11,10,11,12,11,188,9,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,5,12,198,8,12,10,12,12,12,201,9,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,4,13,212,8,13,11,13,12,13,
        213,1,13,1,13,3,13,218,8,13,1,14,1,14,1,14,4,14,223,8,14,11,14,12,
        14,224,1,15,1,15,1,15,1,15,1,15,1,15,4,15,233,8,15,11,15,12,15,234,
        1,15,5,15,238,8,15,10,15,12,15,241,9,15,1,15,1,15,1,16,1,16,1,16,
        1,16,3,16,249,8,16,1,16,1,16,1,17,1,17,3,17,255,8,17,1,17,1,17,1,
        18,1,18,1,18,1,18,1,18,1,18,5,18,265,8,18,10,18,12,18,268,9,18,1,
        19,1,19,1,19,1,19,1,19,1,19,5,19,276,8,19,10,19,12,19,279,9,19,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,290,8,20,1,21,1,
        21,1,21,1,21,1,21,3,21,297,8,21,1,22,1,22,3,22,301,8,22,1,23,1,23,
        1,23,1,23,1,24,1,24,1,24,0,2,36,38,25,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,5,2,0,5,5,29,29,1,0,
        30,34,1,0,13,14,1,0,15,16,1,0,17,22,325,0,53,1,0,0,0,2,58,1,0,0,
        0,4,95,1,0,0,0,6,98,1,0,0,0,8,105,1,0,0,0,10,115,1,0,0,0,12,126,
        1,0,0,0,14,128,1,0,0,0,16,144,1,0,0,0,18,165,1,0,0,0,20,167,1,0,
        0,0,22,179,1,0,0,0,24,192,1,0,0,0,26,205,1,0,0,0,28,219,1,0,0,0,
        30,226,1,0,0,0,32,244,1,0,0,0,34,254,1,0,0,0,36,258,1,0,0,0,38,269,
        1,0,0,0,40,289,1,0,0,0,42,296,1,0,0,0,44,300,1,0,0,0,46,302,1,0,
        0,0,48,306,1,0,0,0,50,52,3,2,1,0,51,50,1,0,0,0,52,55,1,0,0,0,53,
        51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,1,0,0,0,56,57,3,14,
        7,0,57,1,1,0,0,0,58,59,5,31,0,0,59,70,5,1,0,0,60,61,5,29,0,0,61,
        67,5,31,0,0,62,63,5,2,0,0,63,64,5,29,0,0,64,66,5,31,0,0,65,62,1,
        0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,71,1,0,0,0,69,
        67,1,0,0,0,70,60,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,73,5,3,0,
        0,73,74,5,4,0,0,74,78,7,0,0,0,75,77,3,16,8,0,76,75,1,0,0,0,77,80,
        1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,84,1,0,0,0,80,78,1,0,0,0,
        81,83,3,12,6,0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,
        0,0,0,85,90,1,0,0,0,86,84,1,0,0,0,87,89,3,10,5,0,88,87,1,0,0,0,89,
        92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,90,1,0,0,
        0,93,94,5,6,0,0,94,3,1,0,0,0,95,96,3,6,3,0,96,97,5,7,0,0,97,5,1,
        0,0,0,98,99,5,31,0,0,99,101,5,1,0,0,100,102,3,8,4,0,101,100,1,0,
        0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,104,5,3,0,0,104,7,1,0,0,
        0,105,113,3,36,18,0,106,107,5,2,0,0,107,109,3,36,18,0,108,106,1,
        0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,114,1,
        0,0,0,112,110,1,0,0,0,113,110,1,0,0,0,113,114,1,0,0,0,114,9,1,0,
        0,0,115,116,5,28,0,0,116,117,3,34,17,0,117,11,1,0,0,0,118,127,3,
        24,12,0,119,127,3,22,11,0,120,127,3,32,16,0,121,127,3,34,17,0,122,
        127,3,26,13,0,123,127,3,30,15,0,124,127,3,4,2,0,125,127,3,10,5,0,
        126,118,1,0,0,0,126,119,1,0,0,0,126,120,1,0,0,0,126,121,1,0,0,0,
        126,122,1,0,0,0,126,123,1,0,0,0,126,124,1,0,0,0,126,125,1,0,0,0,
        127,13,1,0,0,0,128,129,5,8,0,0,129,133,5,4,0,0,130,132,3,16,8,0,
        131,130,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,
        134,139,1,0,0,0,135,133,1,0,0,0,136,138,3,12,6,0,137,136,1,0,0,0,
        138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,
        141,139,1,0,0,0,142,143,5,6,0,0,143,15,1,0,0,0,144,145,5,9,0,0,145,
        147,5,4,0,0,146,148,3,18,9,0,147,146,1,0,0,0,148,149,1,0,0,0,149,
        147,1,0,0,0,149,150,1,0,0,0,150,17,1,0,0,0,151,153,5,31,0,0,152,
        154,5,2,0,0,153,152,1,0,0,0,153,154,1,0,0,0,154,156,1,0,0,0,155,
        151,1,0,0,0,156,157,1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,
        159,1,0,0,0,159,160,5,4,0,0,160,161,5,29,0,0,161,166,5,7,0,0,162,
        163,3,20,10,0,163,164,5,7,0,0,164,166,1,0,0,0,165,155,1,0,0,0,165,
        162,1,0,0,0,166,19,1,0,0,0,167,175,5,10,0,0,168,169,5,31,0,0,169,
        170,5,11,0,0,170,171,7,1,0,0,171,173,1,0,0,0,172,174,5,2,0,0,173,
        172,1,0,0,0,173,174,1,0,0,0,174,176,1,0,0,0,175,168,1,0,0,0,176,
        177,1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,21,1,0,0,0,179,180,
        5,26,0,0,180,181,5,1,0,0,181,186,3,36,18,0,182,183,5,2,0,0,183,185,
        3,36,18,0,184,182,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,
        1,0,0,0,187,189,1,0,0,0,188,186,1,0,0,0,189,190,5,3,0,0,190,191,
        5,7,0,0,191,23,1,0,0,0,192,193,5,27,0,0,193,194,5,1,0,0,194,199,
        5,31,0,0,195,196,5,2,0,0,196,198,5,31,0,0,197,195,1,0,0,0,198,201,
        1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,202,1,0,0,0,201,199,
        1,0,0,0,202,203,5,3,0,0,203,204,5,7,0,0,204,25,1,0,0,0,205,206,5,
        24,0,0,206,207,5,1,0,0,207,208,3,42,21,0,208,209,5,3,0,0,209,211,
        5,4,0,0,210,212,3,12,6,0,211,210,1,0,0,0,212,213,1,0,0,0,213,211,
        1,0,0,0,213,214,1,0,0,0,214,217,1,0,0,0,215,218,3,28,14,0,216,218,
        5,6,0,0,217,215,1,0,0,0,217,216,1,0,0,0,218,27,1,0,0,0,219,220,5,
        25,0,0,220,222,5,4,0,0,221,223,3,12,6,0,222,221,1,0,0,0,223,224,
        1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,29,1,0,0,0,226,227,5,
        23,0,0,227,228,5,1,0,0,228,229,3,42,21,0,229,230,5,3,0,0,230,232,
        5,4,0,0,231,233,3,12,6,0,232,231,1,0,0,0,233,234,1,0,0,0,234,232,
        1,0,0,0,234,235,1,0,0,0,235,239,1,0,0,0,236,238,5,12,0,0,237,236,
        1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,242,
        1,0,0,0,241,239,1,0,0,0,242,243,5,6,0,0,243,31,1,0,0,0,244,245,5,
        31,0,0,245,248,5,11,0,0,246,249,3,36,18,0,247,249,3,42,21,0,248,
        246,1,0,0,0,248,247,1,0,0,0,249,250,1,0,0,0,250,251,5,7,0,0,251,
        33,1,0,0,0,252,255,3,36,18,0,253,255,3,42,21,0,254,252,1,0,0,0,254,
        253,1,0,0,0,255,256,1,0,0,0,256,257,5,7,0,0,257,35,1,0,0,0,258,259,
        6,18,-1,0,259,260,3,38,19,0,260,266,1,0,0,0,261,262,10,1,0,0,262,
        263,7,2,0,0,263,265,3,38,19,0,264,261,1,0,0,0,265,268,1,0,0,0,266,
        264,1,0,0,0,266,267,1,0,0,0,267,37,1,0,0,0,268,266,1,0,0,0,269,270,
        6,19,-1,0,270,271,3,40,20,0,271,277,1,0,0,0,272,273,10,1,0,0,273,
        274,7,3,0,0,274,276,3,40,20,0,275,272,1,0,0,0,276,279,1,0,0,0,277,
        275,1,0,0,0,277,278,1,0,0,0,278,39,1,0,0,0,279,277,1,0,0,0,280,290,
        5,31,0,0,281,290,5,33,0,0,282,290,5,34,0,0,283,290,5,32,0,0,284,
        290,3,6,3,0,285,286,5,1,0,0,286,287,3,36,18,0,287,288,5,3,0,0,288,
        290,1,0,0,0,289,280,1,0,0,0,289,281,1,0,0,0,289,282,1,0,0,0,289,
        283,1,0,0,0,289,284,1,0,0,0,289,285,1,0,0,0,290,41,1,0,0,0,291,297,
        3,44,22,0,292,293,5,1,0,0,293,294,3,42,21,0,294,295,5,3,0,0,295,
        297,1,0,0,0,296,291,1,0,0,0,296,292,1,0,0,0,297,43,1,0,0,0,298,301,
        3,48,24,0,299,301,3,46,23,0,300,298,1,0,0,0,300,299,1,0,0,0,301,
        45,1,0,0,0,302,303,3,36,18,0,303,304,7,4,0,0,304,305,3,36,18,0,305,
        47,1,0,0,0,306,307,5,30,0,0,307,49,1,0,0,0,32,53,67,70,78,84,90,
        101,110,113,126,133,139,149,153,157,165,173,177,186,199,213,217,
        224,234,239,248,254,266,277,289,296,300
    ]

class CompilerParser ( Parser ):

    grammarFileName = "Compiler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "':'", "'void'", 
                     "'end'", "';'", "'main'", "'var'", "'const'", "'='", 
                     "'break;'", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'while'", "'if'", "'else'", 
                     "'print'", "'scanf'", "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "CMDWHILE", 
                      "CMDIF", "CMDELSE", "PRINT", "SCAN", "RETORNO", "VARTYPE", 
                      "VALBOOL", "VARNAME", "STRING", "VALFLOAT", "VALINT", 
                      "PONTUACAO", "COMMENT", "LINE_COMMENT", "WS" ]

    RULE_prog = 0
    RULE_decFuncao = 1
    RULE_call = 2
    RULE_callFunction = 3
    RULE_valsCallFunc = 4
    RULE_return = 5
    RULE_comandos = 6
    RULE_main = 7
    RULE_decVar = 8
    RULE_varlist = 9
    RULE_consts = 10
    RULE_funcprint = 11
    RULE_funcinput = 12
    RULE_condicional = 13
    RULE_condElse = 14
    RULE_cmdWhile = 15
    RULE_opMath = 16
    RULE_opMathR = 17
    RULE_expressaoAritmetica = 18
    RULE_termo = 19
    RULE_fator = 20
    RULE_expressaoBooleana = 21
    RULE_condicao = 22
    RULE_expressaoRelacional = 23
    RULE_valorBool = 24

    ruleNames =  [ "prog", "decFuncao", "call", "callFunction", "valsCallFunc", 
                   "return", "comandos", "main", "decVar", "varlist", "consts", 
                   "funcprint", "funcinput", "condicional", "condElse", 
                   "cmdWhile", "opMath", "opMathR", "expressaoAritmetica", 
                   "termo", "fator", "expressaoBooleana", "condicao", "expressaoRelacional", 
                   "valorBool" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    CMDWHILE=23
    CMDIF=24
    CMDELSE=25
    PRINT=26
    SCAN=27
    RETORNO=28
    VARTYPE=29
    VALBOOL=30
    VARNAME=31
    STRING=32
    VALFLOAT=33
    VALINT=34
    PONTUACAO=35
    COMMENT=36
    LINE_COMMENT=37
    WS=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(CompilerParser.MainContext,0)


        def decFuncao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.DecFuncaoContext)
            else:
                return self.getTypedRuleContext(CompilerParser.DecFuncaoContext,i)


        def getRuleIndex(self):
            return CompilerParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CompilerParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 50
                self.decFuncao()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecFuncaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self, i:int=None):
            if i is None:
                return self.getTokens(CompilerParser.VARNAME)
            else:
                return self.getToken(CompilerParser.VARNAME, i)

        def VARTYPE(self, i:int=None):
            if i is None:
                return self.getTokens(CompilerParser.VARTYPE)
            else:
                return self.getToken(CompilerParser.VARTYPE, i)

        def decVar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.DecVarContext)
            else:
                return self.getTypedRuleContext(CompilerParser.DecVarContext,i)


        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.ComandosContext)
            else:
                return self.getTypedRuleContext(CompilerParser.ComandosContext,i)


        def return_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.ReturnContext)
            else:
                return self.getTypedRuleContext(CompilerParser.ReturnContext,i)


        def getRuleIndex(self):
            return CompilerParser.RULE_decFuncao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecFuncao" ):
                listener.enterDecFuncao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecFuncao" ):
                listener.exitDecFuncao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecFuncao" ):
                return visitor.visitDecFuncao(self)
            else:
                return visitor.visitChildren(self)




    def decFuncao(self):

        localctx = CompilerParser.DecFuncaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decFuncao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(CompilerParser.VARNAME)
            self.state = 59
            self.match(CompilerParser.T__0)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 60
                self.match(CompilerParser.VARTYPE)
                self.state = 61
                self.match(CompilerParser.VARNAME)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 62
                    self.match(CompilerParser.T__1)
                    self.state = 63
                    self.match(CompilerParser.VARTYPE)
                    self.state = 64
                    self.match(CompilerParser.VARNAME)
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 72
            self.match(CompilerParser.T__2)
            self.state = 73
            self.match(CompilerParser.T__3)
            self.state = 74
            _la = self._input.LA(1)
            if not(_la==5 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 75
                self.decVar()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 81
                    self.comandos() 
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 87
                self.return_()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
            self.match(CompilerParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def callFunction(self):
            return self.getTypedRuleContext(CompilerParser.CallFunctionContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = CompilerParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.callFunction()
            self.state = 96
            self.match(CompilerParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None

        def VARNAME(self):
            return self.getToken(CompilerParser.VARNAME, 0)

        def valsCallFunc(self):
            return self.getTypedRuleContext(CompilerParser.ValsCallFuncContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_callFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallFunction" ):
                listener.enterCallFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallFunction" ):
                listener.exitCallFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallFunction" ):
                return visitor.visitCallFunction(self)
            else:
                return visitor.visitChildren(self)




    def callFunction(self):

        localctx = CompilerParser.CallFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_callFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(CompilerParser.VARNAME)
            self.state = 99
            self.match(CompilerParser.T__0)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254722) != 0):
                self.state = 100
                self.valsCallFunc()


            self.state = 103
            self.match(CompilerParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValsCallFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoAritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.ExpressaoAritmeticaContext)
            else:
                return self.getTypedRuleContext(CompilerParser.ExpressaoAritmeticaContext,i)


        def getRuleIndex(self):
            return CompilerParser.RULE_valsCallFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValsCallFunc" ):
                listener.enterValsCallFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValsCallFunc" ):
                listener.exitValsCallFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValsCallFunc" ):
                return visitor.visitValsCallFunc(self)
            else:
                return visitor.visitChildren(self)




    def valsCallFunc(self):

        localctx = CompilerParser.ValsCallFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_valsCallFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.expressaoAritmetica(0)
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 106
                    self.match(CompilerParser.T__1)
                    self.state = 107
                    self.expressaoAritmetica(0)
                    self.state = 112
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNO(self):
            return self.getToken(CompilerParser.RETORNO, 0)

        def opMathR(self):
            return self.getTypedRuleContext(CompilerParser.OpMathRContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)




    def return_(self):

        localctx = CompilerParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(CompilerParser.RETORNO)
            self.state = 116
            self.opMathR()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcinput(self):
            return self.getTypedRuleContext(CompilerParser.FuncinputContext,0)


        def funcprint(self):
            return self.getTypedRuleContext(CompilerParser.FuncprintContext,0)


        def opMath(self):
            return self.getTypedRuleContext(CompilerParser.OpMathContext,0)


        def opMathR(self):
            return self.getTypedRuleContext(CompilerParser.OpMathRContext,0)


        def condicional(self):
            return self.getTypedRuleContext(CompilerParser.CondicionalContext,0)


        def cmdWhile(self):
            return self.getTypedRuleContext(CompilerParser.CmdWhileContext,0)


        def call(self):
            return self.getTypedRuleContext(CompilerParser.CallContext,0)


        def return_(self):
            return self.getTypedRuleContext(CompilerParser.ReturnContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_comandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandos" ):
                listener.enterComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandos" ):
                listener.exitComandos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandos" ):
                return visitor.visitComandos(self)
            else:
                return visitor.visitChildren(self)




    def comandos(self):

        localctx = CompilerParser.ComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comandos)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.funcinput()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.funcprint()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.opMath()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self.opMathR()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 122
                self.condicional()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 123
                self.cmdWhile()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 124
                self.call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 125
                self.return_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decVar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.DecVarContext)
            else:
                return self.getTypedRuleContext(CompilerParser.DecVarContext,i)


        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.ComandosContext)
            else:
                return self.getTypedRuleContext(CompilerParser.ComandosContext,i)


        def getRuleIndex(self):
            return CompilerParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = CompilerParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(CompilerParser.T__7)
            self.state = 129
            self.match(CompilerParser.T__3)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 130
                self.decVar()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33780924418) != 0):
                self.state = 136
                self.comandos()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(CompilerParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.VarlistContext)
            else:
                return self.getTypedRuleContext(CompilerParser.VarlistContext,i)


        def getRuleIndex(self):
            return CompilerParser.RULE_decVar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecVar" ):
                listener.enterDecVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecVar" ):
                listener.exitDecVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecVar" ):
                return visitor.visitDecVar(self)
            else:
                return visitor.visitChildren(self)




    def decVar(self):

        localctx = CompilerParser.DecVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_decVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(CompilerParser.T__8)
            self.state = 145
            self.match(CompilerParser.T__3)
            self.state = 147 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 146
                    self.varlist()

                else:
                    raise NoViableAltException(self)
                self.state = 149 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARTYPE(self):
            return self.getToken(CompilerParser.VARTYPE, 0)

        def VARNAME(self, i:int=None):
            if i is None:
                return self.getTokens(CompilerParser.VARNAME)
            else:
                return self.getToken(CompilerParser.VARNAME, i)

        def consts(self):
            return self.getTypedRuleContext(CompilerParser.ConstsContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_varlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarlist" ):
                listener.enterVarlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarlist" ):
                listener.exitVarlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarlist" ):
                return visitor.visitVarlist(self)
            else:
                return visitor.visitChildren(self)




    def varlist(self):

        localctx = CompilerParser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_varlist)
        self._la = 0 # Token type
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 151
                    self.match(CompilerParser.VARNAME)
                    self.state = 153
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==2:
                        self.state = 152
                        self.match(CompilerParser.T__1)


                    self.state = 157 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==31):
                        break

                self.state = 159
                self.match(CompilerParser.T__3)
                self.state = 160
                self.match(CompilerParser.VARTYPE)
                self.state = 161
                self.match(CompilerParser.T__6)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.consts()
                self.state = 163
                self.match(CompilerParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self, i:int=None):
            if i is None:
                return self.getTokens(CompilerParser.VARNAME)
            else:
                return self.getToken(CompilerParser.VARNAME, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(CompilerParser.STRING)
            else:
                return self.getToken(CompilerParser.STRING, i)

        def VALINT(self, i:int=None):
            if i is None:
                return self.getTokens(CompilerParser.VALINT)
            else:
                return self.getToken(CompilerParser.VALINT, i)

        def VALFLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(CompilerParser.VALFLOAT)
            else:
                return self.getToken(CompilerParser.VALFLOAT, i)

        def VALBOOL(self, i:int=None):
            if i is None:
                return self.getTokens(CompilerParser.VALBOOL)
            else:
                return self.getToken(CompilerParser.VALBOOL, i)

        def getRuleIndex(self):
            return CompilerParser.RULE_consts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConsts" ):
                listener.enterConsts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConsts" ):
                listener.exitConsts(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConsts" ):
                return visitor.visitConsts(self)
            else:
                return visitor.visitChildren(self)




    def consts(self):

        localctx = CompilerParser.ConstsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_consts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(CompilerParser.T__9)
            self.state = 175 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 168
                self.match(CompilerParser.VARNAME)

                self.state = 169
                self.match(CompilerParser.T__10)
                self.state = 170
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33285996544) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 172
                    self.match(CompilerParser.T__1)


                self.state = 177 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncprintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(CompilerParser.PRINT, 0)

        def expressaoAritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.ExpressaoAritmeticaContext)
            else:
                return self.getTypedRuleContext(CompilerParser.ExpressaoAritmeticaContext,i)


        def getRuleIndex(self):
            return CompilerParser.RULE_funcprint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncprint" ):
                listener.enterFuncprint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncprint" ):
                listener.exitFuncprint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncprint" ):
                return visitor.visitFuncprint(self)
            else:
                return visitor.visitChildren(self)




    def funcprint(self):

        localctx = CompilerParser.FuncprintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcprint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(CompilerParser.PRINT)
            self.state = 180
            self.match(CompilerParser.T__0)

            self.state = 181
            self.expressaoAritmetica(0)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 182
                self.match(CompilerParser.T__1)

                self.state = 183
                self.expressaoAritmetica(0)
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 189
            self.match(CompilerParser.T__2)
            self.state = 190
            self.match(CompilerParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncinputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCAN(self):
            return self.getToken(CompilerParser.SCAN, 0)

        def VARNAME(self, i:int=None):
            if i is None:
                return self.getTokens(CompilerParser.VARNAME)
            else:
                return self.getToken(CompilerParser.VARNAME, i)

        def getRuleIndex(self):
            return CompilerParser.RULE_funcinput

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncinput" ):
                listener.enterFuncinput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncinput" ):
                listener.exitFuncinput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncinput" ):
                return visitor.visitFuncinput(self)
            else:
                return visitor.visitChildren(self)




    def funcinput(self):

        localctx = CompilerParser.FuncinputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_funcinput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(CompilerParser.SCAN)
            self.state = 193
            self.match(CompilerParser.T__0)
            self.state = 194
            self.match(CompilerParser.VARNAME)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 195
                self.match(CompilerParser.T__1)
                self.state = 196
                self.match(CompilerParser.VARNAME)
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self.match(CompilerParser.T__2)
            self.state = 203
            self.match(CompilerParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CMDIF(self):
            return self.getToken(CompilerParser.CMDIF, 0)

        def expressaoBooleana(self):
            return self.getTypedRuleContext(CompilerParser.ExpressaoBooleanaContext,0)


        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.ComandosContext)
            else:
                return self.getTypedRuleContext(CompilerParser.ComandosContext,i)


        def condElse(self):
            return self.getTypedRuleContext(CompilerParser.CondElseContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = CompilerParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(CompilerParser.CMDIF)
            self.state = 206
            self.match(CompilerParser.T__0)
            self.state = 207
            self.expressaoBooleana()
            self.state = 208
            self.match(CompilerParser.T__2)
            self.state = 209
            self.match(CompilerParser.T__3)
            self.state = 211 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 210
                self.comandos()
                self.state = 213 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33780924418) != 0)):
                    break

            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.state = 215
                self.condElse()
                pass
            elif token in [6]:
                self.state = 216
                self.match(CompilerParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CMDELSE(self):
            return self.getToken(CompilerParser.CMDELSE, 0)

        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.ComandosContext)
            else:
                return self.getTypedRuleContext(CompilerParser.ComandosContext,i)


        def getRuleIndex(self):
            return CompilerParser.RULE_condElse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondElse" ):
                listener.enterCondElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondElse" ):
                listener.exitCondElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondElse" ):
                return visitor.visitCondElse(self)
            else:
                return visitor.visitChildren(self)




    def condElse(self):

        localctx = CompilerParser.CondElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_condElse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(CompilerParser.CMDELSE)
            self.state = 220
            self.match(CompilerParser.T__3)
            self.state = 222 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 221
                    self.comandos()

                else:
                    raise NoViableAltException(self)
                self.state = 224 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CMDWHILE(self):
            return self.getToken(CompilerParser.CMDWHILE, 0)

        def expressaoBooleana(self):
            return self.getTypedRuleContext(CompilerParser.ExpressaoBooleanaContext,0)


        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.ComandosContext)
            else:
                return self.getTypedRuleContext(CompilerParser.ComandosContext,i)


        def getRuleIndex(self):
            return CompilerParser.RULE_cmdWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdWhile" ):
                listener.enterCmdWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdWhile" ):
                listener.exitCmdWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdWhile" ):
                return visitor.visitCmdWhile(self)
            else:
                return visitor.visitChildren(self)




    def cmdWhile(self):

        localctx = CompilerParser.CmdWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_cmdWhile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(CompilerParser.CMDWHILE)
            self.state = 227
            self.match(CompilerParser.T__0)
            self.state = 228
            self.expressaoBooleana()
            self.state = 229
            self.match(CompilerParser.T__2)
            self.state = 230
            self.match(CompilerParser.T__3)
            self.state = 232 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 231
                self.comandos()
                self.state = 234 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33780924418) != 0)):
                    break

            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 236
                self.match(CompilerParser.T__11)
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
            self.match(CompilerParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpMathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None
            self.isBool = None
            self.val = None

        def VARNAME(self):
            return self.getToken(CompilerParser.VARNAME, 0)

        def expressaoAritmetica(self):
            return self.getTypedRuleContext(CompilerParser.ExpressaoAritmeticaContext,0)


        def expressaoBooleana(self):
            return self.getTypedRuleContext(CompilerParser.ExpressaoBooleanaContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_opMath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpMath" ):
                listener.enterOpMath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpMath" ):
                listener.exitOpMath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpMath" ):
                return visitor.visitOpMath(self)
            else:
                return visitor.visitChildren(self)




    def opMath(self):

        localctx = CompilerParser.OpMathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_opMath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(CompilerParser.VARNAME)

            self.state = 245
            self.match(CompilerParser.T__10)
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 246
                self.expressaoAritmetica(0)
                pass

            elif la_ == 2:
                self.state = 247
                self.expressaoBooleana()
                pass


            self.state = 250
            self.match(CompilerParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpMathRContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None
            self.isBool = None
            self.val = None

        def expressaoAritmetica(self):
            return self.getTypedRuleContext(CompilerParser.ExpressaoAritmeticaContext,0)


        def expressaoBooleana(self):
            return self.getTypedRuleContext(CompilerParser.ExpressaoBooleanaContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_opMathR

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpMathR" ):
                listener.enterOpMathR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpMathR" ):
                listener.exitOpMathR(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpMathR" ):
                return visitor.visitOpMathR(self)
            else:
                return visitor.visitChildren(self)




    def opMathR(self):

        localctx = CompilerParser.OpMathRContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_opMathR)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 252
                self.expressaoAritmetica(0)
                pass

            elif la_ == 2:
                self.state = 253
                self.expressaoBooleana()
                pass


            self.state = 256
            self.match(CompilerParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoAritmeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None
            self.isBool = None
            self.val = None


        def getRuleIndex(self):
            return CompilerParser.RULE_expressaoAritmetica

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_
            self.isBool = ctx.isBool
            self.val = ctx.val


    class Sum_minusContext(ExpressaoAritmeticaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompilerParser.ExpressaoAritmeticaContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expressaoAritmetica(self):
            return self.getTypedRuleContext(CompilerParser.ExpressaoAritmeticaContext,0)

        def termo(self):
            return self.getTypedRuleContext(CompilerParser.TermoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum_minus" ):
                listener.enterSum_minus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum_minus" ):
                listener.exitSum_minus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum_minus" ):
                return visitor.visitSum_minus(self)
            else:
                return visitor.visitChildren(self)


    class E_termoContext(ExpressaoAritmeticaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompilerParser.ExpressaoAritmeticaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def termo(self):
            return self.getTypedRuleContext(CompilerParser.TermoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE_termo" ):
                listener.enterE_termo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE_termo" ):
                listener.exitE_termo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_termo" ):
                return visitor.visitE_termo(self)
            else:
                return visitor.visitChildren(self)



    def expressaoAritmetica(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CompilerParser.ExpressaoAritmeticaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expressaoAritmetica, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CompilerParser.E_termoContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 259
            self.termo(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CompilerParser.Sum_minusContext(self, CompilerParser.ExpressaoAritmeticaContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expressaoAritmetica)
                    self.state = 261
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 262
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==13 or _la==14):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 263
                    self.termo(0) 
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None
            self.val = None


        def getRuleIndex(self):
            return CompilerParser.RULE_termo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_
            self.val = ctx.val


    class E_factorContext(TermoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompilerParser.TermoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fator(self):
            return self.getTypedRuleContext(CompilerParser.FatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE_factor" ):
                listener.enterE_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE_factor" ):
                listener.exitE_factor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_factor" ):
                return visitor.visitE_factor(self)
            else:
                return visitor.visitChildren(self)


    class Time_divContext(TermoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompilerParser.TermoContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def termo(self):
            return self.getTypedRuleContext(CompilerParser.TermoContext,0)

        def fator(self):
            return self.getTypedRuleContext(CompilerParser.FatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_div" ):
                listener.enterTime_div(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_div" ):
                listener.exitTime_div(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTime_div" ):
                return visitor.visitTime_div(self)
            else:
                return visitor.visitChildren(self)



    def termo(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CompilerParser.TermoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_termo, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CompilerParser.E_factorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 270
            self.fator()
            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CompilerParser.Time_divContext(self, CompilerParser.TermoContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_termo)
                    self.state = 272
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 273
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==15 or _la==16):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 274
                    self.fator() 
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None
            self.val = None


        def getRuleIndex(self):
            return CompilerParser.RULE_fator

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_
            self.val = ctx.val



    class Str_valContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompilerParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CompilerParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr_val" ):
                listener.enterStr_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr_val" ):
                listener.exitStr_val(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr_val" ):
                return visitor.visitStr_val(self)
            else:
                return visitor.visitChildren(self)


    class Float_valueContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompilerParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VALFLOAT(self):
            return self.getToken(CompilerParser.VALFLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_value" ):
                listener.enterFloat_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_value" ):
                listener.exitFloat_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_value" ):
                return visitor.visitFloat_value(self)
            else:
                return visitor.visitChildren(self)


    class ExprContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompilerParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressaoAritmetica(self):
            return self.getTypedRuleContext(CompilerParser.ExpressaoAritmeticaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)


    class Func_callContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompilerParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def callFunction(self):
            return self.getTypedRuleContext(CompilerParser.CallFunctionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)


    class Var_nameContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompilerParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARNAME(self):
            return self.getToken(CompilerParser.VARNAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_name" ):
                listener.enterVar_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_name" ):
                listener.exitVar_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_name" ):
                return visitor.visitVar_name(self)
            else:
                return visitor.visitChildren(self)


    class Int_valueContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CompilerParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VALINT(self):
            return self.getToken(CompilerParser.VALINT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_value" ):
                listener.enterInt_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_value" ):
                listener.exitInt_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_value" ):
                return visitor.visitInt_value(self)
            else:
                return visitor.visitChildren(self)



    def fator(self):

        localctx = CompilerParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_fator)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                localctx = CompilerParser.Var_nameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.match(CompilerParser.VARNAME)
                pass

            elif la_ == 2:
                localctx = CompilerParser.Float_valueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(CompilerParser.VALFLOAT)
                pass

            elif la_ == 3:
                localctx = CompilerParser.Int_valueContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 282
                self.match(CompilerParser.VALINT)
                pass

            elif la_ == 4:
                localctx = CompilerParser.Str_valContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 283
                self.match(CompilerParser.STRING)
                pass

            elif la_ == 5:
                localctx = CompilerParser.Func_callContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 284
                self.callFunction()
                pass

            elif la_ == 6:
                localctx = CompilerParser.ExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 285
                self.match(CompilerParser.T__0)
                self.state = 286
                self.expressaoAritmetica(0)
                self.state = 287
                self.match(CompilerParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoBooleanaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None
            self.inh_type = None
            self.isBool = None
            self.val = None

        def condicao(self):
            return self.getTypedRuleContext(CompilerParser.CondicaoContext,0)


        def expressaoBooleana(self):
            return self.getTypedRuleContext(CompilerParser.ExpressaoBooleanaContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_expressaoBooleana

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoBooleana" ):
                listener.enterExpressaoBooleana(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoBooleana" ):
                listener.exitExpressaoBooleana(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoBooleana" ):
                return visitor.visitExpressaoBooleana(self)
            else:
                return visitor.visitChildren(self)




    def expressaoBooleana(self):

        localctx = CompilerParser.ExpressaoBooleanaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expressaoBooleana)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.condicao()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.match(CompilerParser.T__0)
                self.state = 293
                self.expressaoBooleana()
                self.state = 294
                self.match(CompilerParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None
            self.isBool = None
            self.val = None

        def valorBool(self):
            return self.getTypedRuleContext(CompilerParser.ValorBoolContext,0)


        def expressaoRelacional(self):
            return self.getTypedRuleContext(CompilerParser.ExpressaoRelacionalContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_condicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicao" ):
                listener.enterCondicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicao" ):
                listener.exitCondicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicao" ):
                return visitor.visitCondicao(self)
            else:
                return visitor.visitChildren(self)




    def condicao(self):

        localctx = CompilerParser.CondicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_condicao)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.valorBool()
                pass
            elif token in [1, 31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.expressaoRelacional()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoRelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None
            self.isBool = None
            self.val = None
            self.op = None # Token

        def expressaoAritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.ExpressaoAritmeticaContext)
            else:
                return self.getTypedRuleContext(CompilerParser.ExpressaoAritmeticaContext,i)


        def getRuleIndex(self):
            return CompilerParser.RULE_expressaoRelacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoRelacional" ):
                listener.enterExpressaoRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoRelacional" ):
                listener.exitExpressaoRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoRelacional" ):
                return visitor.visitExpressaoRelacional(self)
            else:
                return visitor.visitChildren(self)




    def expressaoRelacional(self):

        localctx = CompilerParser.ExpressaoRelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expressaoRelacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.expressaoAritmetica(0)
            self.state = 303
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 304
            self.expressaoAritmetica(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorBoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None
            self.isBool = None
            self.val = None

        def VALBOOL(self):
            return self.getToken(CompilerParser.VALBOOL, 0)

        def getRuleIndex(self):
            return CompilerParser.RULE_valorBool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValorBool" ):
                listener.enterValorBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValorBool" ):
                listener.exitValorBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValorBool" ):
                return visitor.visitValorBool(self)
            else:
                return visitor.visitChildren(self)




    def valorBool(self):

        localctx = CompilerParser.ValorBoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_valorBool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(CompilerParser.VALBOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expressaoAritmetica_sempred
        self._predicates[19] = self.termo_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressaoAritmetica_sempred(self, localctx:ExpressaoAritmeticaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def termo_sempred(self, localctx:TermoContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




