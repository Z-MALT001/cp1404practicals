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
    # print(in_reader)
    name_to_win = {}
    winning_countries = set()
    for row in in_reader:
        try:
            name_to_win[row[2]] += 1
        except KeyError:
            name_to_win[row[2]] = 1
            winning_countries.add(row[1])
    print("Wimbledon Champions: ")
    for champ in name_to_win:
        print(f"{champ}: {name_to_win[champ]}")
    print(f"\nThese 12 countries have won Wimbledon:"
          f"\n{', '.join(sorted(winning_countries))}")

    # print(name_to_win)q

