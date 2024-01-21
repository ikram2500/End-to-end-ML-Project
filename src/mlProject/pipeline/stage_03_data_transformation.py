from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation 
from mlProject import logger
from pathlib import Path

STAGE_NAME = "Data Transformation stage"



class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_split()