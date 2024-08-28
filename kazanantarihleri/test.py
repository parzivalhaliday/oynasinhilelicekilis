import json
import os
from datetime import datetime
#KATILANLARLA KAZANANLARI EŞLEYİP TARİHLERİ EKLEYEN KOD KAZANANLARIN DATASINA
katilanlar_klasoru = r".\katilan"
kazananlar_klasoru = r".\kazanan"
cikis_klasoru = r".\kazanantarihleri"

katilanlar_dosyalari = [f for f in os.listdir(katilanlar_klasoru) if f.endswith('.json')]
kazananlar_dosyalari = [f for f in os.listdir(kazananlar_klasoru) if f.endswith('.json')]


for katilan_dosyasi in katilanlar_dosyalari:

    kazanan_dosyasi = katilan_dosyasi.replace('katilanlar', 'winners')

    if kazanan_dosyasi in kazananlar_dosyalari:

        katilanlar_dosyasi_yolu = os.path.join(katilanlar_klasoru, katilan_dosyasi)
        kazananlar_dosyasi_yolu = os.path.join(kazananlar_klasoru, kazanan_dosyasi)


        with open(katilanlar_dosyasi_yolu, "r", encoding="utf-8") as f:
            katilanlar = json.load(f)

        with open(kazananlar_dosyasi_yolu, "r", encoding="utf-8") as f:
            kazananlar = json.load(f)


        katilanlar = sorted(katilanlar, key=lambda x: datetime.strptime(x["CreateDate"], "%Y-%m-%d %H:%M:%S"))


        kazanan_katilimcilar = [
            katilimci for katilimci in katilanlar
            if any(
                kazanan["FirstName"] == katilimci["FirstName"] and kazanan["LastName"] == katilimci["LastName"]
                for kazanan in kazananlar
            )
        ]


        cikis_dosyasi = os.path.join(cikis_klasoru, f"tarihli-{katilan_dosyasi}")


        with open(cikis_dosyasi, "w", encoding="utf-8") as f:
            json.dump(kazanan_katilimcilar, f, ensure_ascii=False, indent=4)

        print(f"Kazananlar {cikis_dosyasi} dosyasına kaydedildi.")
    else:
        print(f"Eşleşen kazanan dosyası bulunamadı: {katilan_dosyasi}")
