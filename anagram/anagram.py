def find_anagrams(word, candidates):
    word_list = sorted(word.lower())
    patterns = []
    for candidate in candidates:
        candidate_list = sorted(candidate.lower())
        if word.lower() != candidate.lower() and candidate_list == word_list:
            patterns.append(candidate)

    return patterns
