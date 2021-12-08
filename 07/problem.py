from utils.utility import *
import pathlib
DATA_FILE_PATH = str(pathlib.Path().resolve()) + '/07/data.txt'


def problem1():
    print('problem 1')
    data = load_file_into_array(DATA_FILE_PATH)
    data = data[0].split(",")
    data = [int(val) for val in data]
    start = np.array(data, dtype="i")
    count = len(start)
    max_x = start.max()
    min_x = start.min()
    range_x = max_x - min_x
    print("max is {}".format(max_x))
    changes = np.zeros((count, range_x), dtype="i")
    for i in range(count):
        for j in range(range_x):
            changes[i][j] = abs(start[i]-(j+min_x))
    print(changes)
    sum_change = changes.sum(axis=0, dtype="i")
    print(sum_change)
    min_sum = sum_change.min(axis=0)
    print(min_sum)
    min_pos = np.where(sum_change == min_sum)
    print(min_pos)
    print("min pos is {}".format(min_pos[0][0]))


def problem2():
    print('problem 2')
    data = load_file_into_array(DATA_FILE_PATH)
    data = data[0].split(",")
    data = [int(val) for val in data]
    start = np.array(data, dtype="i")
    count = len(start)
    max_x = start.max()
    min_x = start.min()
    range_x = max_x - min_x
    print("max is {}".format(max_x))
    changes = np.zeros((count, range_x), dtype="i")
    for i in range(count):
        for j in range(range_x):
            n = abs(start[i]-(j+min_x))
            cost = (n/2)*(1+n)
            changes[i][j] = cost
    print(changes)
    sum_change = changes.sum(axis=0, dtype="i")
    print(sum_change)
    min_sum = sum_change.min(axis=0)
    print(min_sum)
    min_pos = np.where(sum_change == min_sum)
    print(min_pos)
    print("min pos is {}".format(min_pos[0][0]))


def main():
    # problem1()
    problem2()


if __name__ == '__main__':
    # functions if main argument
    main()
