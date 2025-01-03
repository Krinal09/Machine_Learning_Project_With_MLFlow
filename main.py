from src.Wine_Shop_Project import logger
from src.Wine_Shop_Project.pipeline.stage_01_data_ingetion import DataIngestionTrainingPapeline

STAGE_NAME = "Data Ingetion stage"

try:
    logger.info(f"---- stage {STAGE_NAME} started ----")
    obj =  DataIngestionTrainingPapeline()    
    obj.main()
    logger.info(f"---- stage {STAGE_NAME} completed ---- \n\nx=======x")
        
except Exception as e:
    logger.exception(e)
    raise e