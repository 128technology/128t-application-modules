#!/usr/bin/python
###############################################################################
# AWS application module
# 10-August-2021, Patrick Timmons
###############################################################################

import json
import sys
import urllib3
import ipaddress

sys.path.append('/etc/128technology/application-modules')
import app_module_utils

URL = 'https://ip-ranges.amazonaws.com/ip-ranges.json'

"""
Oracle conveniently offers a public API that lets you retrieve the list of
IP addresses that they use for ingress traffic and egress traffic.

More information at the following links:
https://docs.oracle.com/en-us/iaas/Content/General/Concepts/addressranges.htm

"""

MODULE_NAME = 'aws'

def main():
    app_id = app_module_utils.AppIdBuilder(MODULE_NAME, 86400)

    http = urllib3.PoolManager()
    response = http.request('GET', URL)
    if response.status == 200:
        jResponse = json.loads(response.data.decode('utf-8'))
        for prefix in jResponse["prefixes"]:
            try:
                v4prefix = ipaddress.IPv4Network(prefix["ip_prefix"])
                app_id.add_entry("AWS-" + prefix["service"], str(v4prefix))
            except:
                continue
    app_id.write_to_disk()

if __name__ == '__main__':
    main()
