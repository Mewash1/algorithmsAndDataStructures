from node import Node

def read_nodes_from_file(filename):
    with open(filename, 'r') as file:
        nodes = file.read()
        nodes_string = nodes.replace("\n", "")
        nodes_list = []
        line_length = len(nodes.split("\n")[0])
        has_been_zero = False
        for i, char in enumerate(nodes_string):
            end = False
            enter_cost = int(char)
            if enter_cost == 0 and has_been_zero:
                enter_cost = 1
                end = True
            if enter_cost == 0:
                has_been_zero = True
            nodes_list.append(Node(enter_cost, i, end))
    if not has_been_zero:
        raise ValueError("There are no zeroes in the input file!")
    if len(nodes_list) == 0:
        raise ValueError("The graph is empty!")
    for node in nodes_list:
        if node.end:
            return nodes_list, nodes, line_length
    raise ValueError("There is only one zero in the input file!")
       
