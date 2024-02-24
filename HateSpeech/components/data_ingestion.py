import os
import sys
from zipfile import ZipFile
from HateSpeech.logger import logging
from HateSpeech.exception import CustomException
from HateSpeech.configuration.gcloud_syncer import GCloudSync
from HateSpeech.entity.config_entity import DataIngestionConfig
from HateSpeech.entity.artifact_entity import DataIngestionArtifacts

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.gcloud = GCloudSync()
        
    def get_data_from_gcloud(self) -> None:
        try:
            logging.info("Data ingestion started from the GCloud")
            os.makedirs(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR, exist_ok=True)
            self.gcloud.sync_folder_from_cloud(
                self.data_ingestion_config.BUCKET_NAME,
                self.data_ingestion_config.ZIP_FILE_NAME,
                self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR
            )
            
            logging.info("Data Ingestion Completed from GCloud")
        except Exception as e:
            raise CustomException(e, sys) from e
        
    def unzip_and_clean(self):
        logging.info("Entered the unzip_and_clean method of Data Ingestion class")
        try:
            with ZipFile(self.data_ingestion_config.ZIP_FILE_PATH, 'r') as f:
                f.extractall(self.data_ingestion_config.ZIP_FILE_DIR)
            
            logging.info("Exited the unzip_and_clean method of Data ingestion class")
            
            return self.data_ingestion_config.DATA_ARTIFACTS_DIR, self.data_ingestion_config.NEW_DATA_ARTIFACTS_DIR
        
        except Exception as e:
            raise CustomException(e, sys) from e
        
        
    
    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered into the initiate_data_ingestion method of DataIngestion class")
        try:
            self.get_data_from_gcloud()
            logging.info("Fetched the data from gcloud bucket")
            imbalance_data_file_path, raw_data_file_path = self.unzip_and_clean()
            logging.info("Unzip file and split into train and valid")
            
        except Exception as e:
            raise CustomException(e, sys) from e