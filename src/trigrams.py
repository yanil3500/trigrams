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
    with open(text) as infile:
        data = infile.read()
        create_trigrams(data)


def create_trigrams(text):
    text_list = remove_punctuation(text).split(' ')
    print('Inside of create_trigrams: ', text_list)
    words_trigrams = {}
    for index in range(len(text_list)-1):
        trigram_key = text_list[index]+' '+text_list[index + 1]
        if trigram_key not in words_trigrams:
            if index != len(text_list) - 2:
                words_trigrams[trigram_key] = [text_list[index + 2]]
        else:
            if index == len(text_list)-1:
                words_trigrams[trigram_key].append(text_list[index])
            words_trigrams[trigram_key].append(text_list[index + 2])
    return words_trigrams


def remove_punctuation(text):
    """
    removes punctuation and newlines
    """
    from string import punctuation
    exclude_punctuation = set(punctuation)
    text_list = ''.join(punc for punc in text if punc not in exclude_punctuation)
    return text_list


if __name__ == '__main__':
    solution_trigrams(sys.argv[1], sys.argv[2])

