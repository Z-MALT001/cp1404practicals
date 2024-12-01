"""
Hex colours lookup
"""

# http://www.color-hex.com/color-names.html

COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alice Blue": "#f0f8ff",
                  "Alizarin Crimson": "#e32636", "Amaranth": "e52b50", "Amber": "#ffbf00",
                  "Amethyst": "#9966cc", "Antique White": "#fqebd7", "Apricot": "#fbceb1",
                  "Aqua": "#00ffff"}

max_length = max(len(colour) for colour in COLOUR_TO_CODE.keys())
line = max_length * '-'
print("The available colours are: ")
print(line)
for colour, code in COLOUR_TO_CODE.items():
    print(f"{colour:{max_length}}")
print(line)


colour_name = input("Please enter a colours name: ").lower()
while colour_name != "":
    try:
        print(f"{colour_name.title()} is {COLOUR_TO_CODE[colour_name]}")
    except KeyError:
        print("Enter a valid colour name.")
    colour_name = input("Please enter a colours name: ").lower()
print("Exiting...")
