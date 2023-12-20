from src.cnnClassifier.constants import *
from src.cnnClassifier.utils.util import read_yaml, create_directories
from src.cnnClassifier.entity.config_entity import (DataIngestionConfig)

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