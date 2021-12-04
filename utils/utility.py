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


def test_function():
    print('HelloWorld')
