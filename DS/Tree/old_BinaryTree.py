from __future__ import annotations


class Node:
    """ Node for binary tree """

    def __init__(self, key: int, left: Node = None, right: Node = None):
        self.key = key
        self.left = left
        self.right = right


class Tree:
    """ Binary tree """

    def __init__(self, node: Node = None):
        self.root = node

    def empty(self) -> bool:
        return True if self.root is None else False

    def l_child(self) -> Tree:
        temp_tree = Tree(self.root.left)
        return temp_tree

    def r_child(self) -> Tree:
        temp_tree = Tree(self.root.right)
        return temp_tree

    def search(self, key) -> bool:
        temp = self.root
        while True:
            if temp is None:
                return False
            elif key == temp.key:
                return True
            elif key < temp.key:
                temp = temp.right
            else:
                temp = temp.left

    def insert(self, node) -> bool:
        while True:
            if self.root is None:
                self.root = node
                return True
            elif node.key == self.root.key:
                return False
            elif node.key < self.root.key:
                self.l_child().insert(node)
            else:
                self.r_child().insert(node)

    def delete(self, ):
        pass
