from trees.AVL import AVL  
from trees.Node import Node

def test_one():
    data = [2,5,4,6,7]
    tree = AVL(data)
    nodes_list = tree.traverse_postorder(tree.root, None)
    key_list = []
    tree.print_tree()
    for node in nodes_list:
        key_list.append(node.key)
    assert key_list == [2,5,7,6,4]


def test_two():
    data = [1,5,56,56,43,8,47,33,22,88,1,2,7,9,4,6,3,5,9,2,5,66]
    tree = AVL(data)
    nodes_list = tree.traverse_inorder(tree.root, None)
    assert len(nodes_list) == len(data)
    for node in nodes_list:
        assert node.balance in {-1,0,1}
    tree.insert_node_AVL(tree.root, 100)
    for node in nodes_list:
        assert node.balance in {-1,0,1}

def test_three():
    tree = AVL([4])
    tree.root.right = Node(5)
    tree.root.right.right = Node(6)
    tree.root.right.left = Node(4)
    nodes_list = tree.traverse_inorder(tree.root, None)
    tree.rebalance()
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