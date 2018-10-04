from Tree import *
from Genetic_Operations import *
from Individual import *
from Operators import *
from Logger import Logger
from Configuration import Configuration
from Genetics_Exceptions import *


class Genetics:

    def __init__(self,experiment_file_name,configuration_file_name="no_file"):
        Configuration.read_configuration_file(configuration_file_name)
        print "====================="
        print "Configurations:"
        print "Population size: {}".format(Configuration.get_population_size())
        print "Num generations: {}".format(Configuration.get_num_generations())
        print "Max tree level:  {}".format(Configuration.get_max_tree_level())
        print "Mutation rate:   {}".format(Configuration.get_mutation_rate())
        print "Tournament size: {}".format(Configuration.get_tournament_group_size())
        print "====================="
        self.log = Logger(experiment_file_name.split("/")[-1],configuration_file_name.split("/")[-1])
        self.last_fitness = None
        self.population = None
        self.generation = 0
#        print Configuration.get_max_tree_level()

    def generate_initial_population(self,num_variables,recover_population_file_name="no_file"):
        if recover_population_file_name == "no_file":
            print "Creating new random initial population..."
            self.population = Population(Configuration.get_population_size(),num_variables)
        else:
            print "Trying to recover the population in file {}...".format(recover_population_file_name)
            self.population = Population(Configuration.population_size,num_variables,recover_population_file_name)


    def get_population_fitness(self,x_values,y_values):
        self.last_fitness = self.population.eval_population(self.population.get_population(),x_values,y_values)

    def run_genetic(self,x_values,y_values):
        if self.population == None:
            
            raise EmptyPopulation()
        else:
            for i in xrange(Configuration.get_num_generations()):
                self.get_population_fitness(x_values,y_values)
                if i%20 == 0:
                    self.log.write_fitness(self.last_fitness,i)
                    #self.log.write_population(self.population.get_population(),i)
                self.do_population_selection(x_values,y_values)

        self.log.save_population(self.population.get_population())
        self.log.close_files()
        self.on_end(x_values,y_values)

    def do_population_selection(self,x_values,y_values):
        self.population.update_population(Genetic_Operations.select_population(self.population.get_population(),self.last_fitness,x_values,y_values))

    def on_end(self,x_values,y_values):
        self.last_fitness = self.get_population_fitness(x_values,y_values)
        best_individual_index = 0
        for i in xrange(len(self.last_fitness)):
            if self.last_fitness[best_individual_index] > self.last_fitness[i]:
                best_individual_index = i

        print "Best final function:\n{}".format(self.population.get_population()[best_individual_index])
        print "Final fitness:\n{}".format(self.last_fitness[best_individual_index])