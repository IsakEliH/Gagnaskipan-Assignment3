from abc import ABC, abstractmethod

class Pair:
    """
    Pair represents the key-value pair (dictionary entry).
    """
    def __init__(self, key: object, value: object = None):
        self.key = key
        self.value = value

    def __str__(self):
        if self.value is None:
            s = str(self.key)
        else:
            s = '{' + str(self.key) + ': ' + str(self.value) + '}'
        return s


class IBinarySearchTree(ABC):
    """
    Abstract base class for a binary search tree, storing (key, value) pairs.
    Only unique key values are allowed.
    """

    @abstractmethod
    def __str__(self) -> str:
        """
        Returns a string representation of the tree.
        """
        pass

    @abstractmethod
    def insert(self, pair: Pair) -> bool:
        """
        Insert (key, value) element at the appropriate location in the tree if key does not already exist;
        if the key already exists in the tree, then override with the new (key, value) pair.
        Returns True is a new element was inserted, otherwise False (was updated).
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Returns True if the tree is empty, False otherwise.
        """
        pass

    @abstractmethod
    def is_in(self, key: object) -> bool:
        """
        Returns True if an element with key is in the tree, otherwise False.
        """
        pass

    @abstractmethod
    def get(self, key: object) -> object:
        """
        Returns the value of the element with the given key, or None if the key does not exist.
        """
        pass

    @abstractmethod
    def pairs(self) -> list[Pair]:
        """
        Returns a list of all the (key, value) pairs in the tree, in an increasing order.
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Removes all elements from the tree (tree becomes empty).
        """
        pass

    @abstractmethod
    def delete(self, key: object) -> bool:
        """
        Deletes the element with key, if exists.
        Returns True if the element was deleted (existed), otherwise False (does not exist).
        """
        pass
