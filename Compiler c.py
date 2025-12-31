# Simple Lexical Analyzer (Compiler Construction mini project)

operators = ['+','-','*','/','=','>','<']
keywords = ['if','else','while','for','int','float','char','double']

print("Enter your program line:")
code = input()

tokens = code.split()

print("\nTokens Found:\n")

for token in tokens:
    if token in operators:
        print(token , " = Operator")
    elif token in keywords:
        print(token , " = Keyword")
    elif token.isnumeric():
        print(token , " = Number")
    else:
        print(token , " = Identifier")
