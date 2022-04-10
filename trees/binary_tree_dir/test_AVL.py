from binary_tree_dir.BST import BST
from binary_tree_dir.AVL import AVL  
from binary_tree_dir.binary_tree import Node



def test_one():
    data = [1,2]
    tree = AVL(data)
    tree.calculate_balance(tree.root)
    assert tree.root.balance == -1
    assert tree.root.right.balance == 0
