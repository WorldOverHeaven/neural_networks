import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow import keras


train = pd.read_csv("data/segmentation.test")
test = pd.read_csv("data/segmentation.data")

print(f"{train.shape=}")
print(f"{test.shape=}")

val_dataframe = train.sample(frac=1)
train_dataframe = test.sample(frac=1)

print(
    "Using %d samples for training and %d for validation"
    % (len(train_dataframe), len(val_dataframe))
)


def dataframe_to_dataset(dataframe):
    dataframe = dataframe.copy()
    labels = dataframe.pop("REGION-CENTROID-COL")
    ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
    ds = ds.shuffle(buffer_size=len(dataframe))
    return ds


train_ds = dataframe_to_dataset(train_dataframe)
val_ds = dataframe_to_dataset(val_dataframe)
