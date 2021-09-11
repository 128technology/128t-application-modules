#!/usr/bin/python
###############################################################################
# Github application module
# 11-September-2021, Patrick Timmons
###############################################################################

import json
import sys
import urllib3
import ipaddress

sys.path.append('/etc/128technology/application-modules')
import app_module_utils

URL = 'https://api.github.com/meta'

"""
Amazon conveniently offers a public API that lets you retrieve the list of
IP addresses that they use for ingress traffic and egress traffic.

More information at the following link(s):
https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html

"""

MODULE_NAME = 'github'

def main():
    app_id = app_module_utils.AppIdBuilder(MODULE_NAME, 86400)

    http = urllib3.PoolManager()
    response = http.request('GET', URL)
    if response.status == 200:
        jResponse = json.loads(response.data.decode('utf-8'))
        for section in ['hooks', 'web', 'api', 'git', 'packages', 'importer', 'actions', 'dependabot']:
            for prefix in jResponse[section]:
                try:
                    v4prefix = ipaddress.IPv4Network(prefix)
                    app_id.add_entry("GITHUB", str(v4prefix))
                except:
                    continue
    app_id.write_to_disk()

if __name__ == '__main__':
    main()