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
        4,1,19,98,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,
        1,28,8,1,5,1,30,8,1,10,1,12,1,33,9,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,
        1,2,5,2,43,8,2,10,2,12,2,46,9,2,1,2,5,2,49,8,2,10,2,12,2,52,9,2,
        1,2,1,2,1,3,1,3,1,3,4,3,59,8,3,11,3,12,3,60,1,4,1,4,3,4,65,8,4,4,
        4,67,8,4,11,4,12,4,68,1,4,1,4,1,4,1,4,1,4,1,4,3,4,77,8,4,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,89,8,6,1,6,3,6,92,8,6,4,6,94,
        8,6,11,6,12,6,95,1,6,0,0,7,0,2,4,6,8,10,12,0,1,2,0,5,5,14,14,103,
        0,17,1,0,0,0,2,22,1,0,0,0,4,39,1,0,0,0,6,55,1,0,0,0,8,76,1,0,0,0,
        10,78,1,0,0,0,12,80,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,19,1,
        0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,20,1,0,0,0,19,17,1,0,0,0,20,
        21,3,4,2,0,21,1,1,0,0,0,22,23,5,16,0,0,23,31,5,1,0,0,24,25,5,14,
        0,0,25,27,5,15,0,0,26,28,5,2,0,0,27,26,1,0,0,0,27,28,1,0,0,0,28,
        30,1,0,0,0,29,24,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,
        0,32,34,1,0,0,0,33,31,1,0,0,0,34,35,5,3,0,0,35,36,5,4,0,0,36,37,
        7,0,0,0,37,38,5,6,0,0,38,3,1,0,0,0,39,40,5,7,0,0,40,44,5,4,0,0,41,
        43,3,6,3,0,42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,
        0,45,50,1,0,0,0,46,44,1,0,0,0,47,49,3,10,5,0,48,47,1,0,0,0,49,52,
        1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,
        53,54,5,6,0,0,54,5,1,0,0,0,55,56,5,8,0,0,56,58,5,4,0,0,57,59,3,8,
        4,0,58,57,1,0,0,0,59,60,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,7,
        1,0,0,0,62,64,5,15,0,0,63,65,5,2,0,0,64,63,1,0,0,0,64,65,1,0,0,0,
        65,67,1,0,0,0,66,62,1,0,0,0,67,68,1,0,0,0,68,66,1,0,0,0,68,69,1,
        0,0,0,69,70,1,0,0,0,70,71,5,4,0,0,71,72,5,14,0,0,72,77,5,9,0,0,73,
        74,3,12,6,0,74,75,5,9,0,0,75,77,1,0,0,0,76,66,1,0,0,0,76,73,1,0,
        0,0,77,9,1,0,0,0,78,79,5,10,0,0,79,11,1,0,0,0,80,93,5,11,0,0,81,
        82,5,15,0,0,82,88,5,12,0,0,83,84,5,13,0,0,84,85,5,15,0,0,85,89,5,
        13,0,0,86,89,5,18,0,0,87,89,5,17,0,0,88,83,1,0,0,0,88,86,1,0,0,0,
        88,87,1,0,0,0,89,91,1,0,0,0,90,92,5,2,0,0,91,90,1,0,0,0,91,92,1,
        0,0,0,92,94,1,0,0,0,93,81,1,0,0,0,94,95,1,0,0,0,95,93,1,0,0,0,95,
        96,1,0,0,0,96,13,1,0,0,0,12,17,27,31,44,50,60,64,68,76,88,91,95
    ]

class CompilerParser ( Parser ):

    grammarFileName = "Compiler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "':'", "'void'", 
                     "'end'", "'main'", "'var'", "';'", "'COMANDO'", "'const'", 
                     "'='", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "VARTYPE", "VARNAME", "NAME", 
                      "VALFLOAT", "VALINT", "WS" ]

    RULE_prog = 0
    RULE_decFuncao = 1
    RULE_main = 2
    RULE_decVar = 3
    RULE_varlist = 4
    RULE_comandos = 5
    RULE_consts = 6

    ruleNames =  [ "prog", "decFuncao", "main", "decVar", "varlist", "comandos", 
                   "consts" ]

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
    VARTYPE=14
    VARNAME=15
    NAME=16
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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 14
                self.decFuncao()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
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

        def NAME(self):
            return self.getToken(CompilerParser.NAME, 0)

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
            self.state = 22
            self.match(CompilerParser.NAME)
            self.state = 23
            self.match(CompilerParser.T__0)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 24
                self.match(CompilerParser.VARTYPE)
                self.state = 25
                self.match(CompilerParser.VARNAME)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 26
                    self.match(CompilerParser.T__1)


                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(CompilerParser.T__2)
            self.state = 35
            self.match(CompilerParser.T__3)
            self.state = 36
            _la = self._input.LA(1)
            if not(_la==5 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 37
            self.match(CompilerParser.T__5)
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
        self.enterRule(localctx, 4, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(CompilerParser.T__6)
            self.state = 40
            self.match(CompilerParser.T__3)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 41
                self.decVar()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 47
                self.comandos()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
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




    def decVar(self):

        localctx = CompilerParser.DecVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(CompilerParser.T__7)
            self.state = 56
            self.match(CompilerParser.T__3)
            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.varlist()
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==11 or _la==15):
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
        self.enterRule(localctx, 8, self.RULE_varlist)
        self._la = 0 # Token type
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 62
                    self.match(CompilerParser.VARNAME)
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==2:
                        self.state = 63
                        self.match(CompilerParser.T__1)


                    self.state = 68 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==15):
                        break

                self.state = 70
                self.match(CompilerParser.T__3)
                self.state = 71
                self.match(CompilerParser.VARTYPE)
                self.state = 72
                self.match(CompilerParser.T__8)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.consts()
                self.state = 74
                self.match(CompilerParser.T__8)
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
        self.enterRule(localctx, 10, self.RULE_comandos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(CompilerParser.T__9)
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
            self.state = 80
            self.match(CompilerParser.T__10)
            self.state = 93 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 81
                self.match(CompilerParser.VARNAME)
                self.state = 82
                self.match(CompilerParser.T__11)
                self.state = 88
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [13]:
                    self.state = 83
                    self.match(CompilerParser.T__12)
                    self.state = 84
                    self.match(CompilerParser.VARNAME)
                    self.state = 85
                    self.match(CompilerParser.T__12)
                    pass
                elif token in [18]:
                    self.state = 86
                    self.match(CompilerParser.VALINT)
                    pass
                elif token in [17]:
                    self.state = 87
                    self.match(CompilerParser.VALFLOAT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 90
                    self.match(CompilerParser.T__1)


                self.state = 95 
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





