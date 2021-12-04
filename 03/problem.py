from utils.utility import *
import pathlib
DATA_FILE_PATH = str(pathlib.Path().resolve()) + '/03/data.txt'


def problem1():
    data = load_file_into_array(DATA_FILE_PATH)

    data_as_chars = convert_array_strings_to_chars(data)

    counts = cumulate_indexes(data_as_chars)

    print('The line count is {}\n'.format(len(data)))
    print('The array is: ')
    print(counts)

    gamma_rate = ''
    epsilon_rate = ''

    for i in range(len(counts)):
        if (counts[i] > len(data)/2):
            gamma_rate = gamma_rate + '1'
            epsilon_rate = epsilon_rate + '0'
        else:
            gamma_rate = gamma_rate + '0'
            epsilon_rate = epsilon_rate + '1'

    print('gamma_rate is {}'.format(gamma_rate))
    print('epsilon_rate is {}'.format(epsilon_rate))

    power_rate = binary_to_decimal(
        int(gamma_rate)) * binary_to_decimal(int(epsilon_rate))
    print('power_rate is {}'.format(power_rate))
    # 349 , 000101011101
    # 3746, 111010100010
    # 1307354


def oxygen_rating():
    data = load_file_into_array(DATA_FILE_PATH)
    code_length = len(data[0])
    for i in range(code_length):
        if len(data) == 1:
            return data
        most = get_max_for_index(data, i)
        data = keep_match_values(data, i, most)
    return data


def carbon_rating():
    data = load_file_into_array(DATA_FILE_PATH)
    code_length = len(data[0])
    for i in range(code_length):
        if len(data) == 1:
            return data
        least = get_least_for_index(data, i)
        data = keep_match_values(data, i, least)
    return data


def problem2():
    o2_rating = oxygen_rating()
    print('02 rating is {}'.format(o2_rating))
    o2_rating_binary = [int(val) for val in o2_rating][0]
    print('o2 rating as int {}'.format(o2_rating_binary))
    o2_rating_decimal = binary_to_decimal(o2_rating_binary)
    print('o2 rating as decimal {}'.format(o2_rating_decimal))

    co2_rating = carbon_rating()
    print("co2 rating is {}".format(co2_rating))
    co2_rating_binary = [int(val) for val in co2_rating][0]
    print('co2 rating as int {}'.format(co2_rating_binary))
    co2_rating_decimal = binary_to_decimal(co2_rating_binary)
    print('co2 rating as decimal {}'.format(co2_rating_decimal))

    lifesupport = o2_rating_decimal * co2_rating_decimal
    print("lifesupport rating is {}".format(lifesupport))
    # o2 is  1111101  125
    # co2 is 111100010100 3860
    # lifesupport of 482500


def main():
    problem1()
    # problem2()


if __name__ == '__main__':
    # functions if main argument
    main()
