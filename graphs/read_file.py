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
    return nodes_list, nodes, line_length            
