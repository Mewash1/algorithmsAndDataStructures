class Node:
    def __init__(self, data=None) -> None:
        self.key = data
        self.right = None
        self.left = None


def create_BT(node: Node, data, used_data=None):
    used_data = [] if used_data is None else used_data
    if node is None:
        node = Node(data)

    if node.key > data:
        used_data.pop()
        node.left, used_data = create_BT(node.left, data, used_data)
    elif node.key < data or (node.key == data and data in used_data):
        used_data.pop()
        node.right, used_data = create_BT(node.right, data, used_data)

    used_data.append(data)

    return node, used_data


def create_BT_loop(data):
    root = None
    used_data = None
    for value in data:
        root, used_data = create_BT(root, value, used_data)

    return root


def search_BT(root: Node, key) -> Node:
    if root is None or root.key == key:
        return root

    if key < root.key:
        root = search_BT(root.left, key)
    else:
        root = search_BT(root.right, key)
    return root


def insert_nood_BT(node: Node, data, used_data=None):
    used_data = [] if used_data is None else used_data
    if node is None:
        node = Node(data)

    if node.key > data:
        if len(used_data) != 0:
            used_data.pop()
        node.left, used_data = insert_nood_BT(node.left, data, used_data)
    elif node.key < data or (node.key == data and data in used_data):
        if len(used_data) != 0:
            used_data.pop()
        node.right, used_data = insert_nood_BT(node.right, data, used_data)

    used_data.append(data)

    return node, used_data


def recursively_remove_nodes(root: Node, side):
    if side == 'left' and root.left is not None:
        root.key = root.left.key
        recursively_remove_nodes(root.left, side)
    elif side == 'right' and root.right is not None:
        root.key = root.right.key
        recursively_remove_nodes(root.right, side)
    else:
        root.key = None


def remove_node_BT(root: Node, key):

    nood_rm = search_BT(root, key)

    if nood_rm.left is None and nood_rm.right is None:
        nood_rm.key = None
        pass

    elif nood_rm.left is not None and nood_rm.right is None:
        recursively_remove_nodes(nood_rm, 'left')

    elif nood_rm.left is None and nood_rm.right is not None:
        recursively_remove_nodes(nood_rm, 'right')

    else:
        exchanged_node = nood_rm.right
        while exchanged_node.left is not None:
            exchanged_node = exchanged_node.left

        recursively_remove_nodes(exchanged_node, 'right')


def inorder(root: Node, tree_list=[]):
    if root.left is not None:
        tree_list = inorder(root.left)

    tree_list.append(root.key)

    if root.right is not None:
        tree_list = inorder(root.right)

    return tree_list


# def print_tree(root: Node, space):
#     tree_list = inorder(root)
#     tree_list.reverse()

#     if root.key is None:
#         return

#     space += 10

#     print_tree(root.right, space)

#     print()




# def print_tree(root: Node):
#     if root is not None:
#         print(root.key)
#         if root.left is not None:
#             print(root.left.key, end=' ')
#         else:
#             print('-', end=' ')
#         if root.right is not None:
#             print(root.right.key)
#         else:
#             print('-')
#         print_tree(root.left)
#         print_tree(root.right)


# def tree_deep(root: Node, deep):
#     if root.left is not None:
#         deep_l += 1
#         deep_l, deep_r = tree_deep(root.left, deep)
#     elif root.right is not None:
#         deep_r += 1
#         deep_l, deep_r = tree_deep(root.right, deep)

#     return deep_l, deep_r
