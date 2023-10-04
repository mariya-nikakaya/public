import random


def hello(name: str) -> int:
    print(f'\n\nHello {name}!\n')
    return 0


def rules():
    print('You need to guess a number from 1 to 1000\n')
    print('To exit, press "q".\n')
    print('For reference, press "h".\n\n')


def questions() -> int:
    rules()
    number = random.randrange(1, 1001)
    counter = 0
    print("What number did I make up?")
    while True:
        answer = input()

        match answer:
            case 'q':
                print("It was nice playing with you!")
                break
            case 'h':
                rules()
                continue

        try:
            answer = int(answer)
        except ValueError:
            print(
                '\033[31m' + "Oops! Than was not a number. Please enter number!" + '\033[39m')
            continue

        counter = counter + 1

        if (answer == number):
            print('\033[33m' +
                  f'\n\nRight! I made a wish for the number {number}\n')
            print(
                f'You were able to guess the number in {counter} attempts\n\n' + '\033[39m' + '\n\n')
            break

        if (answer > number):
            print('My number' + '\033[32m' +
                  ' less ' + '\033[39m' + f'then {answer}')
            continue

        if (answer < number):
            print('My number' + '\033[31m' +
                  ' greather ' + '\033[39m' + f'then {answer}')
            continue
    return 0


def goodbye(name: str) -> int:
    print(f'Goodbye {name}!')
