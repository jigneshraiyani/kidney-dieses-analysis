from src.cnnClassifier.constants import *
from src.cnnClassifier.utils.util import read_yaml, create_directories
from src.cnnClassifier.entity.config_entity import (DataIngestionConfig, PrepareBaseModelConfig)

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
