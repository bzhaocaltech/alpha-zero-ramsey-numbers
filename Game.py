class Game:
    """
    This class specifies the base Game class. To define your own game, subclass
    this class and implement the functions below. This works when the game is
    single-player, adversarial and turn-based.
    """

    def __init__(self):
        pass

    def getInitGraph(self):
        """
        Returns:
            startgraph: a representation of the graph (ideally this is the form
                        that will be the input to your neural network)
        """
        pass

    def getGraphSize(self):
        """
        Returns:
            (x,y): a tuple of graph dimensions
        """
        pass

    def getActionSize(self):
        pass

    def getCanonicalForm(self, graph):
        pass

    def getNextState(self, graph, action):
        """
        Input:
            graph: current graph
            player: current player (1 or -1)
            action: action taken by current player

        Returns:
            nextgraph: graph after applying action
            nextPlayer: player who plays in the next turn (should be -player)
        """
        pass

    def getValidMoves(self, graph):
        """
        Input:
            graph: current graph
            player: current player

        Returns:
            validMoves: a binary vector of length self.getActionSize(), 1 for
                        moves that are valid from the current graph and player,
                        0 for invalid moves
        """
        pass

    def getGameEnded(self, graph):
        """
        Input:
            graph: current graph
            player: current player (1 or -1)

        Returns:
            r: 0 if game has not ended. 1 if player won, -1 if player lost,
               small non-zero value for draw.

        """
        pass

    def stringRepresentation(self, graph):
        """
        Input:
            graph: current graph

        Returns:
            graphString: a quick conversion of graph to a string format.
                         Required by MCTS for hashing.
        """
        pass