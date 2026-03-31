from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    # Step 1: Data Ingestion
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()

    # Step 2: Data Transformation
    transformation = DataTransformation()
    train_arr, test_arr, _ = transformation.initiate_data_transformation(train_path, test_path)

    # Step 3: Model Training
    trainer = ModelTrainer()
    trainer.initiate_model_trainer(train_arr, test_arr)

    print("Training completed. Model and preprocessor saved.")