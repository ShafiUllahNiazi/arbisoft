import sys

CHARACTERS_SCORE = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                    "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                    "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                    "x": 8, "z": 10}


def get_word_score(valid_word):
    """
    Calculates the scrabble score of valid words and returns it.
    """
    word_score = 0
    for character in valid_word:
        word_score += CHARACTERS_SCORE[character]
    return word_score


def is_word_from_rack(word, rack):
    """
    This function check the word that if it is made of the letters that are subset of rack letters.
    """
    rack = rack.lower()
    for character in word:
        if character not in rack:
            return False

        rack = rack.replace(character, "", 1)
    return True


def display_score(valid_words):
    """
    This function takes the list of valid words and then get their score and dispalys final result.
    """
    if valid_words:
        valid_words_score = {}
        for word in valid_words:
            scrabble_score_of_valid_word = get_word_score(word)
            valid_words_score[word] = scrabble_score_of_valid_word
        sorted_words_score = sorted(valid_words_score.items(), key=lambda kv: kv[1], reverse=True)
        for word, score in sorted_words_score:
            print(str(score) + " " + word)
    else:
        print("No valid word is found")


def find_valid_words(rack):
    """
    This function gives the valid words that are  made of the letters that are subset of rack letters.
    """
    file = "sowpods.txt"
    with open(file, "r") as file:

        valid_words = []
        for word in file:
            word = word.strip('\n')
            word = word.lower()
            if is_word_from_rack(word, rack):
                valid_words.append(word)
    return valid_words


def main():
    if len(sys.argv) == 2:
        valid_words = find_valid_words(sys.argv[1])
        display_score(valid_words)
    else:
        print("please enter the command line argument")
        exit()


if __name__ == '__main__':
    main()
