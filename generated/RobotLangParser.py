# Generated from RobotLang.g4 by ANTLR 4.13.1
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
        4,1,18,75,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,4,2,38,8,2,11,2,12,2,39,1,
        2,1,2,1,3,1,3,1,3,3,3,47,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,56,
        8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,
        1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,1,0,12,14,72,0,21,1,
        0,0,0,2,27,1,0,0,0,4,31,1,0,0,0,6,46,1,0,0,0,8,48,1,0,0,0,10,57,
        1,0,0,0,12,63,1,0,0,0,14,68,1,0,0,0,16,72,1,0,0,0,18,22,3,2,1,0,
        19,22,3,4,2,0,20,22,3,6,3,0,21,18,1,0,0,0,21,19,1,0,0,0,21,20,1,
        0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,
        26,5,0,0,1,26,1,1,0,0,0,27,28,5,7,0,0,28,29,5,15,0,0,29,30,5,1,0,
        0,30,3,1,0,0,0,31,32,5,8,0,0,32,33,5,15,0,0,33,34,5,2,0,0,34,35,
        5,3,0,0,35,37,5,4,0,0,36,38,3,6,3,0,37,36,1,0,0,0,38,39,1,0,0,0,
        39,37,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,5,5,0,0,42,5,1,0,
        0,0,43,47,3,8,4,0,44,47,3,10,5,0,45,47,3,12,6,0,46,43,1,0,0,0,46,
        44,1,0,0,0,46,45,1,0,0,0,47,7,1,0,0,0,48,49,5,9,0,0,49,50,3,14,7,
        0,50,51,5,6,0,0,51,55,3,6,3,0,52,53,5,10,0,0,53,54,5,6,0,0,54,56,
        3,6,3,0,55,52,1,0,0,0,55,56,1,0,0,0,56,9,1,0,0,0,57,58,5,11,0,0,
        58,59,5,15,0,0,59,60,5,2,0,0,60,61,5,3,0,0,61,62,5,1,0,0,62,11,1,
        0,0,0,63,64,5,15,0,0,64,65,5,2,0,0,65,66,5,3,0,0,66,67,5,1,0,0,67,
        13,1,0,0,0,68,69,5,15,0,0,69,70,3,16,8,0,70,71,5,16,0,0,71,15,1,
        0,0,0,72,73,7,0,0,0,73,17,1,0,0,0,5,21,23,39,46,55
    ]

class RobotLangParser ( Parser ):

    grammarFileName = "RobotLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "')'", "'{'", "'}'", "':'", 
                     "'sensor'", "'rutina'", "'si'", "'sino'", "'ejecutar'", 
                     "'<'", "'>'", "'=='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "SENSOR", "RUTINA", 
                      "SI", "SINO", "EJECUTAR", "LT", "GT", "EQ", "ID", 
                      "NUMBER", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_routine = 2
    RULE_statement = 3
    RULE_control = 4
    RULE_action = 5
    RULE_call = 6
    RULE_expr = 7
    RULE_comparator = 8

    ruleNames =  [ "program", "declaration", "routine", "statement", "control", 
                   "action", "call", "expr", "comparator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    SENSOR=7
    RUTINA=8
    SI=9
    SINO=10
    EJECUTAR=11
    LT=12
    GT=13
    EQ=14
    ID=15
    NUMBER=16
    WS=17
    COMMENT=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RobotLangParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotLangParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(RobotLangParser.DeclarationContext,i)


        def routine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotLangParser.RoutineContext)
            else:
                return self.getTypedRuleContext(RobotLangParser.RoutineContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(RobotLangParser.StatementContext,i)


        def getRuleIndex(self):
            return RobotLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = RobotLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 18
                    self.declaration()
                    pass
                elif token in [8]:
                    self.state = 19
                    self.routine()
                    pass
                elif token in [9, 11, 15]:
                    self.state = 20
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 35712) != 0)):
                    break

            self.state = 25
            self.match(RobotLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SENSOR(self):
            return self.getToken(RobotLangParser.SENSOR, 0)

        def ID(self):
            return self.getToken(RobotLangParser.ID, 0)

        def getRuleIndex(self):
            return RobotLangParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = RobotLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(RobotLangParser.SENSOR)
            self.state = 28
            self.match(RobotLangParser.ID)
            self.state = 29
            self.match(RobotLangParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoutineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RUTINA(self):
            return self.getToken(RobotLangParser.RUTINA, 0)

        def ID(self):
            return self.getToken(RobotLangParser.ID, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(RobotLangParser.StatementContext,i)


        def getRuleIndex(self):
            return RobotLangParser.RULE_routine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoutine" ):
                listener.enterRoutine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoutine" ):
                listener.exitRoutine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoutine" ):
                return visitor.visitRoutine(self)
            else:
                return visitor.visitChildren(self)




    def routine(self):

        localctx = RobotLangParser.RoutineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_routine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(RobotLangParser.RUTINA)
            self.state = 32
            self.match(RobotLangParser.ID)
            self.state = 33
            self.match(RobotLangParser.T__1)
            self.state = 34
            self.match(RobotLangParser.T__2)
            self.state = 35
            self.match(RobotLangParser.T__3)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.statement()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 35328) != 0)):
                    break

            self.state = 41
            self.match(RobotLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def control(self):
            return self.getTypedRuleContext(RobotLangParser.ControlContext,0)


        def action(self):
            return self.getTypedRuleContext(RobotLangParser.ActionContext,0)


        def call(self):
            return self.getTypedRuleContext(RobotLangParser.CallContext,0)


        def getRuleIndex(self):
            return RobotLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = RobotLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.control()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.action()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.call()
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


    class ControlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(RobotLangParser.SI, 0)

        def expr(self):
            return self.getTypedRuleContext(RobotLangParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RobotLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(RobotLangParser.StatementContext,i)


        def SINO(self):
            return self.getToken(RobotLangParser.SINO, 0)

        def getRuleIndex(self):
            return RobotLangParser.RULE_control

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControl" ):
                listener.enterControl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControl" ):
                listener.exitControl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControl" ):
                return visitor.visitControl(self)
            else:
                return visitor.visitChildren(self)




    def control(self):

        localctx = RobotLangParser.ControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_control)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(RobotLangParser.SI)
            self.state = 49
            self.expr()
            self.state = 50
            self.match(RobotLangParser.T__5)
            self.state = 51
            self.statement()
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 52
                self.match(RobotLangParser.SINO)
                self.state = 53
                self.match(RobotLangParser.T__5)
                self.state = 54
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EJECUTAR(self):
            return self.getToken(RobotLangParser.EJECUTAR, 0)

        def ID(self):
            return self.getToken(RobotLangParser.ID, 0)

        def getRuleIndex(self):
            return RobotLangParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = RobotLangParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(RobotLangParser.EJECUTAR)
            self.state = 58
            self.match(RobotLangParser.ID)
            self.state = 59
            self.match(RobotLangParser.T__1)
            self.state = 60
            self.match(RobotLangParser.T__2)
            self.state = 61
            self.match(RobotLangParser.T__0)
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

        def ID(self):
            return self.getToken(RobotLangParser.ID, 0)

        def getRuleIndex(self):
            return RobotLangParser.RULE_call

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

        localctx = RobotLangParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(RobotLangParser.ID)
            self.state = 64
            self.match(RobotLangParser.T__1)
            self.state = 65
            self.match(RobotLangParser.T__2)
            self.state = 66
            self.match(RobotLangParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(RobotLangParser.ID, 0)

        def comparator(self):
            return self.getTypedRuleContext(RobotLangParser.ComparatorContext,0)


        def NUMBER(self):
            return self.getToken(RobotLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return RobotLangParser.RULE_expr

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




    def expr(self):

        localctx = RobotLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(RobotLangParser.ID)
            self.state = 69
            self.comparator()
            self.state = 70
            self.match(RobotLangParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(RobotLangParser.LT, 0)

        def GT(self):
            return self.getToken(RobotLangParser.GT, 0)

        def EQ(self):
            return self.getToken(RobotLangParser.EQ, 0)

        def getRuleIndex(self):
            return RobotLangParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = RobotLangParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
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





