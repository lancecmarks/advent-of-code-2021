from typing import ItemsView
from utils.utility import *
import pathlib
import time
DATA_FILE_PATH = str(pathlib.Path().resolve()) + '/10/data.txt'


def problem1():
    print('problem 1')
    # data = load_file_into_array(DATA_FILE_PATH)
    # score = 0
    # for line in data:
    #     print(line)
    #     open_stack = []
    #     for item in line:
    #         if item in ['{', '(', '<', '[']:
    #             open_stack.append(item)
    #         else:
    #             print(item)
    #             if item == '}' and open_stack[-1] == '{':
    #                 open_stack.pop()
    #             elif item == ')' and open_stack[-1] == '(':
    #                 open_stack.pop()
    #             elif item == '>' and open_stack[-1] == '<':
    #                 open_stack.pop()
    #             elif item == ']' and open_stack[-1] == '[':
    #                 open_stack.pop()
    #             else:
    #                 print("item {} not found in stack".format(item))
    #                 if item == ')':
    #                     score += 3
    #                 if item == ']':
    #                     score += 57
    #                 if item == '}':
    #                     score += 1197
    #                 if item == '>':
    #                     score += 25137
    #                 break
    # print("total score is {}".format(score))


def problem2():
    print('problem 2')
    data = load_file_into_array(DATA_FILE_PATH)
    score = []
    ending = []
    for line in data:
        # print(line)
        open_stack = []
        ending = []
        skip = False
        for item in line:
            # time.sleep(2)
            if item in ['{', '(', '<', '[']:
                # print(item)
                open_stack.append(item)
            else:
                # print(item)
                # print("what we working with")
                # print(open_stack)
                if item == '}' and open_stack[-1] == '{':
                    # print("pop for item {}".format(item))
                    open_stack.pop()
                elif item == ')' and open_stack[-1] == '(':
                    # print("pop for item {}".format(item))
                    open_stack.pop()
                elif item == '>' and open_stack[-1] == '<':
                    # print("pop for item {}".format(item))
                    open_stack.pop()
                elif item == ']' and open_stack[-1] == '[':
                    # print("pop for item {}".format(item))
                    open_stack.pop()
                elif len(open_stack) == 0:
                    # print("stack is empty and item is {}".format(item))
                    # print(item)
                    if item == '{':
                        ending.append('}')
                    elif item == '(':
                        ending.append(')')
                    elif item == '<':
                        ending.append('>')
                    elif item == '[':
                        ending.append(']')
                else:
                    if len(open_stack) != 0:
                        # print("stack not empty")
                        # print(open_stack)
                        # print("item {} not found in stack".format(item))
                        skip = True
                        break
        # print("we got to an end of a line and the stuff is ")
        # print(open_stack)
        if not skip:
            for item in open_stack:
                # print(item)
                if item == '{':
                    ending.append('}')
                elif item == '(':
                    ending.append(')')
                elif item == '<':
                    ending.append('>')
                elif item == '[':
                    ending.append(']')
            temp_score = 0
            # print(ending)
            while len(ending) != 0:
                # print("score = {}".format(temp_score))
                item = ending.pop()
                temp_score *= 5
                if item == ')':
                    temp_score += 1
                if item == ']':
                    temp_score += 2
                if item == '}':
                    temp_score += 3
                if item == '>':
                    temp_score += 4
                # print("after item score is {}".format(temp_score))
            # print("line score is {}".format(temp_score))
            score.append(temp_score)
    length = len(score)
    print(length)
    mid = length // 2
    print(mid)
    score = sorted(score)
    print(score)
    print("middle is {}".format(score[mid]))


def main():
    # problem1()
    problem2()


if __name__ == '__main__':
    # functions if main argument
    main()
