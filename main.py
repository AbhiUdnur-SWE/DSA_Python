# from Graph.BellmanFord import Graph
from Graph.FloydWarshall_AllPairssp import floyd_warshall
from Graph.SSSPP_BFS import SSSPP_Graph
from Graph.SSSPP_DijKstras import Dijkstra, Node
from Graph.disjointset import DisjointSet
from Search.binary import binary_search_iter, binary_search_recur
from Sorting.heapsort import heapsort
from Sorting.quick_sort import quicksort
from Sorting.sort import bubble_sort, insertion_sort, merge_sort, selection_sort
from Tree.Trie import Trie
from Tree.BinaryHeap import BinaryHeap, HeapNode
from Tree.AVL import AVLNode, AVLTree
from Tree.BST import BST, BSTNode
from Tree.BinaryTreeWithList import BinaryTreeWithList
from Tree.BinaryTree import TreeNode

# from Graph.Kruskals import Graph
from Graph.Prims import Graph

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

    # root = BinaryHeap(HeapNode(5, "max"))
    # root.insert(4)
    # root.insert(5)
    # root.insert(2)
    # root.insert(1)
    # root.extract_node()
    # root.level_order_traversal()
    # root.clear()
    # print(root.level_order_traversal())
    # new_trie = Trie()
    # new_trie.insert("Hello")
    # new_trie.insert("Apple")
    # new_trie.insert("App")

    # print(new_trie.search("App"))
    # print(new_trie.delete("App"))
    # print(new_trie.search("App"))

    # lst = [5, 4, 1000, 2, 1]
    # print(binary_search_iter(lst, 1000))

    # cutomDict = {
    #     "a": ["b", "c"],
    #     "b": ["a", "d", "e"],
    #     "c": ["a", "e"],
    #     "d": ["b", "e", "f"],
    #     "e": ["d", "f", "c"],
    #     "f": ["d", "e"],
    # }

    # g = Graph()
    # g.add_vertex("a")
    # g.add_vertex("c")
    # g.add_vertex("e")
    # g.add_vertex("h")
    # g.add_vertex("f")
    # g.add_vertex("b")
    # g.add_vertex("d")
    # g.add_vertex("g")

    # g.add_edge_unidirectional("a", "c")
    # g.add_edge_unidirectional("c", "e")
    # g.add_edge_unidirectional("e", "h")
    # g.add_edge_unidirectional("e", "f")
    # g.add_edge_unidirectional("f", "g")
    # g.add_edge_unidirectional("b", "d")
    # g.add_edge_unidirectional("b", "c")
    # g.add_edge_unidirectional("d", "f")

    # g.print_graph()
    # print(g.remove_vertex("a"))
    # # g.print_graph()
    # g.topological_sort()

    # custome_dict = {
    #     "a" : ["b", "c"],
    #     "b" : ["d", "G"],
    #     "c" : ["d", "e"],
    #     "d" : ["f"],
    #     "e" : ["f"],
    #     "g" : ["f"]
    # }

    # g = SSSPP_Graph(custome_dict)
    # print(g.bfs("a", "f"))

    # nodeA = Node("A")
    # nodeB = Node("B")
    # nodeC = Node("C")
    # nodeD = Node("D")
    # nodeE = Node("E")
    # nodeF = Node("F")
    # nodeG = Node("G")
    # nodeH = Node("H")

    # nodeA.add_edge(6, nodeB)
    # nodeA.add_edge(10, nodeC)
    # nodeA.add_edge(9, nodeD)

    # nodeB.add_edge(5, nodeD)
    # nodeB.add_edge(16, nodeE)
    # nodeB.add_edge(13, nodeF)

    # nodeC.add_edge(6, nodeD)
    # nodeC.add_edge(5, nodeH)
    # nodeC.add_edge(21, nodeG)

    # nodeD.add_edge(8, nodeF)
    # nodeD.add_edge(7, nodeH)

    # nodeE.add_edge(10, nodeG)

    # nodeF.add_edge(4, nodeE)
    # nodeF.add_edge(12, nodeG)

    # nodeH.add_edge(2, nodeF)
    # nodeH.add_edge(14, nodeG)

    # algo = Dijkstra()
    # algo.calculate(nodeA)
    # algo.get_shortest_path(nodeG)
    # print()

    # g = Graph(5)
    # g.add_node("A")
    # g.add_node("B")
    # g.add_node("C")
    # g.add_node("D")
    # g.add_node("E")

    # g.add_edge("A", "C", 6)
    # g.add_edge("A", "D", 6)
    # g.add_edge("B", "A", 3)
    # g.add_edge("C", "D", 1)
    # g.add_edge("D", "C", 2)
    # g.add_edge("D", "B", 1)
    # g.add_edge("E", "B", 4)
    # g.add_edge("E", "D", 2)
    # g.bellman_ford("E")

    # INF = 999
    # g = [
    #         [0, 8, INF, 1],
    #         [INF, 0, 1, INF],
    #         [4, INF, 0, INF],
    #         [INF, 2, 9, 1]
    #     ]

    # floyd_warshall(4, g)

    # vertices = ["A", "B", "C", "D", "E"]

    # ds = DisjointSet(vertices)
    # ds.union("A", "B")
    # ds.union("B", "C")
    # print(ds.find("C"))

    # g = Graph(5)
    # g.add_node("A")
    # g.add_node("B")
    # g.add_node("C")
    # g.add_node("D")
    # g.add_node("E")

    # g.add_edge("A","B",5)
    # g.add_edge("A","C",13)
    # g.add_edge("A","E",15)
    # g.add_edge("B","A",5)
    # g.add_edge("B","C",10)
    # g.add_edge("B","D",8)
    # g.add_edge("C","A",13)
    # g.add_edge("C","B",10)
    # g.add_edge("C","E",20)

    # g.add_edge("C", "D", "6")
    # g.add_edge("D", "B", "8")
    # g.add_edge("D", "C", "6")
    # g.add_edge("E", "A", "15")
    # g.add_edge("E", "C", "20")

    # g.kruskals_algo()

    g = Graph(5)
    g.graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]

    g.prims_mst()
