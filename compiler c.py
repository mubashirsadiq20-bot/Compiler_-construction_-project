print("Simple Compiler In Python")
print("==========================")

expression = input("Enter Expression: ").strip()

if expression == "":
    print("No input given")
    exit()

operators = ['+','-','*','/']
digits = '0123456789'

tokens = []

# ---------- LEXICAL ANALYZER ----------
for ch in expression:
    if ch in operators:
        tokens.append(("OPERATOR", ch))
    elif ch in digits:
        tokens.append(("NUMBER", ch))
    elif ch == ' ':
        continue
    else:
        tokens.append(("UNKNOWN", ch))

print("\nTokens:")
for t in tokens:
    print(t)

# ---------- SYNTAX CHECKER ----------
valid = True
prev = ""

for t in tokens:
    typ = t[0]

    if prev == "" and typ != "NUMBER":
        valid = False
        break
    if prev == "NUMBER" and typ == "NUMBER":
        valid = False
        break
    if prev == "OPERATOR" and typ == "OPERATOR":
        valid = False
        break
    
    prev = typ

if tokens[-1][0] == "OPERATOR":
    valid = False

print("\nSyntax Result:")
if valid:
    print("VALID EXPRESSION")
else:
    print("INVALID EXPRESSION")