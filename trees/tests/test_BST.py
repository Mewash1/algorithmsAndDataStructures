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
    tree.print_tree()
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


def test_repeated_data():
    data = [2,2,2,3,4,3,4,3,4,1,1,1]
    tree = BST(data)
    inorder_list = tree.traverse_preorder(tree.root, None)
    new_list = []
    for node in inorder_list:
        new_list.append(node.key)
    tree.print_tree()
    assert len(new_list) == len(data)

def test_calc_height_for_nodes():
    data = [2,4,1,5,6,1,9,10]
    tree = BST(data)
    nodes_list = tree.traverse_postorder(tree.root, None)
    for node in nodes_list:
        print(node.key, node.height)
    tree.print_tree()
    
    tree.insert_node_BT(tree.root, 100)
    nodes_list = tree.traverse_postorder(tree.root, None)
    for node in nodes_list:
        print(node.key, node.height)
    tree.print_tree()
    assert 1 == 0