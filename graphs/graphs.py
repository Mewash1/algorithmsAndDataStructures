import sys
from heap.d_ary_heap import Heap
from read_file import read_nodes_from_file

def calculate_distance_and_predecessor_for_each_node(nodes, line_length):
    
    nodes_for_heap = nodes.copy()
    nodes_heap = Heap(4, nodes_for_heap)

    while len(nodes_heap) != 0:
        min_node = nodes_heap.pop()
        if min_node.end:
            return nodes
        neighbours = generate_neighbours(min_node, nodes, line_length)

        for neighbour in neighbours:
            if neighbour:
                if neighbour.distance > min_node.distance + neighbour.enter_cost:
                    neighbour.distance = min_node.distance + neighbour.enter_cost
                    neighbour.predecessor = min_node.index
        nodes_heap = Heap(4, nodes_for_heap)
        

def generate_neighbours(min_node, nodes, line_length):
    neighbours = [None, None, None, None]

    # right neighbour
    if (min_node.index + 1) % line_length != 0:
        try:
            neighbours[0] = nodes[min_node.index + 1]
        except IndexError:
            pass
    
    # left neighbour
    if (min_node.index) % line_length != 0 and min_node.index - 1 >= 0:
        try:
            neighbours[1] = nodes[min_node.index - 1]
        except IndexError:
            pass

    # upper neighbour
    if min_node.index - line_length >= 0:
        try:
            neighbours[2] = nodes[min_node.index - line_length]
        except IndexError:
            pass
    
    # bottom neighbour
    try:
        neighbours[3] = nodes[min_node.index + line_length]
    except IndexError:
        pass
    
    return neighbours

def shortest_path(nodes):
    shortest_path_set = set()
    pre_node = None
    for node in nodes:
        if node.end:
            node.enter_cost = 0
            pre_node = node
            break

    while True:
        shortest_path_set.add(pre_node.index)
        pre_node = nodes[pre_node.predecessor]
        if pre_node.enter_cost == 0:
            shortest_path_set.add(pre_node.index)
            break
    return shortest_path_set

def generate_path_on_board(board, shortest_path_set):
    i = 0
    final_board = ""
    for char in board:
        if char != "\n":
            if i in shortest_path_set:
                final_board += char
            else:
                final_board += " "
            i += 1
        else:
            final_board += char
    return final_board

if __name__ == "__main__":
    filename = sys.argv[1]
    nodes, board, line_length = read_nodes_from_file(filename)
    if len(nodes) != 0:
        calculate_distance_and_predecessor_for_each_node(nodes, line_length)
        shortest_path_set = shortest_path(nodes)
        final_board = generate_path_on_board(board, shortest_path_set)
        print(final_board)