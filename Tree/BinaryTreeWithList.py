import re


class BinaryTreeWithList:
    """BinaryTreeWithList"""

    def __init__(self, size: int):
        self.custom_list = size * [None]
        self.last_index_used = 0
        self.maxsize = size

    def inser_node(self, value):
        """insert node"""

        if self.last_index_used + 1 == self.maxsize:
            return False

        self.custom_list[self.last_index_used + 1] = value
        self.last_index_used += 1
        return True

    def search_node(self, value):
        """Search node"""
        for i in self.custom_list:
            if i == value:
                return True
        return False

    def preorder_traversal(self, index=1):
        """preorder_traversal"""

        if index > self.last_index_used:
            return

        print(self.custom_list[index])
        self.preorder_traversal(index * 2)
        self.preorder_traversal(index * 2 + 1)

    def postorder_traversal(self, index=1):
        """postorder_traversal"""

        if index > self.last_index_used:
            return

        self.postorder_traversal(index * 2)
        self.postorder_traversal(index * 2 + 1)
        print(self.custom_list[index])

    def inorder_traversal(self, index=1):
        """inorder_traversal"""

        if index > self.last_index_used:
            return

        self.inorder_traversal(index * 2)
        print(self.custom_list[index])
        self.inorder_traversal(index * 2 + 1)

    def level_order(self):
        """level_order"""
        for i in range(1, len(self.custom_list)):
            print(self.custom_list[i])

    def del_node(self, value):
        "del_node"
        if self.last_index_used == 0:
            return "empty!!"

        for i, item in enumerate(self.custom_list):
            if item == value:
                self.custom_list[i] = self.custom_list[self.last_index_used]
                self.custom_list[self.last_index_used] = None
                self.last_index_used -= 1
                return "Success"

        return "not found"

    def clear(self):
        "clear"
        self.custom_list = None
        self.last_index_used = 0
