import sys
import os
import random
"""
Solution to trigrams problem
"""

txt_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'story.txt')


def main(text_file = txt_file, number_of_words = 300):
    """
    responsible for validating that the inputs that are passed are valid
    """
    if os.path.isfile(text_file):
        with open(text_file) as infile:
            data = infile.read()
        solution_trigrams(data, number_of_words)


def solution_trigrams(text, number_of_words):
    """
    function that creates new story
    """
    print(create_trigrams(text))
    print(create_random_story(create_trigrams(text), number_of_words))


def create_trigrams(text):
    """
    function that creates trigrams
    """
    text_list = remove_punctuation(text, ' ').split()
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
    text = ''.join(
        punc for punc in text if punc not in exclude_punctuation).lower()
    return text


def create_random_story(words, number_count):
    """
    returns a new story from dictionary
    """
    from random import randint
    random_key = random.choice(list(words.keys()))
    story = []
    new_word = random_key.split(' ')
    story.extend(new_word)
    new_word = ' '.join(new_word)
    i = 0
    while i < int(number_count) - 2:
        values_associated_to_random_key = list(words[random_key])
        print(values_associated_to_random_key)
        num = randint(0, len(values_associated_to_random_key)-1)
        print(num)
        new_word = values_associated_to_random_key[num]
        print(new_word)
        if new_word in words:
            # word_to_add = words[new_word][num]
            # story.extend(words[new_word][num])
            new_word = story[-2] + ' ' + story[-1]
            i += 1
        else:
            i += 1
    print()
    return ' '.join(story)


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) >= 3:
        main(sys.argv[1], sys.argv[2])
    else:
        main()

