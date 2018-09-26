from Individual import *

initial_population = generate_random_population(100,3)
for i in xrange(len(initial_population)):
    print i,initial_population[i].printk(),"\n\n"