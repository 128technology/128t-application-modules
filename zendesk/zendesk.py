#!/usr/bin/python
###############################################################################
# Zendesk application module
# 29-July-2021, Patrick Timmons
###############################################################################

import json
import sys
import urllib3
import ipaddress

sys.path.append('/etc/128technology/application-modules')
import app_module_utils

URL = 'https://all.zendesk.com/ips'

"""
Zendesk conveniently offers a public API that lets you retrieve the list of
IP addresses that they use for ingress traffic and egress traffic. For the
purposes of this application module we are only concerning ourselves with
their "ingress" traffic. (The "ingress" perspective is theirs.)

More information at the following links:
https://support.zendesk.com/hc/en-us/articles/203660846-Configuring-your-firewall-for-use-with-Zendesk
https://developer.zendesk.com/api-reference/ticketing/account-configuration/public_ips/

"""

MODULE_NAME = 'zendesk'
SERVICE_NAME = 'ZENDESK'

def main():
    app_id = app_module_utils.AppIdBuilder(MODULE_NAME, 3600)

    http = urllib3.PoolManager()
    response = http.request('GET', URL)
    if response.status == 200:
        jResponse = json.loads(response.data.decode('utf-8'))
        for prefix in jResponse["ips"]["ingress"]["all"]:
            try:
                v4prefix = ipaddress.IPv4Network(prefix)
                app_id.add_entry(SERVICE_NAME, str(v4prefix))
            except:
                continue
    app_id.write_to_disk()

if __name__ == '__main__':
    main()
