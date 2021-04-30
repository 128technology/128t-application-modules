# 128T AppID Module: Facebook

This AppID module will identify traffic associated with Facebook; adding this module to your system will identify the new application-name "FACEBOOK" which can then be prioritized using service-policy, service-route handling, etc.

> Note: the script operates by retrieving IPv4 prefixes from `https:/stats.ripe.net`, therefore the system must have internet access to retrieve the document.

The service name for this module is FACEBOOK. Please reference this in the `application-name` field of the service you create.

## Dependencies

This module leverages the third party library [netaddr](https://github.com/netaddr/netaddr) to aggregate CIDR prefixes. This library must be installed independently using `pip install netaddr`.

## Disclaimer

This is a community contributed module. No official technical support is provided by Juniper Networks on its use. Please open an issue in Github when encountering any difficulty.