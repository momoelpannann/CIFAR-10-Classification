import gdown
import os
import time

# File IDs from Google Drive
raw_data_file_ids = {
    "cifar-10-python.tar.gz": "1KFAOxIwYjjIMRlMtfB9zEv6rHYRSba_K",
    "test_batch": "1c__0Q8FrYHr2biEmcOoRw_b__axgD3Ep",
    "readme.html": "13o_DTkB4qGIL-sWs3VOPbh0AaGlow48e",
    "data_batch_5": "1QPD26irLlOr6z5B61OLwSBZcdKcliSGW",
    "data_batch_4": "14vn34UToRQV0OTKJJjzFZr40x2oNF6Uo",
    "data_batch_3": "1OiUzACvZ3yBCJvTYN9FLlJ3uFiUswAcs",
    "data_batch_2": "1THQPq5GBJjG8KRhN6rhecOEChydnUMq4",
    "data_batch_1": "1XOqN0h67YUtUdU9w3YjkmZPwpGaEND_2",
    "batches.meta": "1Dgm-nkH59AdJBnMGRiUmf6Gh2tls3xz8",
}
processed_data_file_ids = {
    "train_data.pth": "1rtx-GjE6vqlIZw5RkeCvQ076s_wvPKF4",
    "test_data.pth": "1v1tEoe1A2CHPHAu3CHH-xAOEKg7o5eGp",
}

# Folder paths
raw_data_folder = './Data/RawData'
cifar_batches_folder = os.path.join(raw_data_folder, 'cifar-10-batches-py')
processed_data_folder = './Data/ProcessedData'

# Create folders if they don't exist
os.makedirs(raw_data_folder, exist_ok=True)
os.makedirs(cifar_batches_folder, exist_ok=True)
os.makedirs(processed_data_folder, exist_ok=True)

# Function to download a file
def download_file(file_id, output_folder, file_name, retries=3):
    """
    Downloads a file from Google Drive.

    :param file_id: Google Drive file ID
    :param output_folder: Target folder to save the file
    :param file_name: Desired file name
    :param retries: Number of retry attempts if download fails
    :return: True if download succeeds, False otherwise
    """
    url = f'https://drive.google.com/uc?id={file_id}'
    output_path = os.path.join(output_folder, file_name)
    print(f"\nAttempting to download: {file_name}")
    print(f"URL: {url}")

    for attempt in range(retries):
        try:
            if not os.path.exists(output_path):
                print(f"Downloading {file_name} to {output_folder} (Attempt {attempt + 1}/{retries})...")
                gdown.download(url, output_path, quiet=False, fuzzy=True)
                print(f"Successfully downloaded: {file_name}")
                return True
            else:
                print(f"{file_name} already exists in {output_folder}.")
                return True
        except Exception as e:
            print(f"Error downloading {file_name}: {e}")
            time.sleep(2)  # Wait before retrying

    print(f"Failed to download {file_name} after {retries} attempts.")
    return False

# Download main raw data archive (if needed)
if "cifar-10-python.tar.gz" in raw_data_file_ids:
    download_file(raw_data_file_ids["cifar-10-python.tar.gz"], raw_data_folder, "cifar-10-python.tar.gz")

# Download individual files for cifar-10-batches-py
print("\nDownloading CIFAR-10 Raw Data Files:")
for file_name, file_id in raw_data_file_ids.items():
    if file_name != "cifar-10-python.tar.gz":  # Skip the main archive
        download_file(file_id, cifar_batches_folder, file_name)

# Download processed data files
print("\nDownloading Processed Data:")
for file_name, file_id in processed_data_file_ids.items():
    download_file(file_id, processed_data_folder, file_name)

print("\nAll files downloaded and placed in the correct folders.")