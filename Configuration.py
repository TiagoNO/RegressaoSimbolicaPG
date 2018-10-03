
class Configuration:

    def __init__(self,file_name="default_configuration.txt"):
        self.configuration_file_name = file_name
        self.mutation_rate = 0.0
        self.tournament_group_size = 1
        self.max_tree_level = 1
        self.num_generations = 100
        self.read_configuration_file()

    def read_configuration_file(self):
        configuration_file = open(self.configuration_file_name,"r")
        for line in configuration_file.readlines():
            if line.split()[0] == "mutation_rate":
                self.mutation_rate = float(line.split()[1])
            if line.split()[0] == "tournament_grou_size":
                self.tournament_group_size = int(line.split()[1])
            if line.split()[0] == "max_tree_level":
                self.max_tree_level = int(line.split()[1])
            if line.split()[0] == "num_generations":
                self.num_generations = int(line.split()[1])
        configuration_file.close()

    def get_num_generations(self):
        return self.num_generations

    def get_mutation_rate(self):
        return self.mutation_rate

    def get_tournament_group_size(self):
        return self.tournament_group_size

    def get_max_tree_level(self):
        return self.max_tree_level