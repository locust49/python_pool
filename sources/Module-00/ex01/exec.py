import sys

if __name__ == '__main__':
    args = sys.argv
    len_args = len(args)
    if len(args) > 1:
        args.pop(0)
        len_args = len(args)
        for index, arg in enumerate(args[::-1]):
            print(arg[::-1].swapcase(), end='')
            if index < len_args - 1:
                print(' ', end='')
            else:
                print('')
