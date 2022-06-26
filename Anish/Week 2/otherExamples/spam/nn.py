import csv
import numpy

with open("spambase.csv") as spambase:
    spamReader = csv.reader(spambase)
    spam = list(list(float(elem) for elem in row) for row in spamReader)

