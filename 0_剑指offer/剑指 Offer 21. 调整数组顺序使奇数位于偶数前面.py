# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 下午4:01 2020/7/7
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。 

提示：
1 <= nums.length <= 50000
1 <= nums[i] <= 10000
"""
from typing import List
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        while i < j:
            # 因为第二步和第三步循环过程中，有可能遇到 i == j 的边界情况，此时就应终止，不然 i 就跑到 j 右边了
            while i < j and nums[i] % 2 != 0:
                i += 1
            while i < j and nums[j] % 2 == 0:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        return nums

a = Solution()
print(a.exchange([1,2,3,4]))