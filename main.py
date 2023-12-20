from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionPipeline


STAGE_NAME = "Data Ingestion Stage"
    
try:
    logger.info(f"stage   {STAGE_NAME}  started")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"stage   {STAGE_NAME}  completed")
except Exception as e:
    logger.exception(e)
    raise e
