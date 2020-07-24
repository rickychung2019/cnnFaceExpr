# cnnFaceExpr
Learning purpose CNN models. Aim to familiarise myself with Keras, Numpy, Matplotlib and to compare the performance of different nerual architectures.

Dataset used: icml_face_data.csv (Facial Expression Recognition Challenge https://www.kaggle.com/debanga/facial-expression-recognition-challenge?select=test.csv )<br />

Step1: Massaging the Dataset<br />
Unfortunately, the pixels of each image given by the dataset are just a series of string separated by whitespace. Have to turn it into 48x48 numpy.ndarray with dtype=float.

Step2: Defining Training Set and Validation Set<br />
The Facial Expression Recognition Challenge did not provide validation set. Thus, I will split icml_face_data.csv into training set and validation set. Ratio=3:1.

Step3: Defining Models<br />
Self-defined
VGG16
VGG19
ResNet50
ResNet101

Step4: Training<br />
After 100th epochs:<br />
Self-defined:<br />
loss:  - accuracy:  - val_loss:  - val_accuracy: <br />
VGG16:<br />
loss:  - accuracy:  - val_loss:  - val_accuracy: <br />
VGG19:<br />
loss:  - accuracy:  - val_loss:  - val_accuracy: <br />
ResNet50:<br />
loss:  - accuracy:  - val_loss:  - val_accuracy: <br />
ResNet101:<br />
loss:  - accuracy:  - val_loss:  - val_accuracy: <br />
