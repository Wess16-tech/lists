def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            lst.append(word)
            ctr += 1
    print('List of words with the first and last character the same\n', lst)
    return ctr
count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print('Number of words with the first and last character the same:', count)