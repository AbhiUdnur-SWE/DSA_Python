from collections import deque


class Graph:
    """graph"""

    def __init__(self):
        self.adj_lst = {}

    def add_vertex(self, vertex):
        """add_vertex"""
        if vertex not in self.adj_lst:
            self.adj_lst[vertex] = []
            return True
        return False

    def add_edge(self, vtx1, vtx2):
        """add_edge"""
        if vtx1 in self.adj_lst and vtx2 in self.adj_lst:
            self.adj_lst[vtx1].append(vtx2)
            self.adj_lst[vtx2].append(vtx1)
            return True
        return False

    def add_edge_unidirectional(self, vtx1, vtx2):
        """add_edge_unidirectional"""
        if vtx1 in self.adj_lst and vtx2 in self.adj_lst:
            self.adj_lst[vtx1].append(vtx2)
            return True
        return False

    def print_graph(self):
        """print_graph"""
        for vertex, edges in self.adj_lst.items():
            print(vertex, ":", edges)

    def remove_edge(self, vtx1, vtx2):
        """remove_edge"""
        try:
            if vtx1 in self.adj_lst and vtx2 in self.adj_lst:
                self.adj_lst[vtx1].remove(vtx2)
                self.adj_lst[vtx2].remove(vtx1)
                return True
            return False
        except Exception as e:
            print(e)
            return False

    def remove_edge_unidirectional(self, vtx1, vtx2):
        """remove_edge_unidirectional"""
        try:
            if vtx1 in self.adj_lst and vtx2 in self.adj_lst:
                self.adj_lst[vtx1].remove(vtx2)
                return True
            return False
        except Exception as e:
            print(e)
            return False

    def remove_vertex(self, vtx):
        """remove_vertex"""
        if vtx in self.adj_lst:
            for ovtx in self.adj_lst[vtx]:
                self.adj_lst[ovtx].remove(vtx)
            del self.adj_lst[vtx]
            return True
        return False

    def bfs(self, vertex):
        """bfs"""
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])
        while queue:
            current = queue.popleft()
            print(current)
            for adj_vrtx in self.adj_lst[current]:
                if adj_vrtx not in visited:
                    visited.add(adj_vrtx)
                    queue.append(adj_vrtx)

    def dfs(self, vertex):
        """dfs"""
        visited = set()
        stack = [vertex]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                print(current)
                for adj_vertex in self.adj_lst[current]:
                    if adj_vertex not in visited:
                        stack.append(adj_vertex)

    def topological_sort_util(self, v: str, stack: list, visited: list):
        """topological_sort_util"""
        visited.append(v)

        for i in self.adj_lst[v]:
            if i not in visited:
                self.topological_sort_util(i, stack, visited)

        stack.insert(0, v)

    def topological_sort(self):
        """topological_sort"""
        visited = []
        stack = []

        for i in self.adj_lst:
            if i not in visited:
                self.topological_sort_util(i, stack, visited)

        print(stack)
