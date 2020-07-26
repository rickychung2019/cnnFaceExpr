# cnnFaceExpr
Learning purpose CNN models. Aim to familiarise myself with Keras, Numpy, Matplotlib and to compare the performance of different nerual architectures.

Dataset used: icml_face_data.csv (Facial Expression Recognition Challenge https://www.kaggle.com/debanga/facial-expression-recognition-challenge?select=test.csv )<br />

Step1: Massaging the Dataset<br />
The pixels of each image given by the dataset are just a series of string separated by whitespace. Have to turn it into 48x48 numpy.ndarray with dtype=float.

Step2: Defining Training Set and Validation Set<br />
The Facial Expression Recognition Challenge did not provide validation set. Thus, I will split icml_face_data.csv into training set and validation set. Ratio=3:1.

Step3: Defining Models<br />
Self-defined
VGG16
VGG19
ResNet50
ResNet101

Step4: Training<br />
After 50th epochs, batch_size=32:<br />
Self-defined:<br />
loss: 0.7749 - accuracy: 0.7031 - val_loss: 12.1171 - val_accuracy: 0.2766<br />
VGG16:<br />
loss: 0.0216 - accuracy: 0.9921 - val_loss: 2.8355 - val_accuracy: 0.5870<br />
VGG19:<br />
loss: 0.0361 - accuracy: 0.9876 - val_loss: 3.2098 - val_accuracy: 0.5291<br />
ResNet50:<br />
loss: 0.0652 - accuracy: 0.9767 - val_loss: 2.6912 - val_accuracy: 0.5652<br />
ResNet101:<br />
loss: 0.1422 - accuracy: 0.9525 - val_loss: 2.6376 - val_accuracy: 0.5487<br />

After 100th epochs, batch_size=32:<br />
Self-defined:<br />
loss: 0.6586 - accuracy: 0.7649 - val_loss: 27.7895 - val_accuracy: 0.2796<br />
VGG16:<br />
loss: 0.0033 - accuracy: 0.9978 - val_loss: 4.0657 - val_accuracy: 0.5998<br />
VGG19:<br />
loss: 0.0049 - accuracy: 0.9971 - val_loss: 3.5715 - val_accuracy: 0.5941<br />
ResNet50:<br />
loss: 0.0410 - accuracy: 0.9847 - val_loss: 3.1054 - val_accuracy: 0.5672<br />
ResNet101:<br />
loss: 0.0243 - accuracy: 0.9915 - val_loss: 3.3740 - val_accuracy: 0.5281<br />
