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
        print(create_random_story(create_trigrams(data), number_of_words))



def create_trigrams(text):
    text_list = remove_punctuation(text, ' ').split(' ')
    words_trigrams = {}
    for index in range(len(text_list)-2):
        trigram_key = ' '.join(text_list[index:index+2])
        if trigram_key not in words_trigrams:
            words_trigrams[trigram_key] = [text_list[index + 2]]
        else:
            words_trigrams[trigram_key].append(text_list[index + 2])
    return words_trigrams


def remove_punctuation(text, punc):
    """
    removes punctuation and newlines
    """
    from string import punctuation
    exclude_punctuation = set(punctuation)
    text_list = text.replace('\n', ' ')
    text_list = text_list.replace('--', ' ')
    text_list = ''.join(punc for punc in text_list if punc not in exclude_punctuation)
    return text_list


def create_random_story(words, number_count):
    """
    returns a new story from dictionary
    """
    from random import randint
    all_of_the_keys = list(words.keys())
    num = randint(0, len(all_of_the_keys))
    story = []
    new_word = all_of_the_keys[num].split(' ')
    print(all_of_the_keys)
    print(new_word)
    story.extend(new_word)
    new_word = ' '.join(new_word)
    i = 0
    while i < int(number_count):
        if new_word in words:
            if len(words[new_word]) == 1:
                story.extend(words[new_word])
                new_word = story[-2] + ' ' + story[-1]
                i += 1
            else:
                num = randint(0, len(words[new_word])-1)
                word_to_add = words[new_word][num]
                story.extend(word_to_add)
                new_word = story[-2] + ' ' + story[-1]
                i += 1
        else:
            i += 1
    print(story)
    return ' '.join(story)


if __name__ == '__main__':
    solution_trigrams(sys.argv[1], sys.argv[2])
