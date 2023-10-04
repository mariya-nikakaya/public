import random

def hello(name: str) -> int:
    print(f'Hello {name}!')
    return 0

def questions() -> int:
    number = random.randrange(1, 1001)
    counter = 0
    print("What number did I make up?")
    while True:
        try:
            answer = int(input())
        except ValueError:
            print('\033[31m' + "Oops! Than was not a number. Please enter number!" + '\033[39m')
            continue

        counter = counter + 1

        if (answer == number):
            print('\033[33m' + f'\n\nRight! I made a wish for the number {number}\n')
            print(f'You were able to guess the number in {counter} attempts\n\n' + '\033[39m')
            break

        if (answer > number):
            print('My number' + '\033[32m' + ' less ' + '\033[39m' + f'then {answer}')
            continue

        if (answer < number):
            print('My number' + '\033[31m' + ' greather ' + '\033[39m' + f'then {answer}')
            continue
    return 0