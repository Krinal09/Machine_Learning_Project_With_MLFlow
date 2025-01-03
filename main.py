from src.Wine_Shop_Project import logger
from src.Wine_Shop_Project.pipeline.stage_01_data_ingetion import DataIngestionTrainingPapeline
from src.Wine_Shop_Project.pipeline.stage_02_data_validation import DataValidationTrainingPapeline
from src.Wine_Shop_Project.pipeline.stage_03_data_transformation import DataTransformationTrainingPapeline
from src.Wine_Shop_Project.pipeline.stage_04_model_trainer import ModelTrainerTrainingPapeline


STAGE_NAME = "Data Ingetion stage"

try:
    logger.info(f"---- stage {STAGE_NAME} started ----")
    data_ingetion =  DataIngestionTrainingPapeline()    
    data_ingetion.main()
    logger.info(f"---- stage {STAGE_NAME} completed ---- \n\nx=======x")
        
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"

try:
    logger.info(f"---- stage {STAGE_NAME} started ----")
    data_validation =  DataValidationTrainingPapeline()    
    data_validation.main()
    logger.info(f"---- stage {STAGE_NAME} completed ---- \n\nx=======x")
        
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f"---- stage {STAGE_NAME} started ----")
    data_transformation =  DataTransformationTrainingPapeline()    
    data_transformation.main()
    logger.info(f"---- stage {STAGE_NAME} completed ---- \n\nx=======x")
        
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training stage"

try:
    logger.info(f"---- stage {STAGE_NAME} started ----")
    obj =  ModelTrainerTrainingPapeline()    
    obj.main()
    logger.info(f"---- stage {STAGE_NAME} completed ---- \n\nx=======x")
        
except Exception as e:
    logger.exception(e)
    raise e