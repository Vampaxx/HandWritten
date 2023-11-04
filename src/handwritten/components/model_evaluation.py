import tensorflow as tf
from pathlib import Path
from src.handwritten.logger import logging 
from src.handwritten.exception import CustomException
from src.handwritten.utils.common import save_json
from src.handwritten.config.configuration import  ConfugarationManager
from src.handwritten.entity.config_entity import EvaluationConfig






class Evaluation:

    def __init__(self,config : EvaluationConfig) :
        self.config     = config

    @staticmethod
    def load_model(path:Path) -> tf.keras.models:
        return tf.keras.models.load_model(filepath=path)    
    
    
    def evaluation(self):
        logging.info(f'Model loaded from {self.config.path_of_model}')
        self.model      = self.load_model(self.config.path_of_model)
        logging.info(f'Model evaluation initialization')
        self.score      = self.model.evaluate(self.config.test_data)
        logging.info('Evaluation completed')
        print(self.score)
    
    def save_score(self):
        scores  = { 'loss'      : self.score[0],
                   'accuracy'   : self.score[1]}
        
        save_json(path=Path("scores.json"),data=scores)
        logging.info(f"Evaluation matrics saved on {'scores.json'}")



if __name__ == "__main__":
    config = ConfugarationManager()
    validation_config = config.get_validation_config()
    evaluation = Evaluation(validation_config)
    evaluation.evaluation()
    evaluation.save_score()