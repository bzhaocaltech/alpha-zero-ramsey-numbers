import os
import shutil
import sys
import numpy as np
sys.path.append('..')
from NeuralNet import NeuralNet
from RamseyNNet import RamseyNNet as onnet

# List of arguments to pass to onnet
args = {
    'lr': 0.001,
    'dropout': 0.3,
    'epochs': 10,
    'batch_size': 64,
}

class NNetWrapper(NeuralNet):
    def __init__(self, game):
        self.nnet = onnet(game, args)
        self.board_size = game.n
        self.action_size = game.getActionSize()

    # List of examples where each example is of form (board, pi, v)
    # board = graph
    # pi = MCTS informed policy vector (list of probabilities of choosing
    # each action)
    # v = Final score of player
    def train(self, examples):
        input_boards, target_pis, target_vs = list(zip(*examples))
        input_boards = np.asarray(input_boards)
        new_input_boards = []
        for board in input_boards:
            new_input_boards.append(board.adj_mat.flatten())
        new_input_boards = np.array(new_input_boards)
        target_pis = np.asarray(target_pis)
        target_vs = np.asarray(target_vs)
        self.nnet.model.fit(x = new_input_boards, y = [target_pis, target_vs], \
        batch_size = args["batch_size"], epochs = args["epochs"])

    # Board = graph
    def predict(self, board):
        adj_mat = board.adj_mat
        flat = adj_mat.flatten()
        flat = flat[np.newaxis, :]
        pi, v = self.nnet.model.predict(flat)

        return pi[0], v[0]

    def save_checkpoint(self, folder='checkpoint', filename='checkpoint.pth.tar'):
        filepath = os.path.join(folder, filename)
        if not os.path.exists(folder):
            print("Checkpoint Directory does not exist! Making directory {}".format(folder))
            os.mkdir(folder)
        else:
            print("Checkpoint Directory exists! ")
        self.nnet.model.save_weights(filepath)

    def load_checkpoint(self, folder='checkpoint', filename='checkpoint.pth.tar'):
        # https://github.com/pytorch/examples/blob/master/imagenet/main.py#L98
        filepath = os.path.join(folder, filename)
        if not os.path.exists(filepath):
            raise("No model in path '{}'".format(filepath))
        self.nnet.model.load_weights(filepath)
