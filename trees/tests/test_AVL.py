from trees.AVL import AVL  
from trees.Node import Node

def test_one():
    data = [1,5,7,2,4]
    tree = AVL(data)
    nodes_list = tree.traverse_postorder(tree.root, None)
    key_list = []
    tree.print_tree()
    for node in nodes_list:
        key_list.append(node.key)
    #assert key_list == [2,5,7,6,4]


def test_two():
    data = [5,2,1,7,6,3,4,8]
    #data = [23771, 10911, 8291, 25342, 24498, 12074, 22261, 25997, 29210]
    tree = AVL(data)
    tree.print_tree()
    tree.insert_node_AVL(tree.root, 9)
    tree.print_tree()
    assert 1 == 0

def test_three():
    tree = AVL([4])
    tree.root.right = Node(5)
    tree.root.right.right = Node(6)
    tree.root.right.left = Node(4)
    nodes_list = tree.traverse_inorder(tree.root, None)
    pass

def test_repeated_data():
    data = [2,2,2,3,4,3,4,3,4,1,1,1]
    tree = AVL(data)
    inorder_list = tree.traverse_preorder(tree.root, None)
    new_list = []
    for node in inorder_list:
        new_list.append(node.key)
    tree.print_tree()
    assert len(new_list) == len(data)

def test_remove_node():
    data = [1,5,7,2,4]
    tree = AVL(data)
    nodes_list = tree.traverse_postorder(tree.root, None)
    key_list = []
    tree.print_tree()
    for node in nodes_list:
        key_list.append(node.key)
    tree.remove_node_AVL(tree.root, 7)
    tree.print_tree()
