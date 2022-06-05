from cmath import inf


import math

class Node:
    def __init__(self, enter_cost, index, end):
        self.enter_cost = enter_cost
        self.index = index
        self.predecessor = -1
        self.distance = math.inf if enter_cost != 0 else 0
        self.end = end
    
    def __gt__(self, other) -> bool:
        return self.distance > other.distance

    def __lt__(self, other):
        return not (self.__gt__(other))
    
    def __str__(self):
        return f"{self.index} {self.enter_cost} {self.distance} {self.predecessor}"