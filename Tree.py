from Operators import *
import random

MAX_LEVEL = 7
num_nodes_type = 3

OPERATION_NODE_TYPE = 0
VARIABLE_NODE_TYPE = 1
CONST_NODE_TYPE = 2

def get_random_node(num_variables,level):
    op_probability = float(MAX_LEVEL) - float(level) 
    e = random.randint(0,MAX_LEVEL)
    # probability that gets lower when its deeper in the tree
    
    if e <= op_probability: 
        new_node = Operation_node(level)
        new_node.operation = get_random_operation()
    else:
        random_node_type = random.randint(0,CONST_NODE_TYPE)
        if random_node_type <= VARIABLE_NODE_TYPE:
            new_node = Variable_node(random.randint(0,num_variables - 1),level)
        else:
            new_node = Const_node(level)

    return new_node

class Tree_node:

    def __init__(self):
        self.level = 0
        #print "initializating tree node!"

    def get_value(self):
        return 0

class Operation_node( Tree_node ):

    def __init__(self,level):
        self.left = None
        self.right = None
        self.operation = None
        self.type = OPERATION_NODE_TYPE
        self.level = level
        #print "Initializating operation node!"

    def printk(self):
        print str(self.type) + " ",
        if self.left != None:
            self.left.printk()
        if self.right != None:
            self.right.printk()

    def get_value(self,variable_values):
        left_value = 0.0
        right_value = 0.0

        if self.left != None:
            right_value = self.left.get_value(variable_values)
        if self.right != None:
            left_value = self.right.get_value(variable_values)

        return self.operation.do_operation((left_value,right_value))

class Variable_node( Tree_node ):

    def __init__(self,num_variable,level):
        self.type = VARIABLE_NODE_TYPE
        self.level = level
        self.num_variable = num_variable
        #print "Initializating variable node!"

    def printk(self):
        print str(self.type) + "|",

    def get_value(self,variables_values):
        return variables_values[self.num_variable]


class Const_node( Tree_node ):

    def __init__(self,level,value=random.randint(0,1000)):
        self.type = CONST_NODE_TYPE
        self.value = value
        self.level = level
        #print "Initializating contant node!"

    def printk(self):
        print str(self.type) + "|",

    def get_value(self,variable_values):
        return self.value

