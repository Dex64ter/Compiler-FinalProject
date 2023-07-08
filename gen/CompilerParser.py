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
        4,1,28,199,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,38,8,1,10,1,12,1,41,
        9,1,1,1,5,1,44,8,1,10,1,12,1,47,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        5,2,56,8,2,10,2,12,2,59,9,2,3,2,61,8,2,1,2,1,2,1,3,1,3,1,3,5,3,68,
        8,3,10,3,12,3,71,9,3,1,3,5,3,74,8,3,10,3,12,3,77,9,3,1,3,1,3,1,4,
        1,4,1,4,4,4,84,8,4,11,4,12,4,85,1,5,1,5,3,5,90,8,5,4,5,92,8,5,11,
        5,12,5,93,1,5,1,5,1,5,1,5,1,5,1,5,3,5,102,8,5,1,6,1,6,1,6,1,6,1,
        6,1,6,3,6,110,8,6,4,6,112,8,6,11,6,12,6,113,1,7,4,7,117,8,7,11,7,
        12,7,118,1,7,4,7,122,8,7,11,7,12,7,123,1,7,4,7,127,8,7,11,7,12,7,
        128,1,7,4,7,132,8,7,11,7,12,7,133,3,7,136,8,7,1,8,1,8,1,8,1,8,5,
        8,142,8,8,10,8,12,8,145,9,8,1,8,1,8,1,8,5,8,150,8,8,10,8,12,8,153,
        9,8,3,8,155,8,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,163,8,9,10,9,12,9,166,
        9,9,1,9,1,9,1,10,1,10,1,10,1,10,4,10,174,8,10,11,10,12,10,175,1,
        10,1,10,4,10,180,8,10,11,10,12,10,181,3,10,184,8,10,1,10,1,10,1,
        11,1,11,1,11,1,11,1,11,4,11,193,8,11,11,11,12,11,194,1,11,1,11,1,
        11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,3,2,0,2,2,21,21,2,0,22,
        22,25,27,1,0,24,25,214,0,27,1,0,0,0,2,32,1,0,0,0,4,60,1,0,0,0,6,
        64,1,0,0,0,8,80,1,0,0,0,10,101,1,0,0,0,12,103,1,0,0,0,14,135,1,0,
        0,0,16,137,1,0,0,0,18,158,1,0,0,0,20,169,1,0,0,0,22,187,1,0,0,0,
        24,26,3,2,1,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,
        0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,3,6,3,0,31,1,1,0,0,0,32,
        33,5,23,0,0,33,34,3,4,2,0,34,35,5,1,0,0,35,39,7,0,0,0,36,38,3,8,
        4,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,45,
        1,0,0,0,41,39,1,0,0,0,42,44,3,14,7,0,43,42,1,0,0,0,44,47,1,0,0,0,
        45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,47,45,1,0,0,0,48,49,5,
        3,0,0,49,3,1,0,0,0,50,51,5,21,0,0,51,57,5,24,0,0,52,53,5,4,0,0,53,
        54,5,21,0,0,54,56,5,24,0,0,55,52,1,0,0,0,56,59,1,0,0,0,57,55,1,0,
        0,0,57,58,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,60,50,1,0,0,0,60,61,
        1,0,0,0,61,62,1,0,0,0,62,63,5,5,0,0,63,5,1,0,0,0,64,65,5,6,0,0,65,
        69,5,1,0,0,66,68,3,8,4,0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,
        0,69,70,1,0,0,0,70,75,1,0,0,0,71,69,1,0,0,0,72,74,3,14,7,0,73,72,
        1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,
        77,75,1,0,0,0,78,79,5,3,0,0,79,7,1,0,0,0,80,81,5,7,0,0,81,83,5,1,
        0,0,82,84,3,10,5,0,83,82,1,0,0,0,84,85,1,0,0,0,85,83,1,0,0,0,85,
        86,1,0,0,0,86,9,1,0,0,0,87,89,5,24,0,0,88,90,5,4,0,0,89,88,1,0,0,
        0,89,90,1,0,0,0,90,92,1,0,0,0,91,87,1,0,0,0,92,93,1,0,0,0,93,91,
        1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,96,5,1,0,0,96,97,5,21,0,0,
        97,102,5,8,0,0,98,99,3,12,6,0,99,100,5,8,0,0,100,102,1,0,0,0,101,
        91,1,0,0,0,101,98,1,0,0,0,102,11,1,0,0,0,103,111,5,9,0,0,104,105,
        5,24,0,0,105,106,5,10,0,0,106,107,7,1,0,0,107,109,1,0,0,0,108,110,
        5,4,0,0,109,108,1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,104,
        1,0,0,0,112,113,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,13,1,
        0,0,0,115,117,3,18,9,0,116,115,1,0,0,0,117,118,1,0,0,0,118,116,1,
        0,0,0,118,119,1,0,0,0,119,136,1,0,0,0,120,122,3,16,8,0,121,120,1,
        0,0,0,122,123,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,136,1,
        0,0,0,125,127,3,20,10,0,126,125,1,0,0,0,127,128,1,0,0,0,128,126,
        1,0,0,0,128,129,1,0,0,0,129,136,1,0,0,0,130,132,3,22,11,0,131,130,
        1,0,0,0,132,133,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,136,
        1,0,0,0,135,116,1,0,0,0,135,121,1,0,0,0,135,126,1,0,0,0,135,131,
        1,0,0,0,136,15,1,0,0,0,137,154,5,19,0,0,138,143,5,24,0,0,139,140,
        5,4,0,0,140,142,7,2,0,0,141,139,1,0,0,0,142,145,1,0,0,0,143,141,
        1,0,0,0,143,144,1,0,0,0,144,155,1,0,0,0,145,143,1,0,0,0,146,151,
        5,25,0,0,147,148,5,4,0,0,148,150,7,2,0,0,149,147,1,0,0,0,150,153,
        1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,155,1,0,0,0,153,151,
        1,0,0,0,154,138,1,0,0,0,154,146,1,0,0,0,155,156,1,0,0,0,156,157,
        5,11,0,0,157,17,1,0,0,0,158,159,5,20,0,0,159,164,5,24,0,0,160,161,
        5,4,0,0,161,163,5,24,0,0,162,160,1,0,0,0,163,166,1,0,0,0,164,162,
        1,0,0,0,164,165,1,0,0,0,165,167,1,0,0,0,166,164,1,0,0,0,167,168,
        5,11,0,0,168,19,1,0,0,0,169,170,5,17,0,0,170,171,5,12,0,0,171,173,
        5,13,0,0,172,174,3,14,7,0,173,172,1,0,0,0,174,175,1,0,0,0,175,173,
        1,0,0,0,175,176,1,0,0,0,176,183,1,0,0,0,177,179,5,18,0,0,178,180,
        3,14,7,0,179,178,1,0,0,0,180,181,1,0,0,0,181,179,1,0,0,0,181,182,
        1,0,0,0,182,184,1,0,0,0,183,177,1,0,0,0,183,184,1,0,0,0,184,185,
        1,0,0,0,185,186,5,3,0,0,186,21,1,0,0,0,187,188,5,16,0,0,188,189,
        5,14,0,0,189,190,5,15,0,0,190,192,5,13,0,0,191,193,3,14,7,0,192,
        191,1,0,0,0,193,194,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,
        196,1,0,0,0,196,197,5,3,0,0,197,23,1,0,0,0,26,27,39,45,57,60,69,
        75,85,89,93,101,109,113,118,123,128,133,135,143,151,154,164,175,
        181,183,194
    ]

class CompilerParser ( Parser ):

    grammarFileName = "Compiler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'void'", "'end'", "','", "')'", 
                     "'main'", "'var'", "';'", "'const'", "'='", "');'", 
                     "'<teste logico>'", "'):'", "'('", "'<condi\\u00C3\\u00A7\\u00C3\\u00A3o>'", 
                     "'while'", "'if ('", "'else:'", "'print ('", "'scanf('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "CMDWHILE", "CMDIF", "CMDELSE", "PRINT", "SCAN", "VARTYPE", 
                      "VALBOOL", "NAMEFUNCTION", "VARNAME", "STRING", "VALFLOAT", 
                      "VALINT", "WS" ]

    RULE_prog = 0
    RULE_decFuncao = 1
    RULE_argsFunc = 2
    RULE_main = 3
    RULE_decVar = 4
    RULE_varlist = 5
    RULE_consts = 6
    RULE_comandos = 7
    RULE_funcprint = 8
    RULE_funcinput = 9
    RULE_condicional = 10
    RULE_cmdWhile = 11

    ruleNames =  [ "prog", "decFuncao", "argsFunc", "main", "decVar", "varlist", 
                   "consts", "comandos", "funcprint", "funcinput", "condicional", 
                   "cmdWhile" ]

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
    CMDWHILE=16
    CMDIF=17
    CMDELSE=18
    PRINT=19
    SCAN=20
    VARTYPE=21
    VALBOOL=22
    NAMEFUNCTION=23
    VARNAME=24
    STRING=25
    VALFLOAT=26
    VALINT=27
    WS=28

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
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 24
                self.decFuncao()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
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

        def NAMEFUNCTION(self):
            return self.getToken(CompilerParser.NAMEFUNCTION, 0)

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
            self.state = 32
            self.match(CompilerParser.NAMEFUNCTION)
            self.state = 33
            self.argsFunc()
            self.state = 34
            self.match(CompilerParser.T__0)
            self.state = 35
            _la = self._input.LA(1)
            if not(_la==2 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 36
                self.decVar()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1769472) != 0):
                self.state = 42
                self.comandos()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(CompilerParser.T__2)
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
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 50
                self.match(CompilerParser.VARTYPE)
                self.state = 51
                self.match(CompilerParser.VARNAME)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 52
                    self.match(CompilerParser.T__3)
                    self.state = 53
                    self.match(CompilerParser.VARTYPE)
                    self.state = 54
                    self.match(CompilerParser.VARNAME)
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 62
            self.match(CompilerParser.T__4)
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
        self.enterRule(localctx, 6, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(CompilerParser.T__5)
            self.state = 65
            self.match(CompilerParser.T__0)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 66
                self.decVar()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1769472) != 0):
                self.state = 72
                self.comandos()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(CompilerParser.T__2)
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
        self.enterRule(localctx, 8, self.RULE_decVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(CompilerParser.T__6)
            self.state = 81
            self.match(CompilerParser.T__0)
            self.state = 83 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 82
                self.varlist()
                self.state = 85 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9 or _la==24):
                    break

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
        self.enterRule(localctx, 10, self.RULE_varlist)
        self._la = 0 # Token type
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 87
                    self.match(CompilerParser.VARNAME)
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==4:
                        self.state = 88
                        self.match(CompilerParser.T__3)


                    self.state = 93 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==24):
                        break

                self.state = 95
                self.match(CompilerParser.T__0)
                self.state = 96
                self.match(CompilerParser.VARTYPE)
                self.state = 97
                self.match(CompilerParser.T__7)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.consts()
                self.state = 99
                self.match(CompilerParser.T__7)
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
        self.enterRule(localctx, 12, self.RULE_consts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(CompilerParser.T__8)
            self.state = 111 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                self.match(CompilerParser.VARNAME)
                self.state = 105
                self.match(CompilerParser.T__9)
                self.state = 106
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 239075328) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 108
                    self.match(CompilerParser.T__3)


                self.state = 113 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==24):
                    break

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

        def funcinput(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.FuncinputContext)
            else:
                return self.getTypedRuleContext(CompilerParser.FuncinputContext,i)


        def funcprint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.FuncprintContext)
            else:
                return self.getTypedRuleContext(CompilerParser.FuncprintContext,i)


        def condicional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.CondicionalContext)
            else:
                return self.getTypedRuleContext(CompilerParser.CondicionalContext,i)


        def cmdWhile(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.CmdWhileContext)
            else:
                return self.getTypedRuleContext(CompilerParser.CmdWhileContext,i)


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
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 115
                        self.funcinput()

                    else:
                        raise NoViableAltException(self)
                    self.state = 118 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 120
                        self.funcprint()

                    else:
                        raise NoViableAltException(self)
                    self.state = 123 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 126 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 125
                        self.condicional()

                    else:
                        raise NoViableAltException(self)
                    self.state = 128 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 131 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 130
                        self.cmdWhile()

                    else:
                        raise NoViableAltException(self)
                    self.state = 133 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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


    class FuncprintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(CompilerParser.PRINT, 0)

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
        self.enterRule(localctx, 16, self.RULE_funcprint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(CompilerParser.PRINT)
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 138
                self.match(CompilerParser.VARNAME)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 139
                    self.match(CompilerParser.T__3)
                    self.state = 140
                    _la = self._input.LA(1)
                    if not(_la==24 or _la==25):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 145
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [25]:
                self.state = 146
                self.match(CompilerParser.STRING)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 147
                    self.match(CompilerParser.T__3)
                    self.state = 148
                    _la = self._input.LA(1)
                    if not(_la==24 or _la==25):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 153
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 156
            self.match(CompilerParser.T__10)
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
        self.enterRule(localctx, 18, self.RULE_funcinput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(CompilerParser.SCAN)
            self.state = 159
            self.match(CompilerParser.VARNAME)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 160
                self.match(CompilerParser.T__3)
                self.state = 161
                self.match(CompilerParser.VARNAME)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 167
            self.match(CompilerParser.T__10)
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

        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.ComandosContext)
            else:
                return self.getTypedRuleContext(CompilerParser.ComandosContext,i)


        def CMDELSE(self):
            return self.getToken(CompilerParser.CMDELSE, 0)

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
        self.enterRule(localctx, 20, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(CompilerParser.CMDIF)
            self.state = 170
            self.match(CompilerParser.T__11)
            self.state = 171
            self.match(CompilerParser.T__12)
            self.state = 173 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 172
                self.comandos()
                self.state = 175 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1769472) != 0)):
                    break

            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 177
                self.match(CompilerParser.CMDELSE)
                self.state = 179 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 178
                    self.comandos()
                    self.state = 181 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1769472) != 0)):
                        break



            self.state = 185
            self.match(CompilerParser.T__2)
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
        self.enterRule(localctx, 22, self.RULE_cmdWhile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(CompilerParser.CMDWHILE)
            self.state = 188
            self.match(CompilerParser.T__13)
            self.state = 189
            self.match(CompilerParser.T__14)
            self.state = 190
            self.match(CompilerParser.T__12)
            self.state = 192 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 191
                self.comandos()
                self.state = 194 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1769472) != 0)):
                    break

            self.state = 196
            self.match(CompilerParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





