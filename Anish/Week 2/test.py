import operator

class Person:
    name = "Anish"

    def __init__(self):
        return

p = Person()
name = operator.attrgetter("name")
print(operator.attrgetter("name")(Person()))