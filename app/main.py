import sys

from app.application import Application


def main():
    application = Application()
    application.run()

    sys.exit(0)


if __name__ == "__main__":
    main()