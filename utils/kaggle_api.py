import os
import pandas as pd
from kaggle.api import KaggleApi
import logging


# Configure logging
logging.basicConfig(level=logging.INFO)


def download_dataset(dataset_name, destination_dir):
    try:
        # Instantiate Kaggle API
        api = KaggleApi()
        
        # Authenticate with your Kaggle credentials
        api.authenticate()

        # Download the dataset
        api.dataset_download_files(dataset=dataset_name, path=destination_dir, unzip=True)
        
        # Save the dataset as Parquet
        downloaded_files = os.listdir(destination_dir)
        for file in downloaded_files:
            if file.endswith('.csv'):
                csv_file_path = os.path.join(destination_dir, file)
                parquet_file_path = os.path.join(destination_dir, os.path.splitext(file)[0] + '.parquet')
                df = pd.read_csv(csv_file_path)
                df.to_parquet(parquet_file_path)
                logging.info(f"Saved {parquet_file_path}")
                os.remove(csv_file_path)
                logging.info(f"Deleted {csv_file_path}")
            
    except Exception as e:
        logging.info(f"Error occurred while downloading the dataset: {str(e)}")


