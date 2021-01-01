# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 3:20 PM 7/26/20

给定一个数组 nums 和 滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]

解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


提示：
你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤输入数组的大小。
"""
import json
from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []
        n = len(nums)
        for i, j in zip(range(1-k, n + 1 - k), range(n)):
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft() # 删去队首元素
            while deque and deque[-1] < nums[j]:
                deque.pop() # 删去 所有 小于 nums[j]的 只保留最大的 放在第0位
            deque.append(nums[j])
            if i >= 0:
                res.append(deque[0]) # 记录每次窗口的最大值
        return res

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()

        for i in range(k):  # 未形成窗口
            while deque and deque[-1] < nums[i]: deque.pop()
            deque.append(nums[i])

        res = [deque[0]]

        for i in range(k, len(nums)):  # 形成窗口后
            if deque[0] == nums[i - k]: deque.popleft()
            while deque and deque[-1] < nums[i]: deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res



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
            k = int(line);

            ret = Solution().maxSlidingWindow(nums, k)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
