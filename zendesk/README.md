# 128T AppID Module: Zendesk

This AppID module will identify traffic associated with Zendesk; adding this module to your system will identify the new application-name "ZENDESK" which can then be prioritized using service-policy, service-route handling, etc.

> Note: the script operates by leveraging a public API offered by Zendesk for this purpose. For more information please visit [Configuring your firewall for use with Zendesk](https://support.zendesk.com/hc/en-us/articles/203660846-Configuring-your-firewall-for-use-with-Zendesk) and [information on their public API for retrieving IP addresses](https://developer.zendesk.com/api-reference/ticketing/account-configuration/public_ips/).

The service name for this module is **ZENDESK**. Please reference this in the `application-name` field of the service you create.

Disclaimer: this is a community contributed module.
