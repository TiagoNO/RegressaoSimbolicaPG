import genetics
from data_reader import DataReader
import random
import sys
import argparse

#sys.setrecursionlimit(999999)

random.seed()

parser = argparse.ArgumentParser()

parser.add_argument("--config_file","-cf",type=str,help="configuration file",default="genetics/default_configuration.txt")
parser.add_argument("--train_file","-tf",type=str,help="Training data file",default=None)
parser.add_argument("--data_file","-df",type=str,help="Data file",default=None)
parser.add_argument("--population","-p",type=str,help="Population to be used or recovered (.negri extension)",default=None)



config_file = parser.parse_args().config_file
training_data_file = parser.parse_args().train_file
data_file = parser.parse_args().data_file
population_file = parser.parse_args().population

if training_data_file == None:
    data = DataReader(data_file)
    data.read_data()

    x_values = data.get_x_values()
    y_values = data.get_y_values()
    num_variables = data.get_num_variables()

    simbolic_genetics = genetics.Genetics(data_file,config_file)

    if population_file == None:
        simbolic_genetics.generate_initial_population(len(x_values[0]))
    else:
        simbolic_genetics.generate_initial_population(len(x_values[0]),population_file)
    simbolic_genetics.run_genetic(x_values,y_values)
else:
    training_data = DataReader(training_data_file)
    training_data.read_data()

    train_x_values = training_data.get_x_values()
    train_y_values = training_data.get_y_values()
    train_num_variables = training_data.get_num_variables()
    
    data = DataReader(data_file)
    data.read_data()
    x_values = data.get_x_values()
    y_values = data.get_y_values()

    simbolic_genetics = genetics.Genetics(training_data_file,config_file)
    if population_file == None:
        simbolic_genetics.generate_initial_population(len(train_x_values[0]))
    else:
        simbolic_genetics.generate_initial_population(len(train_x_values[0]),population_file)
    simbolic_genetics.run_genetic(train_x_values,train_y_values)
    simbolic_genetics.change_log_files(data_file,config_file)
    simbolic_genetics.run_genetic(x_values,y_values)


