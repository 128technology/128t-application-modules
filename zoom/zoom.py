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

MODULE_NAME = 'zoom'
SERVICE_NAME = 'ZOOM'

def main():
    app_id = app_module_utils.AppIdBuilder(MODULE_NAME, 86400)

    response = urllib2.urlopen(URL)
    lines = response.readlines()

    for line in lines:
         app_id.add_entry(SERVICE_NAME, line.rstrip())

    app_id.write_to_disk()

if __name__ == '__main__':
    main()

