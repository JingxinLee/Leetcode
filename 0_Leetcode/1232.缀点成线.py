# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 7:10 PM 1/17/21
在一个XY 坐标系中有一些点，我们用数组coordinates来分别记录它们的坐标，其中coordinates[i] = [x, y]表示横坐标为 x、纵坐标为 y的点。

请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。

示例 1：
输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
输出：true

示例 2：
输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-it-is-a-straight-line
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import json
from typing import List


class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        def computeK(i):
            y = (coordinates[i][1] - coordinates[0][1])
            x = (coordinates[i][0] - coordinates[0][0])
            if x != 0:
                k = y * 1.0 / x
            else:
                k = 'inf'
            return k

        k = computeK(1)
        n = len(coordinates)
        for i in range(2, n):
            if computeK(i) == k:
                continue
            return False
        return True

class Solution2:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n1 = coordinates[1][0] - coordinates[0][0]
        n2 = coordinates[1][1] - coordinates[0][1]
        for x, y in coordinates[2:]:
            if n1 * (y - coordinates[0][1]) != n2 * (x - coordinates[0][0]):
                return False
        return True






def stringToInt2dArray(input):
    return json.loads(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            coordinates = stringToInt2dArray(line)

            ret = Solution().checkStraightLine(coordinates)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()