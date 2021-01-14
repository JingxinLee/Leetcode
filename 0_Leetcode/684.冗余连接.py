# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 9:15 AM 1/13/21
在本问题中, 树指的是一个连通且无环的无向图。

输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v]，满足u < v，表示连接顶点u和v的无向图的边。

返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边[u, v] 应满足相同的格式u < v。

示例 1：
输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图为:
  1
 / \
2 - 3

示例 2：
输入: [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
解释: 给定的无向图为:
5 - 1 - 2
    |   |
    4 - 3

注意:
输入的二维数组大小在 3 到 1000。
二维数组中的整数在1到N之间，其中N是输入数组的大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/redundant-connection
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import json
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:  # 并查集
        nodesCount = len(edges)
        parent = list(range(nodesCount + 1))

        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
            else:
                return [node1, node2]
        return []


def stringToInt2dArray(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            edges = stringToInt2dArray(line)

            ret = Solution().findRedundantConnection(edges)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()