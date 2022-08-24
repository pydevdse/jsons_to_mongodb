import json
import os
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["olx"]
mycol = mydb["rent"]


class JsomMogno():
    def __init__(self, path="./jsons/"):
        self.path = path

    def load_jsons(self):
        return os.listdir(self.path)

    def save_to_mongo(self):
        for fname in self.load_jsons():
            print("filename:", fname)
            items = json.loads(open(self.path+fname).read())
            print("items:", len(items))
            for item in items:
                if mydb.mycol.find_one({"id": item['items']['id']}):
                    continue
                mydb.mycol.insert_one(item['items'])
            print(mydb.mycol.count_documents({}))


if __name__ == '__main__':

    print(myclient.list_database_names())
    print(mydb.list_collection_names())
    print(mydb.mycol.count())
    path_to_jsons = "./jsons/"
    # JsomMogno().save_to_mongo()
