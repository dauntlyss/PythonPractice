words = ['go', 'fight', 'win', 'elephant', 'Ear']

def print_upper_words(words):
    """Takes a list of words and returns an uppercase version of the list"""
    for word in words:
        if word[0] == 'e' or word[0] == 'E':
            print(word.upper())

def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given

        >>> print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
        ...                   must_start_with=["A", "E"])
        EDWARD
        ALFRED
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

print_upper_words(words)