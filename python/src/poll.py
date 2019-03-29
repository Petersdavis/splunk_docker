from time import gmtime, strftime, sleep
from dotenv import load_dotenv
from pathlib import Path
import time;
import datetime
import httplib2
import requests
import json
import splunklib.client as client

env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

#service = client.connect(host='10.114.8.239', port=8089, username='petersdavis', password='12345678')
#myindex = service.indexes["cloudflare"]
#mysocket = myindex.attach(sourcetype='_json',host='cloudflare_python_script')

exec(open("./cloudflare/cloudflare.py").read())

h = httplib2.Http()
start_at = 0

api = Cloudflare()

f=open("/mnt/src/logs/raw_log", "a+")

while 1==1:
    now=time.time()
    start= now - 630
    end = now - 600

    records = api.getRecords(start, end)

    for line in records:
        #mysocket.send(line)
        print(line)
        f.write(line)
        f.write("\n")
        sleep(0.01)

    sleep(30 - (time.time()-now))
