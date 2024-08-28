import requests
from bs4 import BeautifulSoup
import json
import os
#kazananları scrapeleyen kod
urls = [
    "https://www.oynasin.com/cekilis/44df076e9c",
    "https://www.oynasin.com/cekilis/c341ce2b5f",
    "https://www.oynasin.com/cekilis/02b1330048",
    "https://www.oynasin.com/cekilis/7b51e46b7c",
    "https://www.oynasin.com/cekilis/fad64bccfa",
    "https://www.oynasin.com/cekilis/e09ff47de8",
    "https://www.oynasin.com/cekilis/0ae897bc09",
    "https://www.oynasin.com/cekilis/7ab8d78fee",
    "https://www.oynasin.com/cekilis/1295f8d5bd",
    "https://www.oynasin.com/cekilis/bb43419cb8",
    "https://www.oynasin.com/cekilis/5360167775",
    "https://www.oynasin.com/cekilis/19844ad426",
    "https://www.oynasin.com/cekilis/a787209f5c",
    "https://www.oynasin.com/cekilis/fb1a316eac"
]

def fetch_winners(url, file_name):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        winners = []

        participants = soup.find_all('div', class_='participant')

        for participant in participants:
            name = participant.find('span', class_='par-name').get_text(strip=True).split()
            if len(name) == 2:
                first_name, last_name = name
            else:
                first_name = name[0]
                last_name = " ".join(name[1:])
            
            winners.append({
                'FirstName': first_name,
                'LastName': last_name
            })

        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(winners, f, ensure_ascii=False, indent=4)

        print(f"Kazananlar {file_name} dosyasına kaydedildi")
    else:
        print(f"URL {url} hata  {response.status_code}")

for idx, url in enumerate(urls):
    file_name = f'winners_{url.split("/")[-1]}.json'
    fetch_winners(url, file_name)
