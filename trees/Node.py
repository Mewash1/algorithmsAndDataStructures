class Node:
    def __init__(self, data = None, right = None, left = None, up = None) -> None:
        self.key = data
        self.right = right
        self.left = left
        self.balance = 0
        self.height = 0
        self.up = up
