from utils.kaggle_api import download_dataset
from utils.bulk_load_to_data_lake import initialize_storage_account_ad,create_file_system,create_directory,upload_file_to_directory_bulk
import logging
from dotenv import load_dotenv
import os 


# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

# Access environment variables
AZURE_CLIENT_ID = os.getenv('AZURE_CLIENT_ID')
AZURE_TENANT_ID = os.getenv('AZURE_TENANT_ID')
AZURE_CLIENT_SECRET = os.getenv('AZURE_CLIENT_SECRET')


if __name__ == "__main__":
    dataset_name = "amitanshjoshi/spotify-1million-tracks"  # Replace with the desired dataset name
    destination_dir = "./data/"  # Replace with the desired destination directory
    storage_account_name = "destorage71" #Replace with storage name 
    file_system = "spotify" #replace with container name
    directory_name = "parquet_files" #Replace with directory name
    file_path = "./data/spotify_data.parquet" #Replace with file path name
    try: 
        download_dataset(dataset_name, destination_dir)
        initialize_storage_account_ad(storage_account_name=storage_account_name)
        create_file_system(file_system=file_system)
        create_directory(directory_name=directory_name)
        upload_file_to_directory_bulk(file_system=file_system,directory_name=directory_name,file_path=file_path)
    except Exception as e:
        logging.info(e)


