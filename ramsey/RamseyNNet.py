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
        self.action_size = game.getActionSize()
        self.args = args

        # Neural Net
        self.model = Sequential()
        self.model.add(Dense(50, activation = "relu", input_dim = self.graphSize * self.graphSize))
        self.model.add(Dropout(0.3, noise_shape=None, seed=None))
        self.model.add(Dense(50, activation = "relu"))
        self.model.add(Dropout(0.2, noise_shape=None, seed=None))
        self.model.add(Dense(50, activation = "relu"))

        self.pi = Dense(self.action_size, activation='softmax', name='pi')   # batch_size x self.action_size
        self.v = Dense(1, activation='tanh', name='v')

        self.model.add(Dense(1, activation = "sigmoid"))
