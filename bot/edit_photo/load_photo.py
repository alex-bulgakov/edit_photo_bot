import os

import requests
from dotenv import load_dotenv


def load_photo(file_id):
    load_dotenv()
    token = os.getenv('TOKEN')
    URI = f"https://api.telegram.org/bot{token}/getFile?file_id=" + file_id
    file_path = requests.get(URI).json()['result']['file_path']
    FILE_URI = f"https://api.telegram.org/file/bot{token}/" + file_path
    img = requests.get(FILE_URI).content
    return img
