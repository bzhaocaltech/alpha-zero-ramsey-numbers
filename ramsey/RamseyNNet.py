import sys
sys.path.append('..')
from utils import *

import argparse
from keras.models import *
from keras.layers import *
from keras.optimizers import *

import sys
sys.path.append('..')
from utils import *

import argparse
from keras.models import *
from keras.layers import *
from keras.optimizers import *

class RamseyNNet():
    def __init__(self, game, args):
        # game params
        self.graphSize = game.getGraphSize()
        self.action_size = game.getValidMoves()
        self.args = args

        # Neural Net
        self.input_boards = Input(shape=(self.graphSize, self.graphSize))
        self.model.add(layers.Dense(50, activation = "relu", input_shape=(self.graphSize, self.graphSize)))
        self.model.add(layers.Dropout(0.3, noise_shape=None, seed=None))
        self.model.add(layers.Dense(50, activation = "relu"))
        self.model.add(layers.Dropout(0.2, noise_shape=None, seed=None))
        self.model.add(layers.Dense(50, activation = "relu"))

        self.pi = Dense(self.action_size, activation='softmax', name='pi')(s_fc2)   # batch_size x self.action_size
        self.v = Dense(1, activation='tanh', name='v')(s_fc2)

        model.add(layers.Dense(1, activation = "sigmoid"))
