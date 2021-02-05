# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 7:20 PM 1/7/21
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。

输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2

输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-provinces
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
import json
from typing import List

class Solution(object):
    def findCircleNum0(self, isConnected): # DFS
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(i):
            for j in range(cities):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        cities = len(isConnected)
        visited = set()
        circles = 0

        for i in range(cities):
            if i not in visited:
                dfs(i)
                circles += 1
        return circles

    def findCircleNum1(self, isConnected: List[List[int]]) -> int: # BFS
        cities = len(isConnected)
        visited = set()
        circles = 0

        for i in range(cities):
            if i not in visited:
                Q = collections.deque([i])
                while Q:
                    j = Q.popleft()
                    visited.add(j)
                    for k in range(cities):
                        if isConnected[j][k] == 1 and k not in visited:
                            Q.append(k)
                circles += 1

        return circles

    def findCircleNum(self, isConnected: List[List[int]]) -> int: # 并查集
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        cities = len(isConnected)
        parent = list(range(cities))

        for i in range(cities):
            for j in range(i + 1, cities):
                if isConnected[i][j] == 1:
                    union(i, j)

        circles = sum(parent[i] == i for i in range(cities))
        return circles




def stringToInt2dArray(input):
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
            isConnected = stringToInt2dArray(line)

            ret = Solution().findCircleNum(isConnected)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()