# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 1:50 PM 1/20/21
给你两个 没有重复元素 的数组nums1 和nums2，其中nums1是nums2的子集。

请你找出 nums1中每个元素在nums2中的下一个比其大的值。

nums1中数字x的下一个更大元素是指x在nums2中对应位置的右边的第一个比x大的元素。如果不存在，对应位置输出 -1 。
                     -------
                     |   -----
        -------------|   |
        |    ----|   |   |
        |    |   |   |   |
nums    2    1   2   4   3
res     4    2   4   -1  -1

示例 1:
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
    对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
    对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

示例 2:
输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
    对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import json
from typing import List

class Solution0:
    def nextGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = []
        res = [-1] * n
        for i in range(n-1, -1, -1):
            while s and s[-1] <= nums[i]:
                s.pop()
            res[i] = s[-1] if s else -1 # 如果s不为空,那么就是s的栈顶,也是最靠近nums[i]的,因为是从后往前入s的
            s.append(nums[i])
        return res

class Solution1:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        n1, n2 = len(nums1), len(nums2)
        for i in range(n1):
            a = nums1[i]
            a_index = nums2.index(a)
            for j in range(a_index+1, n2):
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    break
            else:
                res.append(-1)

        return res

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        if not nums1: return [] #若为空数组，则返回
        ans=[-1 for _ in range(len(nums1))]
        for i in range(len(nums1)-1, -1, -1):#倒着往栈里放
            s = nums2[nums2.index(nums1[i]):][::-1]
            while s and nums1[i] >= s[-1]:
                s.pop()#矮个起开
            ans[i] = s[-1] if s else -1
        return ans

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
            nums1 = stringToIntegerList(line);
            line = next(lines)
            nums2 = stringToIntegerList(line);

            ret = Solution().nextGreaterElement(nums1, nums2)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()