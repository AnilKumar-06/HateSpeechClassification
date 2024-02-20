import logging
from pathlib import Path
import os

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
PROJECT_NAME = "HateSpeechClassification"

path_list = [
    f"{PROJECT_NAME}/componenets/__init__.py",
    f"{PROJECT_NAME}/components/data_ingestion.py",
    f"{PROJECT_NAME}/components/data_transformation.py",
    f"{PROJECT_NAME}/componenets/model_trainer.py",
    f"{PROJECT_NAME}/components/model_evaluation.py",
    f"{PROJECT_NAME}/components/model_pusher.py",
    f"{PROJECT_NAME}/configuration/__init__.py",
    f"{PROJECT_NAME}/configuration/gcloud_syncer.py",
    f"{PROJECT_NAME}/constants/__init__.py",
    f"{PROJECT_NAME}/entity/__init__.py",
    f"{PROJECT_NAME}/entity/config_entity.py",
    f"{PROJECT_NAME}/entity/artifact_entity.py",
    f"{PROJECT_NAME}/exception/__init__.py",
    f"{PROJECT_NAME}/logger/__init__.py",
    f"{PROJECT_NAME}/pipeline/__init__.py",
    f"{PROJECT_NAME}/pipeline/training_pipeline.py",
    f"{PROJECT_NAME}/pipeline/prediction_pipeline.py",
    f"{PROJECT_NAME}/ml/__init__.py",
    f"{PROJECT_NAME}/ml/model.py",
    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    ".dockerignore"
]


for filepath in path_list:
    filepath = Path(filepath)
    
    f_dir, f_name = os.path.split(filepath)
    
    if f_dir != "":
        os.makedirs(f_dir, exist_ok=True)
        logging.info(f"Creating directory: {f_dir} for the file {f_name}")
        
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file at location: {filepath}")
    else:
        logging.info(f"{f_name} is already exists")