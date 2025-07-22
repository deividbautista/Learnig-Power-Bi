# from pymongo import MongoClient
# import json
# from bson import ObjectId 


# connection = "mongodb+srv://florezj328:Peperoni123@cluster0.dpngxg6.mongodb.net/"
# cliente = MongoClient(connection)

# db = cliente["sample_weatherdata"]

# collection = db["data"]

# documents = list(collection.find_all())

# # data = []
# # for doc in documents:
   
# #    print(doc)
# #    doc["_id"] = str(doc["_id"])
# #    data.append(doc)


# json_datos = json.dumps(documents, indent=4)

# # with open("prueba.json", "w") as f:
# #     f.write(json_datos)

# cliente.close

# print(json_datos)


from pymongo import MongoClient
from bson.json_util import dumps

uri = "mongodb+srv://florezj328:Peperoni123@cluster0.dpngxg6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["sample_weatherdata"]
collection = db["data"]


data = list(collection.find())

json_data = dumps(data)

with open("data.json", "w", encoding="utf-8") as f:
    f.write(json_data)

