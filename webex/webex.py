#!/usr/bin/python
###############################################################################
# Cisco Webex application module
# 10-June-2020, Patrick Timmons
###############################################################################

import json
import os
import sys
import urllib2
import ipaddress

BASE_PATH = '/etc/128technology/application-modules'
sys.path.append(BASE_PATH)
import app_module_utils

URL = 'https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS13445'

MODULE_NAME = 'webex'
SERVICE_NAME = 'WEBEX'

def main():
    app_id = app_module_utils.AppIdBuilder(MODULE_NAME, 3600)

    response = urllib2.urlopen(URL)
    jResponse = json.loads(response.read())
    for prefixes in jResponse["data"]["prefixes"]:
        try:
            v4prefix = ipaddress.IPv4Network(prefixes["prefix"])
            app_id.add_entry(SERVICE_NAME, str(v4prefix))
        except:
            continue
    app_id.write_to_disk()

if __name__ == '__main__':
    main()

