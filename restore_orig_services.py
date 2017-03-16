#!/usr/bin/env python
# required packages, install with pip if not present
import requests
import json
# disable self-signed cert warnings
requests.packages.urllib3.disable_warnings()
# replace these variables
vra_ip = '192.168.1.227'
vra_user = 'administrator@vsphere.local'
vra_pass = 'VMware1!'
vra_tenant = 'vsphere.local'
# don't replace anything from here
# get our authorization token
uri = 'https://'+vra_ip+'/identity/api/tokens'
headers = {'Accept':'application/json','Content-Type':'application/json'}
payload = '{"username":"'+vra_user+'","password":"'+vra_pass+'","tenant":"'+vra_tenant+'"}'
r = requests.post(uri, headers=headers, verify=False, data=payload)
token = 'Bearer '+str(json.loads(r.text)["id"])
# delete the current icon
uri = 'https://'+vra_ip+'/catalog-service/api/icons/cafe_default_icon_genericAllServices'
headers = {'Authorization':token}
r = requests.delete(uri, headers=headers, verify=False)
if r.status_code == 201:
    print "Restoration successful"
else:
    print "Expected return code 204, got "+r.status_code+" something went wrong"
