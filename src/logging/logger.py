
import logging
import os 
from datetime import datetime


LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

file_path = os.path.join(os.getcwd(),"Log",LOG_FILE_NAME)

os.makedirs(file_path,exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    filename= os.path.join(file_path,LOG_FILE_NAME),
    format="[%(asctime)s] %(lineno)d %(name)s %(levelname)s %(message)s",
)






