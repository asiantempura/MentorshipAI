def strip(s):
    return s.strip()

def lower(s):
    return s.lower()

def title(s):
    return s.title()

def upper(s):
    return s.upper()

def lstrip(s):
    return s.lstrip()

def rstrip(s):
    return s.rstrip()

def swapcase(s):
    return s.swapcase()

def testCallable(s):
    return s + 1


functions = {
    'strip': strip,
    'lower': lower,
    'title': title, 
    'upper': upper,
    'lstrip': lstrip,
    'rstrip': rstrip,
    'swapcase': swapcase, 
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

