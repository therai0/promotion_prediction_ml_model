
from dataclasses import dataclass


@dataclass
class DataIngestionArtifacts:
    train_file_path:str 
    test_file_path:str 


@dataclass
class DataTransformationArtifacts:
    transformed_object_file_path:str
    transformed_train_file_path:str
    transformed_test_file_path:str 
    

@dataclass 
class ModelTrainArtifacts:
    train_model_file_path:str 
    



