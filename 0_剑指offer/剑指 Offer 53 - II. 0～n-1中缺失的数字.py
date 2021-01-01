# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 2:58 PM 7/25/20
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
输入: [0,1,3]
输出: 2

示例2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8

"""
import json
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int: # 二 分 法
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i



    def missingNumber2(self, nums: List[int]) -> int:  # 利用 index
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        with open('stdin.txt') as f:
            for line in f:
                yield line.strip(('\n'))
    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);

            ret = Solution().missingNumber(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()