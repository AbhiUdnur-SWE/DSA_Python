"""AVL tree module with tree node and traversal operations."""

from sys import path
from os.path import dirname, abspath

# Add parent directory to path to allow imports from sibling packages
path.insert(0, dirname(dirname(abspath(__file__))))
from Queue.QueueLL import Queue


class AVLNode:
    """AVLNode"""

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.height = 1


class AVLTree:
    """AVLTree"""

    def __init__(self, root: AVLNode):
        self.root = root

    def inorder(self):
        """inorder"""
        AVLTree.inorder_helper(self.root)

    @staticmethod
    def inorder_helper(node):
        """inorder helper"""
        if not node:
            return

        AVLTree.inorder_helper(node.left)
        print(node.val)
        AVLTree.inorder_helper(node.right)

    def level_order(self):
        """level order"""
        return AVLTree.level_order_helper(self.root)

    @staticmethod
    def level_order_helper(root):
        """level order"""
        if not root:
            return
        q = Queue()
        q.enqueue(root)
        while not q.is_empty():
            root = q.dequeue()
            print(root.val)
            if root.left is not None:
                q.enqueue(root.left)

            if root.right is not None:
                q.enqueue(root.right)

    def search(self, val: int):
        """search"""
        return AVLTree.search_helper(self.root, val)

    @staticmethod
    def search_helper(node, val: int):
        """search_helper"""
        if not node:
            return False

        if node.val == val:
            return True

        if val < node.val:
            return AVLTree.search_helper(node.left, val)

        if val > node.val:
            return AVLTree.search_helper(node.right, val)

    def insert(self, val: int):
        """insert"""
        self.root = AVLTree.insert_helper(self.root, val)

    @staticmethod
    def insert_helper(root_node: AVLNode, val):
        """insert_helper"""
        if not root_node:
            return AVLNode(val)

        if val < root_node.val:
            root_node.left = AVLTree.insert_helper(root_node.left, val)

        else:
            root_node.right = AVLTree.insert_helper(root_node.right, val)

        root_node.height = 1 + max(
            AVLTree.get_height(root_node.left), AVLTree.get_height(root_node.right)
        )

        ht_diff = AVLTree.get_height_diff(root_node)

        if ht_diff > 1 and val < root_node.left.val:
            return AVLTree.right_rotate(root_node)  # LL

        if ht_diff > 1 and val > root_node.left.val:
            root_node.left = AVLTree.left_rotate(root_node.left)
            return AVLTree.right_rotate(root_node)  # LR

        if ht_diff < -1 and val > root_node.right.val:
            return AVLTree.left_rotate(root_node)  # RR

        if ht_diff < -1 and val < root_node.right.val:
            root_node.right = AVLTree.left_rotate(root_node.right)
            return AVLTree.left_rotate(root_node)  # RL

        return root_node

    def delete(self, val: int):
        """delete"""
        self.root = AVLTree.delete_helper(self.root, val)

    @staticmethod
    def delete_helper(root_node: AVLNode, val: int):
        """delete helper"""
        if not root_node:
            return root_node

        if val < root_node.val:
            root_node.left = AVLTree.delete_helper(root_node.left, val)

        elif val > root_node.val:
            root_node.right = AVLTree.delete_helper(root_node.right, val)
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
            succesor = AVLTree.min_val_node(root_node.right)
            root_node.val = succesor.val
            root_node.right = AVLTree.delete_helper(root_node.right, succesor.val)

        root_node.height = 1 + max(
            AVLTree.get_height(root_node.left), AVLTree.get_height(root_node.right)
        )

        ht_diff = AVLTree.get_height_diff(root_node)

        if ht_diff > 1 and AVLTree.get_height_diff(root_node.left) >= 0:
            return AVLTree.right_rotate(root_node)  # LL

        if ht_diff > 1 and AVLTree.get_height_diff(root_node.left) < 0:
            root_node.left = AVLTree.left_rotate(root_node.left)  # LR
            return AVLTree.right_rotate(root_node)

        if ht_diff < -1 and AVLTree.get_height_diff(root_node.right) <= 0:
            return AVLTree.left_rotate(root_node)  # RR

        if ht_diff < -1 and AVLTree.get_height_diff(root_node.right) > 0:
            root_node.right = AVLTree.left_rotate(root_node.right)  # RL
            return AVLTree.left_rotate(root_node)

        return root_node

    @staticmethod
    def min_val_node(node: AVLNode):
        """min val node"""
        if not node or not node.left:
            return node
        return AVLTree.min_val_node(node.left)

    @staticmethod
    def get_height(node: AVLNode):
        """get height"""
        if not node:
            return 0
        return node.height

    @staticmethod
    def right_rotate(db_node: AVLNode):
        """right rotate"""
        temp = db_node.left
        db_node.left = temp.right
        temp.right = db_node

        db_node.height = 1 + max(
            AVLTree.get_height(db_node.left), AVLTree.get_height(db_node.right)
        )

        temp.height = 1 + max(
            AVLTree.get_height(temp.left), AVLTree.get_height(temp.right)
        )
        return temp

    @staticmethod
    def left_rotate(db_node: AVLNode):
        """lef rotate"""
        temp = db_node.right
        db_node.right = db_node.right.left
        temp.left = db_node

        db_node.height = 1 + max(
            AVLTree.get_height(db_node.left), AVLTree.get_height(db_node.right)
        )

        temp.height = 1 + max(
            AVLTree.get_height(temp.left), AVLTree.get_height(temp.right)
        )
        return temp

    @staticmethod
    def get_height_diff(node: AVLNode):
        """get_height_diff"""
        if not node:
            return 0
        return AVLTree.get_height(node.left) - AVLTree.get_height(node.right)
    
    def clear(self):
        """clear"""
        self.root.val = None
        self.root.left = None
        self.root.right = None
