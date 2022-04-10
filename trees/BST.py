from .Node import Node


class BST:
    def __init__(self, data) -> None:
        self.root = self.create_BT_loop(data)


    def create_BT(self, node: Node, data, used_data=None):
        used_data = [] if used_data is None else used_data
        if node is None:
            node = Node(data)

        if node.key > data:
            used_data.pop()
            node.left, used_data = self.create_BT(node.left, data, used_data)
        elif node.key < data or (node.key == data and data in used_data):
            used_data.pop()
            node.right, used_data = self.create_BT(node.right, data, used_data)

        used_data.append(data)

        return node, used_data


    def create_BT_loop(self, data):
        root = None
        used_data = None
        for value in data:
            root, used_data = self.create_BT(root, value, used_data)

        return root

    def search_BT(self, node: Node, key) -> Node:
        if node is None or node.key == key:
            return node

        if key < node.key:
            node = self.search_BT(node.left, key)
        else:
            node = self.search_BT(node.right, key)
        return node

    def insert_nood_BT(self, node: Node, data, used_data=None):
        used_data = [] if used_data is None else used_data
        if node is None:
            node = Node(data)

        if node.key > data:
            if len(used_data) != 0:
                used_data.pop()
            node.left, used_data = self.insert_nood_BT(node.left, data, used_data)
        elif node.key < data or (node.key == data and data in used_data):
            if len(used_data) != 0:
                used_data.pop()
            node.right, used_data = self.insert_nood_BT(node.right, data, used_data)

        used_data.append(data)

        return node, used_data

    def recursively_remove_nodes(self, node: Node, side):
        if side == 'left' and node.left is not None:
            node.key = node.left.key
            self.recursively_remove_nodes(node.left, side)
        elif side == 'right' and node.right is not None:
            node.key = node.right.key
            self.recursively_remove_nodes(node.right, side)
        else:
            node.key = None


    def remove_node_BT(self, node: Node, key):

        nood_rm = self.search_BT(node, key)

        if nood_rm.left is None and nood_rm.right is None:
            nood_rm.key = None
            pass

        elif nood_rm.left is not None and nood_rm.right is None:
            self.recursively_remove_nodes(nood_rm, 'left')

        elif nood_rm.left is None and nood_rm.right is not None:
            self.recursively_remove_nodes(nood_rm, 'right')

        else:
            exchanged_node = nood_rm.right
            while exchanged_node.left is not None:
                exchanged_node = exchanged_node.left

            self.recursively_remove_nodes(exchanged_node, 'right')

    def calc_tree_height(self, node):
        if node is None or (node.left is None and node.right is None):
            return 0
        left_height = self.calc_tree_height(node.left)
        right_height = self.calc_tree_height(node.right)
        return max(left_height, right_height) + 1
    
    def traverse_inorder(self, node, nodes_list):
        nodes_list = [] if nodes_list is None else nodes_list
        if node.left is not None:
            self.traverse_inorder(node.left, nodes_list)
        new_list = [node]
        nodes_list += new_list
        if node.right is not None:
            self.traverse_inorder(node.right, nodes_list)
        return nodes_list