import sys
import numpy as np
import pandas as pd
import tensorflow as tf
from src.handwritten.exception import CustomException
from src.handwritten.logger import logging
from src.handwritten.utils.data_processing import preprocessing
#from src.handwritten.config.configuration import ConfugarationManager
from src.handwritten.entity.config_entity import PreprocessingConfig




class DataProcessing:

    def __init__(self, config: PreprocessingConfig):
        self.config_ = config

    def get_processing_data_path(self, dataset_type: str):
        logging.info('Started Data Transformation')
        try:
            self.dataset_type = dataset_type
            data_file_path = ""

            if self.dataset_type == 'train':
                data_file_path = self.config_.train_data_path 
            elif self.dataset_type == 'test':
                data_file_path = self.config_.test_data_path
            elif self.dataset_type == 'val':
                data_file_path = self.config_.val_data_path
            else:
                raise ValueError("Invalid data_type. Use 'train', 'test', or 'val'.")
            logging.info(f'{self.dataset_type} file is created')
            target_column_name = 'class'
            
            data = pd.read_csv(data_file_path)  

            logging.info('split the test data into independent and dependent features')
            x_data = data.drop(target_column_name, axis=1)
            y_data = data[target_column_name]
            logging.info('completed')
            logging.info('Data processing and reshaping started')

            pro_x_data = preprocessing(x_data)
            x_data_ = tf.reshape(pro_x_data, [-1] + self.config_.image_size)
            y_data_ = np.array(y_data)
            logging.info('Data processing and reshaping completed')
            return x_data_,y_data_
        
        except Exception as e:
            raise CustomException(e, sys)
        

    def get_processing_pipeline(self,datas):
        logging.info('image file converted into tensor')
        data = tf.data.Dataset.from_tensor_slices(datas)
        data = data.shuffle(buffer_size=self.config_.buffer_size,)# reshuffle_each_iteration=False)
        data = data.batch(self.config_.batch_size)
        data = data.prefetch(16)
        logging.info('image file converted into tensor is completed')
        
        return data    




        
        
if __name__ == "__main__":
    config                  = ConfugarationManager()
    data_processing_config  = config.get_data_processing_config()
    data_processing         = DataProcessing(config=data_processing_config)
    val                     = data_processing.get_processing_data_path('train')
    a = data_processing.get_processing_pipeline(val)
    print(a)

