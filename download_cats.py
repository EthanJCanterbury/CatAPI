
import os
import requests
import shutil

def download_cat(index):
    response = requests.get('https://cataas.com/cat', stream=True)
    if response.status_code == 200:
        with open(f'cats/cat{index}.jpg', 'wb') as f:
            shutil.copyfileobj(response.raw, f)
    return response.status_code == 200

for i in range(10, 40):  # Download 30 more cats
    print(f"Downloading cat {i}...")
    if download_cat(i):
        print(f"Downloaded cat{i}.jpg")
    else:
        print(f"Failed to download cat{i}.jpg")
