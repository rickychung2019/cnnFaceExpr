#import tensorflow as tf
import pandas as pd
import numpy as np

def getData(file):
    data=pd.read_csv(file)
    return data.shape[0], data
def load():
    n,train=getData('train.csv')
    index=int(3*n/4)
    y_train=train['emotion'].iloc[0:index].to_numpy()
    x_train=[np.reshape(np.asarray(tmp.split(),dtype=float),(-1,48)) for tmp in train[' pixels'].iloc[0:index]]
    y_test=train['emotion'].iloc[index:-1].to_numpy()
    x_test=[np.reshape(np.asarray(tmp.split(),dtype=float),(-1,48)) for tmp in train[' pixels'].iloc[index:-1]]
    return x_train, y_train, x_test, y_test
