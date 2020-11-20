# 128T AppID Module: TOR

This AppID module is to identify outbound traffic destined for the TOR (The Onion Router) network. It retrieves a list of TOR "guard nodes" (the nodes that TOR clients connect to), such that any and all connections to the TOR network are properly classified.

> Note: the script retrieves the list of TOR nodes from https://www.dan.me.uk/tornodes, which can only be queried every 30 minutes. Any attempts to query faster than every 30 minutes will result in an error, and hence an empty set of prefixes. The default refresh time for this script is every hour (3600 seconds).

This script will generate a LOT of FIB entries. (There are a lot of TOR guard nodes out there.) As of this writing, this is 5,500 unique prefixes; for each tenant that is granted access to this service, expect that many new FIB entries. Be careful about subtenants, too: this can balloon up quickly.

The service name for this module is **TOR**. Please reference this in the `application-name` field of the service you create.

Disclaimer: this is meant for experimentation/educational purposes only.
