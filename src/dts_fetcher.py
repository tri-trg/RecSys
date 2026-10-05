import os
import requests
import zipfile
from tqdm import tqdm

# Path definition
url = "https://files.grouplens.org/datasets/movielens/ml-32m.zip"
zip_file_name = "ml-32m.zip"
target_dir = "data"
zip_path = os.path.join(target_dir, zip_file_name)


# Fetch the dataset
def download_data():
    # Create target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Download the dataset
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        total_size = int(response.headers.get('content-length', 0))

        with open(zip_path, 'wb') as f, tqdm(
            desc="Downloading dataset",
            total=total_size,
            unit='B',          
            unit_scale=True,   
            unit_divisor=1024, 
        ) as bar:
            # Write the content to a zip file in chunks and update the progress bar
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                bar.update(len(chunk))

        return zip_path

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error. Status code: {response.status_code}, \nDetails: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Network Error. \nDetails: {e}")
        return None


def extract_data(zip_path):
    # Extract the dataset
    with zipfile.ZipFile(zip_path, 'r') as zip_ref, tqdm(
        desc="Extracting dataset",
        total=len(zip_ref.infolist()),
        unit='file',
    ) as bar:
        for file in zip_ref.infolist():
            zip_ref.extract(file, target_dir)
            bar.update(1)

    # Clean up the zip file
    os.remove(zip_path)

def main():
    zip_path = download_data()
    if zip_path:
        extract_data(zip_path)

if __name__ == "__main__":
    main()