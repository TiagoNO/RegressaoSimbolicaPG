import os

class Logger:

    def __init__(self,experiment_name="default"):
        i = 0
        while os.path.isfile('logs/{}_population_{}.txt'.format(experiment_name,i)):
            i += 1
        self.population_file_name = 'logs/{}_population_{}.txt'.format(experiment_name,i)
        i = 0
        while os.path.isfile('logs/{}_fitness_{}.txt'.format(experiment_name,i)):
            i += 1
        self.fitness_file_name = 'logs/{}_fitness_{}.txt'.format(experiment_name,i)

        self.population_file = open(self.population_file_name,"w")
        self.fitness_file = open(self.fitness_file_name,"w")


    def write_fitness(self,fitness,num_generation,important_values):        
        self.fitness_file.write("------[begin_generation {}]------\n".format(num_generation))
        self.fitness_file.write("generation_num {}\n".format(num_generation))
        a = ""
        for i in xrange(len(fitness)):
            a += "[{}] {}\n".format(i,fitness)
        self.fitness_file.write("fitness_values\n{}".format(a))
        self.fitness_file.write("end_fitness_values\n")
        self.fitness_file.write("max_fit {}\n".format(important_values[0]))
        self.fitness_file.write("min_fit {}\n".format(important_values[1]))
        self.fitness_file.write("avarege_fit {}\n".format(important_values[2]))
        self.fitness_file.write("------[end_generation {}]------\n".format(num_generation))
        