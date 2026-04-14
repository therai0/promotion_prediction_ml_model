import os 
from dotenv import load_dotenv 

load_dotenv()
"""
All constant varialable are define here
"""
TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"
RAW_FILE_NAME:str = "employee_promotion.csv"
ARTIFACTS_DIR:str = "Artifacts"
TARGET_COLUMN = "promoted"
DATABASE_NAME = "employee"
COLLECTION_NAME = "emp_promotion_db"
PREPROCESSOR_MODEL = "preprocessor.pkl"
MONGODB_URL = os.getenv("MONGODB_URL")




"""
All the constant variable use for Data ingestion 
"""
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE = "feature_store"
DATA_INGESTION_TRAIN_AND_TEST_RATIO:float = 0.2
DATA_INGESTION_INGESTED_DIR = "ingested"


"""
All the constant varaible use for Data transformation
"""
