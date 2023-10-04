import random

def hello(name: str) -> int:
    print(f'Hello {name}!')
    return 0

def questions() -> int:
    number = random.randrange(1, 1001)
    print("What number did I make up?")
    while True:
        answer = int(input())

        if (answer == number):
            print('\033[33m' + f'Right! I made a wish for the number {number}')
            break

        if (answer > number):
            print('My number' + '\033[32m' + ' less ' + '\033[39m' + f'then {answer}')
            continue

        if (answer < number):
            print('My number' + '\033[31m' + ' greather ' + '\033[39m' + f'then {answer}')
            continue
    return 0