import genetics
from data_reader import DataReader
import random
import sys

def avarege(fitness_values):
    min_fit = float("inf")
    max_fit = float("-inf")
    avarege = 0.0
    for i in fitness_values:
        if min_fit > i:
            min_fit = i
        if max_fit < i:
            max_fit = i
        avarege += i
    return (max_fit,min_fit,avarege/(len(fitness_values)))

sys.setrecursionlimit(999999)

random.seed()

data = DataReader("datasets/concrete/concrete-test.csv")
data.read_data()

x_values = data.get_x_values()
y_values = data.get_y_values()
num_variables = data.get_num_variables()


population = genetics.generate_random_population(20,num_variables)

print "---------------------"
for i in xrange(0,1001):
    fitness_values = genetics.eval_population(population,x_values,y_values)
    statics = avarege(fitness_values)
    if i%20 == 0:
        print "============={}==================".format(i)
        print "Population size:",len(population)
        print "Population:"
        for i in xrange(len(population)):
#            if population[i].get_depht() > genetics.MAX_LEVEL:
                print i,population[i].get_depht()#population[i],
        print "End Population"
        print "Max:{}\nMin:{}\nAvarege:{}".format(statics[0],statics[1],statics[2])
        print "================================"
    population = genetics.select_population(population,fitness_values,x_values,y_values)
