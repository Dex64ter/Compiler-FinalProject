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
        4,1,19,107,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,5,1,31,8,1,10,1,12,1,34,9,1,1,1,5,1,37,8,1,10,1,12,1,40,
        9,1,1,1,1,1,1,2,1,2,1,2,3,2,47,8,2,5,2,49,8,2,10,2,12,2,52,9,2,1,
        3,1,3,1,3,5,3,57,8,3,10,3,12,3,60,9,3,1,3,5,3,63,8,3,10,3,12,3,66,
        9,3,1,3,1,3,1,4,1,4,1,4,4,4,73,8,4,11,4,12,4,74,1,5,1,5,3,5,79,8,
        5,4,5,81,8,5,11,5,12,5,82,1,5,1,5,1,5,1,5,1,5,1,5,3,5,91,8,5,1,6,
        1,6,1,6,1,6,1,6,1,6,3,6,99,8,6,4,6,101,8,6,11,6,12,6,102,1,7,1,7,
        1,7,0,0,8,0,2,4,6,8,10,12,14,0,2,2,0,3,3,12,12,2,0,13,13,16,18,111,
        0,19,1,0,0,0,2,24,1,0,0,0,4,50,1,0,0,0,6,53,1,0,0,0,8,69,1,0,0,0,
        10,90,1,0,0,0,12,92,1,0,0,0,14,104,1,0,0,0,16,18,3,2,1,0,17,16,1,
        0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,
        19,1,0,0,0,22,23,3,6,3,0,23,1,1,0,0,0,24,25,5,14,0,0,25,26,3,4,2,
        0,26,27,5,1,0,0,27,28,5,2,0,0,28,32,7,0,0,0,29,31,3,8,4,0,30,29,
        1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,38,1,0,0,0,
        34,32,1,0,0,0,35,37,3,14,7,0,36,35,1,0,0,0,37,40,1,0,0,0,38,36,1,
        0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,38,1,0,0,0,41,42,5,4,0,0,42,
        3,1,0,0,0,43,44,5,12,0,0,44,46,5,15,0,0,45,47,5,5,0,0,46,45,1,0,
        0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,43,1,0,0,0,49,52,1,0,0,0,50,48,
        1,0,0,0,50,51,1,0,0,0,51,5,1,0,0,0,52,50,1,0,0,0,53,54,5,6,0,0,54,
        58,5,2,0,0,55,57,3,8,4,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,
        0,58,59,1,0,0,0,59,64,1,0,0,0,60,58,1,0,0,0,61,63,3,14,7,0,62,61,
        1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,
        66,64,1,0,0,0,67,68,5,4,0,0,68,7,1,0,0,0,69,70,5,7,0,0,70,72,5,2,
        0,0,71,73,3,10,5,0,72,71,1,0,0,0,73,74,1,0,0,0,74,72,1,0,0,0,74,
        75,1,0,0,0,75,9,1,0,0,0,76,78,5,15,0,0,77,79,5,5,0,0,78,77,1,0,0,
        0,78,79,1,0,0,0,79,81,1,0,0,0,80,76,1,0,0,0,81,82,1,0,0,0,82,80,
        1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,85,5,2,0,0,85,86,5,12,0,0,
        86,91,5,8,0,0,87,88,3,12,6,0,88,89,5,8,0,0,89,91,1,0,0,0,90,80,1,
        0,0,0,90,87,1,0,0,0,91,11,1,0,0,0,92,100,5,9,0,0,93,94,5,15,0,0,
        94,95,5,10,0,0,95,96,7,1,0,0,96,98,1,0,0,0,97,99,5,5,0,0,98,97,1,
        0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,93,1,0,0,0,101,102,1,0,0,
        0,102,100,1,0,0,0,102,103,1,0,0,0,103,13,1,0,0,0,104,105,5,11,0,
        0,105,15,1,0,0,0,13,19,32,38,46,50,58,64,74,78,82,90,98,102
    ]

class CompilerParser ( Parser ):

    grammarFileName = "Compiler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "')'", "':'", "'void'", "'end'", "','", 
                     "'main'", "'var'", "';'", "'const'", "'='", "'COMANDO'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "VARTYPE", "VALBOOL", "NAMEFUNCTION", "VARNAME", "STRING", 
                      "VALFLOAT", "VALINT", "WS" ]

    RULE_prog = 0
    RULE_decFuncao = 1
    RULE_argsFunc = 2
    RULE_main = 3
    RULE_decVar = 4
    RULE_varlist = 5
    RULE_consts = 6
    RULE_comandos = 7

    ruleNames =  [ "prog", "decFuncao", "argsFunc", "main", "decVar", "varlist", 
                   "consts", "comandos" ]

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
    VARTYPE=12
    VALBOOL=13
    NAMEFUNCTION=14
    VARNAME=15
    STRING=16
    VALFLOAT=17
    VALINT=18
    WS=19

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
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 16
                self.decFuncao()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
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
            self.state = 24
            self.match(CompilerParser.NAMEFUNCTION)
            self.state = 25
            self.argsFunc()
            self.state = 26
            self.match(CompilerParser.T__0)
            self.state = 27
            self.match(CompilerParser.T__1)
            self.state = 28
            _la = self._input.LA(1)
            if not(_la==3 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 29
                self.decVar()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 35
                self.comandos()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(CompilerParser.T__3)
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
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 43
                self.match(CompilerParser.VARTYPE)
                self.state = 44
                self.match(CompilerParser.VARNAME)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 45
                    self.match(CompilerParser.T__4)


                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 53
            self.match(CompilerParser.T__5)
            self.state = 54
            self.match(CompilerParser.T__1)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 55
                self.decVar()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 61
                self.comandos()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(CompilerParser.T__3)
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
            self.state = 69
            self.match(CompilerParser.T__6)
            self.state = 70
            self.match(CompilerParser.T__1)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.varlist()
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9 or _la==15):
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
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 76
                    self.match(CompilerParser.VARNAME)
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 77
                        self.match(CompilerParser.T__4)


                    self.state = 82 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==15):
                        break

                self.state = 84
                self.match(CompilerParser.T__1)
                self.state = 85
                self.match(CompilerParser.VARTYPE)
                self.state = 86
                self.match(CompilerParser.T__7)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.consts()
                self.state = 88
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
            self.state = 92
            self.match(CompilerParser.T__8)
            self.state = 100 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                self.match(CompilerParser.VARNAME)
                self.state = 94
                self.match(CompilerParser.T__9)
                self.state = 95
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 466944) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 97
                    self.match(CompilerParser.T__4)


                self.state = 102 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==15):
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
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(CompilerParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





