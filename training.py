#!/usr/bin/env python
# coding: utf-8

# source ~/venv/bin/activate

import argparse
import csv
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import random
import sys
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


class MyTraining:
    def __init__(self, height, width, chanel):
        self.height = height
        self.width = width
        self.chanel = chanel
        self.batch = 100
        self.label_dict = {}
        self.img_dict = {}
        self.img_label_dict = {}
        self.test_ratio = 0.1
        self.test_set = set()
        self.train_set = set()

    def LoadData(self, path):
        for filename in os.listdir(path):
            if filename.endswith(".jpg") or filename.endswith(".JPG"):
                img = cv2.imread(path + filename)
                self.img_dict[filename] = img
        # print(self.img_dict)

    def LoadLabel(self, file):
        with open(file) as label_file:
            reader = csv.reader(label_file)
            for row in reader:
                self.label_dict[row[0]] = row[1]
        # print(self.label_dict)

    def SplitTestData(self):
        test_size = int(self.test_ratio * len(self.label_dict))
        # print(test_size)
        while test_size > 0:
            item = random.choice(list(self.label_dict.items()))
            if item[0] in self.test_set:
                continue
            self.test_set.add(item[0])
            test_size = test_size - 1
        # print(self.test_set)

        for key in self.label_dict.keys():
            if key in self.test_set:
                continue
            self.train_set.add(key)
        # print(self.train_set)
        # print(len(self.train_set))

    def RunModel(self, path):
        # Input
        img_inputs = keras.Input(shape=(self.height, self.width, self.chanel))
        print(img_inputs.shape)

        model = keras.Sequential()
        model.add(layers.Conv2D(filters=6, kernel_size=(3, 3), activation='relu',
                                input_shape=(self.height, self.width, self.chanel)))
        model.add(layers.AveragePooling2D())
        model.add(layers.Conv2D(
            filters=16, kernel_size=(3, 3), activation='relu'))
        model.add(layers.AveragePooling2D())
        model.add(layers.Flatten())
        model.add(layers.Dense(units=120, activation='relu'))
        model.add(layers.Dense(units=84, activation='relu'))
        model.add(layers.Dense(units=1, activation='relu'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, default=os.getcwd() + '/data/Video/',
                        help='The path of input data')
    parser.add_argument('-l', '--label', type=str, default=os.getcwd() + '/data/Video_label.csv',
                        help='The path of data label')
    args = parser.parse_args()
    path = str(args.input)
    label = str(args.label)
    dim = []
    for filename in os.listdir(path):
        if filename.endswith(".jpg") or filename.endswith(".JPG"):
            img = cv2.imread(path + filename)
            dim = img.shape
            break
    my_training = MyTraining(dim[0], dim[1], dim[2])
    my_training.LoadData(path)
    my_training.LoadLabel(label)
    my_training.SplitTestData()
    # my_training.RunModel(path)
