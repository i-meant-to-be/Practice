from __future__ import annotations


class Node:
    """ Node included in binary tree """

    def __init__(self, key: int, l_child: Node = None, r_child: Node = None):
        self.key = key
        self.l_child = l_child
        self.r_child = r_child


class Tree:
    """ Binary tree """

    def __init__(self, root: Node = None):
        self.root = root

    def _traverse(self, key: int):
        pointer = self.root
        while True:
            if key < pointer.key:
                pointer = pointer.l_child
            elif key > pointer.key:
                pointer = pointer.r_child
            elif key == pointer.key:
                return pointer
            else:
                return None

    def is_empty(self) -> bool:
        """ Check whether a tree is empty """
        def _empty():
            return True if not self.root else False
        return _empty()

    def search(self, key: int) -> bool:
        """ Check whether a key is in a tree """
        def _search(key: int):
            return True if self._traverse(key) else False
        return _search(key)

    def insert(self, node: Node) -> bool:
        """ Insert a node in tree using iteration """
        def _insert(node: Node):
            pointer = self.root
            if not pointer:
                self.root = node
                return True
            while True:
                if node.key == pointer.key:
                    return False
                elif node.key < pointer.key:
                    if not pointer.l_child:
                        pointer.l_child = node
                        return True
                    pointer = pointer.l_child
                else:
                    if not pointer.r_child:
                        pointer.r_child = node
                        return True
                    pointer = pointer.l_child
        return _insert(node)

    def delete(self, key: int) -> bool:
        """ Delete a node from tree """
        def _delete(key: int):
            pointer = self.root
            parant = self._traverse(key)
