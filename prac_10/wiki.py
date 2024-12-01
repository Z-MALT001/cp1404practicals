"""
CP1404 Practical 10 Zachary Maltby
Wikipedia?????
"""

import wikipedia

query = input("Search: ")
while query != "":
    page_result = wikipedia.page(query)
    print(page_result.title)
    print(page_result.url)
    print(page_result.summary)
    query = input("Search: ")