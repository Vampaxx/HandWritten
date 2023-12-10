from datetime import datetime
from sql_connection import sql_connector
from flask import Flask, render_template,request
from src.handwritten.pipeline.prediction import PredictionPipeline



app = Flask(__name__)   

class ClientApp:
    def __init__(self):
        self.image = None
    def init_classifier(self):
        self.classifier = PredictionPipeline(self.image)

clApp = ClientApp()

@app.route('/',methods=['GET','POST'])
def home():
    conncetion,cursor = sql_connector()
    cursor.execute("""CREATE TABLE IF NOT EXISTS hand_written (
                   Id INT AUTO_INCREMENT PRIMARY KEY,
                   Time_stamp DATETIME,
                   Image_binary BLOB,
                   Prediction Float)""")
    
    conncetion.commit()
    if request.method == 'POST':
        quary = "INSERT INTO hand_written (Time_stamp,Image_binary,Prediction) VALUES (%s,%s,%s)"

        image           = request.files['image']
        if image:
            time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            clApp.image = image
            clApp.init_classifier()
            image_encoded,pred = clApp.classifier.prediction()

            cursor.execute(quary,(time_stamp,image_encoded,pred))
            
            conncetion.commit()
            return render_template('index_.html',image_loc=image_encoded, pred_= pred)
        conncetion.close()
        cursor.close()
    return render_template('index_.html',image_loc="upload image file")
    




if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)