from RamseyGame import RamseyGame

# game = RamseyGame(6, 3, 3)
# state = game.getInitGraph()
# state = game.getNextState(state, (0, 1, 1))
# state = game.getNextState(state, (1, 2, 1))
# state = game.getNextState(state, (0, 2, 1))
#
# state.display()
# print(game.getGameEnded(state))
# print(game.getScore(state))

game = RamseyGame(5, 3, 3)
state = game.getInitGraph()
for i in range(5):
    state = game.getNextState(state, (i, (i+1) % 5, 1))

state.display()
print(game.getGameEnded(state))
print(game.getScore(state))