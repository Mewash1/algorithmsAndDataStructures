from ..BST import BST

def test_insert_nood():
    data = [5, 4, 2, 6, 8, 8]
    tree = BST(data)
    tree.insert_node_BT(tree.root, 7)
    tree.insert_node_BT(tree.root, 7)
    list_inorder = tree.traverse_inorder_keys(tree.root)
    assert list_inorder == [2, 4, 5, 6, 7, 7, 8, 8]


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
    tree.print_tree()
    inorder_list = tree.traverse_inorder(tree.root, None)
    new_list = []
    for node in inorder_list:
        new_list.append(node.key)
    assert new_list == [2, 4, 5, 6, 8, 8]


def test_traverse_preorder():
    data = [5, 4, 2, 6, 7, 8, 8]
    tree = BST(data)
    inorder_list = tree.traverse_preorder(tree.root, None)
    new_list = []
    for node in inorder_list:
        new_list.append(node.key)
    assert new_list == [5, 4, 2, 6, 7, 8, 8]


def test_repeated_data():
    data = [2, 2, 2, 3, 4, 3, 4, 3, 4, 1, 1, 1]
    tree = BST(data)
    inorder_list = tree.traverse_inorder_keys(tree.root, None)
    assert len(inorder_list) == len(data)


def test_remove_node_one_child():
    data = [5, 4, 2, 6, 8, 8]
    tree = BST(data)
    inorder_list1 = tree.traverse_inorder_keys(tree.root)
    assert inorder_list1 == [2, 4, 5, 6, 8, 8]
    tree.remove_node_BT(tree.root, 4)
    inorder_list2 = tree.traverse_inorder_keys(tree.root)
    assert inorder_list2 == [2, 5, 6, 8, 8]


def test_remove_node_one_child():
    data = [5, 4, 2, 6, 8, 8]
    tree = BST(data)
    inorder_list1 = tree.traverse_inorder_keys(tree.root)
    assert inorder_list1 == [2, 4, 5, 6, 8, 8]
    tree.remove_node_BT(tree.root, 4)
    inorder_list2 = tree.traverse_inorder_keys(tree.root)
    assert inorder_list2 == [2, 5, 6, 8, 8]


def test_remove_node_two_children():
    data = [5, 4, 2, 7, 6, 8, 8, 11, 55]
    tree = BST(data)
    inorder_list1 = tree.traverse_inorder_keys(tree.root)
    assert inorder_list1 == [2, 4, 5, 6, 7, 8, 8, 11, 55]
    tree.remove_node_BT(tree.root, 7)
    inorder_list2 = tree.traverse_inorder_keys(tree.root)
    assert inorder_list2 == [2, 4, 5, 6, 8, 8, 11, 55]