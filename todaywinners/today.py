import random
import requests
import json
import time
import os

# HEADER  Cookie VE Referer EDİTLEYİN
x_header = {
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    'h-country-code': 'TR',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    'Content-Type': 'application/json; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'h-region-code': 'TR',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://www.oynasin.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'REFERANS İÇİN HERHANGI Bİ URL?',      
    'Accept-Language': 'en-US,en;q=0.9,tr;q=0.8',
    'Cookie': 'oynasin_session=SESSIONTOKEN; dark-theme=true', 
    'dnt': '1',
    'sec-gpc': '1'
}
urls = [
    "https://www.oynasin.com/cekilis/80c369080a",
    "https://www.oynasin.com/cekilis/8a67632b33",
    "https://www.oynasin.com/cekilis/fc008c6f89",
    "https://www.oynasin.com/cekilis/f12ae15872",
    "https://www.oynasin.com/cekilis/b32b217581"
]


output_dir = r'C:\Users\parzival\Desktop\oynasindoc\yee\todaywinners'

os.makedirs(output_dir, exist_ok=True)

for url in urls:
    unique_id = url.split("/")[-1]  
    output_file = os.path.join(output_dir, f'katilanlar_{unique_id}.json')

    all_names = []
    n = 1  
    while True:
        payload = {"page": f"{n}", "query": ""}
        try:
            response = requests.post(f"{url}/participants", json=payload, headers=x_header)

            if response.status_code == 200:
                data = response.json()
                participants = data["data"]["data"]

                if not participants:
                    print(f"{url} - Page {n} is empty, ending loop.")
                    break

                for participant in participants:
                    create_date = participant['CreateDate']
                    first_name = participant['CustomerData']["FirstName"]
                    last_name = participant['CustomerData']["LastName"]
                    all_names.append({
                        "CreateDate": create_date,
                        "FirstName": first_name,
                        "LastName": last_name
                    })

                print(f"{url} - Page {n} processed.")
            else:
                print(f"{url} - Error loading page {n}: {response.status_code}")
                break

        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            break  

        n += 1  
        time.sleep(random.randint(1, 3)) 

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_names, f, ensure_ascii=False, indent=4)

    print(f"{url} - Data saved to {output_file}.")
