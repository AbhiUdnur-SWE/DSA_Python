from Graph.disjointset import DisjointSet as dst


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def add_edge(self, s, d, w):
        if isinstance(w, str):
            try:
                w = int(w)
            except ValueError:
                pass
        self.graph.append([s, d, w])

    def add_node(self, val):
        self.nodes.append(val)

    def print_soln(self, s, d, w):
        for s, d, w in self.MST:
            print(f"{s} - {d} : {w}")

    def kruskals_algo(self):
        i, e = 0, 0
        ds = dst(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.v - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s, d, w])
                ds.union(x, y)

        self.print_soln(s, d, w)

