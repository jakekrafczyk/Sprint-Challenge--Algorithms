'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    
    # TBC
    #s = set()
    c = 0

    print(word[len(word)-2:len(word)])

    if len(word) < 2:
        return c

    elif word[len(word)-2:len(word)] == 'th':
        #c += 1
        #return c['count']
        #c.add(1)
        word = word[:-1]
        print(len(word))
        c += count_th(word) + 1
        #return 1
    else:
        word = word[:-1]
        c += count_th(word)

    return c

print(count_th('worthth'))