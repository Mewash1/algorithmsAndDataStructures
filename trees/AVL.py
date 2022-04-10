from .BST import BST 
from .Node import Node


class AVL(BST):
    def __init__(self, data) -> None:
        super().__init__(data)
    
    def calculate_balance(self, node, nodes_list):
        for node in nodes_list:
            node_1, node_2 = Node(1), Node(1)
            node_1.left, node_2.right = node.left, node.right
            left = self.calc_tree_height(node_1)
            right = self.calc_tree_height(node_2)
            node.balance = left - right

    def rebalance(self):
        good_balance = {-1, 0, 1}
        nodes_list = self.traverse_inorder(self.root, None)
        self.calculate_balance(self.root, nodes_list)
        for node in nodes_list:
            if node.balance not in good_balance:
                if node.balance < 0:
                    if node.right.balance > 0:
                        self.rotate_left_right(node, nodes_list)
                    else:
                        self.rotate_left_left(node, nodes_list)
                else:
                    if node.left.balance < 0:
                        self.rotate_right_left(node, nodes_list)
                    else:
                        self.rotate_right_right(node, nodes_list)
                nodes_list = self.traverse_inorder(self.root, None)
                self.calculate_balance(self.root, nodes_list)

    def rotate_right_right(self, node, nodes_list):
        new_root = Node(node.left.key)
        new_root.left = node.left.left
        new_root.right = node
        for s_node in nodes_list:
            if s_node.right == node:
                s_node.right = new_root
                break
            elif s_node.left == node:
                s_node.left = new_root
                break

    def rotate_right_left(self, node, nodes_list):
        self.rotate_left_left(node.left, nodes_list)
        self.right_right(node, nodes_list)
    
    def rotate_left_left(self, node, nodes_list):
        new_root = Node(node.right.key)
        new_child = Node(node.key)
        new_root.right = node.right.right
        new_root.left = new_child
        for s_node in nodes_list:
            if s_node.right == node:
                s_node.right = new_root
                break
            elif s_node.left == node:
                s_node.left = new_root
                break

    def rotate_left_right(self, node, nodes_list):
        self.rotate_right_right(node.right, nodes_list)
        self.rotate_left_left(node, nodes_list)


