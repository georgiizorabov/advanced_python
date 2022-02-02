import ast
import graphviz

g = graphviz.Graph()
cnt = 0


def getlabel(node):
    label = node.__class__.__name__
    if isinstance(node, ast.Constant):
        label += ": " + str(node.value)
    elif isinstance(node, ast.Name):
        label += ": " + str(node.id)
    elif isinstance(node, ast.FunctionDef):
        label += ": " + str(node.name)
    elif isinstance(node, ast.arg):
        label += ": " + str(node.arg)
    return label


class Visitor(object):
    def generic_visit(self, node):
        global cnt
        curnum = cnt
        g.node(str(curnum), label=getlabel(node), shape="square")

        cnt += 1
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        g.edge(str(curnum), str(self.generic_visit(item)))
            elif isinstance(value, ast.AST):
                g.edge(str(curnum), str(self.generic_visit(value)))
        return curnum


def action():
    x = Visitor()
    x.generic_visit(ast.parse(open('hw1_easy.py').read()))
    g.render('artifacts/ast')


if __name__ == '__main__':
    action()
