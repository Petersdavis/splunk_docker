import os
import requests
import json



class Cloudflare:
    import os
    SECRET_KEY = os.getenv("EMAIL")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

    CLOUDFLARE_USER=os.getenv("CLOUDFLARE_USER")
    CLOUDFLARE_KEY=os.getenv("CLOUDFLARE_KEY")
    CLOUDFLARE_ZONE=os.getenv("CLOUDFLARE_ZONE")

    FIELDS="ClientIP,ClientCountry,ClientRequestUserAgent,ClientRequestHost,OriginResponseTime,EdgeStartTimestamp,OriginResponseBytes,OriginResponseStatus"
    SAMPLE="1"
    ZONE=\"CLOUDFLARE_ZONE\"
    HEADERS={'X-Auth-Email':'CLOUDFLARE_USER' , 'X-Auth-Key':'CLOUDFLARE_KEY' , 'Content-Type':'application/json'}

    def getRecords(self, start_at, end_at):
        url = 'https://api.cloudflare.com/client/v4/zones/'+self.ZONE+'/logs/received?start='+str(int(start_at+0.5))+'&end='+str(int(end_at+0.5))+'&count=500&sample='+self.SAMPLE+'&fields='+ self.FIELDS + '&timestamps=rfc3339'
        r = requests.get(url, headers=self.HEADERS)
        return r.text.splitlines()


curl -X GET "https://api.cloudflare.com/client/v4/zones/7b030d952484720e5ebfdfe87f6b38a1/logs/received/fields" \
     -H "X-Auth-Email: itsupport@lifelearn.com" \
     -H "X-Auth-Key: c7cf6f1a5ef2e8920f04a75ebdea9369bb433" \
     -H "Content-Type: application/json"