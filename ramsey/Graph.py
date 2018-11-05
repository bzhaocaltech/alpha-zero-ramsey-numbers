import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

# Undirected graph represented by adjacency matrix with values serving as colors
class Graph:
    # Constructor for graph.
    # has_clique: flag set if the graph contains a clique
    # n: Number of nodes in the graph
    # adj_mat: The adjacency matrix itself
    # num_edges: Number of colored (non-zero) edges
    def __init__(self, n, updates=False):
        self.has_clique = False
        self.n = n
        self.adj_mat = np.zeros((self.n, self.n))
        self.num_edges = 0
        self.total_edges = (n * (n - 1)) // 2

    def __str__(self):
        return np.array_str(self.adj_mat)

    # Displays the graph using matplotlib and networkx
    def display(self):
        G = nx.from_numpy_matrix(self.adj_mat)
        for i in range(self.n):
            for j in range(self.n):
                if self.adj_mat[i, j] == 1:
                    G[i][j]["color"] = "r"
                elif self.adj_mat[i, j] == -1:
                    G[i][j]["color"] = "b"
        edges = G.edges()
        colors = [G[u][v]['color'] for u, v in edges]
        pos = nx.circular_layout(G)
        nx.draw(G, pos, edges=edges, edge_color=colors, node_color="yellow", with_labels=True)
        plt.show()

    # Check if subgraph is a monochromatic clique of a given size and color
    def isClique(self, subgraph, color):
        return all(self.getEdgeColor(u, v) == color for u, v in combinations(subgraph, 2))

    # Check for monochromatic cliques of given sizes and colors
    def hasClique(self, colors):
        for color in colors:
            size = colors[color]
            for subgraph in combinations(range(self.n), size):
                if self.isClique(subgraph, color):
                    self.has_clique = True
                    return True

        return False

    # Get the color/weight of the edge (i, j)
    def getEdgeColor(self, i, j):
        return self.adj_mat[i, j]

    # Check if graph has edge (i, j)
    def hasEdge(self, i, j):
        return self.adj_mat[i, j] != 0

    # Color edge (i, j) c
    def colorEdge(self, i, j, c, colors=None):
        # Don't recolor edges
        assert self.adj_mat[i, j] == 0 and self.adj_mat[j, i] == 0
        self.adj_mat[i, j] = c
        self.adj_mat[j, i] = c
        self.num_edges += 1

        if colors:
            size = colors[c]
            for subgraph_without_edge in combinations([x for x in range(self.n) if x != i and x != j], size - 2):
                subgraph = list(subgraph_without_edge) + [i, j]
                if self.isClique(subgraph, c):
                    self.has_clique = True

    # Returns iterator over possible edges
    def edgeIter(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                yield (i, j)
