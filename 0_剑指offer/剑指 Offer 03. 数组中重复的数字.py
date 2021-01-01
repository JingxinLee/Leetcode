# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 下午12:08 2020/7/4
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

限制：
2 <= n <= 100000
"""
import json
from typing import List
# 法 1
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        result = []
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

# 法 2
class Solution2:
    def findRepeatNumber(self, nums: List[int]) -> int:
        result = {}
        for i,num in enumerate(nums):
            if num in result:
                return num
            else:
                result[num] = i
        return result

# 法 3
class Solution3:
    def findRepeatNumber(self, nums: List[int]) -> int:
        result = {}
        for i in nums:
            if i not in result:
                result[i] = 0
            else:
                return i
# 法 4
class Solution4:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                     nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return None


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

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);

            ret = Solution().findRepeatNumber(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()