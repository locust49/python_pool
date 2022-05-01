import sys
import string


def remove_punct(word):
    cleaned = ''
    for character in word:
        if character not in string.punctuation:
            cleaned += character
    return cleaned


def filter_words(sentence, limit):
    list_sentence = sentence.split()
    filtered = list(map(remove_punct, list_sentence))
    filtered_wo_punct = [correct for correct in filtered
                         if len(correct) > limit]
    return filtered_wo_punct


def main():
    if len(sys.argv) == 3:
        sentence = sys.argv[1]
        limit = sys.argv[2]
        if limit.isnumeric() is False:
            print('ERROR')
        else:
            limit = int(limit)
            print(filter_words(sentence, limit))
    else:
        print('Invalid number of arguments.\n\
Usage :\n\tpython3 filterwords.py <string> <number>')


if __name__ == '__main__':
    main()
