# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:32 PM 1/31/21

"""
import json
from typing import List


class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        class UnionFind:
            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]

            def get_count(self):
                return self.count

            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root == q_root:
                    return
                self.parent[p_root] = q_root
                self.count -= 1

        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])

        def get_index(x, y):
            return x * col + y

        # 陆地的个数
        spaces = 0
        uf = UnionFind(row * col)

        # 1、统计陆地的个数；2、合并水域
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    spaces += 1
                else:
                    if i + 1 < row and grid[i + 1][j] == '1':
                        uf.union(get_index(i, j), get_index(i + 1, j))
                    if j + 1 < col and grid[i][j + 1] == '1':
                        uf.union(get_index(i, j), get_index(i, j + 1))

        return uf.get_count() - spaces


class UF:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        self.parent[rootP] = rootQ
        self.count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def getCount(self):
        return self.count


class Solution:
    # 并查集中连通分量的个数 - 空地的个数，就是岛屿数量。
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        if row == 0: return 0

        def getIndex(x, y):
            return x * col + y
            # 陆地个数

        spaces = 0
        uf = UF(row * col)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    spaces += 1
                else:
                    if i + 1 < row and grid[i + 1][j] == '1':
                        uf.union(getIndex(i, j), getIndex(i + 1, j))

                    if j + 1 < col and grid[i][j + 1] == '1':
                        uf.union(getIndex(i, j), getIndex(i, j + 1))
        return uf.getCount() - spaces

def stringToChar2dArray(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            grid = stringToChar2dArray(line)

            ret = Solution().numIslands(grid)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()