#!/usr/bin/python
###############################################################################
# Zoom application identification module
# 10-Apr-2020, Patrick Timmons
###############################################################################

import json
import os
import re
import sys
import urllib2

BASE_PATH = '/etc/128technology/application-modules'
sys.path.append(BASE_PATH)
import app_module_utils

URL = 'https://assets.zoom.us/docs/ipranges/Zoom.txt'
cidr = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))$"

MODULE_NAME = 'zoom'
SERVICE_NAME = 'ZOOM'

def main():
    app_id = app_module_utils.AppIdBuilder(MODULE_NAME, 86400)

    response = urllib2.urlopen(URL)
    lines = response.readlines()

    for line in lines:
        if re.match(cidr, line):
            app_id.add_entry(SERVICE_NAME, line.rstrip())

    app_id.write_to_disk()

if __name__ == '__main__':
    main()

