from re import findall

def is_isogram(string):
    temp = findall(r'\w', string.upper())
    return len(list(set(temp))) == len(temp)
