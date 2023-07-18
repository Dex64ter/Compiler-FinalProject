# Generated from C:/Users/davij/PycharmProjects/Compiler-FinalProject\Compiler.g4 by ANTLR 4.12.0
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
        4,1,41,304,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,5,0,54,
        8,0,10,0,12,0,57,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,68,
        8,1,10,1,12,1,71,9,1,1,1,5,1,74,8,1,10,1,12,1,77,9,1,1,1,5,1,80,
        8,1,10,1,12,1,83,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,5,2,92,8,2,10,2,
        12,2,95,9,2,3,2,97,8,2,1,3,1,3,1,3,1,4,1,4,3,4,104,8,4,1,4,1,4,1,
        5,1,5,1,5,5,5,111,8,5,10,5,12,5,114,9,5,3,5,116,8,5,1,6,1,6,1,6,
        3,6,121,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,132,8,7,1,8,
        1,8,1,8,5,8,137,8,8,10,8,12,8,140,9,8,1,8,5,8,143,8,8,10,8,12,8,
        146,9,8,1,8,1,8,1,9,1,9,1,9,4,9,153,8,9,11,9,12,9,154,1,10,1,10,
        3,10,159,8,10,4,10,161,8,10,11,10,12,10,162,1,10,1,10,1,10,1,10,
        1,10,1,10,3,10,171,8,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,179,8,
        11,4,11,181,8,11,11,11,12,11,182,1,12,1,12,1,12,1,12,1,12,5,12,190,
        8,12,10,12,12,12,193,9,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,5,13,
        202,8,13,10,13,12,13,205,9,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,
        1,14,4,14,215,8,14,11,14,12,14,216,1,14,1,14,3,14,221,8,14,1,15,
        1,15,4,15,225,8,15,11,15,12,15,226,1,16,1,16,1,16,1,16,1,16,1,16,
        4,16,235,8,16,11,16,12,16,236,1,16,5,16,240,8,16,10,16,12,16,243,
        9,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,3,18,261,8,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,3,19,272,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,3,20,283,8,20,1,21,1,21,1,21,1,21,1,21,3,21,290,8,21,1,
        22,1,22,3,22,294,8,22,1,23,1,23,1,23,1,23,1,24,1,24,1,25,1,25,1,
        25,0,0,26,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,0,4,2,0,4,4,32,32,1,0,33,37,1,0,18,23,1,0,24,25,
        319,0,55,1,0,0,0,2,60,1,0,0,0,4,96,1,0,0,0,6,98,1,0,0,0,8,101,1,
        0,0,0,10,107,1,0,0,0,12,117,1,0,0,0,14,131,1,0,0,0,16,133,1,0,0,
        0,18,149,1,0,0,0,20,170,1,0,0,0,22,172,1,0,0,0,24,184,1,0,0,0,26,
        196,1,0,0,0,28,208,1,0,0,0,30,222,1,0,0,0,32,228,1,0,0,0,34,246,
        1,0,0,0,36,260,1,0,0,0,38,271,1,0,0,0,40,282,1,0,0,0,42,289,1,0,
        0,0,44,293,1,0,0,0,46,295,1,0,0,0,48,299,1,0,0,0,50,301,1,0,0,0,
        52,54,3,2,1,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,
        0,0,0,56,58,1,0,0,0,57,55,1,0,0,0,58,59,3,16,8,0,59,1,1,0,0,0,60,
        61,5,34,0,0,61,62,5,1,0,0,62,63,3,4,2,0,63,64,5,2,0,0,64,65,5,3,
        0,0,65,69,7,0,0,0,66,68,3,18,9,0,67,66,1,0,0,0,68,71,1,0,0,0,69,
        67,1,0,0,0,69,70,1,0,0,0,70,75,1,0,0,0,71,69,1,0,0,0,72,74,3,14,
        7,0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,81,
        1,0,0,0,77,75,1,0,0,0,78,80,3,12,6,0,79,78,1,0,0,0,80,83,1,0,0,0,
        81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,
        5,0,0,85,3,1,0,0,0,86,87,5,32,0,0,87,93,5,34,0,0,88,89,5,6,0,0,89,
        90,5,32,0,0,90,92,5,34,0,0,91,88,1,0,0,0,92,95,1,0,0,0,93,91,1,0,
        0,0,93,94,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,96,86,1,0,0,0,96,97,
        1,0,0,0,97,5,1,0,0,0,98,99,3,8,4,0,99,100,5,7,0,0,100,7,1,0,0,0,
        101,103,5,34,0,0,102,104,3,10,5,0,103,102,1,0,0,0,103,104,1,0,0,
        0,104,105,1,0,0,0,105,106,5,2,0,0,106,9,1,0,0,0,107,115,3,36,18,
        0,108,109,5,6,0,0,109,111,3,36,18,0,110,108,1,0,0,0,111,114,1,0,
        0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,116,1,0,0,0,114,112,1,0,
        0,0,115,112,1,0,0,0,115,116,1,0,0,0,116,11,1,0,0,0,117,120,5,31,
        0,0,118,121,3,42,21,0,119,121,3,36,18,0,120,118,1,0,0,0,120,119,
        1,0,0,0,121,122,1,0,0,0,122,123,5,7,0,0,123,13,1,0,0,0,124,132,3,
        26,13,0,125,132,3,24,12,0,126,132,3,34,17,0,127,132,3,28,14,0,128,
        132,3,32,16,0,129,132,3,6,3,0,130,132,3,12,6,0,131,124,1,0,0,0,131,
        125,1,0,0,0,131,126,1,0,0,0,131,127,1,0,0,0,131,128,1,0,0,0,131,
        129,1,0,0,0,131,130,1,0,0,0,132,15,1,0,0,0,133,134,5,8,0,0,134,138,
        5,3,0,0,135,137,3,18,9,0,136,135,1,0,0,0,137,140,1,0,0,0,138,136,
        1,0,0,0,138,139,1,0,0,0,139,144,1,0,0,0,140,138,1,0,0,0,141,143,
        3,14,7,0,142,141,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,145,
        1,0,0,0,145,147,1,0,0,0,146,144,1,0,0,0,147,148,5,5,0,0,148,17,1,
        0,0,0,149,150,5,9,0,0,150,152,5,3,0,0,151,153,3,20,10,0,152,151,
        1,0,0,0,153,154,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,19,1,
        0,0,0,156,158,5,34,0,0,157,159,5,6,0,0,158,157,1,0,0,0,158,159,1,
        0,0,0,159,161,1,0,0,0,160,156,1,0,0,0,161,162,1,0,0,0,162,160,1,
        0,0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,165,5,3,0,0,165,166,5,
        32,0,0,166,171,5,7,0,0,167,168,3,22,11,0,168,169,5,7,0,0,169,171,
        1,0,0,0,170,160,1,0,0,0,170,167,1,0,0,0,171,21,1,0,0,0,172,180,5,
        10,0,0,173,174,5,34,0,0,174,175,5,11,0,0,175,176,7,1,0,0,176,178,
        1,0,0,0,177,179,5,6,0,0,178,177,1,0,0,0,178,179,1,0,0,0,179,181,
        1,0,0,0,180,173,1,0,0,0,181,182,1,0,0,0,182,180,1,0,0,0,182,183,
        1,0,0,0,183,23,1,0,0,0,184,185,5,29,0,0,185,186,5,1,0,0,186,191,
        3,36,18,0,187,188,5,6,0,0,188,190,3,36,18,0,189,187,1,0,0,0,190,
        193,1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,194,1,0,0,0,193,
        191,1,0,0,0,194,195,5,12,0,0,195,25,1,0,0,0,196,197,5,30,0,0,197,
        198,5,1,0,0,198,203,5,34,0,0,199,200,5,6,0,0,200,202,5,34,0,0,201,
        199,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,
        206,1,0,0,0,205,203,1,0,0,0,206,207,5,12,0,0,207,27,1,0,0,0,208,
        209,5,27,0,0,209,210,5,1,0,0,210,211,3,42,21,0,211,212,5,2,0,0,212,
        214,5,3,0,0,213,215,3,14,7,0,214,213,1,0,0,0,215,216,1,0,0,0,216,
        214,1,0,0,0,216,217,1,0,0,0,217,220,1,0,0,0,218,221,3,30,15,0,219,
        221,5,5,0,0,220,218,1,0,0,0,220,219,1,0,0,0,221,29,1,0,0,0,222,224,
        5,28,0,0,223,225,3,14,7,0,224,223,1,0,0,0,225,226,1,0,0,0,226,224,
        1,0,0,0,226,227,1,0,0,0,227,31,1,0,0,0,228,229,5,26,0,0,229,230,
        5,1,0,0,230,231,3,42,21,0,231,232,5,2,0,0,232,234,5,3,0,0,233,235,
        3,14,7,0,234,233,1,0,0,0,235,236,1,0,0,0,236,234,1,0,0,0,236,237,
        1,0,0,0,237,241,1,0,0,0,238,240,5,13,0,0,239,238,1,0,0,0,240,243,
        1,0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,244,1,0,0,0,243,241,
        1,0,0,0,244,245,5,5,0,0,245,33,1,0,0,0,246,247,5,34,0,0,247,248,
        5,11,0,0,248,249,3,36,18,0,249,250,5,7,0,0,250,35,1,0,0,0,251,261,
        3,38,19,0,252,253,3,38,19,0,253,254,5,14,0,0,254,255,3,36,18,0,255,
        261,1,0,0,0,256,257,3,38,19,0,257,258,5,15,0,0,258,259,3,36,18,0,
        259,261,1,0,0,0,260,251,1,0,0,0,260,252,1,0,0,0,260,256,1,0,0,0,
        261,37,1,0,0,0,262,272,3,40,20,0,263,264,3,40,20,0,264,265,5,16,
        0,0,265,266,3,38,19,0,266,272,1,0,0,0,267,268,3,40,20,0,268,269,
        5,17,0,0,269,270,3,38,19,0,270,272,1,0,0,0,271,262,1,0,0,0,271,263,
        1,0,0,0,271,267,1,0,0,0,272,39,1,0,0,0,273,283,5,34,0,0,274,283,
        5,36,0,0,275,283,5,37,0,0,276,283,5,35,0,0,277,283,3,8,4,0,278,279,
        5,1,0,0,279,280,3,36,18,0,280,281,5,2,0,0,281,283,1,0,0,0,282,273,
        1,0,0,0,282,274,1,0,0,0,282,275,1,0,0,0,282,276,1,0,0,0,282,277,
        1,0,0,0,282,278,1,0,0,0,283,41,1,0,0,0,284,290,3,44,22,0,285,286,
        5,1,0,0,286,287,3,42,21,0,287,288,5,2,0,0,288,290,1,0,0,0,289,284,
        1,0,0,0,289,285,1,0,0,0,290,43,1,0,0,0,291,294,3,50,25,0,292,294,
        3,46,23,0,293,291,1,0,0,0,293,292,1,0,0,0,294,45,1,0,0,0,295,296,
        3,36,18,0,296,297,3,48,24,0,297,298,3,36,18,0,298,47,1,0,0,0,299,
        300,7,2,0,0,300,49,1,0,0,0,301,302,7,3,0,0,302,51,1,0,0,0,31,55,
        69,75,81,93,96,103,112,115,120,131,138,144,154,158,162,170,178,182,
        191,203,216,220,226,236,241,260,271,282,289,293
    ]

class CompilerParser ( Parser ):

    grammarFileName = "Compiler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':'", "'void'", "'end'", 
                     "','", "';'", "'main'", "'var'", "'const'", "'='", 
                     "');'", "'break;'", "'+'", "'-'", "'*'", "'/'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'true'", "'false'", 
                     "'while'", "'if'", "'else:'", "'print'", "'scanf'", 
                     "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "CMDWHILE", "CMDIF", "CMDELSE", 
                      "PRINT", "SCAN", "RETORNO", "VARTYPE", "VALBOOL", 
                      "VARNAME", "STRING", "VALFLOAT", "VALINT", "PONTUACAO", 
                      "COMMENT", "LINE_COMMENT", "WS" ]

    RULE_prog = 0
    RULE_decFuncao = 1
    RULE_argsFunc = 2
    RULE_call = 3
    RULE_callFunction = 4
    RULE_valsCallFunc = 5
    RULE_return = 6
    RULE_comandos = 7
    RULE_main = 8
    RULE_decVar = 9
    RULE_varlist = 10
    RULE_consts = 11
    RULE_funcprint = 12
    RULE_funcinput = 13
    RULE_condicional = 14
    RULE_condElse = 15
    RULE_cmdWhile = 16
    RULE_opMath = 17
    RULE_expressaoAritmetica = 18
    RULE_termo = 19
    RULE_fator = 20
    RULE_expressaoBooleana = 21
    RULE_condicao = 22
    RULE_expressaoRelacional = 23
    RULE_operadorRelacional = 24
    RULE_valorBool = 25

    ruleNames =  [ "prog", "decFuncao", "argsFunc", "call", "callFunction", 
                   "valsCallFunc", "return", "comandos", "main", "decVar", 
                   "varlist", "consts", "funcprint", "funcinput", "condicional", 
                   "condElse", "cmdWhile", "opMath", "expressaoAritmetica", 
                   "termo", "fator", "expressaoBooleana", "condicao", "expressaoRelacional", 
                   "operadorRelacional", "valorBool" ]

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
    T__22=23
    T__23=24
    T__24=25
    CMDWHILE=26
    CMDIF=27
    CMDELSE=28
    PRINT=29
    SCAN=30
    RETORNO=31
    VARTYPE=32
    VALBOOL=33
    VARNAME=34
    STRING=35
    VALFLOAT=36
    VALINT=37
    PONTUACAO=38
    COMMENT=39
    LINE_COMMENT=40
    WS=41

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




    def prog(self):

        localctx = CompilerParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 52
                self.decFuncao()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
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

        def VARNAME(self):
            return self.getToken(CompilerParser.VARNAME, 0)

        def argsFunc(self):
            return self.getTypedRuleContext(CompilerParser.ArgsFuncContext,0)


        def VARTYPE(self):
            return self.getToken(CompilerParser.VARTYPE, 0)

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




    def decFuncao(self):

        localctx = CompilerParser.DecFuncaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decFuncao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(CompilerParser.VARNAME)
            self.state = 61
            self.match(CompilerParser.T__0)
            self.state = 62
            self.argsFunc()
            self.state = 63
            self.match(CompilerParser.T__1)
            self.state = 64
            self.match(CompilerParser.T__2)
            self.state = 65
            _la = self._input.LA(1)
            if not(_la==4 or _la==32):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 66
                self.decVar()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 72
                    self.comandos() 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 78
                self.return_()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(CompilerParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARTYPE(self, i:int=None):
            if i is None:
                return self.getTokens(CompilerParser.VARTYPE)
            else:
                return self.getToken(CompilerParser.VARTYPE, i)

        def VARNAME(self, i:int=None):
            if i is None:
                return self.getTokens(CompilerParser.VARNAME)
            else:
                return self.getToken(CompilerParser.VARNAME, i)

        def getRuleIndex(self):
            return CompilerParser.RULE_argsFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgsFunc" ):
                listener.enterArgsFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgsFunc" ):
                listener.exitArgsFunc(self)




    def argsFunc(self):

        localctx = CompilerParser.ArgsFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_argsFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 86
                self.match(CompilerParser.VARTYPE)
                self.state = 87
                self.match(CompilerParser.VARNAME)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 88
                    self.match(CompilerParser.T__5)
                    self.state = 89
                    self.match(CompilerParser.VARTYPE)
                    self.state = 90
                    self.match(CompilerParser.VARNAME)
                    self.state = 95
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



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




    def call(self):

        localctx = CompilerParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.callFunction()
            self.state = 99
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




    def callFunction(self):

        localctx = CompilerParser.CallFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_callFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(CompilerParser.VARNAME)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 257698037762) != 0):
                self.state = 102
                self.valsCallFunc()


            self.state = 105
            self.match(CompilerParser.T__1)
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




    def valsCallFunc(self):

        localctx = CompilerParser.ValsCallFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_valsCallFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.expressaoAritmetica()
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 108
                    self.match(CompilerParser.T__5)
                    self.state = 109
                    self.expressaoAritmetica()
                    self.state = 114
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

        def expressaoBooleana(self):
            return self.getTypedRuleContext(CompilerParser.ExpressaoBooleanaContext,0)


        def expressaoAritmetica(self):
            return self.getTypedRuleContext(CompilerParser.ExpressaoAritmeticaContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)




    def return_(self):

        localctx = CompilerParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(CompilerParser.RETORNO)
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 118
                self.expressaoBooleana()
                pass

            elif la_ == 2:
                self.state = 119
                self.expressaoAritmetica()
                pass


            self.state = 122
            self.match(CompilerParser.T__6)
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




    def comandos(self):

        localctx = CompilerParser.ComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comandos)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.funcinput()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.funcprint()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.opMath()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.condicional()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.cmdWhile()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
                self.call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 130
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




    def main(self):

        localctx = CompilerParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(CompilerParser.T__7)
            self.state = 134
            self.match(CompilerParser.T__2)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 135
                self.decVar()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 21139292160) != 0):
                self.state = 141
                self.comandos()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 147
            self.match(CompilerParser.T__4)
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




    def decVar(self):

        localctx = CompilerParser.DecVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_decVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(CompilerParser.T__8)
            self.state = 150
            self.match(CompilerParser.T__2)
            self.state = 152 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 151
                    self.varlist()

                else:
                    raise NoViableAltException(self)
                self.state = 154 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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




    def varlist(self):

        localctx = CompilerParser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_varlist)
        self._la = 0 # Token type
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 156
                    self.match(CompilerParser.VARNAME)
                    self.state = 158
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6:
                        self.state = 157
                        self.match(CompilerParser.T__5)


                    self.state = 162 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==34):
                        break

                self.state = 164
                self.match(CompilerParser.T__2)
                self.state = 165
                self.match(CompilerParser.VARTYPE)
                self.state = 166
                self.match(CompilerParser.T__6)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.consts()
                self.state = 168
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




    def consts(self):

        localctx = CompilerParser.ConstsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_consts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(CompilerParser.T__9)
            self.state = 180 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 173
                self.match(CompilerParser.VARNAME)

                self.state = 174
                self.match(CompilerParser.T__10)
                self.state = 175
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 266287972352) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 177
                    self.match(CompilerParser.T__5)


                self.state = 182 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==34):
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




    def funcprint(self):

        localctx = CompilerParser.FuncprintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_funcprint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(CompilerParser.PRINT)
            self.state = 185
            self.match(CompilerParser.T__0)

            self.state = 186
            self.expressaoAritmetica()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 187
                self.match(CompilerParser.T__5)

                self.state = 188
                self.expressaoAritmetica()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 194
            self.match(CompilerParser.T__11)
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




    def funcinput(self):

        localctx = CompilerParser.FuncinputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_funcinput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(CompilerParser.SCAN)
            self.state = 197
            self.match(CompilerParser.T__0)
            self.state = 198
            self.match(CompilerParser.VARNAME)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 199
                self.match(CompilerParser.T__5)
                self.state = 200
                self.match(CompilerParser.VARNAME)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206
            self.match(CompilerParser.T__11)
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




    def condicional(self):

        localctx = CompilerParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(CompilerParser.CMDIF)
            self.state = 209
            self.match(CompilerParser.T__0)
            self.state = 210
            self.expressaoBooleana()
            self.state = 211
            self.match(CompilerParser.T__1)
            self.state = 212
            self.match(CompilerParser.T__2)
            self.state = 214 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 213
                self.comandos()
                self.state = 216 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 21139292160) != 0)):
                    break

            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.state = 218
                self.condElse()
                pass
            elif token in [5]:
                self.state = 219
                self.match(CompilerParser.T__4)
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




    def condElse(self):

        localctx = CompilerParser.CondElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_condElse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(CompilerParser.CMDELSE)
            self.state = 224 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 223
                    self.comandos()

                else:
                    raise NoViableAltException(self)
                self.state = 226 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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




    def cmdWhile(self):

        localctx = CompilerParser.CmdWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_cmdWhile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(CompilerParser.CMDWHILE)
            self.state = 229
            self.match(CompilerParser.T__0)
            self.state = 230
            self.expressaoBooleana()
            self.state = 231
            self.match(CompilerParser.T__1)
            self.state = 232
            self.match(CompilerParser.T__2)
            self.state = 234 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 233
                self.comandos()
                self.state = 236 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 21139292160) != 0)):
                    break

            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 238
                self.match(CompilerParser.T__12)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 244
            self.match(CompilerParser.T__4)
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

        def VARNAME(self):
            return self.getToken(CompilerParser.VARNAME, 0)

        def expressaoAritmetica(self):
            return self.getTypedRuleContext(CompilerParser.ExpressaoAritmeticaContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_opMath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpMath" ):
                listener.enterOpMath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpMath" ):
                listener.exitOpMath(self)




    def opMath(self):

        localctx = CompilerParser.OpMathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_opMath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(CompilerParser.VARNAME)

            self.state = 247
            self.match(CompilerParser.T__10)
            self.state = 248
            self.expressaoAritmetica()
            self.state = 249
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

        def termo(self):
            return self.getTypedRuleContext(CompilerParser.TermoContext,0)


        def expressaoAritmetica(self):
            return self.getTypedRuleContext(CompilerParser.ExpressaoAritmeticaContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_expressaoAritmetica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoAritmetica" ):
                listener.enterExpressaoAritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoAritmetica" ):
                listener.exitExpressaoAritmetica(self)




    def expressaoAritmetica(self):

        localctx = CompilerParser.ExpressaoAritmeticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expressaoAritmetica)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.termo()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.termo()
                self.state = 253
                self.match(CompilerParser.T__13)
                self.state = 254
                self.expressaoAritmetica()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 256
                self.termo()
                self.state = 257
                self.match(CompilerParser.T__14)
                self.state = 258
                self.expressaoAritmetica()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self):
            return self.getTypedRuleContext(CompilerParser.FatorContext,0)


        def termo(self):
            return self.getTypedRuleContext(CompilerParser.TermoContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)




    def termo(self):

        localctx = CompilerParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_termo)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.fator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.fator()
                self.state = 264
                self.match(CompilerParser.T__15)
                self.state = 265
                self.termo()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
                self.fator()
                self.state = 268
                self.match(CompilerParser.T__16)
                self.state = 269
                self.termo()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(CompilerParser.VARNAME, 0)

        def VALFLOAT(self):
            return self.getToken(CompilerParser.VALFLOAT, 0)

        def VALINT(self):
            return self.getToken(CompilerParser.VALINT, 0)

        def STRING(self):
            return self.getToken(CompilerParser.STRING, 0)

        def callFunction(self):
            return self.getTypedRuleContext(CompilerParser.CallFunctionContext,0)


        def expressaoAritmetica(self):
            return self.getTypedRuleContext(CompilerParser.ExpressaoAritmeticaContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)




    def fator(self):

        localctx = CompilerParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_fator)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(CompilerParser.VARNAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.match(CompilerParser.VALFLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
                self.match(CompilerParser.VALINT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 276
                self.match(CompilerParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 277
                self.callFunction()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 278
                self.match(CompilerParser.T__0)
                self.state = 279
                self.expressaoAritmetica()
                self.state = 280
                self.match(CompilerParser.T__1)
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




    def expressaoBooleana(self):

        localctx = CompilerParser.ExpressaoBooleanaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expressaoBooleana)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.condicao()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.match(CompilerParser.T__0)
                self.state = 286
                self.expressaoBooleana()
                self.state = 287
                self.match(CompilerParser.T__1)
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




    def condicao(self):

        localctx = CompilerParser.CondicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_condicao)
        try:
            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.valorBool()
                pass
            elif token in [1, 34, 35, 36, 37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
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

        def expressaoAritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.ExpressaoAritmeticaContext)
            else:
                return self.getTypedRuleContext(CompilerParser.ExpressaoAritmeticaContext,i)


        def operadorRelacional(self):
            return self.getTypedRuleContext(CompilerParser.OperadorRelacionalContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_expressaoRelacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoRelacional" ):
                listener.enterExpressaoRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoRelacional" ):
                listener.exitExpressaoRelacional(self)




    def expressaoRelacional(self):

        localctx = CompilerParser.ExpressaoRelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expressaoRelacional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.expressaoAritmetica()
            self.state = 296
            self.operadorRelacional()
            self.state = 297
            self.expressaoAritmetica()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperadorRelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CompilerParser.RULE_operadorRelacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperadorRelacional" ):
                listener.enterOperadorRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperadorRelacional" ):
                listener.exitOperadorRelacional(self)




    def operadorRelacional(self):

        localctx = CompilerParser.OperadorRelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_operadorRelacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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


        def getRuleIndex(self):
            return CompilerParser.RULE_valorBool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValorBool" ):
                listener.enterValorBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValorBool" ):
                listener.exitValorBool(self)




    def valorBool(self):

        localctx = CompilerParser.ValorBoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_valorBool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





