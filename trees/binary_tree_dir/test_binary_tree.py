from binary_tree_dir.binary_tree import (
    create_BT_loop, search_BT, insert_nood_BT
)


def test_ehh():
    data = [5, 4, 2, 6, 8, 8]
    root = create_BT_loop(data)
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
