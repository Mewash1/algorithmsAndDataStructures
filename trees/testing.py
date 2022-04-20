import random
import cProfile
from AVL import AVL

def random_list():
    random_list = []
    for _ in range(10000):
        random_list.append(random.randint(1, 30000))
    return random_list

random_list1 = random_list()
avl = AVL([1])
cProfile.run("avl.create_AVL_loop(random_list1[:2000])")