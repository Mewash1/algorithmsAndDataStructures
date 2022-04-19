class Node:
    def __init__(self, data = None, right = None, left = None, up = None) -> None:
        self.key = data
        self.right = right
        self.left = left
        self.up = up
        self.balance = 0