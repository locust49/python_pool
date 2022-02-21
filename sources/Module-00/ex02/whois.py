import sys

if __name__ == '__main__':
    args = sys.argv
    args.pop(0)
    len_args = len(args)
    try:
        assert len_args <= 1, 'more than one argument is provided'
    except AssertionError as error_message:
        print('AssertionError: {}'.format(error_message))
    if len_args == 1:
        try:
            assert args[0].isdigit(), 'argument is not integer'
            arg_numerical = int(args[0])
            if arg_numerical == 0:
                print('I\'m Zero.')
            elif arg_numerical % 2 == 0:
                print('I\'m Even.')
            else:
                print('I\'m Odd.')
        except AssertionError as error_message:
            print('AssertionError: {}'.format(error_message))
