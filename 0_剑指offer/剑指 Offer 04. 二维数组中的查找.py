# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 下午12:10 2020/7/4
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。

限制：
0 <= n <= 1000
0 <= m <= 1000
"""
# class Solution:
#     def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
#         m, n = len(matrix), len(matrix[0])
#         if target < matrix[0][0] or target > matrix[m-1][n-1]:
#             return False
#         i, j = 0, n-1
#         while(i < m and j >= 0):
#             if target > matrix[i][j]:
#                 i += 1
#             elif target < matrix[i][j]:
#                 j -= 1
#             else:
#                 return True
#         return False

import json
from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        i, j = 0, len(matrix[0])-1
        while i < len(matrix) and j >= 0:
            if target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            else:
                return True
        return False

def stringToInt2dArray(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


def main():
    import sys
    def readlines():
        with open('stdin.txt') as f:
            for line in f:
                yield line.strip(('\n'))
    lines = readlines()
    while True:
        try:
            line = next(lines)
            matrix = stringToInt2dArray(line)
            line = next(lines)
            target = stringToInt(line)

            ret = Solution().findNumberIn2DArray(matrix, target)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()