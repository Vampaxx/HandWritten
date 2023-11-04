import os
import pandas as pd
from pathlib import Path
import tensorflow as tf
from src.handwritten.logger import logging
from src.handwritten.exception import CustomException
from src.handwritten.utils.common import (read_yaml,
                                          create_directories)

from src.handwritten.constants import *
from src.handwritten.components.data_procesing import DataProcessing
from src.handwritten.entity.config_entity import (DataIngestionConfig,
                                                  PrepareBaseModelConfig,
                                                  PreprocessingConfig,
                                                  TrainigConfig,
                                                  EvaluationConfig)



class ConfugarationManager:

    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH):
        
        self.config_ = read_yaml(config_file_path)
        self.params_ = read_yaml(params_file_path)
        create_directories([self.config_.artifacts_root])
        #load Datapreprocessing 
        self.data_processing = DataProcessing(config=self.get_data_processing_config())
    

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config_ = self.config_.data_ingestion 
        create_directories([config_.root_dir])

        self.data_ingestion_config = DataIngestionConfig(
            train_data_path = Path(config_.train_data_path),
            test_data_path  = Path(config_.test_data_path),
            val_data_path   = Path(config_.val_data_path),
            raw_data_path   = Path(config_.raw_data_path),)
            
        return self.data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:

        config_ = self.config_.prepare_base_model 
        create_directories([config_.root_dir])
        prepare_base_model_Config   = PrepareBaseModelConfig(
            root_dir                = Path (config_.root_dir),
            base_model_path         = Path (config_.base_model_path), 
            updated_base_model_path = Path (config_.updated_base_model_path),
            params_image_size       = list (self.params_.IMAGE_SIZE),
            params_learning_rate    = float(self.params_.LEARNING_RATE))
                
        return prepare_base_model_Config


    def get_data_processing_config(self) -> PreprocessingConfig:
        config_                     = self.config_.data_ingestion
        self.data_processing_config = PreprocessingConfig(
            train_data_path = Path(config_.train_data_path),
            test_data_path  = Path(config_.test_data_path), 
            val_data_path   = Path(config_.val_data_path),
            image_size      = list(self.params_.IMAGE_SIZE),
            buffer_size     = int(self.params_.BUFFER_SIZE),
            batch_size      = int(self.params_.BATCH_SIZE))
        
        return self.data_processing_config
    

    def get_training_config(self) -> TrainigConfig:
        
        #self.dataset_type              = dataset_type
        self.training                   = self.config_.training 
        self.prepare_base_model         = self.config_.prepare_base_model
        training_data                   = self.data_processing.get_processing_data_path(dataset_type='train')
        testining_data                   = self.data_processing.get_processing_data_path(dataset_type='test')

        create_directories([Path(self.training.root_dir)])
        self.training_config                 = TrainigConfig(
            root_dir                        = Path(self.training.root_dir),
            trained_model_path              = Path(self.training.trained_model_path),
            updated_base_model_path         = Path(self.prepare_base_model.updated_base_model_path),
            train_data_for_pipeline         = self.data_processing.get_processing_pipeline(datas=training_data),
            test_data_for_pipeline          = self.data_processing.get_processing_pipeline(datas=testining_data),
            params_epochs                   = self.params_.EPOCHS,
            params_batch_size               = self.params_.BATCH_SIZE,
            params_image_size               = self.params_.IMAGE_SIZE,)
        
        return self.training_config
    

    def get_validation_config(self) -> EvaluationConfig:
        trainig         = self.config_.training 
        testining_data  = self.data_processing.get_processing_data_path(dataset_type='test')

        eval_config     = EvaluationConfig(
            path_of_model       = Path(trainig.trained_model_path),
            test_data           = self.data_processing.get_processing_pipeline(datas=testining_data),
            all_params          = self.params_,
            params_image_size   = self.params_.IMAGE_SIZE,
            params_batch_size   = self.params_.BATCH_SIZE,)
        return eval_config
    
        
    

if __name__ == "__main__":
    obj = ConfugarationManager()

    print(obj.get_validation_config().test_data)
    