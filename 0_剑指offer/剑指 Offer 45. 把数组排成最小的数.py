# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 10:00 AM 7/22/20
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:
输入: [10,2]
输出: "102"

示例 2:
输入: [3,30,34,5,9]
输出: "3033459"

说明:
输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
"""
import json
from typing import List
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        """
        x + y > y + x   =>  x > y :  3 30 > 30 3 =>  '3' > '30'
        x + y < y + x   =>  x < y
        """
        strs = [str(num) for num in nums]

        # 快排
        def quickSort(l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                while i < j and strs[j] + strs[l] >= strs[l] + strs[j]: j -= 1
                while i < j and strs[i] + strs[l] <= strs[l] + strs[i]: i += 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            quickSort(l, i - 1)
            quickSort(i + 1, r)

        quickSort(0, len(strs) - 1)
        return "".join(strs)


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

            ret = Solution().minNumber(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()