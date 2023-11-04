import cv2
import numpy as np
import tensorflow as tf


def preprocessing(data):
    data = data/255.0
    return data

def load_image(path: str):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    image = cv2.resize(image, (28, 28))
    image = image / 255.0
    image = image.reshape(28, 28, 1)  # Reshape to (28, 28, 1)
    return image