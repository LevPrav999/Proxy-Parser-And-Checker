from parser import parsing
from checker import start_checking


def main():
    parsing_list = parsing()
    start_checking(parsing_list)


if __name__ == '__main__':
    main()