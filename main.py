
from math import log
from src.logging.logger import logging
from src.component.data_ingestion import DataIngestion
from src.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig


if __name__ == "__main__":
    logging.info("Data ingestion initiate")
    traing_pipeline_config = TrainingPipelineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config=traing_pipeline_config)
    data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
    data_ingestion = data_ingestion.init_data_ingestion()
    logging.info("Data ingestion ended")
    print(data_ingestion.train_file_path)
    print(data_ingestion.test_file_path)