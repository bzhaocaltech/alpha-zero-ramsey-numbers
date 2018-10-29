from copy import deepcopy
import sys
sys.path.append('..')
from Game import Game
from Graph import Graph


class RamseyGame(Game):

    def __init__(self, n, p, q):
        self.n = n
        self.colors = {-1: p, 1: q}

    # Return a graph representing the initial board state
    def getInitGraph(self):
        # return initial graph (numpy graph)
        return Graph(self.n)

    # Get the graph size
    def getGraphSize(self):
        return self.n

    # Given a graph and an action, returns a new graph after that action has
    # been made
    def getNextState(self, graph, action):
        i, j, c = action
        new_graph = deepcopy(graph)
        new_graph.colorEdge(i, j, c)

        return new_graph

    # Get all valid actions
    # Actions are in form (i, j, c) where i and j are nodes and c is the
    # color to make edge (i, j)
    def getValidMoves(self, graph):
        # return a fixed size binary vector
        actions = []

        for i in range(self.n):
            for j in range(i + 1, self.n):
                if graph[i, j] == 0:
                    for c in self.colors:
                        actions.append((i, j, c))

        return actions

    # Check if state is terminal by checking for monochromatic cliques of given size and color
    # and if there are uncolored edges remaining
    def getGameEnded(self, graph):
        if graph.hasClique(self.colors):
            return True

        # Check for uncolored edges
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if graph.getEdgeColor(i, j) == 0:
                    return False

        # All edges colored
        return True

    def stringRepresentation(self, graph):
        return str(graph)

    # Get the score of a graph. Equivalent to number of edges in the graph
    # minus an additional 1 if the graph has a clique
    def getScore(self, graph):
        reward = graph.num_edges
        return reward - 1 if graph.has_clique else reward
