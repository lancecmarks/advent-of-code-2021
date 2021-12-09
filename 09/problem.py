from numpy import inf
from utils.utility import *
import pathlib
from scipy.signal import argrelmin
import time
DATA_FILE_PATH = str(pathlib.Path().resolve()) + '/09/data.txt'


def problem1():
    print('problem 1')
    data = load_file_into_array(DATA_FILE_PATH)
    print(data)
    size = (len(data), len(data[0]))
    print(size)
    floor = np.zeros(size, dtype=np.int32)
    for idx in range(len(data)):
        temp = [s.strip() for s in data[idx]]
        print(temp)
        floor[idx][:] = temp
    print(floor)
    mask = np.full(floor.shape, 10, dtype=np.int32)
    for i in range(floor.shape[0]):
        for j in range(floor.shape[1]):
            local_min, local_x, local_y = check_surrounding(floor, i, j)
            # if (local_min < floor[i][j]):
            #     mask[local_x][local_y] = local_min
            if (local_min == floor[i][j]):
                mask[i][j] = floor[i][j]
    print(mask)
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            local_min, local_x, local_y = check_surrounding(mask, i, j)
            # if (local_min < mask[i][j]):
            #     mask[local_x][local_y] = local_min
            #     mask[i][j] = 10
            if (local_min != mask[i][j]):
                mask[i][j] = 10
    print(mask)
    count = np.sum((mask < 10).astype(np.int32))
    print(count)
    mask[mask == 10] = 0
    print(mask)
    print(np.sum(mask))
    print((mask > 0).astype(np.int32))
    total = np.sum(mask) + count
    print("total is {}".format(total))


def check_surrounding(nd_array, i, j):
    temp_x = 0
    temp_y = 0
    curr_min = nd_array[i][j]
    # print("curr is {} at {}, {}".format(curr_min, i, j))
    x = [0]
    y = [0]
    ext_x = [0]
    ext_y = [0]
    if (i > 0):
        x.append(-1)
    # if (i > 1):
    #     x.append(-2)
    if (i < nd_array.shape[0]-1):
        x.append(1)
    # if (i < nd_array.shape[0]-2):
    #     x.append(2)
    if (j > 0):
        y.append(-1)
    # if (j > 1):
    #     y.append(-2)
    if (j < nd_array.shape[1]-1):
        y.append(1)
    # if (j < nd_array.shape[1]-1):
    #     y.append(2)
    #################
    # round1 = []
    # if (i > 0):
    #     round1.append((-1, 0))
    #     if (j > 0):
    #         round1.append((-1, -1))
    #     if (j < nd_array.shape[0]-1):
    #         round1.append((-1, 1))
    # if (j > 0):
    #     round1.append((0, -1))
    # if (j < nd_array.shape)

    for xx in x:
        for yy in y:
            # time.sleep(2)
            check = nd_array[i+xx][j+yy]
            # print("checking {} at {}, {}".format(check, i+xx, j+yy))
            if check < curr_min:
                # print("less than current so checking its local min")
                n, g, h = check_surrounding(nd_array, i+xx, j+yy)
                if n < check:
                    # print("{} had a local min of {} at {}, {}".format(
                    #     check, n, g, h))
                    # print("{} < {} at pos {},{}".format(
                    #     check, curr_min, i+xx, j+yy))
                    curr_min = check
                    temp_x = g
                    temp_y = h
                else:
                    curr_min = check
                    temp_x = i+xx
                    temp_y = j+yy
    return curr_min, temp_x, temp_y


def top_three(num, array):
    if len(array) < 3:
        array.append(num)
    else:
        min_num = min(array)
        if min_num < num:
            array[array.index(min_num)] = num


def count_basin(floor, i, j, count):
    count += 1
    floor[i][j] = 99
    if i > 0 and floor[i-1][j] != 99:
        count, floor = count_basin(floor, i-1, j, count)
    if i < floor.shape[0]-1 and floor[i+1][j] != 99:
        count, floor = count_basin(floor, i+1, j, count)
    if j > 0 and floor[i][j-1] != 99:
        count, floor = count_basin(floor, i, j-1, count)
    if j < floor.shape[1]-1 and floor[i][j+1] != 99:
        count, floor = count_basin(floor, i, j+1, count)
    return count, floor


def problem2():
    print('problem 2')
    data = load_file_into_array(DATA_FILE_PATH)
    # print(data)
    size = (len(data), len(data[0]))
    print("shape is {}".format(size))
    floor = np.zeros(size, dtype=np.int32)
    for idx in range(len(data)):
        temp = [s.strip() for s in data[idx]]
        # print(temp)
        floor[idx][:] = temp
    # print(floor)
    floor[floor == 9] = 99
    # print(floor)
    top = []
    for i in range(floor.shape[0]):
        for j in range(floor.shape[1]):
            if (floor[i][j] != 99):
                count, floor = count_basin(floor, i, j, 0)
                top_three(count, top)
    total = 1
    for item in top:
        total *= item
    print("total is {}".format(total))


def main():
    # problem1()
    problem2()


if __name__ == '__main__':
    # functions if main argument
    main()
