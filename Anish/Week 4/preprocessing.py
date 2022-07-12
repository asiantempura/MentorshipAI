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

parsedAST = ast.parse(contents)
prettyPrint = parsedAST.body[0]
#astpretty.pprint(prettyPrint, indent=2)

with tokenize.open(inputData) as f:
    tokens = generate_tokens(f.readline)
    tokens = list(tokens)

    for i in tokens:
        pass
        #print(i)

def likeOneHotEncoding(tree: ast.AST, tokens: list[tuple]) -> list[int]:
    tree.name = 'func'
    print(tree.name)

    counter = 0
    for i in range(len(tree.args.args)):
        tree.args.args[i].arg = 'out' + str(counter)



print(likeOneHotEncoding(prettyPrint, tokens)) 
print(astpretty.pprint(prettyPrint, indent=2))
print(ast.unparse(prettyPrint))