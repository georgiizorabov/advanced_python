import hw1_easy
import inspect
import ast
import astunparse

print(astunparse.dump(ast.parse(inspect.getsource(hw1_easy.fib))))