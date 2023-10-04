import sys
import getpass

import app

def main() -> int:
    """Run application"""
    app.hello(getpass.getuser())
    app.questions()
    return 0

if __name__ == '__main__':
    sys.exit(main())

