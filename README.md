# 128T AppID Modules

This repository contains scripts for use with your 128T *Session Smart Router*, to extend its application identification capability. For more information on the 128T's Application Identification behavior, and how to configure AppID modules, refer to our [user documentation](https://docs.128technology.com/docs/concepts_appid#appid-using-modules).

## About AppID Modules

Generally, AppID modules are scripts placed in `/etc/128technology/application-modules/` that generate JSON output to `/var/run/128technology/application-modules/`. This JSON output is dynamically, and periodically ingested by the 128T to create FIB entries for a designated `service` within the 128T's configuration.

Each module can specify its time to live; after this TTL expires, the 128T will re-execute the AppID script and (re)generate the JSON file.

## Contributing

Each contribution should include comments that indicate:

- The author of the module
- The purpose of the module
- Any caveats, etc.