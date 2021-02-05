# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 7:24 PM 1/23/21
珂珂喜欢吃香蕉。这里有N堆香蕉，第 i 堆中有piles[i]根香蕉。警卫已经离开了，将在H小时后回来。

珂珂可以决定她吃香蕉的速度K（单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

示例 1：
输入: piles = [3,6,7,11], H = 8
输出: 4

示例2：
输入: piles = [30,11,23,4,20], H = 5
输出: 30

示例3：
输入: piles = [30,11,23,4,20], H = 6
输出: 23

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/koko-eating-bananas
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import json
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def possible(K):
            return sum((p - 1) // K + 1 for p in piles) <= H
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        return left


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            piles = stringToIntegerList(line);
            line = next(lines)
            H = int(line);

            ret = Solution().minEatingSpeed(piles, H)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()