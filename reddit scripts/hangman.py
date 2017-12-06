"""
Hangman challenge from reddit
"""

def validate_input(chances, word):
    i = 0
    valid = [None] * len(word)
    while i < len(word):
        letter = raw_input("Enter %d letter: " % (i))
        while chances > 0:
            if word[i] == letter:
                valid[i] = word[i]
                break
            else:
                chances -= 1
                print "Chances left: ", chances
                letter = raw_input("Enter %d letter: " % (i))
        if chances == 0:
            return
        i += 1
    valid1 = ''.join(valid)
    if word == valid1:
        print "you got the word"
        return


def main():
    word = raw_input("Enter a word greater than 3 letters: ")
    chance = raw_input("Enter number of chances per letter to guess it: ")
    c = int(chance)
    if chance == 0:
        print "Number of chances must be greater than 0"
        chance = raw_input("Enter number of chances per letter to guess it: ")
        c = int(chance)
    chances = c * len(word)
    if len(word) < 3:
        print "Number of letters is less than 3"
        word = raw_input("Enter a word greater than 3 letters: ")

    validate_input(chances, word)

main()
