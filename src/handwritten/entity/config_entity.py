import os
import sys
import tensorflow as tf
from pathlib import Path
from dataclasses import dataclass




@dataclass(frozen=True)
class DataIngestionConfig:

    train_data_path  : Path
    test_data_path   : Path
    val_data_path    : Path
    raw_data_path    : Path 


@dataclass(frozen=True)
class PrepareBaseModelConfig:

    root_dir                : Path
    base_model_path         : Path
    updated_base_model_path : Path  
    params_image_size       : list
    params_learning_rate    : float
