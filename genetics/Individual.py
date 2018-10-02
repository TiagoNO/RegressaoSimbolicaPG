from Operators_config import * 
from Tree import *
import math

def generate_random_population(num_ind,num_variables):
    random.seed()
    initial_population = []
    for i in xrange(num_ind):
        if i >= num_ind/2:
            initial_population.append(generate_random_individual(num_variables,True))
        else:
            initial_population.append(generate_random_individual(num_variables,False))
    return initial_population

def generate_random_individual(num_variables,full,max_tree_level=MAX_LEVEL):
    random.seed()
    root = get_random_node(num_variables,1)
    max_depht = 0
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        if node.level > max_depht:
            max_depht = node.level
        if node.type == OPERATION_NODE_TYPE:
            if full:
                node.left = get_random_full_node(num_variables,node.level+1)
            else:
                node.left = get_random_node(num_variables,node.level+1)                
            stack.append(node.left)

            if node.operation.get_num_op() == 2:

                if full:
                    node.right = get_random_full_node(num_variables,node.level+1)
                else:
                    node.right = get_random_node(num_variables,node.level+1)                
                stack.append(node.right)

        if node.level + 1 > max_tree_level:
            continue
    root.max_depht = max_depht
    return root

def eval_population(population,x_values,y_values):
    fitness_values = []
    for i in xrange(len(population)):
        fitness_values.append(calculate_fitness(population[i],x_values,y_values))
    return fitness_values

def calculate_fitness(individual,x_values,y_values):
    A = 0.0
    B = 0.0
    avarege = 0.0
    for i in xrange(len(x_values)):
        ind_value = individual.get_value(x_values[i])
        A += math.pow(y_values[i] - ind_value,2)
        avarege += y_values[i]
    avarege/len(y_values)

    for i in xrange(len(y_values)):
        B += math.pow(y_values[i] - avarege,2)

    return math.sqrt(A/B)