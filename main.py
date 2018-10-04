import genetics
from data_reader import DataReader
import random
import sys
import argparse

#sys.setrecursionlimit(999999)

random.seed()

parser = argparse.ArgumentParser()

parser.add_argument("--config_file","-cf",type=str,help="configuration file",default="genetics/default_configuration.txt")
parser.add_argument("--data_file","-df",type=str,help="Data file",default="datasets/concrete/concrete-test.csv")

config_file = parser.parse_args().config_file
data_file = parser.parse_args().data_file

data = DataReader(data_file)
data.read_data()

x_values = data.get_x_values()
y_values = data.get_y_values()
num_variables = data.get_num_variables()

simbolic_genetics = genetics.Genetics(data_file.split("/")[-1])
simbolic_genetics.generate_initial_population(len(x_values[0]))
simbolic_genetics.run_genetic(x_values,y_values)