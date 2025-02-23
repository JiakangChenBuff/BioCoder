"""
This script allows users to input an ID corresponding to a file
and its related zip archive hosted on S3. It repeatedly
downloads these files using the provided ID and S3 URLs and
saves them into a local "outputs" directory.
"""
import os
import zipfile
import shutil
import requests

s3url = "https://Lab.s3.amazonaws.com/output_logs"
s3url2 = "https://Lab.s3.amazonaws.com/functions"

def download(id):
    url = f"{s3url}/{id[0]}/{id[1]}/{id[2]}/{id}.txt"
    url2 = f"{s3url2}/{id[0]}/{id}.zip"
    print(url)
    r = requests.get(url)
    r2 = requests.get(url2)
    if r.status_code == 200:
        data = r.content
        if not os.path.exists("outputs"):
            os.makedirs("outputs")
        with open(f"outputs/{id}.txt", "wb") as f:
            f.write(data)
        with open(f"outputs/{id}.zip", "wb") as f:
            f.write(r2.content)
        print("Downloaded file at", f"{id}.txt")
        print("Downloaded file at", f"{id}.zip")
    else:
        print("Error downloading file")
        return None
      
while True:
    id = input("Enter id: ")
    download(id)

