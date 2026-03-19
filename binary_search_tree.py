#
# BST - Trees (Binary Search Trees)
# Your name:
#  - Ísak Elí Hauksson
#
from interface.binary_search_tree_abc import Pair, IBinarySearchTree
from enum import StrEnum


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

    def _representation(self, node: _Node | None) -> str:
        if node is None:
            return "-"
        left = self._representation(node.left)
        right = self._representation(node.right)
        return "(" + str(node.pair) + " " + left + " " + right + ")"

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
        curr = self._root
        if curr is None:
            return None

        while curr.left is not None:
            curr = curr.left

        return curr

    def _last(self) -> _Node | None:
        """
        In a non-empty tree, returns the maximum key node (last in an inorder traversal), otherwise None.
        """
        curr = self._root
        if curr is None:
            return None

        while curr.right is not None:
            curr = curr.right

        return curr

    def _before(self, node: _Node) -> _Node | None:
        """
        Returns the in-order predecessor of node, or None if it does not exist.
        """

        if node is None:
            return None

        if node.left is not None:
            curr: BinarySearchTree._Node = node.left
            while curr.right is not None:
                curr = curr.right
            return curr

        curr = node
        parent: BinarySearchTree._Node = curr.parent
        while parent is not None and curr == parent.left:
            curr = parent
            parent = parent.parent

        return parent

    def _after(self, node: _Node) -> _Node | None:
        """
        Returns the in-order successor of node, or None if it does not exist.
        """
        if node is None:
            return None

        if node.right is not None:
            curr: BinarySearchTree._Node = node.right
            while curr.left is not None:
                curr = curr.left
            return curr

        curr = node
        parent: BinarySearchTree._Node = curr.parent
        while parent is not None and curr == parent.right:
            curr = parent
            parent = parent.parent

        return parent

    # --------------------------------------------------------------------------------------
    # Public methods, implementing the abstract-base-class interface.
    # --------------------------------------------------------------------------------------

    def __init__(self):
        # This is the only member variable you need. Do not change the constructor.
        self._root: None | BinarySearchTree._Node = None

    def __str__(self) -> str:
        """
        Returns a string representation of the tree.
        """
        return self._representation(self._root)

    def insert_key(
        self, key: object
    ) -> bool:  # Method is non-essential, but added for testing convenience.
        """
        Insert (key, None) element at the appropriate location in the tree if key does not already exist;
        if the key already exists in the tree, then override with the new (key, None) pair.
        Returns True is a new element was inserted, otherwise False (was updated).
        """
        return self.insert(Pair(key, None))

    def keys(
        self,
    ) -> list[object]:  # Method is non-essential, but added for testing convenience.
        """
        Returns a list of all the keys in the tree, in an increasing order.
        """
        return [pair.key for pair in self.pairs()]

    def _move_to_key(self, node: _Node, key: object) -> _Node:
        """
        A helper function that takes in a starting Node and a key.
        Return the node containing key if it exists.
        Otherwise return the parent node where a new key should be inserted.
        """

        if key == node.pair.key:
            return node

        if key < node.pair.key:  # type: ignore
            if node.left is None:
                return node
            return self._move_to_key(node.left, key)

        else:  # key > node.pair.key
            if node.right is None:
                return node
            return self._move_to_key(node.right, key)

    def insert(self, pair: Pair) -> bool:
        """
        Insert (key, value) element at the appropriate location in the tree if key does not already exist;
        if the key already exists in the tree, then override with the new (key, value) pair.
        Returns True is a new element was inserted, otherwise False (was updated).
        """

        if self._root is None:
            self._root = self._Node(None, None, None, pair)
            return True

        node: BinarySearchTree._Node = self._move_to_key(self._root, pair.key)

        if pair.key < node.pair.key:  # type: ignore
            node.left = self._Node(node, None, None, pair)
            return True
        if pair.key > node.pair.key:  # type: ignore
            node.right = self._Node(node, None, None, pair)
            return True

        # key already exist, so we override
        node.pair = pair
        return False

    def is_empty(self) -> bool:
        """
        Returns True if the tree is empty, False otherwise.
        """
        return self._root is None

    def is_in(self, key: object) -> bool:
        """
        Returns True if an element with key is in the tree, otherwise False.
        """
        if self._root is None:
            return False

        if self._move_to_key(self._root, key).pair.key == key:
            return True
        return False

    def get(self, key: object) -> object:
        """
        Returns the value of the element with the given key, or None if the key does not exist.
        """
        if not self.is_in(key):
            return None

        if self._root is None:
            return None

        return self._move_to_key(self._root, key).pair.value

    def pairs(self) -> list[Pair]:
        """
        Returns a list of all the (key, value) pairs in the tree, in an increasing order.
        """
        return [pair for pair in self]

    def clear(self):
        """
        Removes all elements from the tree (tree becomes empty).
        """
        self._root = None

    def _child_count(self, node: _Node) -> int:
        """
        Returns the number of children a node has
        """
        counter: int = 0

        if node.left is not None:
            counter += 1

        if node.right is not None:
            counter += 1

        return counter

    def _is_right_child(self, node: _Node) -> bool:
        """
        A helper function that returns if the node inputted is a
        right child or not
        """

        return node.parent.right == node

    def delete(self, key: object) -> bool:
        """
        Deletes the element with key, if exists.
        Returns True if the element was deleted (existed), otherwise False (does not exist).
        """
        if self._root is None:
            return False

        node: BinarySearchTree._Node = self._move_to_key(self._root, key)

        parent: BinarySearchTree._Node = node.parent

        # 3 cases

        # No child
        if self._child_count(node) == 0:
            # if the node is the root
            if node == self._root:
                self._root = None
                return True

            if self._is_right_child(node):
                parent.right = None
                return True

            else:
                parent.left = None
                return True

        # One child
        elif self._child_count(node) == 1:
            if node.left is None:
                right_node: BinarySearchTree._Node = node.right
                right_node.parent = node.parent

                if self._is_right_child(right_node):
                    right_node.parent.right = right_node
                else:
                    right_node.parent.left = right_node

                return True

            else:
                left_node: BinarySearchTree._Node = node.left
                left_node.parent = node.parent

                if self._is_right_child(left_node):
                    left_node.parent.right = left_node
                else:
                    left_node.parent.left = left_node

                return True

        # Two children
        elif self._child_count(node) == 2:
            successor = self._after(node)

            if successor is None:
                return False

            # Copy successor's data into node
            node.pair = successor.pair

            # Now remove successor from its old position
            # Successor can only have at most one child, and only on the right
            child: BinarySearchTree._Node = successor.right

            if child is not None:
                child.parent = successor.parent

            if successor.parent is None:
                self._root = child
            elif self._is_right_child(successor):
                successor.parent.right = child
            else:
                successor.parent.left = child

            return True

        return False
