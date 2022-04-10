from ..AVL import AVL  

def test_one():
    data = [1,2,3,4]
    tree = AVL(data)
    tree.rebalance()
    pass
    #assert tree.root.balance == -1
    #assert tree.root.right.balance == 0
