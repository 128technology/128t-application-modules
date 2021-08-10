#!/usr/bin/python
###############################################################################
# Oracle application module
# 10-August-2021, Patrick Timmons
###############################################################################

import json
import sys
import urllib3
import ipaddress

sys.path.append('/etc/128technology/application-modules')
import app_module_utils

URL = 'https://docs.oracle.com/en-us/iaas/tools/public_ip_ranges.json'

"""
Oracle conveniently offers a public API that lets you retrieve the list of
IP addresses that they use for ingress traffic and egress traffic.

More information at the following links:
https://docs.oracle.com/en-us/iaas/Content/General/Concepts/addressranges.htm

"""

MODULE_NAME = 'oracle'
SERVICE_NAME = 'ORACLE'

def main():
    app_id = app_module_utils.AppIdBuilder(MODULE_NAME, 86400)

    http = urllib3.PoolManager()
    response = http.request('GET', URL)
    if response.status == 200:
        jResponse = json.loads(response.data.decode('utf-8'))
        for region in jResponse["regions"]:
            for prefix in region["cidrs"]:
                try:
                    v4prefix = ipaddress.IPv4Network(prefix["cidr"])
                    app_id.add_entry(SERVICE_NAME, str(v4prefix))
                except:
                    continue
    app_id.write_to_disk()

if __name__ == '__main__':
    main()
