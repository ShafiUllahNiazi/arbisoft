import sys


def get_scrabble_score(valid_word):
    """
    Calculates the scrabble score of valid words and returns it
    """
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
              "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
              "x": 8, "z": 10}
    scrabble_score = 0
    for character in valid_word:
        scrabble_score = scrabble_score + scores[character]
    return scrabble_score


def my_pop(char, rack):
    """
    Removes the letter from the rack letters to handle repeat letters
    """
    charPlace = rack.find(char)
    return rack[0:charPlace] + rack[charPlace + 1:]


def is_word_from_rack(word, rack):
    """
    This function check the word that if it is made of the letters that are subset of rack letters
    """
    rack = str(rack)
    rack = rack.lower()
    for character in word:
        if character not in rack:
            return False
        else:
            rack = my_pop(character, rack)
    return True


def find_valid_words(rack_letters):
    """
    This function gives the valid words that are  made of the letters that are subset of rack letters
    """

    file_path = "sowpods.txt"
    file = open(file_path, "r")
    valid_words = {}
    i = 0
    for word in file:
        word = word.strip('\n')
        word = word.lower()
        rack = rack_letters
        if is_word_from_rack(word, rack):
            score = get_scrabble_score(word)
            valid_words[word] = score
    print(valid_words)
    print(sorted(valid_words))
    result = sorted(valid_words.items(), key=lambda kv: kv[1], reverse=True)
    for k, v in result:
        print(str(v) + ", " + k)


"""
This piece of code checks the command line arguents and proceeds for valid words
"""
if sys.argv.__len__() == 2:
    find_valid_words(sys.argv[1])
else:
    print("please enter the command line argument")
    exit()
