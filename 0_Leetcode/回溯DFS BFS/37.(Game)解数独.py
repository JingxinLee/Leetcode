# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:35 PM 1/31/21

"""
import json
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def backtrack(i, j):
            if j == 9:  # 如果列数是9 继续下一行
                return backtrack(i + 1, 0)
            if i == 9:  # 行数达到9说明找到了一个可行解返回
                return True
            if board[i][j] != '.':  # 如果不是空白格，下一个
                return backtrack(i, j + 1)

            for k in range(1, 10):  # 一个一个试
                ch = str(k)
                if isValid(i, j, ch):  # 合法就放值
                    board[i][j] = ch
                else:
                    continue  # 否则下一个
                if backtrack(i, j + 1):  # 递归
                    return True
                board[i][j] = '.'  # 回溯

            return False  # 说明没找到放的位置，返回False

        def isValid(r, c, n):  # 合法性判断
            for i in range(9):
                if board[r][i] == n:
                    return False
                if board[i][c] == n:
                    return False
                if board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3] == n:
                    return False
            return True

        backtrack(0, 0)


class Solution2: #超出时间限制
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.backtrack(board, 0, 0)

    def backtrack(self, board, row, col):
        m = n = 9
        if col == 9:  # 如果列数是9 继续下一行
            self.backtrack(board, row + 1, 0)
            return
            # 对每个位置进行穷举
        for i in range(row, m):
            for j in range(col, n):
                if board[i][j] != '.':  # 如果不是空白格，下一个
                    self.backtrack(board, i, j + 1)

                for k in range(1, 10):  # 一个一个试
                    ch = str(k)
                    if not self.isValid(board, i, j, ch):  # 否则下一个
                        continue

                    board[i][j] = ch  # 合法就放值
                    self.backtrack(board, i, j + 1)  # 递归
                    board[i][j] = '.'  # 回溯

    def isValid(self, board, row, col, n):  # 合法性判断
        for i in range(9):
            if board[row][i] == n:  # 判断行是否存在重复
                return False
            if board[i][col] == n:  # 判断列是否存在重复
                return False
            if board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == n:  # 判断 3 x 3 方框是否存在重复
                return False
        return True


def stringToChar2dArray(input):
    return json.loads(input)


def char2dArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            board = stringToChar2dArray(line)

            ret = Solution().solveSudoku(board)

            out = char2dArrayToString(board)
            if ret is not None:
                print("Do not return anything, modify board in-place instead.")
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()