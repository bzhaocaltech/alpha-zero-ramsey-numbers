from copy import deepcopy
import sys
sys.path.append('..')
from Game import Game
from Graph import Graph


class RamseyGame(Game):

    def __init__(self, n, p, q):
        assert p >= 2 and q >= 2
        self.n = n
        # For indexing purposes colors keys must be [1, 2, ...]
        self.colors = {1: p, 2: q}
        # Maps index to action
        self.index_to_action = []
        for c in self.colors:
            for i in range(n):
                for j in range(i + 1, n):
                    self.index_to_action.append((i, j, c))

    # Maps action to index in action vector
    def action_to_index(self, i, j, c):
        assert i != j
        if i > j:
            i, j = j, i
        return self.n * i + j + ((c-1) * self.n * (self.n-1) - (i+1) * (i+2)) // 2

    # Return a graph representing the initial board state
    def getInitGraph(self):
        # return initial graph (numpy graph)
        return Graph(self.n)

    # Get the graph size
    def getGraphSize(self):
        return self.n

    def getActionSize(self):
        return len(self.index_to_action)

    def getNextStateFromAction(self, graph, action):
        i, j, c = action
        new_graph = deepcopy(graph)
        new_graph.colorEdge(i, j, c, self.colors)

        return new_graph

    # Given a graph and an action, returns a new graph after that action has
    # been made
    def getNextState(self, graph, index):
        return self.getNextStateFromAction(graph, self.index_to_action[index])

    # Get all valid actions one-hot encoded
    def getValidMoves(self, graph):
        # return a fixed size binary vector
        valid = [0] * self.getActionSize()

        for i, j in graph.edgeIter():
                if not graph.hasEdge(i, j):
                    for c in self.colors:
                        valid[self.action_to_index(i, j, c)] = 1

        return valid

    # Check if state is terminal by checking for monochromatic cliques of given size and color
    # and if there are uncolored edges remaining
    def getGameEnded(self, graph):
        if graph.has_clique:
            return True

        return graph.num_edges == graph.total_edges

    def stringRepresentation(self, graph):
        return str(graph)

    # Get the score of a graph. Equivalent to number of edges in the graph
    # minus an additional 1 if the graph has a clique
    def getScore(self, graph):
        reward = graph.num_edges
        return reward - 1 if graph.has_clique else reward

    def getCanonicalForm(self, graph):
        return graph.adj_mat

