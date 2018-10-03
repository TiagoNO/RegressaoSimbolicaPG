from Individual import Population
from Configuration import Configuration
from Operators import Operations
from Tree import Tree_Operations

import random


class Mutation:

    @staticmethod
    def mutate_individual(individual,num_variables):
        #random.seed()
        node = Tree_Operations.select_random_node(individual,individual.level)
        if random.randint(0,1):
            if node[0].left is node[1]:
                del node[0].left
                node[0].left = Population.generate_random_individual(num_variables,False,node[0].level + 1,Configuration.get_max_tree_level() - node[1].level - 1)
            else:
                del node[0].right
                node[0].right = Population.generate_random_individual(num_variables,False,node[0].level + 1,Configuration.get_max_tree_level() - node[1].level - 1)    