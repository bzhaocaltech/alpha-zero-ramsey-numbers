from RamseyGame import RamseyGame
from NNet import *

# Test 1: Has Clique
# game = RamseyGame(6, 3, 3)
# state = game.getInitGraph()
# state = game.getNextStateFromAction(state, (0, 1, 1))
# state = game.getNextStateFromAction(state, (1, 2, 1))
# state = game.getNextStateFromAction(state, (0, 2, 1))
#
# state.display()
# print(state.has_clique)
# print(game.getScore(state))
# print(game.getGameEnded(state))

# Test 2: No Clique
# game = RamseyGame(5, 3, 3)
# state = game.getInitGraph()
# for i in range(5):
#     action = (i, (i+1) % 5, 1)
#     index = game.action_to_index(*action)
#     state = game.getNextState(state, index)
#
# state.display()
# print(state.has_clique)
# print(game.getScore(state))
# print(game.getGameEnded(state))
#

# Test 3: RamseyNNet
game = RamseyGame(5, 3, 3)
nnet = NNetWrapper(game)
state = game.getInitGraph()
nnet.predict(state)
examples = [[state, game.getActionSize() * [0.1], 1]]
nnet.train(examples)
