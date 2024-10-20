"""
Wimbledon program
"""

import csv

from Demos.RegCreateKeyTransacted import keyname

FILENAME = 'wimbledon.csv'
# Year,Country,Champion,Country,Runner-up,Score in the final
with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
    in_file.readline()
    in_reader = list(csv.reader(in_file))

