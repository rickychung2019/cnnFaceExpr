#import tensorflow as tf
import pandas as pd
import numpy as np

def getData(file):
    data=pd.read_csv(file)
    return data.shape[0], data
def load():
    n,train=getData('train.csv')
    index=int(3*n/4)

    y_train=tf.keras.utils.to_categorical(train['emotion'].iloc[0:index].to_numpy())
    x_train=np.asarray([np.reshape(np.asarray(tmp.split(),dtype=float),(-1,48)) for tmp in train[' pixels'].iloc[0:index]]).reshape(index,48,48,1)
    y_test=tf.keras.utils.to_categorical(train['emotion'].iloc[index:n+1].to_numpy())
    x_test=np.asarray([np.reshape(np.asarray(tmp.split(),dtype=float),(-1,48)) for tmp in train[' pixels'].iloc[index:n+1]]).reshape(n-index,48,48,1)

    return x_train, y_train, x_test, y_test
