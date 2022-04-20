from xxlimited import new
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
        print(data)
        for value in data:
            self.root = self.insert_node_AVL(self.root, value)
            self.root.height = self.calc_node_height(self.root)
            self.root.balance = self.calculate_balance(self.root)
        return self.root


    def insert_node_AVL(self, node, data):
        if node is None:
            node = Node(data)
        elif node.key > data:
            node.left = self.insert_node_AVL(node.left, data)
            node.left.height = self.calc_node_height(node.left)
            new_root = self.rebalance(node)
            if new_root:
                self.change_node(node, new_root)
        elif node.key < data or node.key == data:
            node.right = self.insert_node_AVL(node.right, data)
            node.right.height = self.calc_node_height(node.right)
            new_root = self.rebalance(node)
            if new_root:
                self.change_node(node, new_root)
        return node
    

    def change_node(self, old, new):
        if old:
            old.key = new.key
            old.left = Node(new.left.key, new.left.right, new.left.left) if new.left else None
            old.right = Node(new.right.key, new.right.right, new.right.left) if new.right else None
            old.height = new.height
            old.balance = new.balance

    def calculate_balance(self, node):
        '''
        Calculates balance factor for each node in tree.
        '''
        left_root = Node(0, None, node.left)
        right_root = Node(0, node.right, None)
        left = self.calc_node_height(left_root)
        right = self.calc_node_height(right_root)
        return left - right

    def rebalance(self, node):
        '''
        Rebalances the subtree of node.
        This method should be called after every modification to the tree - insertion or deletion.
        '''
        node.balance = self.calculate_balance(node)
        good_balance = {-1, 0, 1}
        if node.balance not in good_balance:
            if node.balance < 0:
                if node.right is not None and node.right.balance > 0:
                    new_root = self.rotate_left_right(node)
                else:
                    new_root = self.rotate_left_left(node)
            else:
                if node.left is not None and node.left.balance < 0:
                    new_root = self.rotate_right_left(node)
                else:
                    new_root = self.rotate_right_right(node)
            self.calculate_balance(self.root)
            return new_root

    def rotate_right_right(self, node):
        if node.left is not None:
            new_root = Node(node.left.key, node.left.left, node.left.right)
            middle = new_root.right
            middle = Node(new_root.right.key, new_root.right.right, new_root.right.left) if new_root.right is not None else None
            new_root.right = Node(node.key, node.right, node.left)
            new_root.right.left = middle
        
            node.height = self.calc_node_height(node)
            new_root.height = self.calc_node_height(new_root)
            return new_root
    
    def rotate_left_left(self, node):
        if node.right is not None:
            new_root = Node(node.right.key, node.right.right, node.right.left)
            middle = Node(new_root.left.key, new_root.left.right, new_root.left.left) if new_root.left is not None else None
            new_root.left = Node(node.key, node.right, node.left)
            new_root.left.right = middle

            node.height = self.calc_node_height(node)
            new_root.height = self.calc_node_height(new_root)
            return new_root

    def rotate_left_right(self, node):
        temp_root = self.rotate_right_right(node.right)
        self.change_node(node.right, temp_root)
        return self.rotate_left_left(node)

    def rotate_right_left(self, node):
        temp_root = self.rotate_left_left(node.left)
        self.change_node(node.left, temp_root)
        return self.rotate_right_right(node)

    def remove_node_AVL(self, node: Node, key):
        self.remove_node_BT(self, node, key)
        self.root.height = self.calc_node_height(self.root)
        self.rebalance()