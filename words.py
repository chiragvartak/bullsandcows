import requests
from pprint import pprint

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
WORD_LENGTH = 4

response = requests.get(word_site)
WORDS = response.content.splitlines()
WORDS = [word.decode("ascii") for word in WORDS if len(word) is WORD_LENGTH]
WORDS = [word for word in WORDS if word[0].islower()]

if __name__ == "__main__":
    pprint(WORDS)