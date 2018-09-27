from Tree import *
import random

def generate_children(population,fitness_values):
    children = []
    
    gender = random.randint(0,1):
    if gender == 0:
        print "ITS A GIRL!!"
    if gender == 1:
        print "ITS A BOY!!"

    return children

def select_population(population,fitness_values):
    children = generate_children(popoulation,fitness_values)
    
    fitness_avarege = 0.0
    for f in fitness_values:
        fitness_values += f/len(fitness_values)

    