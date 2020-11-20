# 128T AppID Module: Netflix

This AppID module will identify traffic associated with Netflix; adding this module to your system will identify the new application-name "NETFLIX" which can then be prioritized using service-policy, service-route handling, etc.

> Note: the script operates by retrieving all of the BGP prefixes advertised by AS2906, and filtering out all IPv6 prefixes.

The service name for this module is **NETFLIX**. Please reference this in the `application-name` field of the service you create.

Disclaimer: this is a community contributed module.