import ast
from lib2to3.pgen2.tokenize import generate_tokens
from textwrap import indent
import astpretty
import tokenize
import asttokens
import astroid
import numpy
from sklearn import *
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

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
    # Normalizing function name
    tree.name = 'func'
    #print(tree.name)

    # Normalizing input variable names in function signature
    counter = 0
    for i in range(len(tree.args.args)):
        tree.args.args[i].arg = 'out' + str(counter)

    # Record all functions 
    funcs = []
    for i in tree.body:
        #print(type(i))

        if type(i) == ast.Assign: 
            print(i.value.func.attr)
            funcs.append(str(i.value.func.attr))
        elif type(i) == ast.Return:
            pass


    funcs = numpy.array(funcs)
    print(funcs)

    intEncoded = LabelEncoder().fit_transform(funcs)
    print(intEncoded)

    intEncoded = intEncoded.reshape(len(intEncoded), 1)
    print(intEncoded)
    oneHotEncoded = OneHotEncoder(sparse=False).fit_transform(intEncoded)
    #print(oneHotEncoded)

    return oneHotEncoded

        



print(likeOneHotEncoding(prettyPrint, tokens)) 
#print(astpretty.pprint(prettyPrint, indent=2))
print(ast.unparse(prettyPrint))