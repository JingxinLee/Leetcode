# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 2:57 PM 7/25/20
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

"""
import json
from typing import List
class Solution:
    def search(self, nums: [int], target: int) -> int:
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i +j) // 2
                if nums[m] <= tar: i = m + 1
                else: j = m - 1
            return i
        return helper(target) - helper(target - 1)


    def search3(self, nums: List[int], target: int) -> int:
        # 二分法
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) >> 2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        right = i

        if j >= 0 and nums[j] != target:
            return 0
        i = 0
        while i <= j:
            m = (i + j) >> 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        left = j
        return right - left - 1

    def search2(self, nums: List[int], target: int) -> int:
        # Hash
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        if target in dic.keys():
            return dic[target]
        else:
            return 0

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
            line = next(lines)
            target = int(line);

            ret = Solution().search(nums, target)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()