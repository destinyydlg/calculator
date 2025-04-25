import math
from CalculatorVisitor import CalculatorVisitor
from CalculatorParser import CalculatorParser

variables = {}

class EvalVisitor(CalculatorVisitor):

    def visitProgram(self, ctx):
        for child in ctx.statement():
            self.visit(child)

    def visitStatement(self, ctx):
        if ctx.getChildCount() == 1:
            return None
        if ctx.getChild(1).getText() == '=':
            var_name = ctx.ID().getText()
            var_value = self.visit(ctx.expression())
            variables[var_name] = var_value
            print(f"{var_name} = {var_value}")
            return var_value
        else:
            result = self.visit(ctx.expression())
            print(f"Result: {result}")
            return result

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.type == CalculatorParser.MUL:
            return left * right
        else:
            return left / right

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.type == CalculatorParser.ADD:
            return left + right
        else:
            return left - right

    def visitCompareExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.type == CalculatorParser.GT:
            return left > right
        else:
            return left < right

    def visitFunctionExpr(self, ctx):
        func_name = ctx.function().getText()
        value = self.visit(ctx.expression())
        if func_name == 'cos':
            return math.cos(math.radians(value))
        elif func_name == 'sin':
            return math.sin(math.radians(value))
        elif func_name == 'tan':
            return math.tan(math.radians(value))
        elif func_name == 'acos':
            return math.degrees(math.acos(value))
        elif func_name == 'asin':
            return math.degrees(math.asin(value))
        elif func_name == 'atan':
            return math.degrees(math.atan(value))
        elif func_name == 'sqrt':
            return math.sqrt(value)
        elif func_name == 'log':
            return math.log10(value)
        elif func_name == 'ln':
            return math.log(value)
        else:
            raise Exception(f"Unknown function: {func_name}")

    def visitIntExpr(self, ctx):
        return int(ctx.INT().getText())

    def visitIdExpr(self, ctx):
        var_name = ctx.ID().getText()
        if var_name in variables:
            return variables[var_name]
        else:
            raise Exception(f"Undefined variable: {var_name}")

    def visitParensExpr(self, ctx):
        return self.visit(ctx.expression())