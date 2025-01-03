from src.Wine_Shop_Project import logger
from src.Wine_Shop_Project.pipeline.stage_01_data_ingetion import DataIngestionTrainingPapeline
from src.Wine_Shop_Project.pipeline.stage_02_data_validation import DataValidationTrainingPapeline

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