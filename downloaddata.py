from pymongo import MongoClient
from datetime import datetime
import json
import enlighten
client = MongoClient("localhost", 8686, maxPoolSize=50)
db = client.cge_info_system

collections = ['expedientes', 'jobs', 'migrations', 'users']

def dump_collection(db, collection):
    f = open(f'{db.name}({collection})-{datetime.now()}.json', 'w')

    print(f'{db.name}({collection})-{datetime.now()}')

    collection = db[collection]
    pbar = enlighten.Counter(total=collection.find({}).count(), desc='Basic', unit='documents')
    cursor = collection.find({})
    for document in cursor:
        f.write(json.dumps(document, default=str, ensure_ascii=False))
        pbar.update()

    pbar.close()

for c in collections:
    dump_collection(db, c)