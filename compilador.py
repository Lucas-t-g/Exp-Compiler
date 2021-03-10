from time import sleep
import old_functions as of
import random

header = """
.source Test.src
.class  public Test
.super  java/lang/Object

.method public <init>()V
    aload_0
    invokenonvirtual java/lang/Object/<init>()V
    return
.end method

.method public static main([Ljava/lang/String;)V

    getstatic java/lang/System/out Ljava/io/PrintStream;
"""

footer = """
    invokevirtual java/io/PrintStream/println(I)V

    return  
.limit stack 10
.end method    
"""

class Token:
    def __init__(self, type, text):
        self.type = type
        self.text = text
        
    def __repr__(self):
        return '(' + self.type + ' ' + self.text + ' )'

def lexer(_str):
    tokens = []
    _str+= '$'
    i = 0
    while True:
        char = _str[i]
        if char.isspace(): #_ SKIP SPACES
            i += 1
            continue
        elif char == "+": #_ PLUS
            tokens.append(Token("PLUS", char))
        elif char == "*": #_ TIMES
            tokens.append(Token("TIMES", char))
        elif char == "(": #_ OPEN PARENTHESES
            tokens.append(Token("OP_PAR", char))
        elif char == ")": #_ CLOSE PARENTHESES
            tokens.append(Token("CL_PAR", char))
        elif char.isdigit(): #_ INTEGER
            n = _str[i]
            i += 1
            char = _str[i]
            while char.isdigit():
                n += char
                i += 1
                char = _str[i]
            tokens.append(Token("NUMBER", n))
            continue
        elif char == "$":
            tokens.append(Token("END", char))
            break
        else:
            print("ALERT: unknown character: ", char)
        i += 1
    return tokens

#_ COMPILER
def compiler(s):
    tokens = lexer(s)
    arq_text = header
    # print(header)
    tokens, assembly_text = compiler_expression(tokens)
    arq_text += "\n" + assembly_text + "\n" + footer
    # print(arq_text)
    file = open("test.j","w") 
    file.write(arq_text)
    # print(footer)

def compiler_expression(tokens):
    tokens, assembly_text = compiler_term(tokens)
    if tokens[0].type == "PLUS":
        tokens.pop(0)
        tokens, assembly_text2 = compiler_expression(tokens)
        assembly_text += assembly_text2 + "\n    iadd"
        # print("    iadd") #_ POSTFIX
    return tokens, assembly_text

def compiler_term(tokens):
    tokens, assembly_text = compiler_factor(tokens)
    if tokens[0].type == "TIMES":
        tokens.pop(0)
        tokens, assembly_text2 = compiler_term(tokens)
        assembly_text += assembly_text2 + "\n    imul"
        # print("    imul") #_ POSTFIX
    return tokens, assembly_text

def compiler_factor(tokens):
    t = tokens.pop(0)
    if t.type == "NUMBER":
        assembly_text = "\n    ldc " + t.text
        # print("    ldc", t.text)
    elif t.type == "OP_PAR":
        tokens, assembly_text = compiler_expression(tokens)
        t = tokens.pop(0)
    return tokens, assembly_text

if __name__ == "__main__":
    examples = []
    examples.append("1+ 543 +5* 4")
    examples.append("1+4*3 + insto nao e uma expressao")
    examples.append("((1 + 2) * (3 * 34))")
    examples.append("12 + 62 * (83 + 64 * 45)")
    examples.append("(1 + 2) * 3")
    examples.append("1 + 2 * (3 + 4 * 5)")
    examples.append("1 + 2 * 3")
    examples.append("2 * (3 + 4)")
    examples.append("1 + 2 * (3 + 4) + (5 * 6 + 7)")
    examples.append("")
    examples.append("")
    # print(example1, example2)
    # print(lexer(example1))
    # print(lexer(example2))

    # s = generator()
    s = examples[8]
    print(s)
    l = lexer(s)
    # # print(l)
    t, v = of.interpreter(l)
    print(v)
    # p = parser(l)
    # print(p)
    # p = interpreter(l2)
    # # print(p)
    compiler(s)
