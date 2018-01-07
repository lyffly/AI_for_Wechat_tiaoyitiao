# -*- coding: utf-8 -*- 
#  人工智能跳一跳助手 by 刘云飞
import sys
import numpy as np
import random
from keras import layers
from keras import models
from keras.utils import plot_model

def get_model():
    model = models.Sequential()
    model.add(layers.Conv2D(16,(3,3),activation='relu',input_shape=(135,240,3),padding = 'same'))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Conv2D(32,(3,3),activation='relu',padding = 'same'))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Conv2D(64,(3,3),activation='relu',padding = 'same'))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Conv2D(64,(3,3),activation='relu',padding = 'same'))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Conv2D(128,(3,3),activation='relu',padding = 'same'))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Flatten())
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(128,activation="relu"))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(27,activation="softmax"))

    return model

#model.summary()
#plot_model(model, to_file='model.png')
