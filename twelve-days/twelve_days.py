def recite(start_verse, end_verse):
    verses = [
        ['first', 'a Partridge in a Pear Tree'],
        ['second', 'two Turtle Doves'],
        ['third', 'three French Hens'],
        ['fourth', 'four Calling Birds'],
        ['fifth', 'five Gold Rings'],
        ['sixth', 'six Geese-a-Laying'],
        ['seventh', 'seven Swans-a-Swimming'],
        ['eighth', 'eight Maids-a-Milking'],
        ['ninth', 'nine Ladies Dancing'],
        ['tentth', 'ten Lords-a-Leaping'],
        ['eleventh', 'eleven Pipers Piping'],
        ['twelfth', 'twelve Drummers Drumming']
    ]
    number = verses[start_verse - 1][0]
    lyrics = f'On the {number} day of Christmas my true love gave to me: '
    if start_verse == end_verse:
        range_verse = range(start_verse - 1, -1, -1)
    else:
        range_verse = range(end_verse - 1, start_verse - 2, -1)

    for i in range_verse:
        if i == end_verse - 1:
            if start_verse == end_verse:
                lyrics += f'{verses[i][1]}'
            else:
                lyrics += f'and {verses[i][1]}'
        else:
            lyrics += f'{verses[i][1]}, '

    return [lyrics]
