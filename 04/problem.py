import time
from os import wait

from numpy import remainder
from utils.utility import *
import pathlib
DATA_FILE_PATH = str(pathlib.Path().resolve()) + '/04/data.txt'


def mark_bingo_numbers(number, boards, masks):
    temp_mask = np.isin(boards, number)
    masks[temp_mask] = 1
    print("after marking top 2")
    print(boards[:2])
    print(masks[:2])
    return masks


def sum_unmarked_numbers(board, mask):
    temp_mask = np.isin(mask, 0)
    return np.sum(board[temp_mask])


def check_for_win(board):
    # check across
    print('checking board')
    print(board)
    print(np.sum(board, axis=0))
    if 5 in np.array(np.sum(board, axis=0)).tolist():
        return True
    print(np.sum(board, axis=1))
    if 5 in np.array(np.sum(board, axis=1)).tolist():
        return True
    print(np.trace(board))
    if np.trace(board, dtype="i") == 5:
        return True
    print(np.trace(board, 4))
    if np.trace(board, offset=4, dtype="i") == 5:
        return True


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
    # problem2()


if __name__ == '__main__':
    # functions if main argument
    main()
