#!/usr/bin/python
###############################################################################
# Cisco Webex application module
# 10-June-2020, Patrick Timmons
###############################################################################

import json
import sys
import urllib2
import ipaddress

sys.path.append('/etc/128technology/application-modules')
import app_module_utils

URL = 'https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS13445'

"""
RIPE is kind enough to provide access to all prefixes announced per ASN, and this
is the resource we're using here. The HTTPS query above will return JSON-formatted
output like the following:

--
{
    "status": "ok",
    "server_id": "app021",
    "status_code": 200,
    "version": "1.2",
    ...
    "data": {
        "resource": "13445",
        "prefixes": [
            {
                "timelines": [
                    {
                        "endtime": "2020-06-10T08:00:00",
                        "starttime": "2020-05-27T08:00:00"
                    }
                ],
                "prefix": "208.253.254.0/24"
            },
     ...
--
The python script then will then collect each 'prefix' and create the appID-
formatted JSON output as /var/run/128technology/application-module/webex.json

"""

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

