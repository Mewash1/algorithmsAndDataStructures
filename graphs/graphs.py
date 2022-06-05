from heap.d_ary_heap import Heap
from read_file import read_nodes_from_file

def calculate_distance_and_predecessor_for_each_node(nodes, line_length):
    
    nodes_for_heap = nodes.copy()
    nodes_heap = Heap(4, nodes_for_heap)

    while len(nodes_heap.get_raw_data()) != 0:
        min_node = nodes_heap.pop()
        neighbours = []
        try:
            if (min_node.index + 1) % line_length != 0:
                right_neighbour = nodes[min_node.index + 1]
            else:
                right_neighbour = None
        except IndexError:
            right_neighbour = None
        try:
            if (min_node.index) % line_length != 0 and min_node.index - 1 >= 0:
                left_neighbour = nodes[min_node.index - 1]
            else:
                left_neighbour = None
        except IndexError:
            left_neighbour = None
        try:
            if min_node.index - line_length >= 0:
                upper_neighbour = nodes[min_node.index - line_length]
            else:
                upper_neighbour = None
        except IndexError:
            upper_neighbour = None
        try:
            bottom_neighbour = nodes[min_node.index + line_length]
        except IndexError:
            bottom_neighbour = None

        neighbours = [right_neighbour, left_neighbour, upper_neighbour, bottom_neighbour]
        for neighbour in neighbours:
            if neighbour:
                if neighbour.distance > min_node.distance + neighbour.enter_cost:
                    neighbour.distance = min_node.distance + neighbour.enter_cost
                    neighbour.predecessor = min_node.index
                    nodes_heap = Heap(4, nodes_for_heap)
    
    return nodes

def shortest_path(nodes):
    shortest_path_list = set()
    for node in nodes:
        if node.end:
            node.enter_cost = 0
            pre_node = node
            break

    while True:
        shortest_path_list.add(pre_node.index)
        pre_node = nodes[pre_node.predecessor]
        if pre_node.enter_cost == 0:
            shortest_path_list.add(pre_node.index)
            break
    return shortest_path_list

def generate_path_on_board(board, shortest_path_list):
    i = 0
    final_board = ""
    for char in board:
        if char != "\n":
            if i in shortest_path_list:
                final_board += char
            else:
                final_board += " "
            i += 1
        else:
            final_board += char
    return final_board

if __name__ == "__main__":
    filename = "/home/miloszun/AISDI/aisdi/graphs/graf4.txt"
    nodes, board, line_length = read_nodes_from_file(filename)
    calculate_distance_and_predecessor_for_each_node(nodes, line_length)
    shortest_path_list = shortest_path(nodes)
    final_board = generate_path_on_board(board, shortest_path_list)

    print(final_board)
