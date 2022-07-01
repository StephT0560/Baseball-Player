import requests
import sqlalchemy as db
import pandas as pd

# Returns a list of keys
def getList(dict):
    return list(dict.keys())


# Returns the nested dictionary from a key
def nestedGet(dic, keys):
    for key in keys:
        dic = dic[key]
    return dic


# Returns dictionary from API data
def createAPIData(url):
    response = requests.get(url)
    data = response.json()
    return data


# filter dictionary data
def filterDict(d, search):
    return {k: v for k, v in d.items() if k.startswith(search)}


# Returns player info from API data
def parsing_MLB_data(Api_data):
    data_keys = getList(Api_data)
    catogories = nestedGet(Api_data, data_keys)
    query_dict = catogories["queryResults"]
    player_info_dict = query_dict["row"]
    player_info_keys = getList(player_info_dict)

    # creating dictionary suitable for database
    table_dict = {}
    for key in player_info_keys:
        table_dict[key] = [player_info_dict[key]]

    return table_dict


url = "http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='cespedes%25'"
data = createAPIData(url)
table_dict = parsing_MLB_data(data)

df = pd.DataFrame.from_dict(table_dict)
col_names = list(df.columns.values)

engine = db.create_engine("sqlite:///data_base_name.db")
df.to_sql("Player", con=engine, if_exists="replace", index=True)
query_result = engine.execute("SELECT * FROM Player;").fetchall()
print(pd.DataFrame(query_result))
