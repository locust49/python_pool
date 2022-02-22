def text_analyzer(text=None, *args):
    try:
        assert len(args) == 0, 'ERROR'
    except AssertionError as error_message:
        print(error_message)

    if text is None:
        text = str(input('What is the text to analyse?'))

    character_count = 0
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    spaces_count = 0

    if text == '':
        answer = f'The text contains {character_count} characters:\
                    - {upper_count} upper letters\
                    - {lower_count} lower letters\
                    - {punctuation_count} punctuation marks\
                    - {spaces_count} spaces'
        print(answer)


text_analyzer('h', 's')
