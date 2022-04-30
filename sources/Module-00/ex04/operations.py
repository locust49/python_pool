import sys


def operations(first_number, second_number):
    addition = first_number + second_number
    difference = first_number - second_number
    product = first_number * second_number
    if second_number != 0:
        quotien = first_number / second_number
        remainder = first_number % second_number
    else:
        quotien = 'ERROR (div by zero)'
        remainder = 'ERROR (modulo by zero)'
    answer = f'Sum:\t\t{addition}\nDifference:\t{difference}\n\
Product:\t{product}\nQuotient:\t{quotien}\nRemainder:\t{remainder}'
    print(answer)


def input_error(error_message):
    print(f'InputError: {error_message}')


def main():
    args = sys.argv[1:]
    usage = 'Usage: python operations.py <number1> <number2>\n\
Example:\n\tpython operations.py 10 3'
    if len(args) < 2:
        print(usage)
    elif len(args) > 2:
        input_error('too many arguments')
        print(usage)
    else:
        if args[0].isnumeric() and args[1].isnumeric():
            operations(int(args[0]), int(args[1]))
        else:
            input_error('only numbers')
            print(usage)


if __name__ == "__main__":
    main()
