from datetime import datetime
from tkinter import E
from src.constant.traning_pipeline import training_pipeline


import os 

class TrainingPipelineConfig:
    def __init__(self):
        try:
            self.time_stamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
            self.artifact_dir = os.path.join(training_pipeline.ARTIFACTS_DIR,self.time_stamp)
        except Exception as e:
            raise Exception(e)


class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME)
            self.raw_file_path = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE,training_pipeline.RAW_FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TEST_FILE_NAME)
            self.train_test_split_ratio = training_pipeline.DATA_INGESTION_TRAIN_AND_TEST_RATIO
            self.database = training_pipeline.DATABASE_NAME
            self.collection_name = training_pipeline.COLLECTION_NAME
            self.mongodb_url = training_pipeline.MONGODB_URL
        except Exception as e:
            raise Exception(e)



