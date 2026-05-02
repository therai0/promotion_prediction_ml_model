import pandas as pd 
import numpy as np 


from src.constant.traning_pipeline.training_pipeline import TARGET_COLUMN
from src.entity.config_entity import DataTransformationConfig
from src.entity.entity_artifacts import DataTransformationArtifacts,DataIngestionArtifacts
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.utils.main_utils.utils import save_object ,save_numpy_arr


class DataTransformation:
    def __init__(self,data_ingestion_artifacts:DataIngestionArtifacts,data_transformation_config:DataTransformationConfig):
        try:
            self.data_ingestion_artifacts = data_ingestion_artifacts
            self.data_transformation_config = data_transformation_config
        except Exception as e:
            raise Exception(e)
    
    def get_transformer_object(self):
        try:
            oridnal_encod_columns = ["education_level","city_tier","gender","marital_status","employment_type"]
            onehot_encod_columns  = ["department"]
            num_columns = ['age', 'years_at_company',
            'years_in_current_role', 'years_since_last_promotion', 'team_size',
            'performance_score', 'performance_last_year',
            'performance_two_years_ago', 'manager_rating', 'peer_feedback_score',
            'projects_completed', 'kpi_achievement_percent', 'innovation_score',
            'leadership_score', 'problem_solving_score', 'avg_monthly_hours',
            'overtime_hours', 'tasks_completed', 'deadline_adherence_rate',
            'meeting_hours_per_month', 'remote_work_ratio',
            'training_hours_last_year', 'certifications_count',
            'skill_assessment_score', 'cross_department_projects',
            'mentoring_sessions', 'salary', 'salary_increase_percent',
            'bonus_last_year', 'stock_options', 'attendance_rate', 'late_days',
            'employee_engagement_score', 'job_satisfaction_score',
            'internal_mobility_score']

            ordinal_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("OrdinalEncoder",OrdinalEncoder()),
                    ("scalar",StandardScaler())
                ]
            )
            onehot_pipeline = Pipeline(
                steps=[
                    ("imouter",SimpleImputer(strategy="most_frequent")),
                    ("OneHotEncoding",OneHotEncoder()),
                    # ("scalar",StandardScaler())
                ]
                )
            num_pipeline = Pipeline(
                steps = [
                    ("imputer",SimpleImputer(strategy="mean")),
                    ("scalar",StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer(
                [
                    ("num_values",num_pipeline,num_columns),
                    ("ordinal_cat",ordinal_pipeline,oridnal_encod_columns),
                    ("onehot",onehot_pipeline,onehot_encod_columns)
                ]
            )
            return preprocessor

        except Exception as e:
            raise Exception(e)


    def init_data_transformation(self):
        try:
            train_data = pd.read_csv(self.data_ingestion_artifacts.train_file_path)
            test_data = pd.read_csv(self.data_ingestion_artifacts.test_file_path)

            # droping employee_id and employee_id is exist 
            train_df = train_data.drop(["employee_id","Unnamed: 0"],axis=1, errors="ignore")
            test_df = test_data.drop(["employee_id","Unnamed: 0"],axis=1, errors="ignore")

            

            input_fet_train_df = train_df.drop([TARGET_COLUMN],axis=1,errors="ignore")
            target_train_fet = train_df[TARGET_COLUMN]

            input_fet_test_df = test_df.drop([TARGET_COLUMN],axis=1,errors="ignore")
            target_test_fet = test_df[TARGET_COLUMN]

            preprocessor = self.get_transformer_object()
            transform_input_train_fet = preprocessor.fit_transform(input_fet_train_df)
            transform_input_test_fet  = preprocessor.transform(input_fet_test_df)

            train_arr = np.c_[transform_input_train_fet,np.array(target_train_fet)]
            test_arr = np.c_[transform_input_test_fet,np.array(target_test_fet)]

            # saving object in transform folder
            save_object(file_path = self.data_transformation_config.data_transformed_object_file_path,obj=preprocessor)

            # saving object for model train
            save_object("final_model/preprocessor.pkl",obj=preprocessor)

            # saving numpy array 
            save_numpy_arr(self.data_transformation_config.data_transformed_train_file_path,train_arr)
            save_numpy_arr(self.data_transformation_config.data_transformed_test_file_path,test_arr)

            return DataTransformationArtifacts(
                transformed_object_file_path=self.data_transformation_config.data_transformed_object_file_path,
                transformed_train_file_path = self.data_transformation_config.data_transformed_train_file_path,
                transformed_test_file_path = self.data_transformation_config.data_transformed_test_file_path
            )
        except Exception as e:
            raise Exception(e)