# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 3:18 PM 7/26/20

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

示例 2：
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
"""
import json
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # 双指针
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return [nums[i], nums[j]]
        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]: # 双指针 + 二分法
        i, j = 0, len(nums) - 1
        split_index = (i + j) >> 1
        while i < j - 1:
            if nums[i] + nums[j] > target:       # 下面根据 nums[i] + nums[split_index]的结果判断是否缩进
                if nums[i] + nums[split_index] > target: # nums[i]加上（split_index,j)内的任意一个元素均大于target，可加速缩进
                    j = split_index - 1
                    split_index = (i + j) >> 1
                elif nums[i] + nums[split_index] < target:  # 不能加速缩进，潜在的右边数字在(split_index,j)范围内   说明nums[j] 很大
                    j -= 1
                    split_index = (split_index + j) >> 1    # 根据潜在范围计算
                else:
                    return [nums[i], nums[split_index]]

            elif nums[i] + nums[j] < target:              # 下面根据nums[split_index] + nums[j]的结果来判断是否缩进
                if nums[split_index] + nums[j] > target:  # 无法加速缩进，潜在的左边数字范围在(i,split_index)。    说明 nums[i] 小了
                    i += 1
                    split_index = (i + split_index) >> 1  # 根据潜在范围计算
                elif nums[split_index] + nums[j] < target: # nums[j]加上范围内(i,split_index)任意一个元素均小于target， 加速缩进
                    i = split_index + 1
                    split_index = (i + j) >> 1
                else:
                    return [nums[split_index], nums[j]]
            else:
                return [nums[i], nums[j]]
        if i == j - 1 and nums[j] + nums[i] == target:
            return [nums[i], nums[j]]
        else:
            return []


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
            line = next(lines)
            target = int(line);

            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()