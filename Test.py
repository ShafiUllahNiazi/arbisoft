import sys

"""
Calculates the scrabble score of valid words
"""


def scrabbleScore(word):
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
              "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
              "x": 8, "z": 10}
    totalScore = 0
    for score in word:
        totalScore = totalScore + scores[score]
    return totalScore


"""
Removes the letter from the rack letters to handle repeat letters
"""


def my_pop(char, rack):
    charPlace = rack.find(char)
    return rack[0:charPlace] + rack[charPlace + 1:]


"""
This function check the word that if it is made of the letters that are subset of rack letters
"""


def lettersInRack(word, rack):
    rack = str(rack)
    rack = rack.lower()
    for everyLetter in word:
        if everyLetter not in rack:
            return False
        else:
            rack = my_pop(everyLetter, rack)
    return True


"""
This function gives the valid words that are  made of the letters that are subset of rack letters
"""


def find_valid_words(rack_letters):
    filename = "/home/shafi/Desktop/s/sowpods.txt"
    file = open(filename, "r")
    validWords = {}
    i = 0
    for line in file:
        word = line.strip('\n')
        word = word.lower()
        rack = rack_letters
        if lettersInRack(word, rack):
            score = scrabbleScore(word)
            validWords[word] = score
    print(validWords)
    print(sorted(validWords))
    result = sorted(validWords.items(), key=lambda kv: kv[1], reverse=True)
    for k, v in result:
        print(str(v) + ", " + k)


"""
This piece of code checks the command line arguents and proceeds for valid words
"""
if sys.argv.__len__() < 3:
    find_valid_words(sys.argv[1])
else:
    print("please enter the command line argument")
    exit()
