from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage04_model_evaluation import EvaluationPipeline

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
    logger.info(f"stage   {STAGE_NAME2}  started")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f"stage   {STAGE_NAME2}  completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME3 = "Training Stage"
    
try:
    logger.info(f"stage   {STAGE_NAME3}  started")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"stage   {STAGE_NAME3}  completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME4 = "Evaluation Stage"
    
try:
    logger.info(f"stage   {STAGE_NAME4}  started")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f"stage   {STAGE_NAME4}  completed")
except Exception as e:
    logger.exception(e)
    raise e