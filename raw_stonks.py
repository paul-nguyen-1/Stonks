import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def json_stonks(url, file, bucket):
    print("Run stonks")
    response = requests.request("GET", url)
    json_data = response.json()

    with open(file, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)
    print("Stonks ready")

def main():
    json_stonks(api_key, 'stonks_data.json', 'data-mbfr')

if __name__ == "__main__":
    main()

