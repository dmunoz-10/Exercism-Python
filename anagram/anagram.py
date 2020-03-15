def find_anagrams(word, candidates):
    wordList = list(word.lower())
    wordList.sort()
    patterns = []
    for candidate in candidates:
        if word.lower() != candidate.lower():
            candidateList = list(candidate.lower())
            candidateList.sort()
            if candidateList == wordList:
                patterns.append(candidate)

    return patterns
