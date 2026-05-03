from src.entity.config_entity import ModelTrainerConfig
from src.entity.entity_artifacts import ModelTrainArtifacts,DataTransformationArtifacts

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC 
from sklearn.ensemble import AdaBoostClassifier,RandomForestClassifier
from sklearn.metrics import accuracy_score

# load numpy arrray 
from src.utils.main_utils.utils import load_numpy_arr, save_object

class ModelTrainer:
    def __init__(self,data_transformation_artifacts:DataTransformationArtifacts,model_trainer_config:ModelTrainerConfig):
        try:
            self.data_transformation_artifacts = data_transformation_artifacts
            self.model_trainer_config = model_trainer_config
        except Exception as e:
            raise Exception(e)
    
    def get_best_model(self,models,X_train,y_train,X_test,y_test):
        try:
            models_acc = {}
            for mod in models:
                model = models[mod]
                model.fit(X_train,y_train)
                y_pred = model.predict(X_test)
                acc_score = accuracy_score(y_test,y_pred)
                models_acc[mod] = acc_score

            high_score  = max(list(models_acc.values()))
            index =  list(models_acc.values()).index(high_score)
            return list(models_acc.keys())[index]
        except Exception as e:
            raise Exception(e)

    def init_model_traning(self):
        try:
            train_arr = load_numpy_arr(self.data_transformation_artifacts.transformed_train_file_path)
            test_arr = load_numpy_arr(self.data_transformation_artifacts.transformed_test_file_path)

            X_train = train_arr[:,:-1]
            y_train = train_arr[:,-1]
            
            X_test = test_arr[:,:-1]
            y_test = test_arr[:,-1]

            models = {
                "LogisticRegression":LogisticRegression(),
                "DecisionTreeClassifier":DecisionTreeClassifier(),
                "RandomForestClassifier":RandomForestClassifier(),
                "SVC":SVC(),
                "AdaBoostClassifier":AdaBoostClassifier()
            }
            
            best_model = self.get_best_model(models=models,X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test)

            save_object(self.model_trainer_config.model_file_path,best_model)

            return ModelTrainArtifacts(
            train_model_file_path = self.model_trainer_config.model_file_path
            )
        except Exception as e:
            raise Exception(e)
