from __future__ import absolute_import, division, print_function

import os

import tensorflow as tf
from tensorflow import keras


import cv2
import glob
import math
import os
#import image


#from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import metrics

from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

train_dataset = pd.read_csv(
  "train.csv",
  sep=",",
  header=None)
  
test_dataset = pd.read_csv(
  "test.csv",
  sep=",",
  header=None)
  
def parse_labels_and_features(dataset):
  """Extracts labels and features.
  
  This is a good place to scale or transform the features if needed.
  
  Args:
    dataset: A Pandas `Dataframe`, containing the label on the first column and
      monochrome pixel values on the remaining columns, in row major order.
  Returns:
    A `tuple` `(labels, features)`:
      labels: A Pandas `Series`.
      features: A Pandas `DataFrame`.
  """
  labels = dataset[0]

  # DataFrame.loc index ranges are inclusive at both ends.
  features = dataset.loc[:,1:1024]
  # Scale the data to [0, 1] by dividing out the max value, 255.
  features = features / 255

  return labels, features
  
  
train_labels, train_images = parse_labels_and_features(train_dataset[:15000])
test_labels, test_images = parse_labels_and_features(test_dataset[:15000])

# Returns a short sequential model
def create_model():
  model = tf.keras.models.Sequential([
    keras.layers.Dense(1024, activation=tf.nn.relu, input_shape=(1024,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(512, activation=tf.nn.relu),
    keras.layers.Dense(512, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
  ])
  
  model.compile(optimizer=tf.keras.optimizers.Adam(), 
                loss=tf.keras.losses.sparse_categorical_crossentropy,
                metrics=['accuracy'])
  
  return model


# Create a basic model instance
model = create_model()
model.summary()

checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create checkpoint callback
cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path, 
                                                 save_weights_only=True,
                                                 verbose=1)

model = create_model()

model.fit(train_images, train_labels, batch_size=50, epochs = 100, 
          validation_data = (test_images,test_labels),
          callbacks = [cp_callback])  # pass callback to training
          
          
#!ls {checkpoint_dir}

          
  
