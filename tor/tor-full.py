#!/usr/bin/python
###############################################################################
# Tor proxy application module (full node list)
# 22-Jan-2022, Patrick Timmons (with contributions by Joe Developer)
###############################################################################

import json
import os
import re
import sys
import urllib2

BASE_PATH = '/etc/128technology/application-modules'
sys.path.append(BASE_PATH)
import app_module_utils

URL = 'https://www.dan.me.uk/tornodes'

MODULE_NAME = 'tor-full'
SERVICE_NAME = 'TOR'

def main():
    app_id = app_module_utils.AppIdBuilder(MODULE_NAME, 14400)
    changed = False
    prefix_list = {}

    response = urllib2.urlopen(URL)
    lines = response.readlines()

    for line in lines:
        matches = re.search("^([0-9.]+)\|(.*?)\|([0-9]+)\|([0-9]+)\|([A-Z]+)\|", line)
        if matches is not None:
            changed = True
            # flags = matches.group(5)
            ip = matches.group(1)
            if ip in prefix_list.keys():
                prefix_list[ip].append(app_module_utils.AppIdBuilder.create_port_range(
                                       matches.group(3), matches.group(3)))
            else:
                prefix_list[ip] = [ app_module_utils.AppIdBuilder.create_port_range(
                                    matches.group(3), matches.group(3)) ]

    for ip in prefix_list.keys():
        app_id.add_entry(SERVICE_NAME, ip + "/32", "tcp", prefix_list[ip])
#        else:
#            app_id.error = 'No mappings found. Perhaps you are requesting too quickly?'

    if changed:
        app_id.write_to_disk()

if __name__ == '__main__':
    main()

