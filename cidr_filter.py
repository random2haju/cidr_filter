#!/usr/bin/python3

from netaddr import *
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="source file what you want to input", required=True)
parser.add_argument("-o", "--output", help="name of the output file", required=True)
parser.add_argument("-f", "--filter", help="what filter you want to use e.g microsoft_range", required=True)
parser.add_argument("-l", "--list", help="lists available filters", action="store_true")
args = parser.parse_args()

# passing arguments to variable
range_filter = args.filter
source_file = args.input
output_file = args.output

# generating mainlist and loading selected filter into mainlist
mainlist = []
infile = open(range_filter,'r')
for line in infile:
    mainlist.append(line.rstrip("\n"))

infile.close()

# generating IPSet from the main
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

# writing the output in csv
print(df_all)
output = df_all.loc[df_all._merge == 'right_only']
output.to_csv(output_file, index=False)
