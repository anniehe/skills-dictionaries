"""Skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list:

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers:

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]



    """

    # Sets are unique collections of items and removes duplicates.
    return set(words)


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not use 'if ___ in ___' or the method 'index'.

    This should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([4, 3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are different data types.

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]

    """

    # Create sets of each list to remove duplicates and
    # return the intersection of the common items.
    return set(list1) & set(list2)


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """

    words = input_string.split()
    word_dict = {}

    # For each word, find current count (possibly 0) and increment it.
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1

    # # ALTERNATIVE SOLUTION:

    # distinct_words = set(words)

    # # Initialize count for each distinct word.
    # for word in distinct_words:
    #     word_dict[word] = 0

    # # Iterate through the list of words from the input string.
    # # Increment the count of the unique word each time it's found in the list of words.
    # for word in words:
    #     word_dict[word] += 1

    return word_dict


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be

    For example:

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    pirate_translation = {}

    pirate_translation["sir"] = "matey"
    pirate_translation["hotel"] = "fleabag inn"
    pirate_translation["student"] = "swabbie"
    pirate_translation["boy"] = "matey"
    pirate_translation["professor"] = "foul blaggart"
    pirate_translation["restaurant"] = "galley"
    pirate_translation["your"] = "yer"
    pirate_translation["excuse"] = "arr"
    pirate_translation["students"] = "swabbies"
    pirate_translation["are"] = "be"
    pirate_translation["restroom"] = "head"
    pirate_translation["my"] = "me"
    pirate_translation["is"] = "be"
    pirate_translation["man"] = "matey"

    words = phrase.split()
    pirate_talk = []

    # Iterate through the list of words from the input phrase.
    # If the word is found in the list of dictionary keys,
    # add the value (Pirate translation) to resulting pirate_talk list.
    # Otherwise, add the word to the resulting list.
    for word in words:
        if word in pirate_translation.iterkeys():
            pirate_talk.append(pirate_translation.get(word))
        else:
            pirate_talk.append(word)

    # Concatenate the resulting list of words and return pirate_talk as a string.
    return " ".join(pirate_talk)


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items---the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """

    # sorted list of tuples
    # tuple (length, list of words with that length)

    # use iteritems?

    word_length_dict = {}

    print word_length_dict

    # for key, value in word_length_dict.iteritems:
    #     tuple_list.append((key, value))

    # return sorted(sorted_list)


def get_sum_zero_pairs(input_list):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """

    return []


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
