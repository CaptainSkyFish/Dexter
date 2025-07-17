from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

load_dotenv()

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

if not connection_string:
    raise ValueError("Missing AZURE_STORAGE_CONNECTION_STRING")

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

input_container = "input_images"
output_container = "output_pdfs"


def upload_file(container_name: str, blob_name: str, data: bytes):
    container_client = blob_service_client.get_container_client(container_name)
    container_client.upload_blob(name=blob_name, data=data, overwrite=True)


def download_file(container_name: str, blob_name: str) -> bytes:
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob_name)
    stream = blob_client.download_blob()
    return stream.readall()
