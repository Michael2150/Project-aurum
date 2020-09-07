import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
print(tf.__version__)

import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling



def build_model():
  model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[len(input_data_set.keys())]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
  ])

  optimizer = tf.keras.optimizers.RMSprop(0.001)

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
  return model

def norm_data(data):
    train_stats = data.describe()
    print(train_stats)
    train_stats = train_stats.transpose()
    data = (data - train_stats['mean']) / train_stats['std']
    print(data)
    return data

def norm(x):
  train_stats = x.describe()
  print(train_stats)
  train_stats = train_stats.transpose()
  return (x - train_stats['mean']) / train_stats['std']


print("======== Reading Data ==========")
data_set = pd.read_csv("TrainingData.csv")
print(data_set)

print("======== Getting Relevent Input Data ==========")
corr_vals = data_set["correlation_coefficient"]
inputdata = {"correlation_coefficient":corr_vals}
input_data_set = pd.DataFrame(data=inputdata)
print(input_data_set)

print("======== Normalizing Input Data ==========")
input_data_set = norm_data(input_data_set)
print(input_data_set)

print("======== Getting Relevent Output Data ==========")
outputdifs = data_set["output_val"]
outputdata = {"output_&_lastval_difference":outputdifs}
output_data_set = pd.DataFrame(data=outputdata)
print(output_data_set)

print("======== Normalizing Output Data ==========")
output_data_set = norm_data(output_data_set)
print(output_data_set)


print("======== Building Model ==========")
model = build_model()
print(model.summary())

print("======== Training Model ==========")
EPOCHS = 10

print(input_data_set.keys()[0])


train_labels = ["Label"]

history = model.fit(
  input_data_set, train_labels,
  epochs=EPOCHS, validation_split = 0.2, verbose=0,
  callbacks=[tfdocs.modeling.EpochDots()])

