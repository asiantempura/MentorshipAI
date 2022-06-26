from functools import partial

def testCallable(s):
    return s()

def progn(*args):
    for arg in args:
        arg()

def prog2(out1, out2): 
    return partial(progn,out1,out2)


def forLoop(func, numTimes):
    for i in range(numTimes):
        func()



functions = { 
    'testCallable': testCallable
}


'''
print(functions.get('strip')(' ABC '))
print(functions.get('lower')(' ABC '))
print(functions.get('title')(' ABC '))
print(functions.get('upper')(' ABC '))
print(functions.get('lstrip')(' ABC '))
print(functions.get('rstrip')(' ABC '))
print(functions.get('swapcase')(' ABC '))
'''

