from HateSpeech.logger import logging
from HateSpeech.exception import CustomException
import sys
from HateSpeech.configuration.gcloud_syncer import GCloudSync

obj = GCloudSync()
obj.sync_folder_from_cloud("")