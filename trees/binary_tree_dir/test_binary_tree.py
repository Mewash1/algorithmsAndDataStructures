from binary_tree_dir.binary_tree import (
    create_BT_loop, search_BT, insert_nood_BT,
    inorder, remove_node_BT
)


def test_ehh():
    data = [5, 4, 2, 6, 8, 8]
    root = create_BT_loop(data)
    insert_nood_BT(root, 7)
    insert_nood_BT(root, 7)
    pass


# data = [5, 4, 2, 6, 8]
# root = create_BT_loop(data)
# inorder(root)


def test_search_BT():
    data = [5, 4, 66, 3, 34, 5]
    root = create_BT_loop(data)
    key = 34
    key_root = search_BT(root, key)
    assert key_root.key == 34


def test_node_rm():
    data = [5, 3, 4, 2, 6, 8]
    root = create_BT_loop(data)

    remove_node_BT(root, 4)
    pass


def test_inorder():
    data = [5, 3, 4, 2, 6, 8]
    root = create_BT_loop(data)
    tree_list = inorder(root)
    assert tree_list == [2, 3, 4, 5, 6, 8]
