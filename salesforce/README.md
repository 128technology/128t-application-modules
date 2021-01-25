# 128T AppID Module: Salesforce

This AppID module will identify traffic associated with Salesforce; adding this module to your system will identify the new application-name "SALESFORCE" which can then be prioritized using service-policy, service-route handling, etc.

> Note: the script operates by retrieving all of the BGP prefixes advertised by AS14340, and filtering out all IPv6 prefixes.

The service name for this module is **SALESFORCE**. Please reference this in the `application-name` field of the service you create.

Disclaimer: this is a community contributed module.