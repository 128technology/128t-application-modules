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
# import app_module_utils

URL = 'https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS13445'

MODULE_NAME = 'webex'
SERVICE_NAME = 'WEBEX'

def main():
    # app_id = app_module_utils.AppIdBuilder(MODULE_NAME, 3600)

    response = urllib2.urlopen(URL)
    jResponse = json.loads(response.read())
    for prefixes in jResponse["data"]["prefixes"]:
        # print prefixes["prefix"]
        if type(ipaddress.ip_network(prefixes["prefix"])) is IPv4Network:
            print(prefixes["prefix"])
        else:
            print("Skip v6")
    #  port_range = [ app_module_utils.AppIdBuilder.create_port_range(port, port) ]

     #       app_id.add_entry(SERVICE_NAME, ip + "/32", "tcp", port_range)
      #      app_id.error = ''
#        else:
#            app_id.error = 'No mappings found. Perhaps you are requesting too quickly?'
#    app_id.write_to_disk()

if __name__ == '__main__':
    main()

