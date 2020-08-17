# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 3:17 PM 7/26/20

一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]

示例 2：
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
 
限制：
2 <= nums.length <= 10000
"""
import json
import functools
from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = 0
        for num in nums:
            ret = ret ^ num  # 得到要找的 2个数的异或
        a, b = 0, 0 # 准备分组 任何数与0 异或都是其本身
        h = 1
        while h & ret == 0: # 找到第一步异或结果的第一个 1
            h <<= 1
        for num in nums:
            if num & h == 0: # 该位为0 分到a组
                a ^= num
            else:    # 该位为1 分到b组
                b ^= num
        return [a,b]


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


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

            ret = Solution().singleNumbers(nums)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()