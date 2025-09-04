from azure.storage.blob import BlobServiceClient
import os

# ======================
# CONFIGURATION
# ======================
# Replace with your Storage Account connection string
CONNECTION_STRING = "AZURE_STORAGE_CONNECTION_STRING"
CONTAINER_NAME = "files"

# ======================
# CONNECT TO AZURE
# ======================
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# ======================
# UPLOAD FILE
# ======================
local_file_name = "test_upload.txt"
with open(local_file_name, "w") as f:
    f.write("Hello from Terraform + Python demo!")

blob_client = container_client.get_blob_client(local_file_name)
with open(local_file_name, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)
print(f"Uploaded {local_file_name} to container '{CONTAINER_NAME}'")

# ======================
# DOWNLOAD FILE
# ======================
download_file_name = "downloaded_test.txt"
with open(download_file_name, "wb") as f:
    blob_data = blob_client.download_blob()
    blob_data.readinto(f)
print(f"Downloaded blob to {download_file_name}")
