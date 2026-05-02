import numpy as np
import os 
import dill 


def save_numpy_arr(file_path:str,array:np.array,):
    """
    Saving the numpy array file 
    """
    try:
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name,exist_ok=True)

        with open(file_path,'wb') as file:
            np.save(file,array)
    except Exception as e:
        raise Exception(e)

def load_numpy_arr(file_path:str)->np.array:
    try:
        with open(file_path,'rb') as file:
            return np.load(file)
    except Exception as e:
        raise Exception(e)

def save_object(file_path:str,obj):
    try:
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise Exception(e)


def load_object(file_path:str):
    try:
        with open(file_path,'rb') as  file:
            return dill.load(file)
    except Exception as e:
        raise Exception(e)

