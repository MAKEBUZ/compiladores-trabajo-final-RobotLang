# Generated from RobotLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RobotLangParser import RobotLangParser
else:
    from RobotLangParser import RobotLangParser

# This class defines a complete listener for a parse tree produced by RobotLangParser.
class RobotLangListener(ParseTreeListener):

    # Enter a parse tree produced by RobotLangParser#program.
    def enterProgram(self, ctx:RobotLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by RobotLangParser#program.
    def exitProgram(self, ctx:RobotLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by RobotLangParser#declaration.
    def enterDeclaration(self, ctx:RobotLangParser.DeclarationContext):
        pass

    # Exit a parse tree produced by RobotLangParser#declaration.
    def exitDeclaration(self, ctx:RobotLangParser.DeclarationContext):
        pass


    # Enter a parse tree produced by RobotLangParser#routine.
    def enterRoutine(self, ctx:RobotLangParser.RoutineContext):
        pass

    # Exit a parse tree produced by RobotLangParser#routine.
    def exitRoutine(self, ctx:RobotLangParser.RoutineContext):
        pass


    # Enter a parse tree produced by RobotLangParser#statement.
    def enterStatement(self, ctx:RobotLangParser.StatementContext):
        pass

    # Exit a parse tree produced by RobotLangParser#statement.
    def exitStatement(self, ctx:RobotLangParser.StatementContext):
        pass


    # Enter a parse tree produced by RobotLangParser#control.
    def enterControl(self, ctx:RobotLangParser.ControlContext):
        pass

    # Exit a parse tree produced by RobotLangParser#control.
    def exitControl(self, ctx:RobotLangParser.ControlContext):
        pass


    # Enter a parse tree produced by RobotLangParser#action.
    def enterAction(self, ctx:RobotLangParser.ActionContext):
        pass

    # Exit a parse tree produced by RobotLangParser#action.
    def exitAction(self, ctx:RobotLangParser.ActionContext):
        pass


    # Enter a parse tree produced by RobotLangParser#call.
    def enterCall(self, ctx:RobotLangParser.CallContext):
        pass

    # Exit a parse tree produced by RobotLangParser#call.
    def exitCall(self, ctx:RobotLangParser.CallContext):
        pass


    # Enter a parse tree produced by RobotLangParser#expr.
    def enterExpr(self, ctx:RobotLangParser.ExprContext):
        pass

    # Exit a parse tree produced by RobotLangParser#expr.
    def exitExpr(self, ctx:RobotLangParser.ExprContext):
        pass


    # Enter a parse tree produced by RobotLangParser#comparator.
    def enterComparator(self, ctx:RobotLangParser.ComparatorContext):
        pass

    # Exit a parse tree produced by RobotLangParser#comparator.
    def exitComparator(self, ctx:RobotLangParser.ComparatorContext):
        pass



del RobotLangParser