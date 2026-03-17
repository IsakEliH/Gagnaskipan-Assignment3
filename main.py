from binary_search_tree import Pair, BinarySearchTree

def test0():
    tree = BinarySearchTree()
    tree.insert_key(20)
    tree.insert_key(30)
    tree.insert_key(40)
    tree.insert_key(10)
    print(tree)
    print(tree.is_in(10))
    print(tree.is_in(50))
    # For testing _before/_after_/_first/_last
    for pair in tree:
        print(pair.key, end=' ')
    print()
    for pair in reversed(tree):
        print(pair.key, end=' ')
    print()
    print('==>', tree.pairs())
    print('=>', tree.keys())

def test1():
    tree = BinarySearchTree()
    keys = [50, 30, 20, 25, 70, 60, 40, 35, 65, 80, 55]
    for key in keys:
        tree.insert_key(key)
    print(tree)
    tree.delete(55)
    print(tree)
    tree.delete(20)
    print(tree)
    tree.delete(70)
    print(tree)
    tree.delete(50)
    print(tree)
    for pair in tree:
        print(pair.key, end=' ')
    print()
    for pair in reversed(tree):
        print(pair.key, end=' ')
    print()


# Some basic BST tests, add more tests as needed!
test0()
test1()
