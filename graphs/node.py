from cmath import inf


import math

class Node:
    def __init__(self, enter_cost):
        self.enter_cost = enter_cost
        self.predecessor = -1
        self.distance = math.inf if enter_cost != 0 else 0
    
    def __gt__(self, other) -> bool:
        return self.distance > other.distance

    def __lt__(self, other):
        return not (self.__gt__(other))