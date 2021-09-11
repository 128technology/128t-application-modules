# 128T AppID Module: Github

This AppID module will identify traffic associated with Github; adding this module to your system will identify the new application-name "GITHUB" which can then be prioritized using service-policy, service-route handling, etc.

> Note: the script operates by accessing a public API published by Github for this purpose. Please note: we filter out all IPv6 addresses.

The service name for this module is **GITHUB**. Please reference this in the `application-name` field of the service you create.

Disclaimer: this is a community contributed module.
