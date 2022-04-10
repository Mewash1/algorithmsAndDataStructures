class Node:
    def __init__(self, data = None) -> None:
        self.key = data
        self.right = None
        self.left = None
        self.balance = 0

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


def tree_deep(root: Node, deep):
    if root.left is not None:
        deep_l += 1
        deep_l, deep_r = tree_deep(root.left, deep)
    elif root.right is not None:
        deep_r += 1
        deep_l, deep_r = tree_deep(root.right, deep)

    return max(deep_l, deep_r)
