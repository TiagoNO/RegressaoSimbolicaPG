import random

num_operations = 4

SUM_OP = 0
SUB_OP = 1
MUL_OP = 2
DIV_OP = 3
LOG_OP = 4
POW_OP = 5
SQRT_OP = 6
SIN_OP = 7
COS_OP = 8
ABS_OP = 9

def get_random_operation():
    operation_selected = random.randint(0,num_operations - 1)

    if operation_selected == SUM_OP:
        return Operation_sum()
    elif operation_selected == SUB_OP:
        return Operation_sub()
    elif operation_selected == MUL_OP:
        return Operation_mul()
    elif operation_selected == DIV_OP:
        return Operation_div()
    else:
        return Operation_sum()

def get_operation(operation_id):
    if operation_id == SUM_OP:
        return Operation_sum()
    elif operation_id == SUB_OP:
        return Operation_sub()
    elif operation_id == MUL_OP:
        return Operation_mul()
    elif operation_id == DIV_OP:
        return Operation_div()
    else:
        return Operation_sum()  

def rand_operation_id():
    return random.randint(1,num_operations)


class Operation:

    def do_operation(self,values):
        print "Doing operation..."

class Operation_sum ( Operation ):

    def do_operation(self,values):
        result = values[0] + values[1]
        return result
    
class Operation_sub ( Operation ):

    def do_operation(self,values):
        result = values[0] - values[1]
        return result

class Operation_mul ( Operation ):

    def do_operation(self,values):
        result = values[0] * values[1]
        return result

class Operation_div ( Operation ):

    def do_operation(self,values):
        if values[1] != 0:
            result = values[0] / values[1]
            return result
        else:
            return 0
