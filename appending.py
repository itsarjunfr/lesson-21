def match_words(words):
    counter = 0
    list = []
    for word in words:
        if len(word) > 1 and word[0] == word [-1]:
            list.append(word)
            counter += 1
            
    print('List of words that have same first and last character:', list)
    return counter
count = match_words(['abc', 'xyz', 'cfc', 'aba', '1221'])
print('Number of words having first and last character same:', count)