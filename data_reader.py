
class DataReader:

    def __init__(self,input_file_name):
        self.input_file_name = input_file_name
        self.x_values = []
        self.y_values = []

    def read_data(self):
        input_file = open(self.input_file_name,"r")

        for line in input_file.readlines():
            self.x_values.append(line.split(",")[0:-1])
            self.y_values.append(float(line.split(",")[-1]))

        for i in xrange(len(self.x_values)):
            for j in xrange(len(self.x_values[i])):
                self.x_values[i][j] = float(self.x_values[i][j])

    def get_num_variables(self):
        return len(self.x_values[0])

    def get_x_values(self):
        return self.x_values

    def get_y_values(self):
        return self.y_values