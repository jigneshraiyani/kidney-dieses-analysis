import os
from cnnClassifier.constants import *
from cnnClassifier.utils.util import read_yaml, create_directories
from cnnClassifier.entity.config_entity import (DataIngestionConfig, PrepareBaseModelConfig, TrainingConfig, EvaluatingConfig)

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            param_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.param = read_yaml(param_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        data_config = self.config.data_ingestion

        create_directories([data_config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= data_config.root_dir,
            source_url= data_config.source_url,
            local_data_file=data_config.local_data_file,
            unzip_dir=data_config.unzip_dir
        )
        return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        model_config = self.config.prepare_base_model

        create_directories([model_config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir= Path(model_config.root_dir),
            base_model_path= Path(model_config.base_model_path),
            updated_base_model_path= Path(model_config.updated_base_model_path),
            params_image_size= self.param.IMAGE_SIZE,
            params_learning_rate= self.param.LEARNING_RATE,
            params_include_top= self.param.INCLUDE_TOP,
            params_weights= self.param.WEIGHTS,
            params_classes= self.param.CLASSES
        )
        return prepare_base_model_config
    

    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model_config = self.config.prepare_base_model
        params = self.param

        trainig_data = os.path.join(self.config.data_ingestion.unzip_dir, "kidney-ct-scan-image")
        create_directories([
            Path(training.root_dir)
            ])
        
        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model_config.updated_base_model_path),
            training_data=Path(trainig_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config
    
    def get_evaluation_config(self) -> EvaluatingConfig:
        evaluation_config  = self.config.evaluation
        eval_config = EvaluatingConfig(
            root_dir=evaluation_config.root_dir,
            path_of_model= evaluation_config.path_of_model,
            training_data= evaluation_config.training_data,
            mlflow_uri= evaluation_config.mlflow_uri,
            all_params= self.param,
            params_image_size= self.param.IMAGE_SIZE,
            params_batch_size= self.param.BATCH_SIZE
        )
        return eval_config
