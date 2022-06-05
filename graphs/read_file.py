from node import Node

def read_nodes_from_file(filename):
    with open(filename, 'r') as file:
        nodes = file.read()
        nodes_list = []
        line_length = 0
        i = 0
        start = True
        for char in nodes:
            if char != "\n":
                line_length += 1
                if int(char) == 0 and start:
                    nodes_list.append(Node(int(char), i, False))
                    start = False
                elif int(char) == 0 and not start:
                    nodes_list.append(Node(1, i, True))
                else:
                    nodes_list.append(Node(int(char), i, False))
                i += 1
            else:
                line_length = 0
    return nodes_list, nodes, line_length            


if __name__ == "__main__":
    nodes_list = read_nodes_from_file("graf1.txt")[0]
    for node in nodes_list:
        print(node.enter_cost)