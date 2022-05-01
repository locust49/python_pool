import sys


morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}


def morse_encoder(word):
    encoded = ''
    for character in word:
        if character.isalnum():
            encoded += morse[character.upper()]
            encoded += ' '
        elif character == ' ':
            encoded += '/ '
        else:
            return 'ERROR'
    return encoded


def main():
    if len(sys.argv) > 1:
        sentence = ' '.join(sys.argv[1:])
        encoded_sentence = morse_encoder(sentence)
        print(encoded_sentence)


if __name__ == '__main__':
    main()
