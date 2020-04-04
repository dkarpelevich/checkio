def find_quotes(text):
    res = []
    i = 0
    while i < len(text)-1:
        try:
            if text[i] == '"':
                res.append(text[i+1:text[i+1:].index('"') + i + 1])
                i = text[i+1:].index('"') + i + 2
            else:
                i += 1
        except ValueError:
            return res
    return res


if __name__ == '__main__':
    # print("Example:")
    # print(find_quotes('"Greetings"'))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert find_quotes('"Greetings"') == ['Greetings']
    # assert find_quotes('Hi') == []
    # assert find_quotes('good morning mister "superman"') == ['superman']
    assert find_quotes('"this" doesn\'t make any "sense"') == ['this', 'sense']
    assert find_quotes('"Lorem Ipsum" is simply dummy text '
 'of the printing and typesetting '
 'industry. Lorem Ipsum has been the '
 '"industry\'s standard dummy text '
 'ever since the 1500s", when an '
 'unknown printer took a galley of '
 'type and scrambled it to make a type '
 'specimen book. It has survived not '
 'only five centuries, but also the '
 'leap into electronic typesetting, '
 'remaining essentially unchanged. "It '
 'was popularised in the 1960s" with '
 'the release of Letraset sheets '
 'containing Lorem Ipsum passages, and '
 'more recently with desktop '
 'publishing software like Aldus '
 'PageMaker including versions of '
 'Lorem Ipsum.') == ['Lorem Ipsum',
 "industry's standard dummy text ever "
 'since the 1500s',
 'It was popularised in the 1960s']
    assert find_quotes('count empty quotes ""') == ['']
    print("Coding complete? Click 'Check' to earn cool rewards!")
