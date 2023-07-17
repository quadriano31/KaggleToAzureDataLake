import os
import os, uuid, sys
from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings
import logging

#initialize logging
logging.basicConfig(level=logging.INFO)


def initialize_storage_account_ad(storage_account_name):
    """Initialize the Azure Data Lake Storage Gen2 account using Azure AD authentication.

    Args:
        storage_account_name (str): The name of the storage account.

    Returns:
        None
    """
    
    try:  
        global service_client

        default_credential = DefaultAzureCredential()

        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=default_credential)
        logging.info("successfully Authenticated with Azure AD")
    
    except Exception as e:
        logging.info(e)

def create_file_system(file_system):
    """Create a file system within the Azure Data Lake Storage Gen2 account.

    Args:
        file_system (str): The name of the file system to create.

    Returns:
        None
    """
    try:
        global file_system_client
        file_system_client = service_client.create_file_system(file_system=file_system)
        logging.info(f"succesfully created {file_system}")
    except Exception as e:
        logging.info(e)

def create_directory(directory_name):
    """Create a directory within the specified file system in Azure Data Lake Storage Gen2.

    Args:
        directory_name (str): The name of the directory to create.

    Returns:
        None
    """
    try:
        file_system_client.create_directory(directory_name)
        logging.info(f"created directory {directory_name}")

    except Exception as e:
        logging.info(e)


def upload_file_to_directory_bulk(file_system,directory_name,file_path):
    """Upload a Parquet file to the specified directory within the file system.

    Args:
        file_system (str): The name of the file system.
        directory_name (str): The name of the directory.
        file_path (str): The local path of the Parquet file to upload.

    Returns:
        None
    """
    try:
        if file_path.split("/")[1] is True:
            file_name =file_path.split("/")[1]
        else:
            file_name = file_path
        # Get the file system client
        file_system_client = service_client.get_file_system_client(file_system=file_system)
        # Get the directory client
        directory_client = file_system_client.get_directory_client(directory_name)
        # Get the file client
        file_client = directory_client.get_file_client(file_path)

        # Upload the Parquet file
        with open(file_path, "rb") as local_file:
            file_client.upload_data(local_file, overwrite=True)

        logging.info("Parquet file uploaded successfully.")

    except Exception as e:
        logging.error(e)
