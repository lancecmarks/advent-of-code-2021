import numpy as np


def decimal_to_binary(n):
    return bin(n).replace("0b", "")


def binary_to_decimal(binary):
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def split_string(string):
    return [char for char in string]


def load_file_into_array(filename):
    file = open(filename, "r")
    data_array = []
    for line in file:
        data_array.append(line.strip())
    file.close()
    return data_array


def convert_array_strings_to_chars(data):
    data_array = []
    for item in data:
        parts = split_string(item.strip())
        data_array.append(parts)
    return data_array


def cumulate_indexes(data):
    counts = np.zeros(len(data[0]))
    for item in data:
        for i in range(len(item)):
            counts[i] = counts[i] + int(item[i])
    print(counts)
    return counts


def get_max_for_index(data, index):
    counts = np.zeros(len(data[0]))
    for i in range(len(data)):
        curr = data[i]
        for j in range(len(curr)):
            counts[j] = counts[j] + int(curr[j])
    max_val = '1' if counts[index] >= len(data)/2 else '0'
    # print('at position {} the max_val is {} for {} items'.format(
    #     index, max_val, len(myList)))
    # print(counts)
    return max_val


def get_least_for_index(data, index):
    counts = np.zeros(len(data[0]))
    for i in range(len(data)):
        curr = data[i]
        for j in range(len(curr)):
            counts[j] = counts[j] + int(curr[j])

    return '0' if counts[index] >= len(data)/2 else '1'


def keep_match_values(data, index, test):
    data_array = []
    for i in range(len(data)):
        curr = data[i]
        if curr[index] == test:
            data_array.append(curr)
    return data_array

# BINGO


def load_bingo_into_array(filename):
    file = open(filename, "r")
    bingo_numbers = []
    bingo_boards = []
    mask_boards = []
    temp_array = []
    line_count = 0
    for line in file:
        line = line.strip()
        if len(line) < 3:
            line_count = 0
            temp_array = []
            continue
        elif len(line) > 15:
            line_count = 0
            line = line.split(',')
            line = list(map(int, line))
            bingo_numbers = np.array(line, dtype="i")
        else:
            temp_array.append(line.split())
            line_count += 1
            if line_count == 5:
                board = np.array(temp_array, dtype="i")
                board = board.reshape(5, 5)
                bingo_boards.append(board)
                mask_boards.append(np.zeros(board.shape, dtype="i"))
                temp_array = []
    bingo_boards = np.array(bingo_boards)
    mask_boards = np.array(mask_boards)

    file.close()
    return bingo_numbers, bingo_boards, mask_boards


def mark_bingo_numbers(number, boards, masks):
    temp_mask = np.isin(boards, number)
    masks[temp_mask] = 1
    return masks


def sum_unmarked_numbers(board, mask):
    temp_mask = np.isin(mask, 0)
    return np.sum(board[temp_mask])


def check_for_win(board):
    if 5 in np.array(np.sum(board, axis=0)).tolist():
        return True
    if 5 in np.array(np.sum(board, axis=1)).tolist():
        return True
    if np.trace(board, dtype="i") == 5:
        return True
    if np.trace(board, offset=4, dtype="i") == 5:
        return True
