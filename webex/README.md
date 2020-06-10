# 128T AppID Module: Cisco Webex

This AppID module will identify traffic associated with Cisco Webex; adding this module to your system will identify the new application-name "WEBEX" which can then be prioritized using service-policy, service-route handling, etc.

> Note: the script operates by retrieving all of the BGP prefixes advertised by AS13445 (the "Cisco Webex LLC" ASN), and filtering out all IPv6 prefixes.

Disclaimer: this is a community contributed module.
