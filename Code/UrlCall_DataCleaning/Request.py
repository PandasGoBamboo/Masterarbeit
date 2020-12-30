# ------------------------------------------------------------------------
# Skript um Daten der Contentschnittstelle des ZDFs zu laden
# 
# ------------------------------------------------------------------------

import requests
from datetime import date

# Einstellbare parameter

# Searchquerry
q = '*'

# Maxcount results
hitcount = 2

zdf = 'zdf'

category = 'dokumentation'

broadcast = 'terra-x'

# show = 'soehne-der-sonne-die-maya-100'

path = '/' + zdf + '/' + category # + '/' + broadcast # + '/' + show

# Videotype
videotype = 'episode_episode'

# sort By 'date' or 'title'
sort = 'date'

# sort order 'desc' = descending, 'asc' = ascending
order = 'desc'

# zeigt ausführliche Ergebnisse
advan1 = 'portal-delivery'

# zeigt ausführliche Erklärungen z.B. editorial tags
advan2 = 'explain:true'

# Baut Suchanfrage zusammen
payload = {'q': q, 'limit': hitcount, 'paths': path, 'videotypes': videotype, 'sortBy': sort, 'sortOrder': order, 'profile': advan1, 'tuning': advan2
}
# Authentifizierungstoken
headers = {'API-Auth': 'Bearer Authentifizierungstoken'}

# Request erstellen

r = requests.get("https://api.zdf.de/search/documents", headers=headers, params=payload)

# Heutiges Datum  
today = date.today()
today = today.strftime("%d_%m")

# Speichern der Datei
with open("Pfad/zum/Speicherort/" + today + "_" + zdf + "_" + category + "_" + broadcast + ".json", "w", encoding="utf-8") as outfile:
    outfile.write(r.text)

print("Done")