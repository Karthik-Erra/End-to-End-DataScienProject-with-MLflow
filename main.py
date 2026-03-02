from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipline import DataTransformationPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluatinPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"stage: {STAGE_NAME} Completed \n\n")
except Exception as e:
    logger.info(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_datavalidation()
    logger.info(f"stage: {STAGE_NAME} Completed\n\n")
except Exception as e:
    logger.info(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    data_transformation = DataTransformationPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f"Stage: {STAGE_NAME} Completed\n\n")
except Exception as e:
    logger.info(e)
    raise(e)

STAGE_NAME = "Model Training Stage"

try:
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_training()
    logger.info(f"Stage: {STAGE_NAME} Completed")
except Exception as e:
    logger.info(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    model_evaluation_pipeline = ModelEvaluatinPipeline()
    model_evaluation_pipeline.initiate_model_evaluation_pipeline()
    logger.info(f"Stage: {STAGE_NAME} Completed")

except Exception as e:
    logger.info(e)
    raise e

