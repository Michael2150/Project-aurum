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

#normalizes
def norm_data(x):
  return(x-x.mean())/x.std()

print("======== Reading Data ==========")
data_set = pd.read_csv("TrainingDataAll.csv")
print(data_set.tail())

print("======== Splitting Data ==========")
train_data_set = data_set.sample(frac=0.8,random_state=0)
test_data_set = data_set.drop(train_data_set.index)

print("======== Getting Relevent Input Data ==========")
corr_vals = train_data_set["correlation_coefficient"]
inputdata = {"correlation_coefficient":corr_vals}
input_data_set = pd.DataFrame(data=inputdata)
print(input_data_set)

print("======== Normalizing Input Data ==========")
input_data_set = norm_data(input_data_set)
print(input_data_set)

print("======== Getting Relevent Output Data ==========")
outputdifs = train_data_set["output_val"]
outputdata = {"output_&_lastval_difference":outputdifs}
output_data_set = pd.DataFrame(data=outputdata)
print(output_data_set)

print("======== Normalizing Output Data ==========")
output_data_set = norm_data(output_data_set)
print(output_data_set)

print("======== Building Model ==========")
model = build_model()
print(model.summary())

print("======== Testing Model Outputs ==========")
example_batch = input_data_set[:10]
print("input batch: " + str(example_batch))
example_output = model.predict(example_batch)
print("output: " + str(example_output))

print("======== Training Model ==========")
EPOCHS = 1000
history = model.fit(
  input_data_set, output_data_set,
  epochs=EPOCHS, validation_split = 0.2, verbose=0,
  callbacks=[tfdocs.modeling.EpochDots()])

#Shows training data.
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
print(hist.tail())

print("======== Saving Model ==========")
tf.keras.models.save_model(model,'saved_model')
print("Saved")

plt.plot(hist["epoch"],hist["loss"])
plt.title("Loss over epoch")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()




