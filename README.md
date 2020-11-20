# 128T AppID Modules

This repository contains scripts for use with your 128T *Session Smart Router*, to extend its application identification capability. For more information on the 128T's Application Identification behavior, and how to configure AppID modules, refer to our [user documentation](https://docs.128technology.com/docs/concepts_appid#appid-using-modules).

## About AppID Modules

Generally, AppID modules are scripts placed on the 128T's filesystem that generate JSON output to `/var/run/128technology/application-modules/`. This JSON output is dynamically, and periodically ingested by the 128T to create FIB entries for a designated `service` within the 128T's configuration.

Each module can specify its time to live; after this TTL expires, the 128T will re-execute the AppID script and (re)generate the JSON file.

## Installing AppID Modules

Copy the script (e.g., `zoom.py`) to `/etc/128technology/application-modules` on the target router. Ensure the permissions are correct using the command `chmod +x zoom.py`. You can test that the script is executable and functioning properly by running it manually: `./zoom.py`. You should see it create a file named `/var/run/128technology/application-modules/zoom.json`, with a number of prefixes contained in it.

## Configuring your 128T to use the Module

Each of the 128T application modules in this repository uses a specific NAME (the naming convention in these modules will use ALL CAPS) that needs to be configured within a `service` definition on your 128T. This NAME will be referenced in the `application-name` field in the configuration. For example:

```
admin@labsystem1.fiedler# show config running authority service ZOOM

config

    authority

        service  ZOOM
            name                  ZOOM

            description           "Zoom meetings"
            scope                 private
            application-name      ZOOM

            access-policy         trusted
                source      trusted
                permission  allow
            exit
            service-policy        voip-video
            share-service-routes  false
        exit
    exit
exit
```

In the case of the Zoom plugin, the `application-name` is ZOOM. The README.md file for each of the modules will indicate its `application-name`.

After configuring the service, don't forget to configure a `service-route` following the basic principles of 128T configuration design. For more information, [review our documentation](https://docs.128technology.com/docs/concepts_glossary/#service-routes).

## Contributing

Each contribution should include comments that indicate:

- The author of the module
- The purpose of the module
- Any caveats, etc.