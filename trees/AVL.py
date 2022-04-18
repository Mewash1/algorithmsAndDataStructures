from .BST import BST 
from .Node import Node


class AVL(BST):
    def __init__(self, data) -> None:
        self.root = self.create_AVL_loop(data)
        # self.root = self.create_BT_loop(data)
    
    def create_AVL_loop(self, data):
        '''
        Creates an AVL tree using an existing create_BT method. \n
        After each insertion the tree is rebalanced.
        '''
        self.root = None
        for value in data:
            self.root = self.insert_node_BT(self.root, value)
            self.rebalance()
        return self.root

    def calculate_balance(self, node, nodes_list):
        '''
        Calculates balance factor for each node in tree.
        '''
        for node in nodes_list:
            node_1, node_2 = Node(1), Node(1)
            node_1.left, node_2.right = node.left, node.right
            left = self.calc_tree_height(node_1)
            right = self.calc_tree_height(node_2)
            node.balance = left - right

    def rebalance(self):
        '''
        Rebalances the whole tree.
        This method should be called after every modification to the tree - insertion or deletion.
        '''
        good_balance = {-1, 0, 1}
        nodes_list = self.traverse_postorder(self.root, None)
        self.calculate_balance(self.root, nodes_list)
        for node in nodes_list:
            if node.balance not in good_balance:
                if node.balance < 0:
                    if node.right is not None and node.right.balance > 0:
                        self.rotate_left_right(node, nodes_list)
                    else:
                        self.rotate_left_left(node, nodes_list)
                else:
                    if node.left is not None and node.left.balance < 0:
                        self.rotate_right_left(node, nodes_list)
                    else:
                        self.rotate_right_right(node, nodes_list)
                self.calculate_balance(self.root, nodes_list)

    def rotate_right_right(self, node, nodes_list):
        if node.left is not None:
            new_root = Node(node.left.key, node.left.left, node.left.right)
            middle = new_root.right
            middle = Node(new_root.right.key, new_root.right.right, new_root.right.left) if new_root.right is not None else None
            new_root.right = node
            node.left = middle
            if node == self.root:
                self.root = new_root
                return 0
            for s_node in nodes_list:
                if s_node.right == node:
                    s_node.right = new_root
                    break
                elif s_node.left == node:
                    s_node.left = new_root
                    break
    
    def rotate_left_left(self, node, nodes_list):
        if node.right is not None:
            new_root = Node(node.right.key, node.right.right, node.right.left)
            middle = Node(new_root.left.key, new_root.left.right, new_root.left.left) if new_root.left is not None else None
            new_root.left = node
            node.right = middle
            if node == self.root:
                self.root = new_root
                return 0
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

    def rotate_right_left(self, node, nodes_list):
        self.rotate_left_left(node.left, nodes_list)
        self.rotate_right_right(node, nodes_list)

    def remove_node_AVL(self, node: Node, key):
        self.remove_node_BT(self, node, key)
        self.rebalance()
    
    def insert_node_AVL(self, node: Node, key):
        self.insert_node_BT(node, key)
        self.rebalance()