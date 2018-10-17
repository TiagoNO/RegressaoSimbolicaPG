import random
import math

class OperationTypes:
    NUM_OPERATIONS = 9
    SUM_OP = 0
    SUB_OP = 1
    MUL_OP = 2
    DIV_OP = 3
    SQRT_OP = 4
    ABS_OP = 5
    LOG_OP = 6
    COS_OP = 7
    SIN_OP = 8

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


class Operations:

    operations_list = [Operation_sum(),Operation_sub(),Operation_mul(),Operation_div()
                    ,Operation_sqrt(),Operation_abs(),Operation_log(),Operation_cos()
                    ,Operation_sin()]

    @staticmethod
    def get_random_operation():
        #random.seed()
        operation_selected = random.randint(0,OperationTypes.NUM_OPERATIONS - 1)
        return Operations.operations_list[operation_selected]

    @staticmethod
    def get_operation(operation_id):
        return Operations.operations_list[operation_id]

    @staticmethod
    def rand_operation_id():
        return random.randint(1,OperationTypes.NUM_OPERATIONS)


