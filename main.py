import genetics
from data_reader import DataReader
import random
import sys

#sys.setrecursionlimit(999999)

random.seed()

data = DataReader("datasets/concrete/concrete-test.csv")
data.read_data()

x_values = data.get_x_values()
y_values = data.get_y_values()
num_variables = data.get_num_variables()

simbolic_genetics = genetics.Genetics("concrete-test.csv")
simbolic_genetics.generate_initial_population(len(x_values[0]))
simbolic_genetics.run_genetic(x_values,y_values)