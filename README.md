# cidr_filter

This is a script I have used in threat hunting to exclude Microsoft CIDR ranges from hunt data. Can be useful when you have lots outbound network connections and want to remove known ranges such as Microsoft. 

Next:
- add more known CIDR ranges (also private IP ranges)

# How to use
Requires "pandas" and "netaddr" modules. Make sure that the column of IP addresses in your source file is named as "remote_address"

