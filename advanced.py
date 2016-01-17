"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    character_count = {}

    # Split input_string into a list of words and join into one string.
    words = input_string.split()
    joined_string = "".join(words)

    # Interate over joined_string.
    # For each letter, find the current count (possibly 0) and increment it.
    for letter in joined_string:
        character_count[letter] = character_count.get(letter, 0) + 1

    # Initialize new dictionary for character count as the key and list of letters as value.
    # For each key-value pair in the list of character_count tuples,
    # initialize value (empty list) for each character count (key) in the dictionary.
    # Add each letter to the list corresponding to its character count.
    sorted_by_count = {}
    for pair in character_count.iteritems():
        sorted_by_count.setdefault(pair[1], [])
        sorted_by_count[pair[1]].append(pair[0])

    # The last item in the list of sorted character counts is the highest frequency.
    highest_frequency = sorted(sorted_by_count)[-1]

    # The letters corresponding to the highest frequency.
    highest_frequency_letters = sorted_by_count[highest_frequency]

    # Return the list of letters that appear the most in alphabetical order.
    return sorted(highest_frequency_letters)


def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    return []


##############################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
