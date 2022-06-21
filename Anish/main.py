from deap import base, creator, tools, algorithms
from modifiedFunctions import *
import random
import numpy as np

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
            error += 2
        elif transformed.islower() and ending.isupper():
            error += 2
        elif transformed.isspace() and not ending.isspace():
            error += 2
        elif not transformed.isspace() and ending.isspace():
            error += 2

    return len(individual), abs(len(endingStr) - len(transformedStr)), error
            


def generateIndividual():
    return [random.choice(list(functions.keys()))]
    # return [random.choice(list(functions.keys())) for i in range(random.randint(1, len(functions.keys())))]


creator.create("FitnessMin", base.Fitness, weights=(-1.0, -1.0, -1.0))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

toolbox.register("generateIndividual", generateIndividual)
toolbox.register("evalFitness", evalFitness)

toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.generateIndividual, n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evalFitness)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)


def main():
    pop = toolbox.population(n=100)

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

        print("-- Generation %i --" % g)
        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))


        # Mate individuals
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values


        # Mutate individuals
        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values


        # Evaluate invalid individuals
        invalid_fit = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_fit)

        for ind, fit in zip(invalid_fit, fitnesses):
            ind.fitness.values = fit

        pop[:] = offspring

        #fits = [ind.fitness for ind in pop]

    best = pop[np.argmin([toolbox.evaluate(ind) for ind in pop])]
    return best

run = True

if run:
    score = main()
    print(score)
    print(evalFitness(score))

print(evalFitness(['title']))
print(apply(['title']))

print(evalFitness(['strip', 'title']))
print(apply(['strip', 'title']))




