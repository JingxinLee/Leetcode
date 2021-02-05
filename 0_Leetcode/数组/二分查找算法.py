# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 4:50 PM 1/23/21

"""
import json
from typing import List

# 二分查找
def binary_search(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right - left) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# 寻找左侧边界
def left_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - mid) / 2
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    if left > len(nums) or nums[left] != target:
        return -1
    return left


# 寻找右侧边界
def right_bound(self, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - mid) / 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if right < 0 or nums[right] != target:
        return -1
    return right

