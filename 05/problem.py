from utils.utility import *
import pathlib
import re
import math
DATA_FILE_PATH = str(pathlib.Path().resolve()) + '/05/data.txt'


def convert_vectors_to_points(array):
    data = []
    for vector in array:
        points = re.findall('\d+', vector)
        points = [int(point) for point in points]
        data.append(points)
    data_out = np.zeros((len(data), 4), dtype="i")
    data_out[:] = data
    return data_out


def find_max_coords(array):
    max_vals = array.max(axis=0)
    return max_vals[0] if max_vals[0] > max_vals[2] else max_vals[2], max_vals[1] if max_vals[1] > max_vals[3] else max_vals[3]


def length_of_diagonal(x1, y1, x2, y2):
    return int(math.sqrt((pow((x2 - x1), 2)**2)+(pow((y2 - y1), 2)**2)))


def draw_vector(topo, vector, diagonal):
    if vector[0] != vector[2] and vector[1] != vector[3] and not diagonal:
        return topo
    if vector[0] != vector[2] and vector[1] != vector[3]:
        x1, y1, x2, y2 = vector
        dif_y = 1 if y1 < y2 else -1
        dif_x = 1 if x1 < x2 else -1
        distance = 0
        if dif_x > 0:
            distance = x2 - x1
        else:
            distance = x1 - x2
        for i in range(distance+1):
            topo[x1, y1] += 1
            x1 += dif_x
            y1 += dif_y
        return topo
    else:
        x_range = [vector[0], vector[2]]
        x_range.sort()
        y_range = [vector[1], vector[3]]
        y_range.sort()
        for i in range(x_range[0], x_range[1]+1):
            for j in range(y_range[0], y_range[1]+1):
                topo[i, j] += 1
        return topo


def find_elevation_higher(topo, elevation):
    print("in find")
    print("max value is {}".format(topo.max()))
    return (topo > elevation).sum()


def problem1():
    print('problem 1')
    data = load_file_into_array(DATA_FILE_PATH)
    data = convert_vectors_to_points(data)
    maxX, maxY = find_max_coords(data)
    sea_floor = np.zeros((maxX+1, maxY+1), dtype="i")
    for vector in data:
        sea_floor = draw_vector(sea_floor, vector, False)
    total = find_elevation_higher(sea_floor, 1)
    print("topo points is {}".format(total))
    # 6113


def problem2():
    print('problem 2')
    data = load_file_into_array(DATA_FILE_PATH)
    data = convert_vectors_to_points(data)
    maxX, maxY = find_max_coords(data)
    sea_floor = np.zeros((maxX+1, maxY+1), dtype="i")
    for vector in data:
        sea_floor = draw_vector(sea_floor, vector, True)
    total = find_elevation_higher(sea_floor, 1)
    print("topo points is {}".format(total))
    # 957972 is too high
    # 20352 is too low


def main():
    # problem1()
    problem2()


if __name__ == '__main__':
    # functions if main argument
    main()
