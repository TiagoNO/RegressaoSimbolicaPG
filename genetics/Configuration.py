
class Configuration:
    configuration_file_name = "genetics/default_configuration.txt"
    mutation_rate = 0.0
    tournament_group_size = 1
    max_tree_level = 1
    num_generations = 100
    population_size = 10

    @staticmethod
    def read_configuration_file(configuration_file_name="no_file"):
        if configuration_file_name == "no_file":
            configuration_file = open(Configuration.configuration_file_name,"r")
        else:
            configuration_file = open(configuration_file_name,"r")                    
            Configuration.configuration_file_name = configuration_file_name

        for line in configuration_file.readlines():
            if line.split()[0] == "population_size":
                Configuration.population_size = int(line.split()[1])

            if line.split()[0] == "mutation_rate":
                Configuration.mutation_rate = float(line.split()[1])
            
            if line.split()[0] == "tournament_group_size":
                Configuration.tournament_group_size = int(line.split()[1])
            
            if line.split()[0] == "max_tree_level":
                Configuration.max_tree_level = int(line.split()[1])
            
            if line.split()[0] == "num_generations":
                Configuration.num_generations = int(line.split()[1])
        configuration_file.close()

    @staticmethod
    def get_population_size():
        return Configuration.population_size

    @staticmethod
    def get_num_generations():
        return Configuration.num_generations

    @staticmethod
    def get_mutation_rate():
        return Configuration.mutation_rate
    
    @staticmethod
    def get_tournament_group_size():
        return Configuration.tournament_group_size

    @staticmethod
    def get_max_tree_level():
        return Configuration.max_tree_level