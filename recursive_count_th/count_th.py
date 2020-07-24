'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # Eliminates words with less than two char
    if len(word) < 2:
        return 0
    # If first two indexes are 'th', then add 1 and use recursion moving over an index
    elif word[0:2] == 'th':
        return 1 + count_th(word[1:])
    # Else just use recursion starting at the next index
    else:
        return count_th(word[1:])


#Should Fail w/ 0
wordfail = 'THdkjfsns'
print(count_th(wordfail))

#Should Pass w/ 3
wordpass = 'thsdkfjthksdjfslth'
print(count_th(wordpass))
