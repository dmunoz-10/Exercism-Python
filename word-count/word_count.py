from re import findall
from collections import Counter


def count_words(sentence):
    word = findall("[a-zA-Z0-9]+(?:\'t)?", sentence.lower())
    return Counter(word)
