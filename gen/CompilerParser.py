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
        4,1,39,304,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,66,8,1,10,1,
        12,1,69,9,1,1,1,5,1,72,8,1,10,1,12,1,75,9,1,1,1,5,1,78,8,1,10,1,
        12,1,81,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,5,2,90,8,2,10,2,12,2,93,
        9,2,3,2,95,8,2,1,3,1,3,1,3,1,4,1,4,1,4,3,4,103,8,4,1,4,1,4,1,5,1,
        5,1,5,5,5,110,8,5,10,5,12,5,113,9,5,3,5,115,8,5,1,6,1,6,1,6,3,6,
        120,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,131,8,7,1,8,1,8,
        1,8,5,8,136,8,8,10,8,12,8,139,9,8,1,8,5,8,142,8,8,10,8,12,8,145,
        9,8,1,8,1,8,1,9,1,9,1,9,4,9,152,8,9,11,9,12,9,153,1,10,1,10,3,10,
        158,8,10,4,10,160,8,10,11,10,12,10,161,1,10,1,10,1,10,1,10,1,10,
        1,10,3,10,170,8,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,178,8,11,4,
        11,180,8,11,11,11,12,11,181,1,12,1,12,1,12,1,12,1,12,5,12,189,8,
        12,10,12,12,12,192,9,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        5,13,202,8,13,10,13,12,13,205,9,13,1,13,1,13,1,13,1,14,1,14,1,14,
        1,14,1,14,1,14,4,14,216,8,14,11,14,12,14,217,1,14,1,14,3,14,222,
        8,14,1,15,1,15,4,15,226,8,15,11,15,12,15,227,1,16,1,16,1,16,1,16,
        1,16,1,16,3,16,236,8,16,1,16,4,16,239,8,16,11,16,12,16,240,1,16,
        5,16,244,8,16,10,16,12,16,247,9,16,1,16,1,16,1,17,1,17,1,17,1,17,
        1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,265,8,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,276,8,19,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,287,8,20,1,21,1,21,
        1,21,1,21,1,21,3,21,294,8,21,1,22,1,22,1,23,1,23,1,23,1,23,1,24,
        1,24,1,24,0,0,25,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,0,3,2,0,4,4,30,30,1,0,31,35,1,0,18,23,320,0,
        53,1,0,0,0,2,58,1,0,0,0,4,94,1,0,0,0,6,96,1,0,0,0,8,99,1,0,0,0,10,
        106,1,0,0,0,12,116,1,0,0,0,14,130,1,0,0,0,16,132,1,0,0,0,18,148,
        1,0,0,0,20,169,1,0,0,0,22,171,1,0,0,0,24,183,1,0,0,0,26,196,1,0,
        0,0,28,209,1,0,0,0,30,223,1,0,0,0,32,229,1,0,0,0,34,250,1,0,0,0,
        36,264,1,0,0,0,38,275,1,0,0,0,40,286,1,0,0,0,42,293,1,0,0,0,44,295,
        1,0,0,0,46,297,1,0,0,0,48,301,1,0,0,0,50,52,3,2,1,0,51,50,1,0,0,
        0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,
        1,0,0,0,56,57,3,16,8,0,57,1,1,0,0,0,58,59,5,32,0,0,59,60,5,1,0,0,
        60,61,3,4,2,0,61,62,5,2,0,0,62,63,5,3,0,0,63,67,7,0,0,0,64,66,3,
        18,9,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,
        73,1,0,0,0,69,67,1,0,0,0,70,72,3,14,7,0,71,70,1,0,0,0,72,75,1,0,
        0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,79,1,0,0,0,75,73,1,0,0,0,76,78,
        3,12,6,0,77,76,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,
        80,82,1,0,0,0,81,79,1,0,0,0,82,83,5,5,0,0,83,3,1,0,0,0,84,85,5,30,
        0,0,85,91,5,32,0,0,86,87,5,6,0,0,87,88,5,30,0,0,88,90,5,32,0,0,89,
        86,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,95,1,0,0,
        0,93,91,1,0,0,0,94,84,1,0,0,0,94,95,1,0,0,0,95,5,1,0,0,0,96,97,3,
        8,4,0,97,98,5,7,0,0,98,7,1,0,0,0,99,100,5,32,0,0,100,102,5,1,0,0,
        101,103,3,10,5,0,102,101,1,0,0,0,102,103,1,0,0,0,103,104,1,0,0,0,
        104,105,5,2,0,0,105,9,1,0,0,0,106,114,3,36,18,0,107,108,5,6,0,0,
        108,110,3,36,18,0,109,107,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,
        0,111,112,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,114,111,1,0,0,
        0,114,115,1,0,0,0,115,11,1,0,0,0,116,119,5,29,0,0,117,120,3,42,21,
        0,118,120,3,36,18,0,119,117,1,0,0,0,119,118,1,0,0,0,120,121,1,0,
        0,0,121,122,5,7,0,0,122,13,1,0,0,0,123,131,3,26,13,0,124,131,3,24,
        12,0,125,131,3,34,17,0,126,131,3,28,14,0,127,131,3,32,16,0,128,131,
        3,6,3,0,129,131,3,12,6,0,130,123,1,0,0,0,130,124,1,0,0,0,130,125,
        1,0,0,0,130,126,1,0,0,0,130,127,1,0,0,0,130,128,1,0,0,0,130,129,
        1,0,0,0,131,15,1,0,0,0,132,133,5,8,0,0,133,137,5,3,0,0,134,136,3,
        18,9,0,135,134,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,
        0,0,0,138,143,1,0,0,0,139,137,1,0,0,0,140,142,3,14,7,0,141,140,1,
        0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,146,1,
        0,0,0,145,143,1,0,0,0,146,147,5,5,0,0,147,17,1,0,0,0,148,149,5,9,
        0,0,149,151,5,3,0,0,150,152,3,20,10,0,151,150,1,0,0,0,152,153,1,
        0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,19,1,0,0,0,155,157,5,32,
        0,0,156,158,5,6,0,0,157,156,1,0,0,0,157,158,1,0,0,0,158,160,1,0,
        0,0,159,155,1,0,0,0,160,161,1,0,0,0,161,159,1,0,0,0,161,162,1,0,
        0,0,162,163,1,0,0,0,163,164,5,3,0,0,164,165,5,30,0,0,165,170,5,7,
        0,0,166,167,3,22,11,0,167,168,5,7,0,0,168,170,1,0,0,0,169,159,1,
        0,0,0,169,166,1,0,0,0,170,21,1,0,0,0,171,179,5,10,0,0,172,173,5,
        32,0,0,173,174,5,11,0,0,174,175,7,1,0,0,175,177,1,0,0,0,176,178,
        5,6,0,0,177,176,1,0,0,0,177,178,1,0,0,0,178,180,1,0,0,0,179,172,
        1,0,0,0,180,181,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,23,1,
        0,0,0,183,184,5,27,0,0,184,185,5,1,0,0,185,190,3,36,18,0,186,187,
        5,6,0,0,187,189,3,36,18,0,188,186,1,0,0,0,189,192,1,0,0,0,190,188,
        1,0,0,0,190,191,1,0,0,0,191,193,1,0,0,0,192,190,1,0,0,0,193,194,
        5,2,0,0,194,195,5,7,0,0,195,25,1,0,0,0,196,197,5,28,0,0,197,198,
        5,1,0,0,198,203,5,32,0,0,199,200,5,6,0,0,200,202,5,32,0,0,201,199,
        1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,206,
        1,0,0,0,205,203,1,0,0,0,206,207,5,2,0,0,207,208,5,7,0,0,208,27,1,
        0,0,0,209,210,5,25,0,0,210,211,5,1,0,0,211,212,3,42,21,0,212,213,
        5,2,0,0,213,215,5,3,0,0,214,216,3,14,7,0,215,214,1,0,0,0,216,217,
        1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,0,218,221,1,0,0,0,219,222,
        3,30,15,0,220,222,5,5,0,0,221,219,1,0,0,0,221,220,1,0,0,0,222,29,
        1,0,0,0,223,225,5,26,0,0,224,226,3,14,7,0,225,224,1,0,0,0,226,227,
        1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,31,1,0,0,0,229,230,5,
        24,0,0,230,231,5,1,0,0,231,235,3,42,21,0,232,233,5,2,0,0,233,236,
        5,3,0,0,234,236,5,12,0,0,235,232,1,0,0,0,235,234,1,0,0,0,236,238,
        1,0,0,0,237,239,3,14,7,0,238,237,1,0,0,0,239,240,1,0,0,0,240,238,
        1,0,0,0,240,241,1,0,0,0,241,245,1,0,0,0,242,244,5,13,0,0,243,242,
        1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,246,248,
        1,0,0,0,247,245,1,0,0,0,248,249,5,5,0,0,249,33,1,0,0,0,250,251,5,
        32,0,0,251,252,5,11,0,0,252,253,3,36,18,0,253,254,5,7,0,0,254,35,
        1,0,0,0,255,265,3,38,19,0,256,257,3,38,19,0,257,258,5,14,0,0,258,
        259,3,36,18,0,259,265,1,0,0,0,260,261,3,38,19,0,261,262,5,15,0,0,
        262,263,3,36,18,0,263,265,1,0,0,0,264,255,1,0,0,0,264,256,1,0,0,
        0,264,260,1,0,0,0,265,37,1,0,0,0,266,276,3,40,20,0,267,268,3,40,
        20,0,268,269,5,16,0,0,269,270,3,38,19,0,270,276,1,0,0,0,271,272,
        3,40,20,0,272,273,5,17,0,0,273,274,3,38,19,0,274,276,1,0,0,0,275,
        266,1,0,0,0,275,267,1,0,0,0,275,271,1,0,0,0,276,39,1,0,0,0,277,287,
        5,32,0,0,278,287,5,34,0,0,279,287,5,35,0,0,280,287,5,33,0,0,281,
        287,3,8,4,0,282,283,5,1,0,0,283,284,3,36,18,0,284,285,5,2,0,0,285,
        287,1,0,0,0,286,277,1,0,0,0,286,278,1,0,0,0,286,279,1,0,0,0,286,
        280,1,0,0,0,286,281,1,0,0,0,286,282,1,0,0,0,287,41,1,0,0,0,288,294,
        3,44,22,0,289,290,5,1,0,0,290,291,3,42,21,0,291,292,5,2,0,0,292,
        294,1,0,0,0,293,288,1,0,0,0,293,289,1,0,0,0,294,43,1,0,0,0,295,296,
        3,46,23,0,296,45,1,0,0,0,297,298,3,36,18,0,298,299,3,48,24,0,299,
        300,3,36,18,0,300,47,1,0,0,0,301,302,7,2,0,0,302,49,1,0,0,0,31,53,
        67,73,79,91,94,102,111,114,119,130,137,143,153,157,161,169,177,181,
        190,203,217,221,227,235,240,245,264,275,286,293
    ]

class CompilerParser ( Parser ):

    grammarFileName = "Compiler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':'", "'void'", "'end'", 
                     "','", "';'", "'main'", "'var'", "'const'", "'='", 
                     "'):'", "'break;'", "'+'", "'-'", "'*'", "'/'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'while'", "'if'", 
                     "'else:'", "'print'", "'scanf'", "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CMDWHILE", "CMDIF", "CMDELSE", "PRINT", "SCAN", "RETORNO", 
                      "VARTYPE", "VALBOOL", "VARNAME", "STRING", "VALFLOAT", 
                      "VALINT", "PONTUACAO", "COMMENT", "LINE_COMMENT", 
                      "WS" ]

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

    ruleNames =  [ "prog", "decFuncao", "argsFunc", "call", "callFunction", 
                   "valsCallFunc", "return", "comandos", "main", "decVar", 
                   "varlist", "consts", "funcprint", "funcinput", "condicional", 
                   "condElse", "cmdWhile", "opMath", "expressaoAritmetica", 
                   "termo", "fator", "expressaoBooleana", "condicao", "expressaoRelacional", 
                   "operadorRelacional" ]

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
    CMDWHILE=24
    CMDIF=25
    CMDELSE=26
    PRINT=27
    SCAN=28
    RETORNO=29
    VARTYPE=30
    VALBOOL=31
    VARNAME=32
    STRING=33
    VALFLOAT=34
    VALINT=35
    PONTUACAO=36
    COMMENT=37
    LINE_COMMENT=38
    WS=39

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
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
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
            self.state = 58
            self.match(CompilerParser.VARNAME)
            self.state = 59
            self.match(CompilerParser.T__0)
            self.state = 60
            self.argsFunc()
            self.state = 61
            self.match(CompilerParser.T__1)
            self.state = 62
            self.match(CompilerParser.T__2)
            self.state = 63
            _la = self._input.LA(1)
            if not(_la==4 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 64
                self.decVar()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 70
                    self.comandos() 
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 76
                self.return_()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
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
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 84
                self.match(CompilerParser.VARTYPE)
                self.state = 85
                self.match(CompilerParser.VARNAME)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 86
                    self.match(CompilerParser.T__5)
                    self.state = 87
                    self.match(CompilerParser.VARTYPE)
                    self.state = 88
                    self.match(CompilerParser.VARNAME)
                    self.state = 93
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
            self.state = 96
            self.callFunction()
            self.state = 97
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
            self.state = 99
            self.match(CompilerParser.VARNAME)
            self.state = 100
            self.match(CompilerParser.T__0)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 64424509442) != 0):
                self.state = 101
                self.valsCallFunc()


            self.state = 104
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
            self.state = 106
            self.expressaoAritmetica()
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 107
                    self.match(CompilerParser.T__5)
                    self.state = 108
                    self.expressaoAritmetica()
                    self.state = 113
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
            self.state = 116
            self.match(CompilerParser.RETORNO)
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 117
                self.expressaoBooleana()
                pass

            elif la_ == 2:
                self.state = 118
                self.expressaoAritmetica()
                pass


            self.state = 121
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
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.funcinput()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.funcprint()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.opMath()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.condicional()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 127
                self.cmdWhile()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 128
                self.call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 129
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
            self.state = 132
            self.match(CompilerParser.T__7)
            self.state = 133
            self.match(CompilerParser.T__2)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 134
                self.decVar()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5284823040) != 0):
                self.state = 140
                self.comandos()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
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
            self.state = 148
            self.match(CompilerParser.T__8)
            self.state = 149
            self.match(CompilerParser.T__2)
            self.state = 151 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 150
                    self.varlist()

                else:
                    raise NoViableAltException(self)
                self.state = 153 
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
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 155
                    self.match(CompilerParser.VARNAME)
                    self.state = 157
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6:
                        self.state = 156
                        self.match(CompilerParser.T__5)


                    self.state = 161 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==32):
                        break

                self.state = 163
                self.match(CompilerParser.T__2)
                self.state = 164
                self.match(CompilerParser.VARTYPE)
                self.state = 165
                self.match(CompilerParser.T__6)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.consts()
                self.state = 167
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
            self.state = 171
            self.match(CompilerParser.T__9)
            self.state = 179 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 172
                self.match(CompilerParser.VARNAME)

                self.state = 173
                self.match(CompilerParser.T__10)
                self.state = 174
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66571993088) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 176
                    self.match(CompilerParser.T__5)


                self.state = 181 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==32):
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
            self.state = 183
            self.match(CompilerParser.PRINT)
            self.state = 184
            self.match(CompilerParser.T__0)

            self.state = 185
            self.expressaoAritmetica()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 186
                self.match(CompilerParser.T__5)

                self.state = 187
                self.expressaoAritmetica()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 193
            self.match(CompilerParser.T__1)
            self.state = 194
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
            self.match(CompilerParser.T__1)
            self.state = 207
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




    def condicional(self):

        localctx = CompilerParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(CompilerParser.CMDIF)
            self.state = 210
            self.match(CompilerParser.T__0)
            self.state = 211
            self.expressaoBooleana()
            self.state = 212
            self.match(CompilerParser.T__1)
            self.state = 213
            self.match(CompilerParser.T__2)
            self.state = 215 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 214
                self.comandos()
                self.state = 217 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 5284823040) != 0)):
                    break

            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.state = 219
                self.condElse()
                pass
            elif token in [5]:
                self.state = 220
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
            self.state = 223
            self.match(CompilerParser.CMDELSE)
            self.state = 225 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 224
                    self.comandos()

                else:
                    raise NoViableAltException(self)
                self.state = 227 
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
            self.state = 229
            self.match(CompilerParser.CMDWHILE)
            self.state = 230
            self.match(CompilerParser.T__0)
            self.state = 231
            self.expressaoBooleana()
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 232
                self.match(CompilerParser.T__1)
                self.state = 233
                self.match(CompilerParser.T__2)
                pass
            elif token in [12]:
                self.state = 234
                self.match(CompilerParser.T__11)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 238 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 237
                self.comandos()
                self.state = 240 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 5284823040) != 0)):
                    break

            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 242
                self.match(CompilerParser.T__12)
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 248
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
            self.state = 250
            self.match(CompilerParser.VARNAME)

            self.state = 251
            self.match(CompilerParser.T__10)
            self.state = 252
            self.expressaoAritmetica()
            self.state = 253
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
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.termo()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.termo()
                self.state = 257
                self.match(CompilerParser.T__13)
                self.state = 258
                self.expressaoAritmetica()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
                self.termo()
                self.state = 261
                self.match(CompilerParser.T__14)
                self.state = 262
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
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.fator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.fator()
                self.state = 268
                self.match(CompilerParser.T__15)
                self.state = 269
                self.termo()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 271
                self.fator()
                self.state = 272
                self.match(CompilerParser.T__16)
                self.state = 273
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
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.match(CompilerParser.VARNAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.match(CompilerParser.VALFLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 279
                self.match(CompilerParser.VALINT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 280
                self.match(CompilerParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 281
                self.callFunction()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 282
                self.match(CompilerParser.T__0)
                self.state = 283
                self.expressaoAritmetica()
                self.state = 284
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
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.condicao()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.match(CompilerParser.T__0)
                self.state = 290
                self.expressaoBooleana()
                self.state = 291
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
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.expressaoRelacional()
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
            self.state = 297
            self.expressaoAritmetica()
            self.state = 298
            self.operadorRelacional()
            self.state = 299
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
            self.state = 301
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





