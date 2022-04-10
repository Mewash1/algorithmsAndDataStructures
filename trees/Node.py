class Node:
    def __init__(self, data = None) -> None:
        self.key = data
        self.right = None
        self.left = None
        self.balance = 0