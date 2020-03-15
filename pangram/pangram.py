from re import findall

def is_pangram(sentence):
    sentence = list(set(findall("[a-z]", sentence.lower())))
    return len(sentence) == 26
