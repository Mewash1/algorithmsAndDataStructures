from binary_tree_dir.BST import BST


def test_one():
    data = [5, 4, 2, 6, 8, 8]
    tree = BST(data)
    tree.insert_nood_BT(tree.root, 7)
    tree.insert_nood_BT(tree.root, 7)
    pass


def test_search_BT():
    data = [5, 4, 66, 3, 34, 5]
    tree = BST(data)
    key = 34
    key_root = tree.search_BT(tree.root, key)
    assert key_root.key == 34