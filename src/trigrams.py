import sys
"""
Solution to trigrams problem
"""


def solution_trigrams(text, number_of_words):
    """
    function that creates new story
    """
    print('Number of words: ', number_of_words)
    print('Text: ', text)


def create_trigrams(text):
    text_list = text.split(' ')
    print(text_list)
    words_trigrams = {}
    previous = 0
    for index in range(len(text_list)-1):
        if index != len(text_list):
            trigram_key = text_list[previous]+' '+text_list[previous + 1]
            previous = index
        if trigram_key not in words_trigrams:
            words_trigrams[trigram_key] = [text_list[previous]]
        else:
            words_trigrams[trigram_key].append(text_list[index])
    print("Trigram dictionary: ", words_trigrams)




create_trigrams('I wish I may I wish I might')
if __name__ == '__main__':
    solution_trigrams(sys.argv[1], sys.argv[2])

