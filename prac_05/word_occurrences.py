"""
Word Occurrences
Estimate: 20 minutes
Actual:   16 minutes
"""

# get input, register strings into a dictionary, for each key in dictionary add one to the value, print

sentence = input("Enter a sentence: ")
word_to_count = {}
for string in sentence.split():
    try:
        word_to_count[string] += 1
    except KeyError:
        word_to_count[string] = 1

max_length = max(len(string) for string in word_to_count.keys())

# print(word_to_count)
for string in word_to_count.keys():
    print(f"{string:{max_length}}: {word_to_count[string]}")
