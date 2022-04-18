from trees.BST import BST
from trees.AVL import AVL  
from trees.Node import Node

def test_one():
    data = [2,5,4,6,7]
    tree = BST(data)
    nodes_list = tree.traverse_postorder(tree.root, None)
    key_list = []
    for node in nodes_list:
        key_list.append(node.key)
    assert key_list == [4,7,6,5,2]


def test_two():
    data = [1,5,9,11,56,56]
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