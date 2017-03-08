import re

def word_count(str):
    words = {}
    words_list = re.compile("[ ,.:] ?").split(str)
    print(words_list)
    for word in words_list:
        lower_word = word.lower()
        if lower_word != '':
            if lower_word in words.keys():
                words[lower_word] += 1
            else:
                words[lower_word] = 1
    return words

str = "Now let’s expand the Roman numeral regular expression to cover the tens and ones place. This example shows the check for tens. "

print(word_count(str))
