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
            new_root = self.rebalance(self.root)
        return self.root


    def insert_node_AVL(self, node, data, up=None):
        if node is None:
            node = Node(data)
            if up is not None:
                node.up = up
        elif node.key > data:
            node.left = self.insert_node_AVL(node.left, data, node)
            node.left.height = self.calc_node_height(node.left)
        elif node.key < data or node.key == data:
            node.right = self.insert_node_AVL(node.right, data, node)
            node.right.height = self.calc_node_height(node.right)
        new_root = self.rebalance(node)
        if new_root:
            new_root.up = node.up if node.up else None
            self.change_node_after_balancing(node, new_root)
        return node
    

    def change_node(self, old, new):
        if old and new:
            old.key = new.key
            if new.up is not None:
                if new.up.up is not None:
                    old.up = Node(new.up.key, new.up.right, new.up.left, new.up.up)
                else:
                    old.up = Node(new.up.key, new.up.right, new.up.left)
            else:
                old.up = None
            old.left = Node(new.left.key, new.left.right, new.left.left, new.left.up) if new.left else None
            old.right = Node(new.right.key, new.right.right, new.right.left, new.right.up) if new.right else None
            old.height = new.height
            old.balance = new.balance
            return old
    
    def change_node_after_balancing(self, old, new):
        if old and new:
            old.key = new.key
            old.left = Node(new.left.key, new.left.right, new.left.left, new.left.up) if new.left else None
            old.right = Node(new.right.key, new.right.right, new.right.left, new.right.up) if new.right else None
            old.height = new.height
            old.balance = new.balance
            if old.left:
                old.left.up = old
            if old.right:
                old.right.up = old
            return old

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
            return new_root

    def rotate_right_right(self, node):
        if node.left is not None:
            new_root = self.change_node(Node(), node.left)
            middle = self.change_node(Node(), new_root.right)
            new_root.right = self.change_node(Node(), node)
            new_root.right.left = middle
        
            node.height = self.calc_node_height(node)
            new_root.height = self.calc_node_height(new_root)
            new_root.up = None
            if new_root.left:
                new_root.left.up = new_root
            if new_root.right:
                new_root.right.up = new_root 
            return new_root
    
    def rotate_left_left(self, node):
        if node.right is not None:
            new_root = self.change_node(Node(), node.right)
            middle = self.change_node(Node(), new_root.left)
            new_root.left = self.change_node(Node(), node)
            new_root.left.right = middle

            node.height = self.calc_node_height(node)
            new_root.height = self.calc_node_height(new_root)  
            new_root.up = None
            if new_root.left:
                new_root.left.up = new_root
            if new_root.right:
                new_root.right.up = new_root
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
        grandfather = self.search_BT(self.root, key).up
        self.remove_node_BT(node, key)
        self.root.height = self.calc_node_height(self.root)
        grandfather.height = self.calc_node_height(grandfather)
        new_root = self.rebalance(grandfather)
        if new_root:
            self.change_node_after_balancing(node, new_root)