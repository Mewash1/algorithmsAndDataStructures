from .Node import Node
import copy


class BST:
    def __init__(self, data) -> None:
        self.root = self.create_BT_loop(data)

    def create_BT_loop(self, data):
        root = None
        for value in data:
            root = self.insert_node_BT(root, value)
        root.height = self.calc_node_height(root)
        return root

    def search_BT(self, node: Node, key) -> Node:
        if node is None or node.key == key:
            return node
        if key < node.key:
            node = self.search_BT(node.left, key)
        else:
            node = self.search_BT(node.right, key)
        return node

    def insert_node_BT(self, node, data, up=None):
        if node is None:
            node = Node(data)
            if up is not None:
                node.up = up
        elif node.key > data:
            node.left = self.insert_node_BT(node.left, data)
            node.left.height = self.calc_node_height(node.left)
        elif node.key < data or node.key == data:
            node.right = self.insert_node_BT(node.right, data)
            node.right.height = self.calc_node_height(node.right)
        return node

    def remove_node_BT(self, node: Node, key):

        node_rm = self.search_BT(node, key)

        if node_rm.left is None and node_rm.right is None:
            node_rm = None

        elif node_rm.left is not None and node_rm.right is None:
            up = node_rm.up
            grandchild = node_rm.left
            self.link_grandchild_with_grandfather(up, node_rm, grandchild)

        elif node_rm.left is None and node_rm.right is not None:
            up = node_rm.up
            self.link_grandchild_with_grandfather(up, node_rm, node_rm.right)

        else:
            self.remove_nodes_two_children(node_rm, node)

    def remove_nodes_two_children(self, node, root):
        next_node = node.right
        while next_node.left is not None:
            next_node = next_node.left

        node.key = next_node.key

        self.remove_node_BT(node.right, next_node.key)

    def link_grandchild_with_grandfather(self, grandfather: Node, child: Node,
                                         grandchild: Node):
        if grandfather.left == child:
            grandfather.left = grandchild
            grandchild.up = grandfather
        else:
            grandfather.right = grandchild
            grandchild.up = grandfather

    def calc_node_height(self, node):
        if node is None or (node.left is None and node.right is None):
            return 0
        left = node.left.height if node.left is not None else 0
        right = node.right.height if node.right is not None else 0
        return max(left, right) + 1

    def traverse_inorder(self, node, nodes_list=None):
        nodes_list = [] if nodes_list is None else nodes_list
        if node is not None:
            self.traverse_inorder(node.left, nodes_list)
            new_list = [node]
            nodes_list += new_list
            self.traverse_inorder(node.right, nodes_list)
        return nodes_list

    def traverse_inorder_keys(self, node, nodes_list=None):
        nodes_list = [] if nodes_list is None else nodes_list
        if node is not None:
            self.traverse_inorder_keys(node.left, nodes_list)
            if node.key is not None:
                new_list = [node.key]
                nodes_list += new_list
            self.traverse_inorder_keys(node.right, nodes_list)
        return nodes_list

    def traverse_postorder(self, node, nodes_list):
        nodes_list = [] if nodes_list is None else nodes_list
        if node is not None:
            self.traverse_postorder(node.left, nodes_list)
            self.traverse_postorder(node.right, nodes_list)
            new_list = [node]
            nodes_list += new_list
        return nodes_list

    def traverse_preorder(self, root, nodes_list=None):
        nodes_list = [] if nodes_list is None else nodes_list
        if root is not None:
            nodes_list.append(root)
            self.traverse_preorder(root.left, nodes_list)
            self.traverse_preorder(root.right, nodes_list)
        return nodes_list

    def make_print_list(self, root, padding=None, nodes_list=None):
        nodes_list = [] if nodes_list is None else nodes_list
        padding = [] if padding is None else padding
        nodes_list.append(str(root.key))
        nodes_list.append('\n')

        if root.right is not None and root.left is None:
            nodes_list += padding
            nodes_list.append('R->')
            padding.append('   ')
            nodes_list, padding = self.make_print_list
            (root.right, padding, nodes_list)

        if root.right is not None and root.left is not None:

            nodes_list += padding
            nodes_list.append('R->')
            padding.append('|  ')
            nodes_list, padding = self.make_print_list(root.right, padding, nodes_list)

        if root.left is not None and root.right is not None:
            padding = self.back_to_left(padding)
            nodes_list += padding
            node = root.left
            if node.right is None and node.left is None:
                pass
            else:
                padding.append('   ')
            nodes_list.append('L->')
            nodes_list, padding = self.make_print_list(root.left, padding, nodes_list)

        if root.left is not None and root.right is None:
            # padding = self.back_to_left(padding)

            nodes_list += padding
            padding.append('    ')
            nodes_list.append('L->')
            nodes_list, padding = self.make_print_list(root.left, padding, nodes_list)

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
        tree_list, padding = self.make_print_list(root)
        print(*tree_list)
