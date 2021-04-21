from re import search


def response(hey_bob):
    RESPONSES = {
        1: 'Sure.', 2: 'Whoa, chill out!',
        3: "Calm down, I know what I'm doing!", 4: 'Fine. Be that way!',
        5: 'Whatever.'
    }
    if len(hey_bob.strip()) == 0:
        return RESPONSES[4]
    if is_uppercase(hey_bob) and hey_bob.strip().endswith('?'):
        return RESPONSES[3]
    if hey_bob.strip().endswith('?'):
        return RESPONSES[1]
    if is_uppercase(hey_bob):
        return RESPONSES[2]

    return RESPONSES[5]


def is_uppercase(phrase):
    if not search('[A-Za-z]', phrase):
        return False

    len_upper = len(search('[A-Z]', phrase).group())
    len_phrase = len(search('[A-Za-z]', phrase).group())
    return len_phrase == len_upper
