from Mutation_config import *
from Tree_config import MAX_LEVEL,OPERATION_NODE_TYPE,CONST_NODE_TYPE,VARIABLE_NODE_TYPE
from Tree import select_random_node,get_random_node
from Operators import get_random_operation
from Individual import generate_random_individual
import random



def mutate_individual(individual,num_variables):
    random.seed()
    node = select_random_node(individual,individual.level)
    if random.randint(0,1):
        if node[0].left is node[1]:
            del node[0].left
            node[0].left = generate_random_individual(num_variables,False,node[0].level + 1,MAX_LEVEL - node[1].level - 1)
        else:
            del node[0].right
            node[0].right = generate_random_individual(num_variables,False,node[0].level + 1,MAX_LEVEL - node[1].level - 1)    