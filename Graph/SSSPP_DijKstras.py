"""Single Source Shortest Path using Dijkstra's algorithm."""

import heapq


class Edge:
    """Edge"""

    def __init__(self, weight, str_vtx, end_vtx):
        self.weight = weight
        self.str_vtx: Node = str_vtx
        self.end_vtx: Node = end_vtx


class Node:
    """Node"""

    def __init__(self, name):
        self.name: str = name
        self.visited: bool = False
        self.predecessor = None
        self.neighbors: list[Edge] = []
        self.min_dist = float("inf")

    # region operators
    def __lt__(self, other):
        return self.min_dist < other.min_dist

    def __le__(self, other):
        return self.min_dist <= other.min_dist

    def __gt__(self, other):
        return self.min_dist > other.min_dist

    def __ge__(self, other):
        return self.min_dist >= other.min_dist

    def __eq__(self, other):
        return self.min_dist == other.min_dist

    def __ne__(self, other):
        return self.min_dist != other.min_dist

    # endregion

    def add_edge(self, weight, destination_vertex):
        """add_edge"""
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)


class Dijkstra:
    """Dijkstra"""

    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex: Node):
        """calculate"""
        start_vertex.min_dist = 0
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            # pop with lowest dist.
            actual_vertex: Node = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            # consider neighbors
            for edge in actual_vertex.neighbors:
                start = edge.str_vtx
                target = edge.end_vtx
                new_distance = start.min_dist + edge.weight

                if new_distance < target.min_dist:
                    target.min_dist = new_distance
                    target.predecessor = start
                    # update the heap
                    heapq.heappush(self.heap, target)
                    # [F-19, F-17]
            actual_vertex.visited = True

    def get_shortest_path(self, vertex: Node):
        """get_shortest_path"""
        print(vertex.min_dist)
        temp = vertex
        while temp:
            print(temp.name, end=" ")
            temp = temp.predecessor


# Detect Cycles  -- FYI purpose
def has_cycle_dfs(graph):
    """Detect cycle using DFS"""
    visited = set()
    rec_stack = set()  # recursion stack

    def dfs(vertex):
        visited.add(vertex)
        rec_stack.add(vertex)

        for edge in vertex.neighbors:
            neighbor = edge.end_vtx
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:  # Back edge = cycle
                return True

        rec_stack.remove(vertex)
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex):
                return True
    return False
