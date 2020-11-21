# cidr_filter

This is a script I have used in threat hunting to exclude Microsoft CIDR ranges from hunt data. Can be useful when you have lots outbound network connections and want to remove known ranges such as Microsoft. 

Next:
- add more known CIDR ranges (also private IP ranges)
- add possibility include more than one range

# How to use
Requires "pandas" and "netaddr" modules. Current configuration is exluding selected CIDR ranges addresses from end result. You can change in row 48 "right_only" to "both"

- "right_only" = selects events that are NOT in selected CIRD range
- "both" = selects events that are ONLY in selected CIRD rane
