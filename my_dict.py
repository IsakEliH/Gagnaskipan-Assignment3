#
# MyDict dictionary.
# Your name:
#  - Ísak Elí Hauksson
#

from collections.abc import MutableMapping
from binary_search_tree import Pair, BinarySearchTree


class MyDict(MutableMapping):
    def __init__(self):
        self._bst = BinarySearchTree()
        self._len = 0

    def __iter__(self):
        """
        Returns an iterator; note, for dictionaries one iterates on the keys (not key-value pairs)
        """
        return iter(self._bst.keys())

    def __str__(self):
        """
        Returns a string representation of the dictionary.
        """
        """
        Returns a string representation of the dictionary (in the same format as Python dict, e.g. {1: 755, 2: 290}
        """
        elements = []
        for elem in self._bst:
            elements.append(f"{elem.key}: {elem.value}")
        return "{" + ", ".join(elements) + "}"

    def __getitem__(self, key):
        """
        Returns the value at key entry, i.e. value = d[key].
        Raises KeyError if the key is not found.
        """
        item = self._bst.get(key)

        if item is None:
            raise KeyError(f"Key '{key}' not found in dictionary.")

        return item

    def get(self, key, default=None):
        """
        Returns the value at key entry, i.e. value = d.get(key) ; or d.get(key,default) .
        Returns default if key not found.
        """
        item = self._bst.get(key)

        if item is None:
            return default

        return item

    def __setitem__(self, key, value):
        """
        Sets the value at key entry, i.e. d[key] = value
        """
        self._bst.insert(Pair(key, value))
        self._len += 1

    def __delitem__(self, key):
        """
        Returns the entry at key, i.e. del d[key]
        """
        self._bst.delete(key)

        return key

    def __len__(self):
        """
        Returns the number of entries in the dictionary.
        """
        return self._len
