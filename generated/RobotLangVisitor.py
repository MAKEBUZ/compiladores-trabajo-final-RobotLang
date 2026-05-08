# Generated from RobotLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RobotLangParser import RobotLangParser
else:
    from RobotLangParser import RobotLangParser

# This class defines a complete generic visitor for a parse tree produced by RobotLangParser.

class RobotLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RobotLangParser#program.
    def visitProgram(self, ctx:RobotLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotLangParser#declaration.
    def visitDeclaration(self, ctx:RobotLangParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotLangParser#routine.
    def visitRoutine(self, ctx:RobotLangParser.RoutineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotLangParser#statement.
    def visitStatement(self, ctx:RobotLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotLangParser#control.
    def visitControl(self, ctx:RobotLangParser.ControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotLangParser#action.
    def visitAction(self, ctx:RobotLangParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotLangParser#call.
    def visitCall(self, ctx:RobotLangParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotLangParser#expr.
    def visitExpr(self, ctx:RobotLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RobotLangParser#comparator.
    def visitComparator(self, ctx:RobotLangParser.ComparatorContext):
        return self.visitChildren(ctx)



del RobotLangParser