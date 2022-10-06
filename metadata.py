get_ipython().system('pip install pyOpenSSL')
import ssl
import os
import time
import requests

def download_metadata(metadata_dir='./Metadata/'):
    os.makedirs(metadata_dir)
    csv_file = {
        'cancer_link.csv' : 'https://drive.google.com/uc?export=download&id=1QD2JEkepX6_W1TeQ5sY42R6flhW6833X',
        'BRCApatients_type.csv' : 'https://drive.google.com/uc?export=download&id=1CmjvbF_i6oYzQFWAnwLZORd4tnnW3GvK',
        'Homo_sapiens.gene_info' : 'https://drive.google.com/uc?export=download&id=1IPQq7lBqbpzz2GBNXT2sDh0Hdn4iL8fN'
    }
    names = [file for file in csv_file]
    with open(f'{metadata_dir}{names[0]}', "wb") as file:
        sess = requests.Session()
        adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
        sess.mount('http://', adapter)
        res = sess.get(csv_file[names[0]])
        file.write(res.content)
    time.sleep(2)
    with open(f'{metadata_dir}{names[1]}', "wb") as file:
        sess = requests.Session()
        adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
        sess.mount('http://', adapter)
        res = sess.get(csv_file[names[1]])
        file.write(res.content)
    time.sleep(2)
    with open(f'{metadata_dir}{names[2]}', "wb") as file:
        requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
        response = requests.get(csv_file[names[2]], verify= False, timeout=30)              
        file.write(response.content)
    
    print(f'Metadata is installed')