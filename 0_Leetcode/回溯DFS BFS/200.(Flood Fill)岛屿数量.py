# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:32 PM 1/31/21

"""
import json
from typing import List
import collections
class Solution: # DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        self.directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]
        if row == 0: return 0
        count = 0
        for i in range(row):
            for j in range(col):
                if not visited[i][j] and grid[i][j] == '1':
                    self.dfs(grid, visited, i, j)
                    count += 1
        return count

    def dfs(self, grid, visited, i, j):
        visited[i][j] = True
        for direction in self.directions:
            newX = i + direction[0]
            newY = j + direction[1]
            if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]) and grid[newX][newY] == '1' and not visited[newX][newY]:
                print("  递归之前 => ", grid)
                self.dfs(grid, visited, newX, newY)
                print("递归之后 => ", grid)

class Solution00: # DFS 的另一种写法
    def numIslands(self, grid: [[str]]) -> int:
        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0': return
            grid[i][j] = '0'
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count


class Solution1: # BFS
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque( [(r, c)] )
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"

        return num_islands

class Solution11: # BFS
    def numIslands(self, grid: [[str]]) -> int:
        def bfs(grid, i, j):
            queue = [[i, j]]
            while queue:
                [i, j] = queue.pop(0)
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0': continue
                bfs(grid, i, j)
                count += 1
        return count

from queue import Queue
class Solution_error:  # BFS 运行不出来!!!!
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                self.bfs(grid, visited, i, j)
                count += 1
        return count

    def bfs(self, grid, visited, i, j):
        que = Queue()
        que.put((i, j))
        visited[i][j] = True
        while not que.empty():
            (row, col) = que.get()
            for x, y in zip((row, row, row+1, row-1), (col+1, col-1, col, col)):
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1' and not visited[x][y]:
                    que.put((x, y))

# class UF:
#     def __init__(self, n):
#         self.count = n
#         self.parent = [i for i in range(n)]
#
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
#
#     def union(self, p, q):
#         rootP = self.find(p)
#         rootQ = self.find(q)
#         if rootP == rootQ:
#             return
#         self.parent[rootP] = rootQ
#         self.count -= 1
#
#     def connected(self, p, q):
#         return self.find(p) == self.find(q)
#
#     def getCount(self):
#         return self.count
#
# class Solution3:
#     # 并查集中连通分量的个数 - 空地的个数，就是岛屿数量。
#     def numIslands(self, grid: List[List[str]]) -> int:
#         row, col = len(grid), len(grid[0])
#         if row == 0: return 0
#
#         def getIndex(x, y):
#             return x * col + y
#
#         # 陆地个数
#         spaces = 0
#         uf = UF(row * col)
#         # 1、统计陆地的个数；2、合并水域
#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] == '0':
#                     spaces += 1
#                 else:
#                     if i + 1 < row and grid[i + 1][j] == '1':
#                         uf.union(getIndex(i, j), getIndex(i + 1, j))
#
#                     if j + 1 < col and grid[i][j + 1] == '1':
#                         uf.union(getIndex(i, j), getIndex(i, j + 1))
#         return uf.getCount() - spaces

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

            ret = Solution1().numIslands(grid)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()