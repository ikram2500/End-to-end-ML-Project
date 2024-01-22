from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer 
from mlProject import logger
from pathlib import Path


STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
        
        
        
if __name__ == "__main__":
    try:
        logger.info(f"Executing {STAGE_NAME}")
        ModelTrainerTrainingPipeline().main()
        logger.info(f"{STAGE_NAME} completed")
    except Exception as e:
        logger.error(f"{STAGE_NAME} failed with error: {e}")
        raise e
    logger.info(f"Executing {STAGE_NAME}")
    ModelTrainerTrainingPipeline().main()
    logger.info(f"{STAGE_NAME} completed")
