import os
import pickle

class Logger:

    def __init__(self,experiment_name="default"):
        if not os.path.exists("logs/"):
            os.makedirs("logs/")
    
        i = 0
        while os.path.isfile('logs/{}_population_{}.txt'.format(experiment_name,i)):
            i += 1
        self.population_file_name = 'logs/{}_population_{}.txt'.format(experiment_name,i)
        i = 0
        while os.path.isfile('logs/{}_fitness_{}.txt'.format(experiment_name,i)):
            i += 1
        self.fitness_file_name = 'logs/{}_fitness_{}.txt'.format(experiment_name,i)

        i = 0
        while os.path.isfile('logs/{}_population_recovery_{}.txt.negri'.format(experiment_name,i)):
            i += 1
        self.population_recovery_file_name = 'logs/{}_population_recovery_{}.txt.negri'.format(experiment_name,i)

        self.population_file = open(self.population_file_name,"w")
        self.fitness_file = open(self.fitness_file_name,"w")
        self.population_recovery_file = open(self.population_recovery_file_name,"w")

    def get_imporant_fitness_values(self,fitness_values):
        min_fit = float("inf")
        max_fit = float("-inf")
        avarege = 0.0
        for i in fitness_values:
            if min_fit > i:
                min_fit = i
            if max_fit < i:
                max_fit = i
            avarege += i
        return (max_fit,min_fit,avarege/(len(fitness_values)))

    def write_fitness(self,fitness,generation):        
        self.fitness_file.write("---------- {} ----------\n".format(generation))
        self.fitness_file.write("generation_num {}\n".format(generation))
        fitness_str = ""
        for i in xrange(len(fitness)):
            fitness_str += "{} {}\n".format(i,fitness)
        self.fitness_file.write("fitness_values\n{}".format(fitness_str))
        self.fitness_file.write("end_fitness_values\n")
        self.fitness_file.write("------[end_generation {}]------\n".format(generation))

        important_values = self.get_imporant_fitness_values(fitness)
        print "========== {} ==========".format(generation)
        print "max_fit {}\n".format(important_values[0])
        print "min_fit {}\n".format(important_values[1])
        print "avarege_fit {}\n".format(important_values[2])
        print "======================\n"
        
    def write_population(self,population,generation):
        self.population_file.write("---------- {} ----------")
        for i in xrange(len(population)):
            self.population_file.write("{} ".format(i) + str(population[i]))           
        self.population_file.write("-------------------------")

    def save_population(self,population):
        pickle.dump(population,self.population_recovery_file)