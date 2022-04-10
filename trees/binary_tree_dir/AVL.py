from binary_tree_dir.BST import BST 
from binary_tree_dir.binary_tree import Node


class AVL(BST):
    def __init__(self, data) -> None:
        super().__init__(data)
    
    def calculate_balance(self, node):
        nodes_list = self.traverse_inorder(self.root, None)
        for node in nodes_list:
            node_1, node_2 = Node(1), Node(1)
            node_1.left, node_2.right = node.left, node.right
            left = self.calc_tree_height(node_1)
            right = self.calc_tree_height(node_2)
            node.balance = left - right

    def rebalance(self):
        pass


