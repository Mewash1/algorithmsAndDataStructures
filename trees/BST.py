from Node import Node
import copy


class BST:
    def __init__(self, data) -> None:
        self.root = self.create_BT_loop(data)

    def create_BT(self, node: Node, data, used_data=None):
        used_data = [] if used_data is None else used_data
        if node is None:
            node = Node(data)

        if node.key > data:
            if len(used_data) != 0:
                used_data.pop()
            node.left, used_data = self.create_BT(node.left, data, used_data)

        elif (node.key < data or (node.key == data and data in used_data) or
              (node.key == data and (node.left is not None or node.right is not None))):

            if len(used_data) != 0:
                used_data.pop()
            node.right, used_data = self.create_BT(node.right, data, used_data)

        used_data.append(data)

        return node, used_data

    def create_BT_loop(self, data):
        root = None
        used_data = None
        for value in data:
            root, used_data = self.create_BT(root, value, used_data)
            used_data = []
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

    def traverse_inorder(self, node, nodes_list=None):
        nodes_list = [] if nodes_list is None else nodes_list
        if node.left is not None:
            self.traverse_inorder(node.left, nodes_list)
        new_list = [node]
        nodes_list += new_list
        if node.right is not None:
            self.traverse_inorder(node.right, nodes_list)
        return nodes_list

    def traverse_preorder(self, root, nodes_list=None):
        nodes_list = [] if nodes_list is None else nodes_list
        nodes_list.append(root)
        if root.left is not None:
            self.traverse_preorder(root.left, nodes_list)

        if root.right is not None:
            self.traverse_preorder(root.right, nodes_list)
        return nodes_list

    def traverse_preorder_inverse_print(self, root, padding=None, nodes_list=None):
        nodes_list = [] if nodes_list is None else nodes_list
        padding = [] if padding is None else padding
        nodes_list.append(str(root.key))
        nodes_list.append('\n')

        if root.right is not None and root.left is None:
            nodes_list += padding
            nodes_list.append('R->')
            padding.append('   ')
            nodes_list, padding = self.traverse_preorder_inverse_print(root.right, padding, nodes_list)

        if root.right is not None and root.left is not None:

            nodes_list += padding
            nodes_list.append('R->')
            padding.append('|  ')
            nodes_list, padding = self.traverse_preorder_inverse_print(root.right, padding, nodes_list)

        if root.left is not None and root.right is not None:
            padding = self.back_to_left(padding)
            nodes_list += padding
            node = root.left
            if node.right is None and node.left is None:
                pass
            else:
                padding.append('   ')
            nodes_list.append('L->')
            nodes_list, padding = self.traverse_preorder_inverse_print(root.left, padding, nodes_list)

        if root.left is not None and root.right is None:
            # padding = self.back_to_left(padding)

            nodes_list += padding
            padding.append('    ')
            nodes_list.append('L->')
            nodes_list, padding = self.traverse_preorder_inverse_print(root.left, padding, nodes_list)

        return nodes_list, padding

    def back_to_left(self, padding: list):
        padding_new = copy.deepcopy(padding)
        padding.reverse()
        for element in padding:
            if '|' in element:
                padding_new.pop()
                break
            else:
                padding_new.pop()
        return padding_new

    def print_tree(self):
        root = self.root
        tree_list, padding = self.traverse_preorder_inverse_print(root)
        print(*tree_list)


data = [3, 2, 0.5, 0.333, 1, 5, 4, 55, 3, 6, 7, 8, 16, 11, 17, 28, 14, 15, 13, 11]
bst = BST(data)

root = bst.root

bst.print_tree()