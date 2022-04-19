import random
from AVL import AVL

def random_list():
    random_list = []
    for _ in range(10000):
        random_list.append(random.randint(1, 30000))
    return random_list

new_list = random_list()
avl = AVL(new_list[:5000])