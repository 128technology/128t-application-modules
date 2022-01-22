# 128T AppID Module: TOR

This AppID module is to identify outbound traffic destined for the Tor (The Onion Router) network. There are two modules in this collection; the first ("`tor.py`") retrieves a list of Tor "guard nodes" (the nodes that Tor clients connect to), such that any and all connections to the Tor network are properly classified. The second ("`tor-full.py`") retrieves a list of *all* Tor nodes – guard, middle, and exit. This is used if your 128T device is acting as a [Tor relay](https://community.torproject.org/relay/) and will be sending traffic to middle nodes and guard nodes.

> Note: the script retrieves the list of Tor nodes from https://www.dan.me.uk/tornodes, which can only be queried every 30 minutes. Any attempts to query faster than every 30 minutes will result in an error, and hence an empty set of prefixes. The default refresh time for the script is every four hours (14,400 seconds). Previous versions of this script refreshed every hour.

This script will generate a LOT of FIB entries. (There are a lot of Tor guard nodes out there.) As of this writing, this is 5,500 unique prefixes; for each tenant that is granted access to this service, expect that many new FIB entries. Be careful about subtenants, too: this can balloon up quickly.

The service name for this module is **TOR**. Please reference this in the `application-name` field of the service you create.

Disclaimer: this is meant for experimentation/educational purposes only.
