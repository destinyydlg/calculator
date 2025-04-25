from antlr4 import *
from CalculatorLexer import CalculatorLexer
from CalculatorParser import CalculatorParser
from EvalVisitor import EvalVisitor

def main():
    # --- INPUT GOES HERE ---
    input_expr = """
    a = 45
    cos(a)
    sin(a)
    tan(a)
    sqrt(25)
    log(1000)
    ln(2)
    10 > 5
    3 + 4 * (2 + 1)
    """

    # --- ANTLR SETUP ---
    input_stream = InputStream(input_expr)
    lexer = CalculatorLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalculatorParser(token_stream)
    tree = parser.program()

    # --- TREE WALKER ---
    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()