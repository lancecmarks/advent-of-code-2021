from utils.utility import *
import pathlib
import numpy as np
DATA_FILE_PATH = str(pathlib.Path().resolve()) + '/01/data.txt'


def problem1():
    file = open(DATA_FILE_PATH, "r")

    Lines = file.readlines()

    prev = None
    increase = 0
    # Strips the newline character
    for line in Lines:
        if prev == None:
            prev = int(line)
        else:
            dif = int(line) - prev
            prev = int(line)
            if dif > 0:
                increase += 1

    print("Total increases is {}".format(increase))


def problem2():
    file = open(DATA_FILE_PATH, "r")

    line_count = 0

    for line in file:

        if line != "\n":

            line_count += 1

    file.close()

    print('Line Count is {}\n'.format(line_count))

    depths = np.zeros((1, int(line_count)))

    file = open(DATA_FILE_PATH, "r")
    index = 0
    for line in file:

        if line != "\n":
            depths[0, index] = int(line)
            index += 1

    file.close()
    print(depths)

    depths_matrix = np.zeros((3, int(line_count)+3))

    for i in range(0, 3):
        for j in range(0, line_count):
            depths_matrix[i, j+i] = depths[0, j]

    print(depths_matrix)
    prev = 0
    increases = 0
    for i in range(2, line_count+3):
        if depths_matrix[0, i] > 0 and depths_matrix[1, i] > 0 and depths_matrix[2, i] > 0:
            total = depths_matrix[0, i] + \
                depths_matrix[1, i] + depths_matrix[2, i]
            if prev == 0:
                prev = total
            else:
                diff = total - prev
                prev = total
                if diff > 0:
                    increases += 1

    print('Increases is {}\n'.format(increases))


def main():
    problem1()
    problem2()


if __name__ == '__main__':
    # functions if main argument
    main()
