from deap import gp, creator, base, tools, algorithms
import operator
import modifiedFunctions

#pset = gp.PrimitiveSet("main", str, str)
pset = gp.PrimitiveSet("main", 1)

pset.addPrimitive(modifiedFunctions.strip, 1)
pset.addPrimitive(modifiedFunctions.lower, 1)
pset.addPrimitive(modifiedFunctions.title, 1)
pset.addPrimitive(modifiedFunctions.upper, 1)
pset.addPrimitive(modifiedFunctions.lstrip, 1)
pset.addPrimitive(modifiedFunctions.rstrip, 1)
pset.addPrimitive(modifiedFunctions.swapcase, 1)

creator.create("fitnessMin", base.Fitness, weights=(-1.0, -1.0, -1.0))
creator.create("individual", gp.PrimitiveTree, fitness=creator.fitnessMin)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=5)
toolbox.register("individual", tools.initIterate, creator.individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

def evalFitness(individual, startingStr=" ABC ", goal="abc"):
    funcs = toolbox.compile(expr=individual)

    result = funcs(startingStr)

    error = 0

    # Strings of different length = small error in error metric
    for transformed, ending in zip(result.strip(), goal.strip()):
        if transformed.isupper() and ending.islower():
            error += 1
        elif transformed.islower() and ending.isupper():
            error += 1
        elif transformed.isspace() and not ending.isspace():
            error += 1
        elif not transformed.isspace() and ending.isspace():
            error += 1
        
    return abs(len(ending) - len(result)), error, len(individual)
    

toolbox.register("evaluate", evalFitness)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=10))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=10))

pop = toolbox.population(n=100)
hof = tools.HallOfFame(3)
pop, log = algorithms.eaSimple(pop, toolbox, 0.5, 0.1, 40, stats=None, halloffame=hof, verbose=False)


print("Starting string:_ABC_ ")
print("Result:%s" %(toolbox.compile(hof[0])(" ABC ")))
print(hof[0])