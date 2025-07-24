from pymongo import MongoClient
from bson.json_util import dumps

url = "mongodb+srv://florezj328:Peperoni123@cluster0.dpngxg6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def ConMongo():

    client = MongoClient(url)
    db = client["sample_supplies"]
    collection = db["sales"]

    data = list(collection.find())

    json_data = dumps(data)

    with open("data.json", "w", encoding="utf-8") as f:
        f.write(json_data)

