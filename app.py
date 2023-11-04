import os
import cv2
import numpy as np
from pathlib import Path

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask, request, render_template

from src.handwritten.pipeline.prediction import PredictionPipeline
from src.handwritten.utils.data_processing import load_image




app             = Flask(__name__)
UPLOAD_FOLDER   = "\\Users\\Asus\\vs_code\\handwritten\\static"
upload_file_path        = os.path.join(UPLOAD_FOLDER,'upload')

class ClientApp:
    def __init__(self):
        self.filename = ""
    def init_classifier(self):
        self.classifier = PredictionPipeline(self.filename)

@app.route("/", methods=["GET","POST"])
def upload_predict():
    if not os.path.exists(upload_file_path):
        os.makedirs(upload_file_path)

    if request.method == 'POST':
        image_file = request.files['image']
        if image_file:
            image_location = os.path.join(upload_file_path,image_file.filename)
            image_file.save(image_location)

            image_jpeg_file = os.path.splitext(image_location)[0] + ".jpeg"
            img_file        = os.path.basename(image_jpeg_file)
            img             = cv2.imread(image_location)
            cv2.imwrite(image_jpeg_file, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


            #prediction
            clApp.filename = image_location         
            clApp.init_classifier()  
            pred    = clApp.classifier.predict()

            return render_template('index.html', prediction = pred ,image_loc= img_file )
        
    return render_template('index.html',prediction='Please Upload files',mask_loc=None, image_loc = None)







    return render_template('index.html',Prediction='Upload the Handwritten file')
    

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(debug=True)

    