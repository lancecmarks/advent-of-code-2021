def split(word):
    return [char for char in word]


def getMaxForIndex(myList, index):
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(myList)):
        curr = myList[i]
        for j in range(12):
            counts[j] = counts[j] + int(curr[j])
    max_val = '1' if counts[index] >= len(myList)/2 else '0'
    # print('at position {} the max_val is {} for {} items'.format(
    #     index, max_val, len(myList)))
    # print(counts)
    return max_val


def getLeastForIndex(myList, index):
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(myList)):
        curr = myList[i]
        for j in range(12):
            counts[j] = counts[j] + int(curr[j])

    return '0' if counts[index] >= len(myList)/2 else '1'


def keepMatchValues(myList, index, test):
    data_array = []
    for i in range(len(myList)):
        curr = myList[i]
        if curr[index] == test:
            data_array.append(curr)
    return data_array


def loadArray():
    file = open("data.txt", "r")
    line_count = 0
    data_array = []
    for line in file:
        parts = split(line.strip())
        line_count += 1
        data_array.append(parts)
    file.close()
    print("Start array size is {}".format(len(data_array)))
    return data_array


def oxygen_rating():
    data = loadArray()
    for i in range(12):
        if len(data) == 1:
            return data
        most = getMaxForIndex(data, i)
        data = keepMatchValues(data, i, most)
    return data


def carbon_rating():
    data = loadArray()
    for i in range(12):
        if len(data) == 1:
            return data
        least = getLeastForIndex(data, i)
        data = keepMatchValues(data, i, least)
    return data


o2_rating = oxygen_rating()
print('02 rating is {}'.format(o2_rating))

co2_rating = carbon_rating()
print("co2 rating is {}".format(co2_rating))

# o2 is  1111101  125
# co2 is 111100010100 3860
# lifesupport of 482500
