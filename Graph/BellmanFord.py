class Graph:
    """Graph"""

    def __init__(self, vertices):
        self.v = vertices
        self.graph_matrix = []
        self.nodes = []

    def add_edge(self, s, d, w):
        """add_edge"""
        self.graph_matrix.append([s, d, w])

    def add_node(self, value):
        """addNode"""
        self.nodes.append(value)

    def print_soln(self, dist):
        """print_soln"""
        for key, value in dist.items():
            print(" " + key + ": ", value)

    def bellman_ford(self, src):
        """bellman_ford"""
        dist = {i: float("inf") for i in self.nodes}
        dist[src] = 0

        for _ in range(self.v - 1):
            for s, d, w in self.graph_matrix:
                if dist[s] != float("inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.graph_matrix:
            if dist[s] != float("inf") and dist[s] + w < dist[d]:
                print("graph has cycle")
                return

        self.print_soln(dist)
