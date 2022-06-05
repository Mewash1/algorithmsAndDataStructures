from asyncore import read
from node import Node

def read_nodes_from_file(filename):
    with open(filename, 'r') as file:
        nodes = file.read()
        nodes_list = []
        line_length = 0
        for char in nodes:
            if char != "\n":
                line_length += 1
                nodes_list.append(Node(int(char)))
            else:
                line_length = 0
    return nodes_list, nodes, line_length            


if __name__ == "__main__":
    nodes_list = read_nodes_from_file("graf1.txt")[0]
    for node in nodes_list:
        print(node.enter_cost)