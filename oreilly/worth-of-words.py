VALUES = {'e': 1,  'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1,
          't': 1,  'l': 1, 's': 1, 'u': 1, 'd': 2, 'g': 2,
          'b': 3,  'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4,
          'v': 4,  'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8,
          'q': 10, 'z': 10}

def worth_of_words(words):
    #return max(words, key=lambda word: sum(VALUES[c] for c in word))
    return max(words, key=lambda word: sum(map(VALUES.get, word)))
    # mvn = 0
    # mvw = ''
    # for word in words:
    #     result = 0
    #     for i in word:
    #         result += VALUES[i]
    #     if result > mvn:
    #         mvn = result
    #         mvw = word
    #
    # return mvw

if __name__ == '__main__':
    print("Example:")
    print(worth_of_words(['hi', 'quiz', 'bomb', 'president']))

    assert worth_of_words(['hi', 'quiz', 'bomb', 'president']) == 'quiz'
    assert worth_of_words(['zero', 'one', 'two', 'three', 'four', 'five']) == 'zero'
    print("Coding complete? Click 'Check' to earn cool rewards!")