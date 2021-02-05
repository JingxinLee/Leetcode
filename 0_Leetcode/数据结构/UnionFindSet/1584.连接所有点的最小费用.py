# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:50 PM 1/19/21
给你一个points数组，表示 2D 平面上的一些点，其中points[i] = [xi, yi]。

连接点[xi, yi] 和点[xj, yj]的费用为它们之间的 曼哈顿距离：|xi - xj| + |yi - yj|，其中|val|表示val的绝对值。
请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有一条简单路径时，才认为所有点都已连接。

示例 1：
输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
输出：20

解释：
我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。

示例 2：
输入：points = [[3,12],[-2,5],[-4,1]]
输出：18

示例 3：
输入：points = [[0,0],[1,1],[1,0],[-1,1]]
输出：4

示例 4：
输入：points = [[-1000000,-1000000],[1000000,1000000]]
输出：4000000

示例 5：
输入：points = [[0,0]]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-to-connect-all-points
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import json
from typing import List

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """


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
            points = stringToInt2dArray(line)

            ret = Solution().minCostConnectPoints(points)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()