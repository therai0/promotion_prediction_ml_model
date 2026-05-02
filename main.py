
from math import log
from src.logging.logger import logging
from src.component.data_ingestion import DataIngestion
from src.component.data_transformation import DataTransformation
from src.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataTransformationConfig


if __name__ == "__main__":
    logging.info("Data ingestion initiate")
    traing_pipeline_config = TrainingPipelineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config=traing_pipeline_config)
    data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
    data_ingestion_artifacts = data_ingestion.init_data_ingestion()
    
    data_transformation_config = DataTransformationConfig(traning_pipeline_config=traing_pipeline_config)
    data_transformation = DataTransformation(data_ingestion_artifacts=data_ingestion_artifacts,data_transformation_config=data_transformation_config)

    data_transformation_artifacts = data_transformation.init_data_transformation()
    print(data_transformation_artifacts.transformed_test_file_path)

    