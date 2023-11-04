import sys
from src.handwritten.logger import logging
from src.handwritten.exception import CustomException
from src.handwritten.config.configuration import ConfugarationManager
from src.handwritten.components.training import Training



STAGE_NAME = "Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_for_training         = ConfugarationManager()
        trainig_config              = config_for_training.get_training_config()
        training                    = Training(config=trainig_config)
        training.get_base_model()
        training.train()



if __name__ == '__main__':
    try:
        logging.info(f"*******************")
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e,sys)
        
        


