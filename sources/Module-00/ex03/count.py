import string

def text_analyzer(text=None, *args):
    """This function counts the number of upper characters, lower characters, \
punctuation and spaces in a given text."""
    try:
        assert len(args) == 0, 'ERROR'
    except AssertionError as error_message:
        print(error_message)
        exit()

    if text is None:
        text = str(input('What is the text to analyse?\n'))

    character_count = 0
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    spaces_count = 0

    print(text)
    character_count = len(text)
    for character in text:
        if character.isupper(): 
            upper_count += 1
        elif character.islower(): 
            lower_count += 1
        elif character in string.punctuation:
            punctuation_count += 1
        elif character.isspace(): 
            spaces_count+= 1

    answer = f'The text contains {character_count} characters:\
                - {upper_count} upper letters\
                - {lower_count} lower letters\
                - {punctuation_count} punctuation marks\
                - {spaces_count} spaces'
    print(answer)