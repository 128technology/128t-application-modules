# 128T AppID Module: Twitch

This AppID module will identify traffic associated with Twitch; adding this module to your system will identify the new application-name "TWITCH" which can then be prioritized using service-policy, service-route handling, etc.

> Note: the script operates by retrieving all of the BGP prefixes advertised by AS46489, and filtering out all IPv6 prefixes.

The service name for this module is **TWITCH**. Please reference this in the `application-name` field of the service you create.

> Note: this presumes the use of 128T release 5.0.0 (or newer), and presence of a parent service named `internet`.

Disclaimer: this is a community contributed module.
