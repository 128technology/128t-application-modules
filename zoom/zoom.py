#!/usr/bin/python
###############################################################################
# Zoom application identification module
# 10-Apr-2020, Patrick Timmons
# 18-Jan-2022, Gene Shtirmer
###############################################################################

import json
import os
import re
import sys
import urllib2

BASE_PATH = '/etc/128technology/application-modules'
sys.path.append(BASE_PATH)
import app_module_utils

URL1 = 'https://assets.zoom.us/docs/ipranges/Zoom.txt'
URL2 = 'https://assets.zoom.us/docs/ipranges/ZoomMeetings.txt'
URL3 = 'https://assets.zoom.us/docs/ipranges/ZoomCRC.txt'
URL4 = 'https://assets.zoom.us/docs/ipranges/ZoomPhone.txt'
URL5 = 'https://assets.zoom.us/docs/ipranges/ZoomCDN.txt'

URLs = [URL1, URL2, URL3, URL4, URL5]
ipv4 = "^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$"

MODULE_NAME = 'zoom'
SERVICE_NAME = 'ZOOM'

def main():
    app_id = app_module_utils.AppIdBuilder(MODULE_NAME, 86400)

    for url in URLs:
       response = urllib2.urlopen(url)
       lines = response.readlines()
       for line in lines:
           if re.match(ipv4, line):
               app_id.add_entry(SERVICE_NAME, line.rstrip())
    app_id.write_to_disk()

if __name__ == '__main__':
    main()
