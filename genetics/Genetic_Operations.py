import random
from Genetic_Operations_config import *
import copy
from Mutation_config import MUTATION_RATE
from Mutation import *
from Tree import get_child_nodes,select_random_node,get_copy,linearize_tree
from Individual import eval_population

def cross_over(parents):
    if len(parents) == 1:
        return [parents[0][0]]
    child_A = get_copy(parents[0][0])
    child_B = get_copy(parents[1][0])

    node_A = select_random_node(child_A,0)
    node_B = select_random_node(child_B,node_A[0].get_depht())


    if node_A[0].left is node_A[1]:
        node_A[0].left = node_B[1]
    else:
        node_A[0].right = node_B[1]

    if node_B[0].left is node_B[1]:
        node_B[0].left = node_A[1]
    else:
        node_B[0].right = node_A[1]

    child_A.recalculate_level(1)
    child_B.recalculate_level(1)

    return [child_A,child_B]
    

def get_best_parent_index(parents):
    if len(parents) == 1:
        return 0
    else:
        if parents[0][1] < parents[1][1]:
            return 0
        else:
            return 1

def better_than_parents(parents,child_fitness):
    for i in parents:
        if child_fitness > i[1]:
            return False
    return True

def compare_family(parents,children,x_values,y_values):
    children_fitness = eval_population(children,x_values,y_values)
    who_pass = []
    while len(children_fitness) != 0:
        child_avaliated = children.pop(0)
        child_avaliated_fitness = children_fitness.pop(0)

        if better_than_parents(parents,child_avaliated_fitness):
            who_pass.append(child_avaliated)
            del child_avaliated
        else:
            index = get_best_parent_index(parents)
            who_pass.append(parents.pop(index)[0])
    return who_pass

def get_mutated_children(parents,x_values):
    first_child = get_copy(parents[0][0])
    if len(parents) > 1:
        second_child = get_copy(parents[1][0])
        mutate_individual(first_child,len(x_values[0]))
        mutate_individual(second_child,len(x_values[0]))
        return [first_child,second_child]
    elif len(parents) == 1:
        mutate_individual(first_child,len(x_values[0]))
        return [first_child]

def make_pairs(population):
    random.seed()
    pairs = []
    while len(population) > 1:
        father_index = random.randint(0,len(population) - 1)
        father = population.pop(father_index)
        mother_index = random.randint(0,len(population) - 1)
        mother = population.pop(mother_index)
        pairs.append([mother,father])
    if len(population) == 1:
        pairs.append([population.pop(0)])

    return pairs

def generate_children(population,x_values,y_values):
    new_population = []
    parents = make_pairs(population)
    for i in parents:
        mutation_chance = random.random()
        if mutation_chance <= MUTATION_RATE:
            children = get_mutated_children(i,x_values)
            new_population += compare_family(i,children,x_values,y_values)
        else:
            children = cross_over(i)
            new_population += compare_family(i,children,x_values,y_values)
    return new_population

def run_tournament(group):
    first_place_index = 0

    for i in xrange(len(group)):
        if group[i][1] < group[first_place_index][1]:
            first_place_index = i        
    return group.pop(first_place_index)

def get_group(population,fitness_values,group_size):
    random.seed()
    group = []
    if len(population) < group_size:
        group_size = len(population)
    for i in xrange(group_size):
        index = random.randint(0,len(population) - 1)
        group.append([population.pop(index),fitness_values.pop(index)])
    return group

def get_cross_over_individual(cross_over_group,fitness_values):
    cross_over_selected = []
    refused = []
    while len(cross_over_group) != 0:
        group = get_group(cross_over_group,fitness_values,TOURNAMENT_GROUP_SIZE)
        winner = run_tournament(group)
        cross_over_selected.append(winner)
        for i in group:
            refused.append(i[0])
            fitness_values.append(i[1])
    return cross_over_selected,refused


def select_population(population,fitness_values,x_values,y_values):
    new_population = []
    while len(population) != 0:
        cross_over_group,population = get_cross_over_individual(population,fitness_values)
        new_population += generate_children(cross_over_group,x_values,y_values)#cross_over(cross_over_group[0],cross_over_group[1])

    return new_population
