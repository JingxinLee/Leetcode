# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 2:57 PM 7/25/20
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:
输入: [7,5,6,4]
输出: 5
https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/jian-dan-yi-dong-gui-bing-pai-xu-python-by-azl3979/
"""
import json
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0
        def merge(nums, start, mid, end, tmp):
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    self.cnt += mid - i + 1   # 左边i比后面的一个值大，  左边i后面的也都比后面的值大，所以逆序对个数为i到mid的距离
                    tmp.append(nums[j])
                    j += 1
            while i <= mid:
                tmp.append(nums[i])
                i += 1
            while j <= end:
                tmp.append(nums[j])
                j += 1
            for i in range(len(tmp)):
                nums[start + i] = tmp[i]
            tmp.clear()
        def mergeSort(nums, start, end, tmp):
            if start >= end: return
            mid = (start + end) >> 1
            mergeSort(nums, start, mid, tmp)
            mergeSort(nums, mid + 1, end, tmp)
            merge(nums, start, mid, end, tmp)
        mergeSort(nums, 0, len(nums) - 1, [])
        return self.cnt


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

            ret = Solution().reversePairs(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()