import os
import cv2
import uuid
import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

import random
from PIL import Image
from src.handwritten.utils.data_processing import load_image



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename

    
    def predict(self):
        model_path      = os.path.join('artifacts','training','model.h5')
        trained_model   = load_model(filepath=model_path,)    
        img             = load_image(self.filename)
        ex_img          = tf.expand_dims(img,axis=0)
        pred            = trained_model.predict(ex_img)
        pred            = tf.argmax(pred,axis=-1).numpy()[0]

        
        return  int(pred)
    

if __name__ == "__main__":
    prediction = PredictionPipeline(filename='3e6ba4dc-26c2-4897-8a3c-ccc7fcac747f.png')
    pred = prediction.predict()