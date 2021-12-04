from utils.utility import *
import pathlib
DATA_FILE_PATH = str(pathlib.Path().resolve()) + '/02/data.txt'


def problem1():
    file = open(DATA_FILE_PATH, "r")

    depth = 0
    horizontal = 0

    for line in file:
        parts = line.strip().split(' ')
        direction = parts[0]
        quantity = int(parts[1])

        if direction == 'forward':
            horizontal += quantity
        if direction == 'down':
            depth += quantity
        if direction == 'up':
            depth -= quantity

    file.close()

    print('Depth is {} and Horizontal is {}\n'.format(depth, horizontal))
    print('Answer is {}'.format(horizontal * depth))


def problem2():
    file = open(DATA_FILE_PATH, "r")

    depth = 0
    horizontal = 0
    aim = 0

    for line in file:
        parts = line.strip().split(' ')
        direction = parts[0]
        quantity = int(parts[1])

        if direction == 'forward':
            horizontal += quantity
            depth += (aim * quantity)
        if direction == 'down':
            aim += quantity
        if direction == 'up':
            aim -= quantity

    file.close()

    print('Depth is {} and Horizontal is {} and Aim is {}\n'.format(
        depth, horizontal, aim))
    print('Answer is {}'.format(horizontal * depth))


def main():
    # problem1()
    problem2()


if __name__ == '__main__':
    # functions if main argument
    main()
