import time
from os import wait

from numpy import remainder
from utils.utility import *
import pathlib
DATA_FILE_PATH = str(pathlib.Path().resolve()) + '/04/data.txt'


def problem1():
    print('problem 1')
    bingo_numbers, bingo_boards, mask_boards = load_bingo_into_array(
        DATA_FILE_PATH)
    escape = False
    winning_number = -1
    winning_mask = None
    winning_board = None
    for number in bingo_numbers:
        mask_boards = mark_bingo_numbers(number, bingo_boards, mask_boards)
        for index, mask in enumerate(mask_boards):
            if(check_for_win(mask)):
                winning_board = bingo_boards[index]
                winning_mask = mask
                winning_number = number
                escape = True
                break
        if escape:
            break

    # calculate answer stuff
    unmarked_sum = sum_unmarked_numbers(winning_board, winning_mask)
    total = winning_number * unmarked_sum
    print("total is {}".format(total))
    print("GAME OVER")

    # 35711


def problem2():
    print('problem 2')
    bingo_numbers, bingo_boards, mask_boards = load_bingo_into_array(
        DATA_FILE_PATH)
    escape = False
    winning_number = -1
    winning_mask = None
    winning_board = None

    for number in bingo_numbers:
        mask_boards = mark_bingo_numbers(number, bingo_boards, mask_boards)

        for index in range(mask_boards.shape[0]-1, -1, -1):
            if(check_for_win(mask_boards[index])):
                if (mask_boards.shape[0] > 1):
                    winning_number = number
                    winning_mask = mask_boards[index]
                    winning_board = bingo_boards[index]

                    mask_boards = np.delete(mask_boards, index, axis=0)
                    bingo_boards = np.delete(bingo_boards, index, axis=0)
                else:
                    winning_board = bingo_boards[index]
                    winning_mask = mask_boards[index]
                    winning_number = number
                    escape = True
                    break
        if escape:
            break
    # calculate answer stuff
    # print("winning board")
    # print(winning_board)
    # print(winning_mask)
    # print(winning_number)
    unmarked_sum = sum_unmarked_numbers(winning_board, winning_mask)
    total = winning_number * unmarked_sum
    print("total is {}".format(total))
    print("GAME OVER")

    # 5586


def main():
    problem1()
    problem2()


if __name__ == '__main__':
    # functions if main argument
    main()
