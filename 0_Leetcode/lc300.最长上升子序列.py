# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 12:57 AM 11/30/20

"""
import json
from typing import List

class Solution:
    # 方法一：动态规划+二分查找：O(nlogn): 遍历 nums列表需 O(N)，二分法需 O(logN)
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return size

        cell = [nums[0]]
        for num in nums[1:]:
            if num > cell[-1]:
                cell.append(num)
                continue # 不执行下面，跳出本次for循环，执行下次for循环

            l, r = 0, len(cell) - 1
            while l < r:
                mid = l + (r - l) // 2
                if cell[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            cell[l] = num # 插入数据 num 替换 比他大的 最小的那个，保证这个队列始终是在保证最长的情况下，值最小的那个
        return len(cell)
    # 方法二： O(n^2)
    def lengthOfLIS2(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)



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

            ret = Solution().lengthOfLIS(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()