# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 下午12:51 2020/7/5
# 154 #
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

示例 1：
输入：[3,4,5,1,2]
输出：1

示例 2：
输入：[2,2,2,0,1]
输出：0

"""
class Solution:
    def minArray(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        mid = left
        while nums[left] >= nums[right]:
            if right - left == 1:
                mid = right
                break
            mid = (left + right) // 2
            if nums[left] == nums[right] and nums[left] == nums[mid]:
                result = nums[left]
                for i in range(left+1, len(nums)):
                    if result > nums[i]:
                        result = nums[i]
                return result
            if nums[mid] >= nums[left]:
                left = mid
            elif nums[mid] <= nums[right]:
                right = mid

        return nums[mid]

    def minNumberInRotateArray(self, rotateArray):
        left, right = 0, len(rotateArray) - 1
        while left < right:
            mid = (left + right) // 2
            # 因为low+high在low和high特别大的时候可能会造成溢出，使用减法避免了溢出发生
            # mid = left + (right - left) // 2
            if rotateArray[mid] > rotateArray[right]:
                left = mid + 1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                right -= 1  # 缩小范围
        return rotateArray[left]

