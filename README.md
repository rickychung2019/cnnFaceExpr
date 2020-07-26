# cnnFaceExpr
Learning purpose CNN models. Aim to familiarise myself with Keras, Numpy, Matplotlib and to compare the performance of different nerual architectures.

Dataset used: icml_face_data.csv (Facial Expression Recognition Challenge https://www.kaggle.com/debanga/facial-expression-recognition-challenge?select=test.csv )<br />

Step1: Massaging the Dataset<br />
The pixels of each image given by the dataset are just a series of string separated by whitespace. Have to turn it into 48x48 numpy.ndarray with dtype=float.

Step2: Defining Training Set and Validation Set<br />
The Facial Expression Recognition Challenge did not provide validation set. Thus, I will split icml_face_data.csv into training set and validation set. Ratio=3:1.

Step3: Defining Models<br />
First Attempt:<br />
Self-defined: optimizer = "adam"<br />
VGG16: optimizer = "adam"<br />
VGG19: optimizer = "adam"<br />
ResNet50: optimizer = "adam"<br />
ResNet101: optimizer = "adam"<br />
##########################################<br />
Discover that VGG will not work with "adam" (no improvement during training). Thus change to "sgd"<br />
Second Attempt:<br />
Self-defined: optimizer = "adam"<br />
VGG16: optimizer = "sgd"<br />
VGG19: optimizer = "sgd"<br />
ResNet50: optimizer = "adam"<br />
ResNet101: optimizer = "adam"<br />
##########################################<br />
Discover that the models are overfitted after 100 epochs (loss significantly smaller than val_loss). Thus define all optimizer myself<br />
Third Attempt:<br />
self_adam = tf.keras.optimizers.Adam(learning_rate = 0.0005)<br />
self_sgd = tf.keras.optimizers.SGD(learning_rate = 0.005)<br />
Self-defined: optimizer = self_adam<br />
VGG16: optimizer = self_sgd<br />
VGG19: optimizer = self_sgd<br />
ResNet50: optimizer = self_adam<br />
ResNet101: optimizer = self_adam<br />
Step4: Training<br />
Second Attempt:<br />
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


