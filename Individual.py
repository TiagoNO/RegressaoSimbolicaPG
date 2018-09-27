from Tree import *
import math

def generate_random_population(num_ind,num_variables):
    initial_population = []
    for i in xrange(num_ind):
        initial_population.append(generate_random_individual(num_variables))
    return initial_population

def generate_random_individual(num_variables):
    level = 0
    root = get_random_node(num_variables,level)
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        if node.level >= MAX_LEVEL:
            continue
        if node.type == OPERATION_NODE_TYPE:
            node.left = get_random_node(num_variables,node.level+1)
            node.right = get_random_node(num_variables,node.level+1)
            stack.append(node.left)
            stack.append(node.right)
    
    return root

def eval_population(population,x_values,y_values):
    fitness_values = []
    for ind in population:
        fitness_values.append(calculate_fitness(ind,x_values,y_values))
    return fitness_values

def calculate_fitness(individual,x_values,y_values):
    A = 0.0
    B = 0.0
    avarege = 0.0
    for i in xrange(len(x_values)):
        ind_value = individual.get_value(x_values[i])
        A += math.pow(y_values[i][0] - ind_value,2)
        avarege += (ind_value/len(x_values))

    for i in xrange(len(y_values)):
        B += math.pow(y_values[i][0] - avarege,2)

    return math.sqrt(A/B)