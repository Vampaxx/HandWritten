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


@dataclass(frozen=True)
class PreprocessingConfig:

    train_data_path : Path
    test_data_path  : Path
    val_data_path   : Path
    image_size      : list
    buffer_size     : int
    batch_size      : int


@dataclass(frozen=True)
class TrainigConfig:
    root_dir                : Path
    trained_model_path      : Path
    updated_base_model_path : Path
    train_data_for_pipeline : tf.data.Dataset
    test_data_for_pipeline  : tf.data.Dataset
    params_epochs           : int
    params_batch_size       : int
    params_image_size       : list


@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model       : Path
    test_data           : tf.data.Dataset
    all_params          : dict
    params_image_size   : list
    params_batch_size   : int
