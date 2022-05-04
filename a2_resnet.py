import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50

# def to create our model
def get_model()
  model = ResNet50(include_top=True, weights="imagenet", input_shape=(224,224,3))
  print("[+] model loaded")
  return model
