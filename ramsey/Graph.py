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
    def __init__(self, n):
        self.has_clique = False
        self.n = n
        self.adj_mat = np.zeros((self.n, self.n))
        self.num_edges = 0

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
    def isClique(self, subgraph, color, size):
        for i in range(size):
            for j in range(i + 1, size):
                u, v = subgraph[i], subgraph[j]
                if self.adj_mat[u, v] != color:
                    return False
        return True

    # Check for monochromatic cliques of given sizes and colors
    def hasClique(self, colors):
        for color in colors:
            size = colors[color]
            subgraphs = combinations(range(self.n), size)
            for subgraph in subgraphs:
                if self.isClique(subgraph, color, size):
                    self.has_clique = True
                    return True

        return False

    # Get the color/weight of the edge (i, j)
    def getEdgeColor(self, i, j):
        return self.adj_mat[i, j]

    # Color edge (i, j) c
    def colorEdge(self, i, j, c):
        # Don't recolor edges
        assert self.adj_mat[i, j] == 0 and self.adj_mat[j, i] == 0
        self.adj_mat[i, j] = c
        self.adj_mat[j, i] = c
        self.num_edges += 1
