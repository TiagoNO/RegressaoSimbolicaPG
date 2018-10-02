import random
from Operators_config import *
import math

class Operation:

    def get_num_op(self):
        return self.num_operators

    def __init__(self):
        self.num_operators = 0

    def do_operation(self,values):
        print "Doing operation..."

class Operation_sum ( Operation ):

    def __init__(self):
        self.num_operators = 2

    def string_representation(self):
        return "( {} + {} )"

    def do_operation(self,values):
        return values[0] + values[1]
    
class Operation_sub ( Operation ):

    def __init__(self):
        self.num_operators = 2

    def string_representation(self):
        return "( {} - {} )"

    def do_operation(self,values):
        return values[0] - values[1]

class Operation_mul ( Operation ):

    def __init__(self):
        self.num_operators = 2

    def string_representation(self):
        return "( {} * {} )"

    def do_operation(self,values):
        return values[0] * values[1]

class Operation_div ( Operation ):

    def __init__(self):
        self.num_operators = 2

    def string_representation(self):
        return "( {} / {} )"

    def do_operation(self,values):
        if values[1] != 0:
            return values[0] / values[1]
        else:
            return 0.0

class Operation_sin ( Operation ):

    def __init__(self):
        self.num_operators = 1

    def string_representation(self):
        return "( sin({}) )"

    def do_operation(self,values):
        return math.sin(float(values[0]))

class Operation_cos ( Operation ):

    def __init__(self):
        self.num_operators = 1

    def string_representation(self):
        return "( cos({}) )"

    def do_operation(self,values):
        return math.cos(float(values[0]))

#class Operation_pow ( Operation ):
#
#    def __init__(self):
#        self.num_operators = 2
#
#    def string_representation(self):
#        return "( {} ^ {} )"
#
#    def do_operation(self,values):
#        return values[0]**values[1]

class Operation_sqrt ( Operation ):

    def __init__(self):
        self.num_operators = 1

    def string_representation(self):
        return "( sqrt({}) )"

    def do_operation(self,values):
        return math.sqrt(math.fabs(float(values[0])))

class Operation_log ( Operation ):

    def __init__(self):
        self.num_operators = 1

    def string_representation(self):
        return "( log_e({}) )"

    def do_operation(self,values):
        if values[0] == 0:
            return 0.0
        else:
            return math.log( math.fabs( float( values[0] ) ) )

class Operation_abs ( Operation ):

    def __init__(self):
        self.num_operators = 1

    def string_representation(self):
        return "( |{}| )"

    def do_operation(self,values):
        return math.fabs(float(values[0]))

operations_list = [Operation_sum(),Operation_sub(),Operation_mul(),Operation_div()
                    ,Operation_sqrt(),Operation_abs(),Operation_log(),Operation_cos()
                    ,Operation_sin()]

def get_random_operation():
    random.seed()
    operation_selected = random.randint(0,NUM_OPERATIONS - 1)
    return operations_list[operation_selected]

def get_operation(operation_id):
    return operations_list[operation_id]

def rand_operation_id():
    return random.randint(1,NUM_OPERATIONS)


