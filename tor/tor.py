#!/usr/bin/python
###############################################################################
# Tor proxy application module
# 29-Jan-2020, Patrick Timmons (with contributions by Joe Developer)
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

MODULE_NAME = 'tor'
SERVICE_NAME = 'TOR'

def main():
    app_id = app_module_utils.AppIdBuilder(MODULE_NAME, 3600)

    response = urllib2.urlopen(URL)
    lines = response.readlines()

    for line in lines:
        matches = re.search("^([0-9.]+)\|(.*?)\|([0-9]+)\|([0-9]+)\|([A-Z]+)\|", line)
        if matches is not None:
            flags = matches.group(5)
            if "G" not in flags:
                # skip anything but guard nodes
                continue
            ip = matches.group(1)
            port = matches.group(3)
            port_range = [ app_module_utils.AppIdBuilder.create_port_range(port, port) ]

            app_id.add_entry(SERVICE_NAME, ip + "/32", "tcp", port_range)
            app_id.error = ''
#        else:
#            app_id.error = 'No mappings found. Perhaps you are requesting too quickly?'

    app_id.write_to_disk()

if __name__ == '__main__':
    main()

