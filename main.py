from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionPipeline
from src.cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelPipeline
from src.cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
    
try:
    logger.info(f"stage   {STAGE_NAME}  started")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"stage   {STAGE_NAME}  completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME2 = "Prepare Base Model Stage"
    
try:
    logger.info(f"stage   {STAGE_NAME}  started")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f"stage   {STAGE_NAME}  completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME3 = "Training Stage"
    
try:
    logger.info(f"stage   {STAGE_NAME}  started")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"stage   {STAGE_NAME}  completed")
except Exception as e:
    logger.exception(e)
    raise e