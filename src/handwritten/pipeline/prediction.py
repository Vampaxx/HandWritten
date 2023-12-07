import os
import base64
import tensorflow as tf
from tensorflow.keras.models import load_model

from PIL import Image
from src.handwritten.utils.data_processing import base64_decode


class PredictionPipeline:

    def __init__(self,file):
        self.file = file 
    def prediction(self):
        model_path      = os.path.join('artifacts','training','model.h5') 
        trained_model   = load_model(model_path)

        image_binary    = self.file.read()    
        image_base64    = base64.b64encode(image_binary).decode('utf-8')
        #decode base64
        image_array         = base64_decode(image_base64)
        image_array         = image_array / 255.0
        image_array         = image_array.reshape(28,28,1)

        ex_img          = tf.expand_dims(image_array,axis=0)
        pred            = trained_model.predict(ex_img)
        pred            = tf.argmax(pred,axis=-1).numpy()[0]
        return image_base64,int(pred)
        
if __name__ == "__main__":
    print('hey')
    #prediction = PredictionPipeline(filename='3e6ba4dc-26c2-4897-8a3c-ccc7fcac747f.png')
    #pred = prediction.predict()  