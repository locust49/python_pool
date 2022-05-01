import sys
import random


def guess(secret_number):
    attempts = 0
    secret_number = 4
    while 1377:
        attempts += 1
        choice = input('What\'s your guess between 1 and 99?\n>> ')
        if choice == 'exit':
            print('Goodbye!')
            break
        elif choice.isnumeric():
            if int(choice) > secret_number:
                print('Too high!')
            elif int(choice) < secret_number:
                print('Too low!')
            else:
                if secret_number == 42:
                    print('The answer to the ultimate question of life, \
the universe and everything is 42.')
                if attempts == 1:
                    print('Congratulations, you got it on your fisrt try')
                else:
                    print(f'Congratulations, you\'ve got it!\n\
You won in {attempts} attempts!')
                break
        else:
            print('That\'s not a number.')


def main():
    if len(sys.argv) == 1:
        secret_number = random.randint(1, 99)
        print('This is an interactive guessing game!\n\
You have to enter a number between 1 and 99 to find out the secret number.\n\
Type \'exit\' to end the game.\n\
Good luck!')
        guess(secret_number)


if __name__ == '__main__':
    main()
