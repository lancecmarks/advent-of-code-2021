from utils.utility import *
import pathlib
DATA_FILE_PATH = str(pathlib.Path().resolve()) + '/08/data.txt'


def problem1():
    print('problem 1')
    data = load_file_into_array(DATA_FILE_PATH)
    # print(data)
    data_split = [str.split('|') for str in data]
    print(data_split)
    output = []
    for i in data_split:
        output.append(i[1])
    print(output)
    output = [str.split() for str in output]
    print(output)
    # 1:2 4:4 7:3 8:7
    count = 0
    for i in output:
        for j in i:
            p = len(j)
            if p == 2 or p == 4 or p == 3 or p == 7:
                count += 1
    print("Count is {}".format(count))


def get_unique(sec, known):
    if len(sec) == 2:
        known[1] = sec
        return "1"
    if len(sec) == 4:
        known[4] = sec
        return "4"
    if len(sec) == 3:
        known[7] = sec
        return "7"
    if len(sec) == 7:
        known[8] = sec
        return "8"
    return "X"


def problem2():
    print('problem 2')
    total = 0
    data = load_file_into_array(DATA_FILE_PATH)
    # print(data)
    for line in data:
        dict = {}
        known = [None] * 10
        parts = line.split(" |")
        # print(parts)
        for p in parts:
            a = p.strip()
            a = p.split()
            for r in a:
                r = "".join(sorted(r))
                # print(r)
                if r not in dict.keys():
                    dict[r] = get_unique(r, known)

        pos1 = set(known[7]).difference(set(known[1]))

        # SOLVING FOR 9
        fourseven = set(known[4]+known[7])
        for num in dict.keys():
            if len(num) == 6 and len(set(num).difference(fourseven)) == 1:
                # print(set(num).difference(fourseven))
                dict[num] = "9"
                known[9] = num

        pos4 = set(known[8]).difference(set(known[9]))
        pos5 = set(known[9]).difference(set(known[4]+known[7]))

        # SOLVING FOR 6
        sevenpos5 = set(known[7]).union(pos5)
        # print(sevenpos5)
        for num in dict.keys():
            if len(num) == 6 and len(set(num).difference(sevenpos5)) == 3:
                # print(set(num).difference(sevenpos5))
                dict[num] = "6"
                known[6] = num

        pos2 = set(known[8]).difference(set(known[6]))

        # SOLVING FOR 0
        for num in dict.keys():
            if len(num) == 6 and len(set(num).difference(sevenpos5)) == 2 and dict[num] == "X":
                # print(set(num).difference(sevenpos5))
                dict[num] = "0"
                known[0] = num

        pos3 = set(known[8]).difference(set(known[0]))

        # SOLVING FOR 5
        assert5 = set(known[8]).difference(pos2.union(pos4))
        for num in dict.keys():
            if len(num) == 5 and set(num) == assert5:
                dict[num] = "5"
                known[5] = num

        # SOLVING FOR 3
        assert3 = set(known[1]).union(pos1, pos3, pos5)
        for num in dict.keys():
            if len(num) == 5 and set(num) == assert3:
                dict[num] = "3"
                known[3] = num

        # SOLVING FOR 2
        for num in dict.keys():
            if len(num) == 5 and dict[num] == "X":
                dict[num] = "2"
                known[2] = num

        # print("1 , 2 , 3 , 4 , 5")
        # print(pos1)
        # print(pos2)
        # print(pos3)
        # print(pos4)
        # print(pos5)

        # # SOLVING
        # print(known)
        # print(dict)

        num_string = line.split("|")[1].strip().split()
        # print(num_string)
        num_string_sorted = ["".join(sorted(num)) for num in num_string]
        # print(num_string_sorted)
        tot_str = ""
        for item in num_string_sorted:
            tot_str += dict[item]
        # print(int(tot_str))
        total += int(tot_str)
    print("total number is {}".format(total))
    # 1031553


def main():
    # problem1()
    problem2()


if __name__ == '__main__':
    # functions if main argument
    main()
