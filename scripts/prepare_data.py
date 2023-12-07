# a. Programmatically downloads and extracts the selected dataset to the data
# directory (as in Assignment 1).
# b. Computes the SHA-256 hash and compares it to a precomputed hash (as in
# Assignment 2).

import requests, hashlib, os
from zipfile import ZipFile


DATA_URL = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"
SHA256_BANK = "e0bf5f5de5b846e2f18e9d90606637267d46dfa260e0f17bb12e605db5efbeb4"

DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/")
DATA_FILE_PATH = os.path.abspath(os.path.join(DATA_PATH, "bank" + '.' + "zip"))
CSV_FILE_PATH = os.path.abspath(os.path.join(DATA_PATH, "unzip/"))
CSV_EXP_FILE_PATH = os.path.abspath(os.path.join(DATA_PATH, "csv/"))


if not os.path.exists(DATA_PATH):
    os.makedirs(DATA_PATH)


# Web request
response = requests.get(DATA_URL)
if response.status_code != 200:
    print("Error in fetching data, stopping")
    exit()

# Check hash and save
with open(file=DATA_FILE_PATH, mode='wb') as f: 

    sha256hash = hashlib.sha256(response.content).hexdigest()
    if sha256hash != SHA256_BANK:
        print("SHA256 Hash Error")
    else:
        f.write(response.content)
        print("Bank data saved")

# Extract ZIP files
with ZipFile(DATA_FILE_PATH, 'r') as zObject: 
    zObject.extractall(path=CSV_FILE_PATH) 

dir_list = os.listdir(CSV_FILE_PATH)
for file in dir_list:
    with ZipFile(os.path.join(CSV_FILE_PATH, file), 'r') as zObject: 
        zObject.extractall(path=CSV_EXP_FILE_PATH) 
