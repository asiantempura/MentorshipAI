import ast
from lib2to3.pgen2.tokenize import generate_tokens
from textwrap import indent
import astpretty
import tokenize
import asttokens
import astroid

contents = ''
inputData = 'inputData.py'
with open(inputData, 'r', encoding='utf-8') as f:
    contents = f.read()

#print(contents)

parsedAST = ast.parse(contents)
astpretty.pprint(parsedAST.body[0], indent=2)

readableAST = ast.dump(parsedAST, indent=2)
print(readableAST)


astToCode = ast.unparse(parsedAST)
#print(astToCode)

with tokenize.open(inputData) as f:
    tokens = generate_tokens(f.readline)

    for i in tokens:
        pass
        print(i)


astTokens = asttokens.ASTTokens(contents, parse=True)
for i in astTokens.tokens:
    pass
    print(i)