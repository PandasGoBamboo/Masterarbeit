import json
from datetime import date
from request import zdf, category

# Für Ordnung bei der Datenspeicherung
today = date.today()
today = today.strftime("%d_%m")

# Datei, die bereinigt werden soll. 
with open("Pfad/zur/Json/Datei", "r", encoding="utf-8") as infile:
    data = json.load(infile)

# Daten aus dem [hits] Objekt laden
hits = (data['Ebene1']['Ebene2']['Ebene3']['hits'])

popedKeys = [
    "Schlüssel", "die", "entfernt", "werden", "sollen"
    ]

# Öffnet Datei für Output
with open("Pfad/zum/Output/Ordner/" + today + "NamederDatei.json", "w", encoding='utf-8') as outfile:
    
    for dic in hits:
        dic.pop("Entfernter Schlüssel1")
        dic.pop("Entfernter Schlüssel2")
        dic.pop("Entfernter Schlüssel3")
        dic.pop("Entfernter Schlüssel4")
        src = dic['Entfernter Schlüssel5']

        for key in popedKeys:
            src.pop(key)
            
        json.dump(dic, outfile, ensure_ascii=False, indent=2)
