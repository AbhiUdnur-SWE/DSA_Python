from Tree.BinaryHeap import BinaryHeap, HeapNode
from Tree.AVL import AVLNode, AVLTree
from Tree.BST import BST, BSTNode
from Tree.BinaryTreeWithList import BinaryTreeWithList
from Tree.BinaryTree import TreeNode

if __name__ == "__main__":
    pass
    # root = TreeNode(0)
    # left = TreeNode(1)
    # right = TreeNode(2)
    # root.left = left
    # root.right = right
    # print(TreeNode.in_order(root))
    # print(TreeNode.search_bt(root,2))
    # TreeNode.del_bt(root)
    # TreeNode.level_order(root)

    # root = BST(BSTNode(70))
    # root.inser_node(50)
    # root.inser_node(90)
    # root.inser_node(30)
    # root.inser_node(60)
    # root.inser_node(80)
    # root.inser_node(100)
    # root.inser_node(20)
    # root.inser_node(40)
    # root.inser_node(10)

    # # root.inorder()
    # root.delete(100)
    # root.inorder()

    # root = AVLTree(AVLNode(10))
    # root.insert(20)
    # root.insert(30)
    # root.insert(40)
    # root.insert(50)
    # root.insert(60)
    # root.insert(70)
    # root.insert(80)

    # # root.inorder()
    # root.clear()
    # root.level_order()

    root = BinaryHeap(HeapNode(5, "max"))
    root.insert(4)
    root.insert(5)
    root.insert(2)
    root.insert(1)
    root.extract_node()
    root.level_order_traversal()
    root.clear()
    print(root.level_order_traversal())
