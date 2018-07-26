import argparse


class myclass:
    """filename = "/home/shafi/Desktop/s/sowpods.txt"
    file = open(filename, "r")
    sowpodsList = []
    for line in file:
        x = line.strip('\n')
        sowpodsList.append(x)
    print(sowpodsList)

    filename = "/home/shafi/Desktop/s/myCopysowpods.txt"
    file = open(filename, "w")
    for line in sowpodsList:
        file.write(line + "\n")
    file.close()
"""


parser = argparse.ArgumentParser()
parser.add_argument('rock', help='help', type=str)

try:
    args = parser.parse_args()
    s = str(args)
    s = s.lower()
    print(s)
except:
    print("handle this invalid argument ")
    exit()


def find_valid_words():
    filename = "/home/shafi/Desktop/s/sowpods.txt"
    file = open(filename, "r")
    sowpodsList = []
    for line in file:
        word = line.strip('\n')
        word = word.lower()
        sowpodsList.append(word)
        for everyLetter in word:
            if everyLetter in s:
                print(s + " " + word)
                continue
        else:break

find_valid_words()
    #print(sowpodsList)
"""
everyLetter = "hel"
if everyLetter in "hello":
    print(everyLetter)
"""