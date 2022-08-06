from collections import namedtuple

# data source information
DataIngestionConfig = namedtuple("DataIngestionConfig",
                                 ["dataset_download_url", "tgz_download_dir", "raw_data_dir", "ingested_train_dir", "ingested_test_dir"])

# schema_file_path: how many columns are there, data type
DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path"])

# for feature engineering, add_bedroom_per_room: this column is not available,need to pass True or false, this is optional;
#  preprocessed_object_file_path for picke file,
DataTransformationConfig = namedtuple("DataTransformationConfig", ["add_bedroom_per_room",
                                                                   "transformed_train_dir",
                                                                   "transformed_test_dir",
                                                                   "preprocessed_object_file_path"])

# save the pickle file location, compare accuracy with previous accuracy
ModelTrainerConfig = namedtuple(
    "ModelTrainerConfig", ["trained_model_file_path", "base_accuracy"])


# all the model that is in production, what time did this activity?
ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", [
                                   "model_evaluation_file_path", "time_stamp"])

# best model saving in the location
ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])

# pipeline create
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])
