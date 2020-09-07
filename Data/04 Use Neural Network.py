import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
print(tf.__version__)

print("======== Loading Model ==========")
model = tf.keras.models.load_model("saved_model_full")
print(model.summary())

inputs = []
