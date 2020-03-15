import re
from collections import Counter

def count_words(sentence):
    word = re.findall("[a-zA-Z0-9]+(?:\'t)?", sentence.lower())
    return Counter(word)
