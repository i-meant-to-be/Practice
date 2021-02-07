from __future__ import annotations


class Node:
    def __init__(self, key: int, l_child: Node = None, r_child: Node = None):
        self.key = key
        self.l_child = l_child
        self.r_child = r_child


class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def isEmpty(self) -> bool:
        return self._isEmpty()

    def search(self, key: int) -> bool:
        return self._search(key)

    def insert(self, node: Node) -> bool:
        return self._insert(node)

    def delete(self, key: int) -> bool:
        return self._delete(key)

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

    def _isEmpty(self):
        return True if not self.root else False

    def _search(self, key: int):
        return True if self._traverse(key) else False

    def _insert(self, node: Node):
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

    def _delete(self, key: int):
        pointer = self.root
        parent_of_pointer = None
        dir_of_branch = None

        while True:
            if pointer is None:
                return False

            if pointer.key == key:
                break
            else:
                parent_of_pointer = pointer
                if key < pointer.key:
                    dir_of_branch = "Left"
                    pointer = pointer.l_child
                else:
                    dir_of_branch = "Right"
                    pointer = pointer.r_child

        if pointer.l_child is None:
            if pointer is self.root:
                self.root = pointer.r_child
            elif dir_of_branch == "Left":
                parent_of_pointer.l_child = pointer.r_child
            else:
                parent_of_pointer.r_child = pointer.r_child

        elif pointer.r_child is None:
            if pointer is self.root:
                self.root = pointer.l_child
            elif dir_of_branch == "Left":
                parent_of_pointer.l_child = pointer.l_child
            else:
                parent_of_pointer.r_child = pointer.l_child

        else:
            parent_of_pointer = pointer
            largest_node = pointer.l_child
            dir_of_branch = "Left"
            while largest_node.r_child:
                parent_of_pointer = largest_node
                largest_node = largest_node.r_child
                dir_of_branch = "Right"

            pointer.key = largest_node.key
            if dir_of_branch == "Left":
                parent_of_pointer.l_child = largest_node.l_child
            else:
                parent_of_pointer.r_child = largest_node.l_child
        return True
