from trees.AVL import AVL  
from trees.Node import Node

def test_one():
    data = [1,2,3]
    tree = AVL(data)
    nodes_list = tree.traverse_inorder(tree.root, None)
    nodes_list[0].left = Node(4)
    assert tree.root.left.key == 4


def test_two():
    data = [1,44,23,67,22,4,0,1,6,7,12,15,19]
    tree = AVL(data)
    nodes_list = tree.traverse_inorder(tree.root, None)
    assert len(nodes_list) == len(data)
    for node in nodes_list:
        assert node.balance in {-1,0,1}
    tree.insert_node_AVL(tree.root, 100)
    for node in nodes_list:
        assert node.balance in {-1,0,1}