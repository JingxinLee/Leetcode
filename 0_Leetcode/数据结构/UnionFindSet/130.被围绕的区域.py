# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 12:00 AM 1/16/21
给定一个二维的矩阵，包含'X'和'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的'O' 用 'X' 填充。

示例:
X X X X
X O O X
X X O X
X O X X

运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X

解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的'O'都不会被填充为'X'。
任何不在边界上，或不与边界上的'O'相连的'O'最终都会被填充为'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import json
from typing import List


class UF:
    def __init__(self, n):
        self.parent = [None] * n
        self.size = [None] * n
        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ: return
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]

    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return
        m, n = len(board), len(board[0])
        uf = UF(m * n + 1)
        dummy = m * n
        # 第一列和最后一列的 O 与 dummy 连通  (x,y) ->  x * n + y
        for i in range(m):
            if board[i][0] == 'O':
                uf.union(i * n, dummy)
            if board[i][n - 1] == 'O':
                uf.union(i * n + n - 1, dummy)
        # 第一行 和 最后一行 的 O 与 dummy 连通
        for j in range(n):
            if board[0][j] == 'O':
                uf.union(j, dummy)
            if board[m - 1][j] == 'O':
                uf.union(n * (m - 1) + j, dummy)
        # 上下左右进行搜索
        s = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O':
                    # 将此O与上下左右的O连通
                    for k in range(4):
                        x = i + s[k][0]
                        y = j + s[k][1]
                        if board[x][y] == 'O':
                            uf.union(x * n + y, i * n + j)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if not uf.connected(dummy, i * n + j):
                    board[i][j] = 'X'


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

            ret = Solution().solve(board)

            out = char2dArrayToString(board)
            if ret is not None:
                print
                "Do not return anything, modify board in-place instead."
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()