import ast
import astpretty


def action():
    astpretty.pprint(ast.parse(open('hw1_easy.py').read()).body[0], show_offsets=False)


if __name__ == '__main__':
    action()
