from Mutation import Mutation
from Individual import Population
from Configuration import Configuration
from Tree import Tree_Operations

import random

class Genetic_Operations:
    
    @staticmethod
    def cross_over(parents):
        if len(parents) == 1:
            return [parents[0][0]]
        child_A = Tree_Operations.get_copy(parents[0][0])
        child_B = Tree_Operations.get_copy(parents[1][0])

        node_A = Tree_Operations.select_random_node(child_A,0)
        node_B = Tree_Operations.select_random_node(child_B,0)

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
        

    @staticmethod
    def get_best_parent_index(parents):
        if len(parents) == 1:
            return 0
        else:
            if parents[0][1] < parents[1][1]:
                return 0
            else:
                return 1

    @staticmethod
    def better_than_parents(parents,child_fitness):
        for i in parents:
            if child_fitness > i[1]:
                return False
        return True

    @staticmethod
    def compare_family(parents,children,x_values,y_values):
        children_fitness = Population.eval_population(children,x_values,y_values)
        who_pass = []
        while len(children_fitness) != 0:
            child_avaliated = children.pop(0)
            child_avaliated_fitness = children_fitness.pop(0)

            if Genetic_Operations.better_than_parents(parents,child_avaliated_fitness):
                who_pass.append(child_avaliated)
                del child_avaliated
            else:
                index = Genetic_Operations.get_best_parent_index(parents)
                who_pass.append(parents.pop(index)[0])
        return who_pass

    @staticmethod
    def get_mutated_children(parents,x_values):
        first_child = Tree_Operations.get_copy(parents[0][0])
        if len(parents) > 1:
            second_child = Tree_Operations.get_copy(parents[1][0])
            Mutation.mutate_individual(first_child,len(x_values[0]))
            Mutation.mutate_individual(second_child,len(x_values[0]))
            return [first_child,second_child]
        elif len(parents) == 1:
            Mutation.mutate_individual(first_child,len(x_values[0]))
            return [first_child]

    @staticmethod
    def make_pairs(population):
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

    @staticmethod
    def generate_children(population,x_values,y_values):
        new_population = []
        parents = Genetic_Operations.make_pairs(population)
        for i in parents:
            mutation_chance = random.random()
            if mutation_chance <= Configuration.get_mutation_rate():
                children = Genetic_Operations.get_mutated_children(i,x_values)
                if Configuration.mutation_elitism:
                    new_population += Genetic_Operations.compare_family(i,children,x_values,y_values)
                else:
                    new_population += children
            else:
                children = Genetic_Operations.cross_over(i)
                if Configuration.cross_over_elitism:
                    new_population += Genetic_Operations.compare_family(i,children,x_values,y_values)                    
                else:
                    new_population += children
        return new_population

    @staticmethod
    def run_tournament(group):
        first_place_index = 0

        for i in xrange(len(group)):
            if group[i][1] < group[first_place_index][1]:
                first_place_index = i        
        return group.pop(first_place_index)

    @staticmethod
    def get_group(population,fitness_values,group_size):
        #random.seed()
        group = []
        if len(population) < group_size:
            group_size = len(population)
        for i in xrange(group_size):
            index = random.randint(0,len(population) - 1)
            group.append([population.pop(index),fitness_values.pop(index)])
        return group

    @staticmethod
    def get_cross_over_individual(cross_over_group,fitness_values):
        cross_over_selected = []
        refused = []
        while len(cross_over_group) != 0:
            group = Genetic_Operations.get_group(cross_over_group,fitness_values,Configuration.get_tournament_group_size())
            winner = Genetic_Operations.run_tournament(group)
            cross_over_selected.append(winner)
            for i in group:
                refused.append(i[0])
                fitness_values.append(i[1])
        return cross_over_selected,refused


    @staticmethod
    def select_population(population,fitness_values,x_values,y_values):
        new_population = []
        while len(population) != 0:
            cross_over_group,population = Genetic_Operations.get_cross_over_individual(population,fitness_values)
            new_population += Genetic_Operations.generate_children(cross_over_group,x_values,y_values)

        return new_population
