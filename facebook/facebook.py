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

URL = 'https://www.netify.ai/resources/applications/facebook'

MODULE_NAME = 'facebook'
SERVICE_NAME = 'FACEBOOK'

def main():
    app_id = app_module_utils.AppIdBuilder(MODULE_NAME, 3600)

    response = urllib2.urlopen(URL)
    lines = response.readlines()

    for line in lines:
        matches = re.search("^\s*<li>(([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2])))?<\/li>", line)
        if matches is not None:
            cidr = matches.group(1)

            app_id.add_entry(SERVICE_NAME, cidr)
            app_id.error = ''
#        else:
#            app_id.error = 'No mappings found. Perhaps you are requesting too quickly?'

    app_id.write_to_disk()

if __name__ == '__main__':
    main()

