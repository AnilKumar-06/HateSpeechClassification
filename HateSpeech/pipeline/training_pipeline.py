import sys
from HateSpeech.logger import logging
from HateSpeech.exception import CustomException
from HateSpeech.components.data_ingestion import DataIngestion
from HateSpeech.entity.config_entity import (DataIngestionConfig,)
from HateSpeech.entity.artifact_entity import (DataIngestionArtifacts)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        
        
    def start_data_Ingestion(self) -> DataIngestionArtifacts:
        logging.info("Getting the start_data_ingestion_method of TrainPipeline class")
        try:
            logging.info("Getting the data from GCloud storage bucket")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Got the training and validation data from GCloud")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifacts
        except Exception as e:
            raise CustomException(e, sys) from e
        
        
    def run_pipeline(self):
        logging.info("Entered into the run_pipeline method of TrainPipeline class")
        try:
            data_ingestion_artifacts = self.start_data_Ingestion()
            
            
            logging.info("Exited from the run_pipeline method of TrainPipeline class")
            
        except Exception as e:
            raise CustomException(e, sys) from e