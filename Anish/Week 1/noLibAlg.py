#from deap import base, creator, tools, algorithms
from modifiedFunctions import *
import random
import numpy as np
import functools

'''
' ABC ' -> 
'ABC'   -> strip()
'abc'   -> lower()
'Abc'   -> title()
'''

def apply(transformed):
    transformedStr = ' ABC '

    for func in transformed:
        transformedStr = functions.get(func)(transformedStr)

    return transformedStr

# Take in list of strings that represent functions
# Return integer of how "wrong" the individual is
def evalFitness(individual):
    #print(individual)
    startingStr = ' ABC '
    endingStr = 'Abc'
    transformedStr = ' ABC '

    try:
        for func in individual:
            transformedStr = functions.get(func)(transformedStr)

    except:
        return 100

    # Metric 1: Number of functions required to transform string
    # Metric 2: Difference in uppercase/lowercase letters
    # Metric 3: Difference in whitespace
    # Metric 4: Difference in length

    #error = len(individual) + abs(len(endingStr) - len(transformedStr))
    error = 0

    # Strings of different length = small error in error metric
    for transformed, ending in zip(transformedStr.strip(), endingStr.strip()):
        if transformed.isupper() and ending.islower():
            error += 1
        elif transformed.islower() and ending.isupper():
            error += 1
        elif transformed.isspace() and not ending.isspace():
            error += 1
        elif not transformed.isspace() and ending.isspace():
            error += 1

    return len(individual) +  abs(len(endingStr) - len(transformedStr)) + error
            


def generateIndividual():
    #return [random.choice(list(functions.keys()))]
    return [random.choice(list(functions.keys())) for i in range(random.randint(1, 3))]

def mate(l1, l2):
    child = []

    for x, y in zip(l1, l2):
        if random.randint(0, 1) == 0:
            child.append(x)
        else:
            child.append(y)

    '''if len(l1) == len(l2):
        return child
    elif len(l1) > len(l2):
        longerList = l1
        shorterList = l2
    else:
        longerList = l2
        shorterList = l1

    for i in range(len(shorterList), len(longerList)):
        if random.randint(0, 1) == 0:
            child.append(longerList[i])'''

    return child

def weightedMating(l1, l2):
    child = []

    better, worse = (l1, l2) if evalFitness(l1) <= evalFitness(l2) else (l2, l1)

    for w, b in zip(worse, better):
        if random.randint(1, evalFitness(l1) + evalFitness(l2)) <= worse:
            child.append(b)
        else:
            child.append(w)

    return child


def mutate(l1):
    #l1[random.randint(0, len(l1)-1)] = random.choice(list(functions.keys()))
    

    '''for i in range(5):
        if random.randint(0, 100) <= 5:
            if len(l1) > i:
                l1[i] = random.choice(list(functions.keys()))
            else:
                l1.append(random.choice(list(functions.keys())))

    return l1'''
    i = 0
    mutated = []

    while i < max(len(l1), 6):
        if random.randint(0, 100) <= 5:
            if random.randint(0, 1) == 0:
                mutated.append(random.choice(list(functions.keys())))
            else:
                i += 1 
        elif i < len(l1):
            mutated.append(l1[i])
            i += 1

    return mutated


populationSize = 1000
gen = 0
population = [generateIndividual() for i in range(populationSize)]
best = population[0]

while gen < 1000:
    gen += 1 

    population = sorted(population, key=evalFitness)
    print('Generation %i -> %i' %(gen, evalFitness(population[0])))

    if evalFitness(best) > evalFitness(population[0]):
        best = population[0]

    if evalFitness(population[0]) == 2:
        print(population[0], population[1])
    

    nextGen = []

    for i in range(populationSize/2):
        #nextGen.append(mutate(mate(population[i], population[i+1])))
        #nextGen.append(mutate(mate(population[i], population[i+1])))
        nextGen.append(mutate(weightedMating(population[i], population[i+1])))
        nextGen.append(mutate(weightedMating(population[i], population[i+1])))


    population = nextGen[:]
    del nextGen[:]

print(sorted(population, key=evalFitness))
print(best, evalFitness(best))




'''
creator.create("FitnessMin", base.Fitness, weights=(-1.0, -1.0, -1.0))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

toolbox.register("generateIndividual", generateIndividual)
toolbox.register("evalFitness", evalFitness)

toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.generateIndividual, 1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evalFitness)
#toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mate", mate)
#toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("mutate", mutate)
toolbox.register("select", tools.selTournament, tournsize=3)


def main():
    pop = toolbox.population(populationSize)

    fitnesses = list(map(toolbox.evaluate, pop))

    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit
        #print(ind, fit)
        #print(ind.fitness.values)

    CXPB, MUTPB = 0.5, 0.2
    #fits = [ind.fitness.values for ind in pop]

    g = 0
    while g < 100:
        g += 1


        #offspring = toolbox.select(pop, len(pop))
        #offspring = list(map(toolbox.clone, offspring))

        print("-- Generation %i --" % g)
        for i in pop:
            print(i)



        # Mate individuals
        for child1, child2 in zip(pop[::2], pop[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values


        # Mutate individuals
        for mutant in pop:
            toolbox.mutate(mutant)
            del mutant.fitness.values


        # Evaluate invalid individuals
        invalid_fit = [ind for ind in pop if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_fit)

        for ind, fit in zip(invalid_fit, fitnesses):
            ind.fitness.values = fit

        #pop[:] = offspring

        #fits = [ind.fitness for ind in pop]

    best = functools.reduce(lambda a, b: a if toolbox.evaluate(a) < toolbox.evaluate(b) else b, pop)
    return best

run = True

if run:
    score = main()
    print("Best result is: " + str(score))
    print(evalFitness(score))

testToolbox = False

if testToolbox:
    print(toolbox.population(5))

applyFunc = False

if applyFunc:
    

    print(evalFitness(['strip', 'title']))
    print(apply(['strip', 'title']))

'''


