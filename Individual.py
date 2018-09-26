from Tree import *

def generate_random_population(num_ind,num_variables):
    initial_population = []
    for i in xrange(num_ind):
        initial_population.append(generate_random_individual(num_variables))
    return initial_population

def generate_random_individual(num_variables):
    level = 0
    root = get_random_node(num_variables,level)
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        if node.level >= MAX_LEVEL:
            continue
        if node.type == OPERATION_NODE_TYPE:
            node.left = get_random_node(num_variables,node.level+1)
            node.right = get_random_node(num_variables,node.level+1)
            stack.append(node.left)
            stack.append(node.right)
    
    return root
