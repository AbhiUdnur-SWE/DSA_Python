class BSTNode:
    """BSTNode"""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    """BST"""

    def __init__(self, node: BSTNode):
        self.root = node

    def inser_node(self, val):
        """insert Node"""
        self.root = self.insert_helper(self.root, val)

    @staticmethod
    def insert_helper(node, val):
        """insert_helper"""
        if not node:
            return BSTNode(val)

        if val <= node.val:
            node.left = BST.insert_helper(node.left, val)

        else:
            node.right = BST.insert_helper(node.right, val)

        return node

    def inorder(self):
        """inorder"""
        BST.inorder_helper(self.root)

    @staticmethod
    def inorder_helper(node):
        """inorder helper"""
        if not node:
            return

        BST.inorder_helper(node.left)
        print(node.val)
        BST.inorder_helper(node.right)

    def search(self, val: int):
        """search"""
        return BST.search_helper(self.root, val)

    @staticmethod
    def search_helper(node, val: int):
        """search_helper"""
        if not node:
            return False

        if node.val == val:
            return True

        if val < node.val:
            return BST.search_helper(node.left, val)

        if val > node.val:
            return BST.search_helper(node.right, val)

    def delete(self, val: int):
        """delete"""
        self.root = BST.delete_helper(self.root, val)

    @staticmethod
    def delete_helper(root_node, val: int):
        """delete helper"""
        if not root_node:
            return root_node

        if val < root_node.val:
            root_node.left = BST.delete_helper(root_node.left, val)

        elif val > root_node.val:
            root_node.right = BST.delete_helper(root_node.right, val)
        else:

            # no child
            if not root_node.left and not root_node.right:
                return None

            # one child
            elif not root_node.left:
                return root_node.right

            elif not root_node.right:
                return root_node.left

            # two children
            succesor = BST.min_val_node(root_node.right)
            root_node.val = succesor.val
            root_node.right = BST.delete_helper(root_node.right, succesor.val)

        return root_node

    @staticmethod
    def min_val_node(root):
        """min val node"""
        temp = root
        while temp.left:
            temp = temp.left
        return temp

    def clear(self):
        """clear tree"""
        self.root = None
