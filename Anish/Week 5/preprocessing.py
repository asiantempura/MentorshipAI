import ast

content = ''
inputData = 'inputData.py'

with open(inputData, 'r', encoding='utf-8') as f:
    contents = f.read()

parsedAST = ast.parse(contents).body[0]
#print(parsedAST)

