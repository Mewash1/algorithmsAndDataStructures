import random
import pytest
from trees.AVL import AVL 
from trees.BST import BST

@pytest.fixture
def random_list():
    random_list = []
    for _ in range(10000):
        random_list.append(random.randint(1, 30000))
    return random_list

def test_create_BST_1000(benchmark, random_list):
    bst = BST([1])
    benchmark(bst.create_BT_loop, random_list[:1000])

def test_create_BST_2000(benchmark, random_list):
    bst = BST([1])
    benchmark(bst.create_BT_loop, random_list[:2000])

def test_create_BST_3000(benchmark, random_list):
    bst = BST([1])
    benchmark(bst.create_BT_loop, random_list[:3000])

def test_create_BST_4000(benchmark, random_list):
    bst = BST([1])
    benchmark(bst.create_BT_loop, random_list[:4000])

def test_create_BST_5000(benchmark, random_list):
    bst = BST([1])
    benchmark(bst.create_BT_loop, random_list[:5000])

def test_create_AVL_1000(benchmark, random_list):
    avl = AVL([1])
    benchmark(avl.create_AVL_loop, random_list[:1000])

def test_create_AVL_2000(benchmark, random_list):
    avl = AVL([1])
    benchmark(avl.create_AVL_loop, random_list[:2000])

