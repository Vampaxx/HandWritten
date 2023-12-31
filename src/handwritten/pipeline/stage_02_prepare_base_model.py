import sys
from src.handwritten.logger import logging
from src.handwritten.exception import CustomException
from src.handwritten.config.configuration import ConfugarationManager
from src.handwritten.components.prepare_base_model import PrepareBaseModel


STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipeline:

    def __init__(self) -> None:
        pass

    def main(self):
        config                      = ConfugarationManager()
        prepare_base_model_config   = config.get_prepare_base_model_config()
        prepare_base_model          = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model_and_updated_model()
        


if __name__ == "__main__":
    try:
        logging.info('***************************************')
        logging.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj         = PrepareBaseModelTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
        logging.info('***************************************')
    except Exception as e:
        raise CustomException(e,sys)
        