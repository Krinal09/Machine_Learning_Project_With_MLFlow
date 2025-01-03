from src.Wine_Shop_Project.config.configuration import ConfigurationManager
from src.Wine_Shop_Project.components.data_ingestion import DataIngestion
from src.Wine_Shop_Project import logger

STAGE_NAME = "Data Ingetion stage"

class DataIngestionTrainingPapeline:
    def __init__(self):
        pass
    
    def main(self):
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            
if __name__ == '__main__':
    try:
        logger.info(f"---- stage {STAGE_NAME} started ----")
        obj =  DataIngestionTrainingPapeline()    
        obj.main()
        logger.info(f"---- stage {STAGE_NAME} completed ---- \n\nx=======x")
        
    except Exception as e:
        logger.exception(e)
        raise e