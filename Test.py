import sys

CHARACTERS_SCORE = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                    "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                    "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                    "x": 8, "z": 10}


def get_scrabble_score(valid_word):
    """
    Calculates the scrabble score of valid words and returns it.
    """

    scrabble_score = 0
    for character in valid_word:
        scrabble_score = scrabble_score + CHARACTERS_SCORE[character]
    return scrabble_score


def is_word_from_rack(word, rack):
    """
    This function check the word that if it is made of the letters that are subset of rack letters.
    """
    rack = str(rack)
    rack = str.lower(rack)
    for character in word:
        if character not in rack:
            return False
        else:
            rack = rack.replace(character, "", 1)
    return True


def display_score(valid_words_list):
    """
        This function takes the list of valid words and then get their score and dispalys final result.
        """

    valid_words_dictionary = {}
    for word in valid_words_list:
        scrabble_score = get_scrabble_score(word)
        valid_words_dictionary[word] = scrabble_score
    result_sorted_by_score = sorted(valid_words_dictionary.items(), key=lambda kv: kv[1], reverse=True)
    for word, score in result_sorted_by_score:
        print(str(score) + " " + word)


def find_valid_words(rack):
    """
    This function gives the valid words that are  made of the letters that are subset of rack letters.
    """

    file_path = "sowpods.txt"
    file = open(file_path, "r")
    valid_words_list = []
    for word in file:
        word = word.strip('\n')
        word = str.lower(word)
        if is_word_from_rack(word, rack):
            valid_words_list.append(word)
    # print(valid_words_list)
    display_score(valid_words_list)


"""

"""
if sys.argv.__len__() == 2:  # condition for command line arguments
    find_valid_words(sys.argv[1])
else:
    print("please enter the command line argument")
    exit()
