import random

num_operations = 4
random.seed()

def get_random_operation():
    operation_selected = random.randint(1,num_operations)

    if operation_selected == 1:
        return Operation_sum()
    elif operation_selected == 2:
        return Operation_sub()
    elif operation_selected == 3:
        return Operation_mul()
    elif operation_selected == 4:
        return Operation_div()
    else:
        return Operation_sum()

def get_operation(operation_id):
    if operation_id == 1:
        return Operation_sum()
    elif operation_id == 2:
        return Operation_sub()
    elif operation_id == 3:
        return Operation_mul()
    elif operation_id == 4:
        return Operation_div()
    else:
        return Operation_sum()  

class Operation:

    def do_operation(self,values):
        print "Doing operation..."

class Operation_sum( Operation ):

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
        result = values[0] / values[1]
        return result

class Value ( Operation ):

    def __init__(self,value):
        self.value = value

    def do_operation(self):
        return self.value

class Tree_node:

    def __init__(self):
        self.left = None
        self.right = None
        self.operation = None
        print "initializating tree node!"

class Operation_node( Tree_node ):

    def __init__(self,operation_id):
        self.left = None
        self.right = None
        self.operation = 
        print "Initializating operation node!"

class Variable_node( Tree_node ):

    def __init__(self,value):
        self.left = None
        self.right = None
        self.operation = None
        print "Initializating variable node!"
