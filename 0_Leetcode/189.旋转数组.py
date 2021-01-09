# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:01 AM 1/8/21

给定一个数组，将数组中的元素向右移动k个位置，其中k是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

示例2:
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为O(1) 的原地算法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import json

class Solution:
    def rotate0(self, nums: List[int], k: int) -> None: # 使用额外的数组  Time and space: O(n)
        """
        Do not return anything, modify nums in-place instead.   不要用
        """
        n = len(nums)
        newArr = []
        for i in range(k):
            newArr.append(nums[n - k + i])

        for j in range(k, n):
            newArr.append(nums[j - k])

        for k in range(n):
            nums[k] = newArr[k]

        return nums

    def rotate2(self, nums: List[int], k: int) -> None: # 使用额外的数组  Time and space: O(n)  不要用
        n = len(nums)
        newArr = [0] * n

        for i in range(n):
            newArr[(i+k) % n] = nums[i]
        for j in range(n):
            nums[j] = newArr[j]



    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)





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
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            line = next(lines)
            k = int(line);

            ret = Solution().rotate(nums, k)

            out = integerListToString(nums)
            if ret is not None:
                print
                "Do not return anything, modify nums in-place instead."
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()