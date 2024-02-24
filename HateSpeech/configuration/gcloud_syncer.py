import os
class GCloudSync:
    def sync_folder_to_cloud(self, gcp_bucket_url, file_path, filename):
        cmd = f"gshutil cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        os.system(cmd)
        
    def sync_folder_from_cloud(self, gcp_bucket_url, filename, destination):
        cmd = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
        os.system(cmd)