# 128T AppID Module: Amazon AWS

This AppID module will identify traffic associated with Amazon's AWS services; adding this module to your system will identify a host of new AWS-based applications, all of which will be prefixed with the string "AWS-". These can then be prioritized using service-policy, service-route handling, etc.

> Note: the script operates by retrieving a publicly available JSON document, published by Amazon for this purpose.

> Note: this script can produce a LOT of prefixes -- nearly 5,000 as of this module's publication. Take this into consideration when running the module on low-end equipment.

This module creates a dynamic list of possible service names based on the JSON returned from Amazon. This will include various popular Amazon AWS services (e.g., S3, EC2, ROUTE53) as well as some lesser known services. Check the output of `show application names` to see which services have been loaded, and create your `service` configuration accordingly by referencing the names of interest in the `application-name` field of the service you create.

Disclaimer: this is a community contributed module.
