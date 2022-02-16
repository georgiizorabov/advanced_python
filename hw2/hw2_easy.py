
def gen_begin():
    return """
\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{array}
\\usepackage[english,russian]{babel} 

\\begin{document} 
\\begin{center} 
\\hspace*{-4cm}
"""
def gen_end():
    return """\\hline
\\end{tabular}
\\end{center}
\\end{document}"""

def gen_body(arr):
    return "\\begin{tabular}{ |" + "m{10em} |" * len(arr[0]) + "}\n\n\t\\hline" + " \\\\ \n\t \\hline\n\t".join(list(map(lambda i : " & ".join(i), arr))) + "\\\\\n"

def make_tex(arr):
    return gen_begin() + gen_body(arr) + gen_end()
def text_to_list(inp):
    arr = [i for i in inp .split()]
    arr = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    return arr
    
if __name__ == '__main__':
    res = make_tex(text_to_list(open('gasstation.txt', 'r').read()))
    with open("artifacts/easy.tex", "w") as f:
        f.write(res)