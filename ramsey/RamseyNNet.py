import sys
sys.path.append('..')
from utils import *

import argparse
from keras.models import *
from keras.layers import *
from keras.optimizers import *


class RamseyNNet:
    def __init__(self, game, args):
        # game params
        self.graphSize = game.getGraphSize()
        self.action_size = game.getActionSize()
        self.args = args

        # Neural Net
        self.input_boards = Input(shape=(self.graphSize * self.graphSize, ))
        layer1 = Dense(50, activation="relu")(self.input_boards)
        dropout1 = Dropout(0.3, noise_shape=None, seed=None)(layer1)
        layer2 = Dense(50, activation="relu")(dropout1)
        dropout2 = Dropout(0.3, noise_shape=None, seed=None)(layer2)

        self.pi = Dense(self.action_size, activation='softmax', name='pi')(dropout2)   # batch_size x self.action_size
        self.v = Dense(1, activation='tanh', name='v')(dropout2)

        self.model = Model(inputs=self.input_boards, outputs=[self.pi, self.v])

