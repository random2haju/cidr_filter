#!/usr/bin/python3

from netaddr import *
import pandas as pd
import argparse
import textwrap

parser = argparse.ArgumentParser(description=textwrap.dedent('''\

Available ranges to use as a filter are listed below. 
You can use more than one range as a filter to exclude or include them from your source data.

Microsoft - microsoft_range
Amazon - amazon_range
Akamai - akamai_range
Cloudflare - cloudflare_range'''), formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-i", "--input", help="source file what you want to input", required=True)
parser.add_argument("-o", "--output", help="name of the output file", required=True)
parser.add_argument("-f", "--filter", nargs='+', help="what filter you want to use e.g microsoft_range", required=True)
parser.add_argument("-m", "--merge", help="'right_only' to exclude selected ranges from the result, 'both' to include ranges ", required=True)
args = parser.parse_args()

# passing arguments to variable
range_filter = args.filter
source_file = args.input
output_file = args.output
merger = args.merge

# generating mainlist and loading selected filters(CIRD ranges) into mainlist
mainlist = []

for x in range_filter:
	infile = open(x,'r')
	for line in infile:
   		mainlist.append(line.rstrip("\n"))

	infile.close()

print("Collecting selected ranges and writing IP address to dataframe! This will take a while depending of the amount of IP addresses and available RAM")

# generating IPSet from the mainlist
ipset = IPSet(mainlist)

# for loop to generate and write IP addresses into list
d = []
for i in ipset:
    d.append(
        {
            'remote_address': i
        }
    )
# loading IP addresses and source file into dataframe
df1 = pd.DataFrame(d).astype('str')
df2 = pd.read_csv(source_file).astype({'remote_address': 'str'})

# merging dataframes together. Make sure you have same column name in both dataframes that you use for merging
df_all = df1.merge(df2.drop_duplicates(), on=['remote_address'],
                   how='right', indicator=True)
print("Almost there! Writing the output file!")
# writing the output in csv
output = df_all.loc[df_all._merge == merger]
output.to_csv(output_file, index=False)

print("Done! Check your output file for results")
