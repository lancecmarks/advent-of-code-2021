from utils.utility import *
import pathlib
DATA_FILE_PATH = str(pathlib.Path().resolve()) + '/06/data.txt'


def life_engine(data):
    count = len(data)
    for i in range(count):
        temp_age = data[i] - 1
        if temp_age < 0:
            data.append(8)
            temp_age = 6
        data[i] = temp_age
    return data


def mass_breeder(data):
    fish = np.zeros((2, 10), dtype=np.int64)
    for i in range(10):
        fish[0][i] = i
    for i in range(8, 0, -1):
        fish[1][i-1] = data[1][i]
    fish[1][8] = data[1][0]
    fish[1][6] += data[1][0]
    return fish


def problem1():
    print('problem 1')
    data = load_file_into_array(DATA_FILE_PATH)
    data = data[0].split(",")
    data = [int(val) for val in data]
    # print(data)
    for i in range(80):
        data = life_engine(data)
        # print(data)
    # print(data)
    print("total is {}".format(len(data)))
    # 350149 (80 days)


def problem2():
    print('problem 2')
    data = load_file_into_array(DATA_FILE_PATH)
    data = data[0].split(",")
    data = [int(val) for val in data]
    print(data)
    fish = np.zeros((2, 10), dtype=np.int64)
    for i in range(10):
        fish[0][i] = i
    print(fish)
    for i in range(len(data)):
        fish[1][data[i]] += 1
    print(fish)
    data = fish
    for i in range(256):
        data = mass_breeder(data)
    print(data)
    output = np.array(data[1][:]).sum(axis=0)
    print("total fish is {}".format(output))


def main():
    # problem1()
    problem2()


if __name__ == '__main__':
    # functions if main argument
    main()
