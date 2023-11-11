import requests
import re

def letter(word):
    strmaker = requests.get(F'https://www.allscrabblewords.com/unscramble/{word}').text
    matches = re.compile(r'<a[^>]*href="/word-description/([^"]+)">([^<]+)</a>').findall(strmaker)

    for match in matches:
        word_in_text = match[1]
        print(F"GOT {word_in_text} {len(word_in_text)} letter")

letter(input("find > "))
