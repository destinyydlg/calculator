# Generated from Calculator.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete listener for a parse tree produced by CalculatorParser.
class CalculatorListener(ParseTreeListener):

    # Enter a parse tree produced by CalculatorParser#program.
    def enterProgram(self, ctx:CalculatorParser.ProgramContext):
        pass

    # Exit a parse tree produced by CalculatorParser#program.
    def exitProgram(self, ctx:CalculatorParser.ProgramContext):
        pass


    # Enter a parse tree produced by CalculatorParser#statement.
    def enterStatement(self, ctx:CalculatorParser.StatementContext):
        pass

    # Exit a parse tree produced by CalculatorParser#statement.
    def exitStatement(self, ctx:CalculatorParser.StatementContext):
        pass


    # Enter a parse tree produced by CalculatorParser#FunctionExpr.
    def enterFunctionExpr(self, ctx:CalculatorParser.FunctionExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#FunctionExpr.
    def exitFunctionExpr(self, ctx:CalculatorParser.FunctionExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:CalculatorParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:CalculatorParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#IdExpr.
    def enterIdExpr(self, ctx:CalculatorParser.IdExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#IdExpr.
    def exitIdExpr(self, ctx:CalculatorParser.IdExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#CompareExpr.
    def enterCompareExpr(self, ctx:CalculatorParser.CompareExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#CompareExpr.
    def exitCompareExpr(self, ctx:CalculatorParser.CompareExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#ParensExpr.
    def enterParensExpr(self, ctx:CalculatorParser.ParensExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#ParensExpr.
    def exitParensExpr(self, ctx:CalculatorParser.ParensExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#IntExpr.
    def enterIntExpr(self, ctx:CalculatorParser.IntExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#IntExpr.
    def exitIntExpr(self, ctx:CalculatorParser.IntExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:CalculatorParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:CalculatorParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#function.
    def enterFunction(self, ctx:CalculatorParser.FunctionContext):
        pass

    # Exit a parse tree produced by CalculatorParser#function.
    def exitFunction(self, ctx:CalculatorParser.FunctionContext):
        pass



del CalculatorParser