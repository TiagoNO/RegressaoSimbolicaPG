from Configuration import Configuration
from Operators import Operations

import random

class NodeTypes:
    NUM_NODES_TYPES = 3
    OPERATION_NODE_TYPE = 0
    VARIABLE_NODE_TYPE = 1
    CONST_NODE_TYPE = 2

class Tree_node:

    def __init__(self):
        self.level = 0
        self.left = None
        self.right = None
        self.depht = 0
        
    def recalculate_level(self,level):
        self.level = 0

    def get_depht(self):
        return 0.0

    def get_value(self):
        return 0.0

class Operation_node( Tree_node ):

    def __init__(self,level):
        self.left = None
        self.right = None
        self.operation = None
        self.type = NodeTypes.OPERATION_NODE_TYPE
        self.level = level            

    def recalculate_level(self,level):
        self.level = level
        if self.right != None:
            self.right.recalculate_level(self.level+1)
        if self.left != None:
            self.left.recalculate_level(self.level+1)

    def get_depht(self):
        right_depht = 0
        left_depht = 0
        if self.right != None:
            right_depht = self.right.get_depht() 
        if self.left != None:
            left_depht = self.left.get_depht()
        return 1 + max(right_depht,left_depht)

    def __str__(self):
        if self.operation.get_num_op() == 1:
            return "[{}]".format(self.level) + " " + self.operation.string_representation().format(str(self.left))
        else:
            return "[{}]".format(self.level) + " " + self.operation.string_representation().format(str(self.left),str(self.right))

    def get_value(self,variable_values):
        left_value = 0.0
        right_value = 0.0

        if self.operation.get_num_op() == 1:
            if self.left != None:
                left_value = self.left.get_value(variable_values)
            return self.operation.do_operation((left_value,0.0))
        else:
            if self.left != None:
                left_value = self.left.get_value(variable_values)
            if self.right != None:
                right_value = self.right.get_value(variable_values)
            return self.operation.do_operation((left_value,right_value))



class Variable_node( Tree_node ):

    def __init__(self,num_variable,level):
        self.type = NodeTypes.VARIABLE_NODE_TYPE
        self.level = level
        self.num_variable = num_variable
        self.num_nodes = 0
        self.left = None
        self.right = None

    def recalculate_level(self,level):
        self.level = level

    def get_depht(self):
        return 0.0

    def __str__(self):
        return "[{}]".format(self.level)  + " " +  "x" + str(self.num_variable)

    def get_value(self,variables_values):
        return variables_values[self.num_variable - 1]


class Const_node( Tree_node ):

    def __init__(self,level,value=0):
        self.type = NodeTypes.CONST_NODE_TYPE
        self.value = random.random()
        self.level = level
        self.num_nodes = 0
        self.left = None
        self.right = None
        #print "Initializating contant node!"

    def recalculate_level(self,level):
        self.level = level

    def get_depht(self):
        return 0.0

    def __str__(self):
        return "[{}]".format(self.level) + " " + str(self.value)

    def get_value(self,variable_values):
        return self.value

class Tree_Operations:

    @staticmethod
    def get_random_full_node(num_variables,level,max_level=None):
        if max_level == None:
            max_level = Configuration.get_max_tree_level()
        #random.seed()
        
        if level < max_level: 
            new_node = Operation_node(level)
            new_node.operation = Operations.get_random_operation()
        else:
            random_node_type = random.randint(0,NodeTypes.CONST_NODE_TYPE)
            if random_node_type <= NodeTypes.VARIABLE_NODE_TYPE:
                new_node = Variable_node(random.randint(0,num_variables - 1),level)
            else:
                new_node = Const_node(level)
        return new_node

    @staticmethod
    def get_random_node(num_variables,level,max_level=None):
        if max_level == None:
            max_level = Configuration.get_max_tree_level()
        #random.seed()

        # probability that gets lower when its deeper in the tree
        op_probability = float(max_level) - float(level) 
        e = random.randint(1,max_level)
        # probability that gets lower when its deeper in the tree

        if e <= op_probability: 
            new_node = Operation_node(level)
            new_node.operation = Operations.get_random_operation()
        else:
            random_node_type = random.randint(0,NodeTypes.CONST_NODE_TYPE)
            if random_node_type <= NodeTypes.VARIABLE_NODE_TYPE:
                new_node = Variable_node(random.randint(0,num_variables - 1),level)
            else:
                new_node = Const_node(level)

        return new_node


    @staticmethod
    def get_copy(tree):
        if tree == None:
            return None

        elif tree.type == NodeTypes.OPERATION_NODE_TYPE:
            new_tree = Operation_node(tree.level)
            new_tree.operation = tree.operation
            new_tree.left = Tree_Operations.get_copy(tree.left)
            new_tree.right = Tree_Operations.get_copy(tree.right)
            return new_tree
        elif tree.type == NodeTypes.VARIABLE_NODE_TYPE:
            new_tree = Variable_node(tree.num_variable,tree.level)
            new_tree.left = None
            new_tree.right = None
            return new_tree

        elif tree.type == NodeTypes.CONST_NODE_TYPE:
            new_tree = Const_node(tree.level,tree.value)
            new_tree.num_nodes = tree.num_nodes
            new_tree.value = tree.value
            new_tree.left = None
            new_tree.right = None
            return new_tree

    @staticmethod
    def select_random_node(node,level=0,min_level=0,max_depht=None):
        if max_depht == None:
            max_depht = Configuration.get_max_tree_level()
    
        iterator = node
        parent = node
        while 1:
            
            if  iterator.get_depht() < max_depht and iterator.level + 1 > Configuration.get_max_tree_level() - level:
                return (parent,iterator)

            elif  iterator.get_depht() < max_depht and random.random() <= float(level)/float(Configuration.get_max_tree_level()):
                return (parent,iterator)

            elif iterator.left == None and iterator.right == None:
                return (parent,iterator)

            elif iterator.left == None:
                parent = iterator
                iterator = iterator.right

            elif iterator.right == None:
                parent = iterator
                iterator = iterator.left

            else:
                left_side = random.randint(0,1)
                if left_side:
                    parent = iterator
                    iterator = iterator.left
                else:
                    parent = iterator
                    iterator = iterator.right
                continue


    @staticmethod
    def linearize_tree(individual):
        closed_node_list = []
        open_node_list = [(individual,individual)]
        while len(open_node_list) != 0:
            node = open_node_list.pop(0)
            closed_node_list.append(node)

            if node[1].left != None:
                open_node_list.append((node[1],node[1].left))
            if node[1].right != None:
                open_node_list.append((node[1],node[1].right))
        return closed_node_list


    @staticmethod
    def get_child_nodes(nodes):
        child_nodes = []
        for i in nodes:
            if i[1].left != None:
                child_nodes.append((i[1],i[1].left))
            if i[1].right != None:
                child_nodes.append((i[1],i[1].right))
        return child_nodes