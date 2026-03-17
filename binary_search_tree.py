#
# BST - Trees (Binary Search Trees)
# Your name:
#  - <Add your name here>
#
from interface.binary_search_tree_abc import Pair, IBinarySearchTree


class BinarySearchTree(IBinarySearchTree):
    """
    A class for a binary search tree, storing (key, value) pairs.
    Only unique key values are allowed.
    IMPORTANT:
        - You are not allowed to change the interface of the existing class methods (public/private),
          nor the _Note class. Doing so will result in non-graded submission.
          However, feel free to add other helper methods as you see fit.
    """

    # --------------------------------------------------------------------------------------
    # Private helper methods and classes (hint: once implemented try to reuse them as
    # much as possible in your public methods).
    # --------------------------------------------------------------------------------------

    class _Node:
        """
        The node class for creating the nodes in the tree (Do not change!).
        """
        def __init__(self, parent, left, right, pair: Pair):
            self.parent = parent
            self.left = left
            self.right = right
            self.pair = pair

    def _representation(self, node: _Node) -> str:
        if node is None:
            return "-"
        l = self._representation(node.left)
        r = self._representation(node.right)
        return '(' + str(node.pair) + ' ' + l + ' ' + r + ')'

    # The __iter__ and __reversed__ will be used to test the _first/_last/_before/_after methods.
    def __iter__(self):
        node = self._first()
        while node is not None:
            yield node.pair
            node = self._after(node)

    def __reversed__(self):
        node = self._last()
        while node is not None:
            yield node.pair
            node = self._before(node)

    def _first(self) -> _Node | None:
        """
        In a non-empty tree, returns the minimum key node (first in an inorder traversal), otherwise None.
        """
        # TO DO ...
        return None

    def _last(self) -> _Node | None:
        """
        In a non-empty tree, returns the maximum key node (last in an inorder traversal), otherwise None.
        """
        # TO DO ...
        return None

    def _before(self, node: _Node) -> _Node | None:
        """
        Returns the in-order predecessor of node, or None if it does not exist.
        """
        # TO DO ...
        return None

    def _after(self, node: _Node) -> _Node | None:
        """
        Returns the in-order successor of node, or None if it does not exist.
        """
        # TO DO ...
        return None

    # --------------------------------------------------------------------------------------
    # Public methods, implementing the abstract-base-class interface.
    # --------------------------------------------------------------------------------------

    def __init__(self):
        # This is the only member variable you need. Do not change the constructor.
        self._root = None

    def __str__(self) -> str:
        """
        Returns a string representation of the tree.
        """
        return self._representation(self._root)

    def insert_key(self, key: object) -> bool:  # Method is non-essential, but added for testing convenience.
        """
        Insert (key, None) element at the appropriate location in the tree if key does not already exist;
        if the key already exists in the tree, then override with the new (key, None) pair.
        Returns True is a new element was inserted, otherwise False (was updated).
        """
        return self.insert(Pair(key, None))

    def keys(self) -> list[object]: # Method is non-essential, but added for testing convenience.
        """
        Returns a list of all the keys in the tree, in an increasing order.
        """
        return [pair.key for pair in self.pairs()]

    def insert(self, pair: Pair) -> bool:
        """
        Insert (key, value) element at the appropriate location in the tree if key does not already exist;
        if the key already exists in the tree, then override with the new (key, value) pair.
        Returns True is a new element was inserted, otherwise False (was updated).
        """
        # TO DO ...
        return False

    def is_empty(self) -> bool:
        """
        Returns True if the tree is empty, False otherwise.
        """
        # TO DO ...
        return True

    def is_in(self, key: object) -> bool:
        """
        Returns True if an element with key is in the tree, otherwise False.
        """
        # TO DO ...
        return False

    def get(self, key: object) -> object:
        """
        Returns the value of the element with the given key, or None if the key does not exist.
        """
        # TO DO ...
        return None

    def pairs(self) -> list[Pair]:
        """
        Returns a list of all the (key, value) pairs in the tree, in an increasing order.
        """
        # TO DO ...
        return []

    def clear(self):
        """
        Removes all elements from the tree (tree becomes empty).
        """
        # TO DO ...
        ...

    def delete(self, key: object) -> bool:
        """
        Deletes the element with key, if exists.
        Returns True if the element was deleted (existed), otherwise False (does not exist).
        """
        # TO DO ...
        return False
