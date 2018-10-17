from Configuration import Configuration
from Tree import NodeTypes,Tree_Operations
import numpy as np
import random
import math
import pickle

class Population:

    def __init__(self,population_size,num_variables,recover_file_name="no_file"):
        if recover_file_name == "no_file":
            self.population = self.generate_random_population(population_size,num_variables)
        else:
            try:
                print "Recovering population...",
                self.recover_population(open(recover_file_name,"rb"))
                print "Population recovered!"
            except:
                print "ERROR: Could not recover population...Random population created..."
                self.population = self.generate_random_population(population_size,num_variables)

    def recover_population(self,recover_file_name):
        self.population = pickle.load(recover_file_name)

    def update_population(self,new_population):
        self.population = new_population

    def get_population(self):
        return self.population

    def get_best_individual(self,fitness_values):
        best_individual_index = 0
        for i in xrange(len(fitness_values)):
            if fitness_values[best_individual_index] > fitness_values[i]:
                best_individual_index = i
        return self.population[best_individual_index]

    @staticmethod
    def generate_random_individual(num_variables,full,initial_level=1,max_tree_level=Configuration.get_max_tree_level()):
        root = Tree_Operations.get_random_node(num_variables,initial_level)
        max_depht = 0
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node.level > max_depht:
                max_depht = node.level
            if node.type == NodeTypes.OPERATION_NODE_TYPE:
                if full:
                    node.left = Tree_Operations.get_random_full_node(num_variables,node.level+1)
                else:
                    node.left = Tree_Operations.get_random_node(num_variables,node.level+1)                
                stack.append(node.left)

                if node.operation.get_num_op() == 2:

                    if full:
                        node.right = Tree_Operations.get_random_full_node(num_variables,node.level+1)
                    else:
                        node.right = Tree_Operations.get_random_node(num_variables,node.level+1)                
                    stack.append(node.right)

            if node.level + 1 > max_tree_level:
                continue
        root.max_depht = max_depht
        return root

    @staticmethod
    def generate_random_population(num_ind,num_variables):
        initial_population = []
        for i in xrange(num_ind):
            if i >= num_ind/2:
                initial_population.append(Population.generate_random_individual(num_variables,True))
            else:
                initial_population.append(Population.generate_random_individual(num_variables,False))
        return initial_population

    @staticmethod
    def calculate_fitness(individual,x_values,y_values):
        A = 0.0
        B = 0.0
        avarege = 0.0

        avarege = np.mean(y_values)

        for i in xrange(len(x_values)):
            ind_value = individual.get_value(x_values[i])
            A += math.pow(y_values[i] - ind_value,2)
            B += math.pow(y_values[i] - avarege,2)
        return math.sqrt(A/B)

    @staticmethod
    def eval_population(population,x_values,y_values):
        fitness_values = []
        for i in xrange(len(population)):
            fitness_values.append(Population.calculate_fitness(population[i],x_values,y_values))
        return fitness_values

