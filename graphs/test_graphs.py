from read_file import read_nodes_from_file
from graphs import calculate_distance_and_predecessor_for_each_node, shortest_path
import pytest


def test_read_file():
    filename = "inputs/graf2.txt"
    nodes, board, line_length = read_nodes_from_file(filename)
    assert line_length == 3
    entry_costs = [1,1,0,1,2,1]
    for i, node in enumerate(nodes):
        assert node.enter_cost == entry_costs[i]

def test_read_file_1_zero():
    filename = "inputs/one_zero_graph.txt"
    with pytest.raises(ValueError):
        nodes, board, line_length = read_nodes_from_file(filename)

def test_read_file_no_zero():
    filename = "inputs/no_zero_graph.txt"
    with pytest.raises(ValueError):
        nodes, board, line_length = read_nodes_from_file(filename)

def test_read_empty_file():
    filename = "inputs/empty_graph.txt"
    with pytest.raises(ValueError):
        nodes, board, line_length = read_nodes_from_file(filename)

def test_calculate_predecessors_and_distances():
    filename = "inputs/graf2.txt"
    nodes, board, line_length = read_nodes_from_file(filename)
    calculate_distance_and_predecessor_for_each_node(nodes, line_length)
    test_predecessors = [1, 2, -1, 0, 1, 2]
    test_distances = [2, 1, 0, 3, 3, 1]
    for i, node in enumerate(nodes):
        assert node.predecessor == test_predecessors[i]
        assert node.distance == test_distances[i]

def test_shortest_path():
    filename = "inputs/graf2.txt"
    nodes, board, line_length = read_nodes_from_file(filename)
    calculate_distance_and_predecessor_for_each_node(nodes, line_length)
    shortest_path_set = shortest_path(nodes)
    assert shortest_path_set == {0, 1, 2, 3}