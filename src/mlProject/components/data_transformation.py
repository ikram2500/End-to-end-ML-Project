import os 
from mlProject import logger 
from sklearn.model_selection import train_test_split 
import pandas as pd 
from mlProject.config.configuration import DataTransformationConfig 


class DataTransformation:
    def __init__(self, config : DataTransformationConfig):
        self.config = config 
    ## you can add different data transformation techniques such as scaler, pca and all
    # you can perform all kinds of EDA in ML cycle here before passing this data to the model
    # I am only adding train_test_split cx this data is already cleaned up
    
    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)
        train, test = train_test_split(data, test_size=0.2, random_state=42)
        
        train.to_csv(os.path.join(self.config.root_dir,  'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)
        
        logger.info(f"train and test data saved at {self.config.root_dir}")
        logger.info(f"train data shape: {train.shape}")
        logger.info(f"test data shape: {test.shape}")
        
        print(f"train and test data saved at {self.config.root_dir}")
        print(f"train data shape: {train.shape}")