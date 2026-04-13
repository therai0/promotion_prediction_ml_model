import os 
import pymongo 
import pandas as pd 
from src.entity.config_entity import DataIngestionConfig 
from src.entity.entity_artifacts import DataIngestionArtifacts
from src.constant.traning_pipeline import training_pipeline
from sklearn.model_selection import train_test_split 

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise Exception(e)

    
    def export_data_as_datafram(self)->pd.DataFrame:
        try:
            self.mongo_client = pymongo.MongoClient(self.data_ingestion_config.mongodb_url)
            self.database = self.mongo_client[self.data_ingestion_config.database]
            self.collection = self.database[self.data_ingestion_config.collection_name]
            records = self.collection.find()
            data_frame = pd.DataFrame(list(records))
            data_frame.drop(["_id"],axis=1,inplace = True)
            return data_frame
        except Exception as e:
            raise Exception(e)
        

    def split_into_train_test(self,data_frame:pd.DataFrame):
        try:
            
            Train_df ,Test_df = train_test_split(data_frame,test_size=self.data_ingestion_config.train_test_split_ratio,random_state=42)
        
            # saving train data
            dir_name = os.path.dirname( self.data_ingestion_config.train_file_path)
            os.makedirs(dir_name,exist_ok=True)
            Train_df.to_csv(self.data_ingestion_config.train_file_path)
            Test_df.to_csv(self.data_ingestion_config.test_file_path)

        except Exception as e:
            raise Exception(e)

    def export_dataframe_to_feature_store(self,data_frame:pd.DataFrame):
        try:
            dir_name = os.path.dirname(self.data_ingestion_config.raw_file_path)
            os.makedirs(dir_name,exist_ok=True)
            data_frame.to_csv(self.data_ingestion_config.raw_file_path)
        except Exception as e:
            raise Exception(e)

    def init_data_ingestion(self)->DataIngestionArtifacts:
        try:
            data_frame = self.export_data_as_datafram()
            self.split_into_train_test(data_frame=data_frame)
            self.export_dataframe_to_feature_store(data_frame=data_frame)
            return DataIngestionArtifacts(
                train_file_path = self.data_ingestion_config.train_file_path,
                test_file_path = self.data_ingestion_config.test_file_path
            )
        except Exception as e:
            raise Exception(e)