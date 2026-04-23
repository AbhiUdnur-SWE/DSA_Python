"""Binary tree module with tree node and traversal operations."""

from collections import deque
from sys import path
from os.path import dirname, abspath

# Add parent directory to path to allow imports from sibling packages
path.insert(0, dirname(dirname(abspath(__file__))))

from Queue.QueueLL import Queue


class TreeNode:
    """Binary tree node with data and left/right children."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @staticmethod
    def pre_order(root):
        """pre order"""
        if not root:
            return
        print(root.data)
        TreeNode.pre_order(root.left)
        TreeNode.pre_order(root.right)

    @staticmethod
    def in_order(root):
        """In-order traversal of binary tree."""
        if not root:
            return

        TreeNode.in_order(root.left)
        print(root.data)
        TreeNode.in_order(root.right)

    @staticmethod
    def post_order(root):
        """post order"""
        if not root:
            return

        TreeNode.post_order(root.left)
        TreeNode.post_order(root.right)
        print(root.data)

    @staticmethod
    def level_order(root):
        """level order"""
        if not root:
            return
        q = Queue()
        q.enqueue(root)
        while not q.is_empty():
            root = q.dequeue()
            print(root.data)
            if root.left is not None:
                q.enqueue(root.left)

            if root.right is not None:
                q.enqueue(root.right)

    @staticmethod
    def search_bt(root, val):
        """Search BT"""
        if not root:
            return False

        q = Queue()
        q.enqueue(root)
        while not q.is_empty():
            root = q.dequeue()
            if root.data == val:
                return True

            if root.left:
                q.enqueue(root.left)

            if root.right:
                q.enqueue(root.right)

        return False

    @staticmethod
    def insert_bt(root, node):
        """insert_bt"""
        if not root:
            root = node

        q = Queue()
        q.enqueue(root)

        while not q.is_empty():
            root = deque()
            if not root.left:
                root.left = node
                return

            if not root.right:
                root.right = node
                return

            if root.left:
                q.enqueue(root.left)

            if root.right:
                q.enqueue(root.right)

    @staticmethod
    def get_deepest_node(root):
        """get Deepest Node"""
        if not root:
            return
        q = Queue()
        q.enqueue(root)
        while not q.is_empty():
            root = q.dequeue()
            # print(root.data)
            if root.left is not None:
                q.enqueue(root.left)

            if root.right is not None:
                q.enqueue(root.right)

        return root

    @staticmethod
    def del_deepest_node(root, dp_node):
        """get Deepest Node"""
        if not root:
            return
        q = Queue()
        q.enqueue(root)
        while not q.is_empty():
            root = q.dequeue()
            # print(root.data)
            if root.right:
                if root.right is dp_node:
                    root.right = None
                    return
                q.enqueue(root.right)

            if root.right:
                if root.right is dp_node:
                    root.right = None
                    return
                q.enqueue(root.right)

        return root

    @staticmethod
    def delete_node_bt(rootnode, node_data):
        """delete_node_bt"""
        if not rootnode:
            return
        q = Queue()
        q.enqueue(rootnode)
        while not q.is_empty():
            root = q.dequeue()
            if rootnode.data == node_data:
                dnode = TreeNode.get_deepest_node(rootnode)
                root.data = dnode.data
                TreeNode.del_deepest_node(rootnode, dnode)

            if root.left is not None:
                q.enqueue(root.left)

            if root.right is not None:
                q.enqueue(root.right)

    @staticmethod
    def del_bt(root):
        """del_node"""
        root.data = None
        root.left = None
        root.right = None
