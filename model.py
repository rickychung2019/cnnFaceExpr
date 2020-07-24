import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Flatten, Dense

def diyModel():
    model=tf.keras.models.Sequential()
    model.add(
      Conv2D(
        64,
        kernel_size=4,
        activation='relu',
        input_shape=(48,48,1)
      )
    )
    model.add(
      Conv2D(
        32,
        kernel_size=4,
        activation='relu',
        input_shape=(48,48,1)
      )
    )
    model.add(
      Conv2D(
        16,
        kernel_size=4,
        activation='relu',
        input_shape=(48,48,1)
      )
    )
    model.add(Flatten())
    model.add(
      Dense(
        7,
        activation='softmax'
      )
    )
    model.compile(
      optimizer='adam',
      loss='categorical_crossentropy',
      metrics=['accuracy'],
    )
    return model

def vgg16():
    model=tf.keras.applications.VGG16(
      include_top=True,
      weights=None,
      input_shape=(48,48,1),
      classes=7,
    )
    model.compile(
      optimizer='adam',
      loss='categorical_crossentropy',
      metrics=['accuracy'],
    )
    return model

def vgg19():
    model=tf.keras.applications.VGG19(
      include_top=True,
      weights=None,
      input_shape=(48,48,1),
      classes=7,
    )
    model.compile(
      optimizer='adam',
      loss='categorical_crossentropy',
      metrics=['accuracy'],
    )
    return model

def resnet50():
    model=tf.keras.applications.ResNet50(
      include_top=True,
      weights=None,
      input_shape=(48,48,1),
      classes=7,
    )
    model.compile(
      optimizer='adam',
      loss='categorical_crossentropy',
      metrics=['accuracy'],
    )
    return model

def resnet101():
    model=tf.keras.applications.ResNet101(
      include_top=True,
      weights=None,
      input_shape=(48,48,1),
      classes=7,
    )
    model.compile(
      optimizer='adam',
      loss='categorical_crossentropy',
      metrics=['accuracy'],
    )
    return model
