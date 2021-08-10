#!/usr/bin/python
###############################################################################
# Atlassian application module
# 10-August-2021, Patrick Timmons
###############################################################################

import json
import sys
import urllib3
import ipaddress

sys.path.append('/etc/128technology/application-modules')
import app_module_utils

URL = 'https://ip-ranges.atlassian.com/'

"""
Atlassian conveniently offers a public API that lets you retrieve the list of
IP addresses that they use for ingress traffic and egress traffic.

More information at the following links:
https://support.atlassian.com/organization-administration/docs/ip-addresses-and-domains-for-atlassian-cloud-products/

"""

MODULE_NAME = 'atlassian'
SERVICE_NAME = 'ATLASSIAN'

def main():
    app_id = app_module_utils.AppIdBuilder(MODULE_NAME, 3600)

    http = urllib3.PoolManager()
    response = http.request('GET', URL)
    if response.status == 200:
        jResponse = json.loads(response.data.decode('utf-8'))
        for prefix in jResponse["items"]:
            try:
                v4prefix = ipaddress.IPv4Network(prefix["cidr"])
                app_id.add_entry(SERVICE_NAME, str(v4prefix))
            except:
                continue
    app_id.write_to_disk()

if __name__ == '__main__':
    main()
