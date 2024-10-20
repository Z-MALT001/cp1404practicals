"""
Wimbledon program
"""

import csv

FILENAME = 'wimbledon.csv'


def main():
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        in_reader = list(csv.reader(in_file))
        # print(in_reader)
        name_to_win, winning_countries = grab_winners_data(in_reader)
        print("Wimbledon Champions: ")
        display_winners(name_to_win)
        display_winning_countries(winning_countries)


def grab_winners_data(in_reader):
    name_to_win = {}
    winning_countries = set()
    for row in in_reader:
        try:
            name_to_win[row[2]] += 1
        except KeyError:
            name_to_win[row[2]] = 1
            winning_countries.add(row[1])
    return name_to_win, winning_countries


def display_winners(name_to_win):
    for champ in name_to_win:
        print(f"{champ}: {name_to_win[champ]}")


def display_winning_countries(winning_countries):
    print(f"\nThese 12 countries have won Wimbledon:"
          f"\n{', '.join(sorted(winning_countries))}")


# Year,Country,Champion,Country,Runner-up,Score in the final
main()

