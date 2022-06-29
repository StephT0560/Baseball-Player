import requests
url =  "http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='cespedes%25'"
r = requests.get(url)
print("MLB DATA!")
print(r)
print(r.json())