from trees.BST import BST


def test_one():
    data = [5, 4, 2, 6, 8, 8]
    tree = BST(data)
    tree.insert_node_BT(tree.root, 7)
    tree.insert_node_BT(tree.root, 7)
    pass


def test_search_BT():
    data = [5, 4, 66, 3, 34, 5]
    tree = BST(data)
    key = 34
    key_root = tree.search_BT(tree.root, key)
    assert key_root.key == 34


def test_calc_tree_height():
    data = [1, 2, 3, 4]
    tree = BST(data)
    assert tree.calc_tree_height(tree.root) == 3


def test_traverse_inorder():
    data = [5, 4, 2, 6, 8, 8]
    tree = BST(data)
    inorder_list = tree.traverse_inorder(tree.root, None)
    new_list = []
    for node in inorder_list:
        new_list.append(node.key)
    assert new_list == [2, 4, 5, 6, 8, 8]


def test_print():
    data = [5, 4, 2, 6, 8, 8]
    bst = BST(data)

    root = bst.root

    bst.print_tree()


def test_traverse_preorder():
    data = [5, 4, 2, 6, 7, 8, 8]
    tree = BST(data)
    inorder_list = tree.traverse_preorder(tree.root, None)
    new_list = []
    for node in inorder_list:
        new_list.append(node.key)
    assert new_list == [5, 4, 2, 6, 7, 8, 8]


