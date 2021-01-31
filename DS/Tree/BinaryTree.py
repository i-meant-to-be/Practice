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

    def search(self, key: int) -> bool:
        pointer = self.root
        while True:
            if key < pointer.key:
                pointer = pointer.l_child
            elif key > pointer.key:
                pointer = pointer.r_child
            elif key == pointer.key:
                return True
            else:
                return False

    def insert_iter(self, node: Node) -> bool:
        """ Implemented by iteration """
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

        def insert_recur(self, node: Node) -> bool:
            """ Implemented by recursion """
            pass

    def delete(self, key: int) -> bool:
        pass
