from Tree.BST import BST, BSTNode
from Tree.BinaryTreeWithList import BinaryTreeWithList
from Tree.BinaryTree import TreeNode

if __name__ == "__main__":
    # root = TreeNode(0)
    # left = TreeNode(1)
    # right = TreeNode(2)
    # root.left = left
    # root.right = right
    # print(TreeNode.in_order(root))
    # print(TreeNode.search_bt(root,2))
    # TreeNode.del_bt(root)
    # TreeNode.level_order(root)

    root = BST(BSTNode(70))
    root.inser_node(50)
    root.inser_node(90)
    root.inser_node(30)
    root.inser_node(60)
    root.inser_node(80)
    root.inser_node(100)
    root.inser_node(20)
    root.inser_node(40)
    root.inser_node(10)

    # root.inorder()
    root.clear()
    root.inorder()


    # print(root.preorder_traversal())
    # print(root.postorder_traversal())
    # print(root.inorder_traversal())
    # root.level_order()
    # print(root.del_node(2))
    # root.level_order()
    # print(root.clear())

