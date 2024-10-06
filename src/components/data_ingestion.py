# the process of collecting data from multiple sources and 
# moving it to a central location for storage, processing, and analysis

import os
import sys
from src.exception import SusamayException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation, DataTransformationConfig

# Default values are provided using the os.path.join() function to ensure proper file path formatting across different operating systems.
@dataclass      #Class decorator to initialize & represent it as string
class DataIngestionConfig:
    train_data_path: str=os.path.join("artifacts","train.csv")
    test_data_path: str=os.path.join("artifacts","test.csv")
    raw_data_path: str=os.path.join("artifacts","data.csv") # ie relative path -> artifacts/data.csv

class DataIngestion: # Connection with datasource (like MongoDB, MySQL, csv, clipboard etc)
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()  

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Dataset as dataframe reading successful')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) #creates folder structure
            # or simply
            # os.mkdir('artifacts/')
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) #copies the whole data

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=101)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
        except Exception as e:
            raise SusamayException(e,sys)
        
if __name__=="__main__":  #checking data_transformation.py file
    obj=DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion() #run upto to check 

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)