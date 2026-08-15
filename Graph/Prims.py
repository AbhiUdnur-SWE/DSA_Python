# Library for INT_MAX
import sys


class Graph:
    """Graph"""
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def min_key(self, key, mstSet):
        """min_key"""
        min = sys.maxsize
        min_index = -1

        for v in range(self.v):
            if key[v] < min and mstSet[v] is False:
                min = key[v]
                min_index = v

        return min_index

    def prims_mst(self):
        """prims_mst"""

        key = [sys.maxsize] * self.v
        parent = [None] * self.v
        key[0] = 0
        mst_set = [False] * self.v
        parent[0] = -1

        for _ in range(self.v):

            u = self.min_key(key, mst_set)
            mst_set[u] = True
            for v in range(self.v):
                if (
                    self.graph[u][v] > 0
                    and mst_set[v] is False
                    and key[v] > self.graph[u][v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

    def print_mst(self, parent):
        """printMST"""
        print("Edge \tWeight")
        for i in range(1, self.v):
            print(parent[i], "-", i, "\t", self.graph[parent[i]][i])