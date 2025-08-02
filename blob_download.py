from azure.storage.blob import BlobServiceClient

def download_blob(container_name, blob_name, local_path):
    conn_str = "<AZURE_BLOB_CONNECTION_STRING>"
    blob_service_client = BlobServiceClient.from_connection_string(conn_str)
    blob_client = blob_service_client.get_container_client(container_name).get_blob_client(blob_name)

    with open(local_path, "wb") as file:
        file.write(blob_client.download_blob().readall())