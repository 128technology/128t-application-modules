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
Github conveniently offers a public API that lets you retrieve the list of
IP addresses that they use via their API.

For more information:
https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/about-githubs-ip-addresses
"""

MODULE_NAME = 'github'

def main():
    app_id = app_module_utils.AppIdBuilder(MODULE_NAME, 86400)

    user_agent = {'User-Agent': 'SSR Github AppID Module; github.com/128technology/128t-application-modules'}
    http = urllib3.PoolManager()
    response = http.request('GET', URL, headers=user_agent)
    prefixes = []
    if response.status == 200:
        jResponse = json.loads(response.data.decode('utf-8'))
        for section in ['hooks', 'web', 'api', 'git', 'packages', 'importer', 'actions', 'dependabot']:
            for prefix in jResponse[section]:
                try:
                    v4prefix = ipaddress.IPv4Network(prefix)
                    prefixes.append(v4prefix)
                except:
                    continue

    # this next section deduplicates the list, since Github uses the same CIDR for different services
    # so there are various prefixes that appear more than once.
    if len(prefixes) > 0:
        prefixes = list(dict.fromkeys(prefixes))
    for prefix in prefixes:
        app_id.add_entry("GITHUB", str(v4prefix))

    app_id.write_to_disk()

if __name__ == '__main__':
    main()
