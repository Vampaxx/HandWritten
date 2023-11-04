import tensorflow as tf
from pathlib import Path
from tensorflow.keras.callbacks import EarlyStopping
from src.handwritten.logger import logging
from src.handwritten.entity.config_entity import TrainigConfig
from src.handwritten.config.configuration import ConfugarationManager





class Training(ConfugarationManager):

    def __init__(self,config:TrainigConfig):
        super().__init__()
        self.config     = config
    
    def get_base_model(self):
        logging.info(f'Model is loading from {self.config.updated_base_model_path}')
        self.model = tf.keras.models.load_model(filepath=self.config.updated_base_model_path)
        logging.info('Completed loading model')
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def train(self):
        early_stop = EarlyStopping(monitor='val_loss',patience=5,verbose=1)
        logging.info('Initializing training')
        self.model.fit(            
            self.config.train_data_for_pipeline,
            validation_data = self.config.test_data_for_pipeline,
            epochs          = self.config.params_epochs,
            callbacks       = [early_stop])
        logging.info('Training completed')
        logging.info(f'Trained model saving in {self.config.trained_model_path}')
        self.save_model(
            path=self.config.trained_model_path,
            model=self.model)
        logging.info('saving completed')
 
        


        

if __name__ == "__main__":
    config_for_training         = ConfugarationManager()
    trainig_config              = config_for_training.get_training_config()
    training                    = Training(config=trainig_config)
    training.get_base_model()
    training.train()
    
