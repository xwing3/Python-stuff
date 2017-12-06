#reddit problem https://www.reddit.com/r/learnpython/comments/6jkavh/i_am_hitting_a_wall_on_this_problem_for_my_edx/

def guessed(word, letter):
    k = 0

    for j in range(len(word)):
        while word[j] not in letter:
            break
        else:
            k+=1
    if k == len(word):
        print "true"
        return True
    else:
        print "false"
        return False


word = 'apples'
letter = ['a', 'p', 'i', 'e', 'p', 'r', 's']

