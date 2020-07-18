# cnnFaceExpr
Learning purpose CNN models. Aim to familiarise myself with Keras, Numpy, Matplotlib and to compare the performance of different nerual architectures.

Dataset used: icml_face_data.csv https://www.kaggle.com/debanga/facial-expression-recognition-challenge?select=test.csv <br />
**Dataset would be divided into half for training and testing**

Step0: Massaging the dataset<br />
Unfortunately, the pixels of each image given by the dataset are just a series of string separated by whitespace. Have to turn it into 48x48 numpy.ndarray first.
