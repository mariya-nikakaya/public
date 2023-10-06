from sys import exit
from enquiries import choose

from guess_number import guess_number


def main() -> int:
    """Run application"""
    options = ['Guess Number', 'Exit']
    choice = choose('Choose one of these options: ', options)

    match choice:
        case "Guess Number":
            guess_number()
        case _:
            return 0


if __name__ == '__main__':
    exit(main())
