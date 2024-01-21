from mlProject  import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline 
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline



STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation stage"
try:
        logger.info(f">>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<")
        DataValidationTrainingPipeline().main()
        logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
        logger.error(f"Failed {STAGE_NAME}", exc_info=True)
        
        
STAGE_NAME = "Data Transformation stage"

logger.info(f">>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<")
DataTransformationTrainingPipeline().main()
logger.info(f"Completed {STAGE_NAME}")

