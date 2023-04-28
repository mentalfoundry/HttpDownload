import requests
import sys
import os

#get this dependency first py -m pip install requests
#run this from your machine like so. py download_zip.py http://myzip.com/filetodownload.zip

def download_zip_file(url, output_file_name):
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(output_file_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

    else:
        print(f"Request failed with status code: {response.status_code}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a URL to download the zip file.")
        sys.exit(1)

    url = sys.argv[1]
    file_name = os.path.basename(url)
    download_zip_file(url, file_name)
    print(f"Zip file {file_name} has been downloaded successfully.")
