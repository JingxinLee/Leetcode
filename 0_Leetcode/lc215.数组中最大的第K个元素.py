# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 1:47 AM 12/3/20

"""
from typing import List
import random
import json

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)

        target = size - k
        left = 0
        right = size - 1
        while True:
            index = self.__partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                # 下一轮在 [index + 1, right] 里找
                left = index + 1
            else:
                right = index - 1

    #  循环不变量：[left + 1, j] < pivot
    #  (j, i) >= pivot
    def __partition(self, nums, left, right):

        pivot = nums[left]
        j = left  # j 每次从 left 开始
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left] # 交换left和最后一个比pivot小的数
        return j


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
            k = int(line);

            ret = Solution().findKthLargest(nums, k)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()