class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def preorder(root):
        if not root:
            return 

        print(root.data)
        TreeNode.preorder(root.left)
        TreeNode.preorder(root.right)    