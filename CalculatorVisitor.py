# Generated from Calculator.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorParser.

class CalculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorParser#program.
    def visitProgram(self, ctx:CalculatorParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#statement.
    def visitStatement(self, ctx:CalculatorParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#FunctionExpr.
    def visitFunctionExpr(self, ctx:CalculatorParser.FunctionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:CalculatorParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#IdExpr.
    def visitIdExpr(self, ctx:CalculatorParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#CompareExpr.
    def visitCompareExpr(self, ctx:CalculatorParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#ParensExpr.
    def visitParensExpr(self, ctx:CalculatorParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#IntExpr.
    def visitIntExpr(self, ctx:CalculatorParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:CalculatorParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#function.
    def visitFunction(self, ctx:CalculatorParser.FunctionContext):
        return self.visitChildren(ctx)



del CalculatorParser