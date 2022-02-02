import ast
import astpretty

astpretty.pprint(ast.parse(open('hw1_easy.py').read()).body[0], show_offsets=False)
