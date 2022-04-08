class Node:
    # Bad declaration with None
    def __init__(self, data = None) -> None:
        self.key = data
        self.right = None
        self.left = None


def create_BT(node: Node, data):
    if node is None:
        node = Node(data)

    if node.key > data:
        node.left = create_BT(node.left, data)
    elif node.key < data:
        node.right = create_BT(node.right, data)

    return node


def create_BT_loop(data):
    root = None
    for value in data:
        root = create_BT(root, value)

    return root