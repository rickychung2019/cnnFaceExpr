import argparse

check=["diyModel", "VGG16", "VGG19", "ResNet50", "ResNet101"]
parser=argparse.ArgumentParser()
parser.add_argument(
  "model",
  help="Choose the type of model from [diyModel, VGG16, VGG19, ResNet50, ResNet101]"
)
parser.add_argument(
  "-n",
  '--new',
  default=False,
  action='store_true',
  help="Create new model in current directory. Existing model will be overwritten if they are the same type. Default=False"
)
parser.add_argument(
  "-b",
  "--batch_size",
  nargs='?',
  default=32,
  help="Batch size. Default=32"
)
parser.add_argument(
  "-e",
  "--epochs",
  nargs='?',
  default=100,
  help="Epochs. Default=100"
)
args=parser.parse_args()

print("Chosen: ",args.model)

if args.model not in check:
    print("Error: Chosen Model not in", check)
    exit()

import tensorflow as tf
import data
import model

print("Loading data...")
x_train,y_train,x_test,y_test=data.load()

if args.new==True:
    if args.model=="diyModel":
        model=model.diyModel()
    elif args.model=="VGG16":
        model=model.vgg16()
    elif args.model=="VGG19":
        model=model.vgg19()
    elif args.model=="ResNet50":
        model=model.ResNet50()
    elif args.model=="ResNet101":
        model=model.ResNet101()
else:
    model = tf.keras.models.load_model("./"+str(args.model)+".h5")

model.fit(x_train, y_train, validation_data=(x_test,y_test), epochs=args.epochs, batch_size=args.batch_size)

model.save("./"+str(args.model)+".h5")
print("Saved")
