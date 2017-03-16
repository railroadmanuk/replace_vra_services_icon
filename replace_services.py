#!/usr/bin/env python
# required packages, install with pip if not present
import requests
import json
# disable self-signed cert warnings
requests.packages.urllib3.disable_warnings()
# replace these variables
filename = 'service.png'
vra_ip = '192.168.1.227'
vra_user = 'administrator@vsphere.local'
vra_pass = 'VMware1!'
vra_tenant = 'vsphere.local'
# don't replace anything from here
# open file and encode it in b64
with open("./"+filename, "rb") as f:
    data = f.read()
    encoded = data.encode("base64")
encoded = encoded.replace("\r","")
encoded = encoded.replace("\n","")
# get our authorization token
uri = 'https://'+vra_ip+'/identity/api/tokens'
headers = {'Accept':'application/json','Content-Type':'application/json'}
payload = '{"username":"'+vra_user+'","password":"'+vra_pass+'","tenant":"'+vra_tenant+'"}'
r = requests.post(uri, headers=headers, verify=False, data=payload)
token = 'Bearer '+str(json.loads(r.text)["id"])
# send the new icon to the API
uri = 'https://'+vra_ip+'/catalog-service/api/icons'
headers = {'Accept':'application/json','Content-Type':'application/json','Authorization':token}
payload = '{"id":"cafe_default_icon_genericAllServices","fileName":"'+filename+'","contentType":"image/png","image":"'+encoded+'"}'
r = requests.post(uri, headers=headers, verify=False, data=payload)
if r.status_code == 201:
    print "Replacement successful"
else:
    print "Expected return code 201, got "+r.status_code+" something went wrong"
