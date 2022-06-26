from StringIO import StringIO 
import sys
from functools import partial

def progn(*args):
    for arg in args:
        arg()

def prog2(out1, out2): 
    return partial(progn,out1,out2)

def do1():
    print(1)

def do2():
    print(2)

def do3():
    print(3)

prog2(do1, do2)(prog2(do3, do2))



def printSomething():
    print("Hello there")
    print("How you doin")
    print("Not bad")


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        self._stringio.close() 
        sys.stdout = self._stdout

with Capturing() as output:
    printSomething()

'''print(output)'''

# -----------

import operator

class Person:
    name = "Anish"

    def __init__(self):
        return

'''p = Person()
name = operator.attrgetter("name")
print(operator.attrgetter("name")(Person()))'''

