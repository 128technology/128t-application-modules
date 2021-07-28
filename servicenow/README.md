# 128T AppID Module: ServiceNow

This AppID module will identify traffic associated with ServiceNow; adding this module to your system will identify the new application-name "SERVICENOW" which can then be prioritized using service-policy, service-route handling, etc.

> Note: the script operates by retrieving all of the BGP prefixes advertised by AS16839 (the "ServiceNow, Inc." ASN), and filtering out all IPv6 prefixes.

The service name for this module is **SERVICENOW**. Please reference this in the `application-name` field of the service you create.

Disclaimer: this is a community contributed module.
