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

@pytest.fixture
def bst_tree(random_list):
    return BST(random_list)

@pytest.fixture
def avl_tree(random_list):
    return AVL(random_list)

def delete_tree_from_list(list, tree: BST):
    for element in list:
        if element != tree.root.key:
            tree.remove_node_BT(tree.root, element)

def test_delete_BST_1000(benchmark, bst_tree, random_list):
    benchmark.pedantic(delete_tree_from_list, args=(random_list[:1000], bst_tree))

def test_delete_BST_2000(benchmark, bst_tree, random_list):
    benchmark.pedantic(delete_tree_from_list, args=(random_list[:2000], bst_tree))

def test_delete_BST_3000(benchmark, bst_tree, random_list):
    benchmark.pedantic(delete_tree_from_list, args=(random_list[:3000], bst_tree))

def test_delete_BST_4000(benchmark, bst_tree, random_list):
    benchmark.pedantic(delete_tree_from_list, args=(random_list[:4000], bst_tree))

def test_delete_BST_5000(benchmark, bst_tree, random_list):
    benchmark.pedantic(delete_tree_from_list, args=(random_list[:5000], bst_tree))

def test_delete_AVL_1000(benchmark, avl_tree, random_list):
    benchmark.pedantic(delete_tree_from_list, args=(random_list[:1000], avl_tree))

def test_delete_AVL_2000(benchmark, avl_tree, random_list):
    benchmark.pedantic(delete_tree_from_list, args=(random_list[:2000], avl_tree))

def test_delete_AVL_3000(benchmark, avl_tree, random_list):
    benchmark.pedantic(delete_tree_from_list, args=(random_list[:3000], avl_tree))

def test_delete_AVL_4000(benchmark, avl_tree, random_list):
    benchmark.pedantic(delete_tree_from_list, args=(random_list[:4000], avl_tree))

def test_delete_AVL_5000(benchmark, avl_tree, random_list):
    benchmark.pedantic(delete_tree_from_list, args=(random_list[:5000], avl_tree))
