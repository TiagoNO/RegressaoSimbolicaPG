from Individual import *

x_values = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
y_values = [[2],[3],[4],[5],[6],[7],[8],[9],[10]]

initial_population = generate_random_population(100,1)

#for i in xrange(len(initial_population)):
#    print i,initial_population[i].printk(),"\n\n"

fitness_values = eval_population(initial_population,x_values,y_values)

