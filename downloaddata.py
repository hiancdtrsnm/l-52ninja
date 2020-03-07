from pymongo import MongoClient
from datetime import datetime
import json
import enlighten



def dump_collection(db, collection):
    f = open(f'{db.name}({collection})-{datetime.now()}.json', 'w')

    print(f'{db.name}({collection})-{datetime.now()}')

    collection = db[collection]
    pbar = enlighten.Counter(total=collection.find({}).count(), desc='Basic', unit='documents')
    cursor = collection.find({})
    for document in cursor:
        f.write(f'{json.dumps(document, default=str, ensure_ascii=False)}\n')
        pbar.update()

    pbar.close()


def dump_collections(db, collections):
    for c in collections:
        dump_collection(db, c)