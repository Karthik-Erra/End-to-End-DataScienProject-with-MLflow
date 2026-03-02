import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.datascience import logger
from src.datascience.entity.config_entity import DataValidationConfig


class DataTransformation:
    def __init__(self,config: DataValidationConfig):
        self.config = config
    def train_test_splitting(self):
        df = pd.read_csv(self.config.data_path)

        train, test = train_test_split(df)

        train.to_csv(os.path.join(self.config.root_dir,'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'),index=False)

        logger.info("Splitting data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

