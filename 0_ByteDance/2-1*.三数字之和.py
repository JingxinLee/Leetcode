# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 4:27 PM 9/9/20
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。



示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
import json
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 注意 不要写成 nums = nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k-1]: continue
            i, j = k+1, len(nums)-1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]: i += 1  # i 和前面的相等  就继续往后加1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]: j -= 1 # j和后面的相等, 就继续往前减1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
        return res


def stringToIntegerList(input):
    return json.loads(input)


def int2dArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        with open('stdin.txt') as f:
            for line in f:
                yield line.strip(('\n'))

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line)

            ret = Solution().threeSum(nums)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()