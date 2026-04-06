from Tree import simpleTree
from Tree.BinaryTree import TreeNode

if __name__ == "__main__":
    # root = simpleTree.SimpleTree(1, [])
    # node2 = simpleTree.SimpleTree(2, [])
    # node3 = simpleTree.SimpleTree(3, [])
    # node4 = simpleTree.SimpleTree(4, [])
    # node5 = simpleTree.SimpleTree(5, [])
    # node6 = simpleTree.SimpleTree(6, [])

    # root.AddChild(node2)
    # root.AddChild(node3)
    # node2.AddChild(node4)
    # node3.AddChild(node5)
    # node3.AddChild(node5)
    # node2.AddChild(node6)
    # print(root)

    root = TreeNode("drinks")
    left = TreeNode("cold")
    right = TreeNode("hot")

    root.left = left
    root.right = right
    print(TreeNode.preorder(root))
