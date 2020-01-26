from pymongo import MongoClient
import subprocess
from downloaddata import dump_collections
collections = ['expedientes', 'jobs', 'migrations', 'users']

cmd = ['ssh', '-L27018:localhost:27017', 'root@93.189.89.222']
process = subprocess.Popen(cmd)

print('kk')
client = MongoClient("localhost", 27018, maxPoolSize=50)
db = client.cge_info_system

dump_collections(db, collections)

process.kill()