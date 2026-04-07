"""Binary tree module with tree node and traversal operations."""
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
        while not q.isEmpty():
            root = q.dequeue()
            print(root.data)
            if root.left is not None:
                q.enqueue(root.left)

            if root.right is not None:
                q.enqueue(root.right)
