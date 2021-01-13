# cidr_filter

This is a script I have used in threat hunting to exclude Microsoft CIDR ranges from hunt data. Can be useful when you have lots outbound network connections and want to remove known ranges such as Microsoft. 

Next:
- add more known CIDR ranges (also private IP ranges)

# How to use
Requires "pandas" and "netaddr" modules. Make sure that the column of IP addresses in your source file is named as "remote_address"

python3 cidr_filter.py -h
usage: cidr_filter.py [-h] -i INPUT -o OUTPUT -f FILTER [FILTER ...] -m MERGE

Available ranges to use as a filter are listed below.
You can use more than one range as a filter to exclude or include them from your source data.

Microsoft - microsoft_range
Amazon - amazon_range
Akamai - akamai_range
Cloudflare - cloudflare_range

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        source file what you want to input
  -o OUTPUT, --output OUTPUT
                        name of the output file
  -f FILTER [FILTER ...], --filter FILTER [FILTER ...]
                        what filter you want to use e.g microsoft_range
  -m MERGE, --merge MERGE
                        'right_only' to exclude selected ranges from the result, 'both' to include ranges

Example:
python3 cidr_filter.py -i source.csv -o output.csv -f microsoft_range amazon_range -m right_only

