from dotenv import load_dotenv
import os 
import pandas as pd 
import json 
import pymongo 

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")


class LoadData:
    def __init__(self):
        try:
            pass 
        except Exception as e:
            raise Exception(e)
    
    def csv_to_json(self,path:str):
        try:
            print(path)
            df = pd.read_csv(f"{path}") 
            df.reset_index(drop=True,inplace=True)
            records = list(json.loads(df.T.to_json()).values())
            return records 
        except FileNotFoundError as e:
            raise Exception(e)
    
    def load_to_database(self,database,collection,records):
        try:
            self.mongo_clients = pymongo.MongoClient(MONGODB_URL)
            self.database = self.mongo_clients[database]
            self.collection = self.database[collection]

            # insert datainto mongo db
            self.collection.insert_many(records)
        except Exception as e:
            raise Exception(e)


if __name__ == "__main__":
    database = "employee"
    collectoin= "emp_promotion_db"
    ld = LoadData()
    records = ld.csv_to_json("data/employee_promotion_prediction.csv")
    ld.load_to_database(collection=collectoin,records=records,database=database)
    