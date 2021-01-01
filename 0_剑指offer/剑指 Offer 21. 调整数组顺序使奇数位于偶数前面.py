# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 下午4:01 2020/7/7
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
输入：nums =[1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。

提示：
1 <= nums.length <= 50000
1 <= nums[i] <= 10000
"""
from typing import List

# 不保留原始顺序
class Solution2:
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

class Solution3:
    def exchange(self, nums: List[int]) -> List[int]:
        m, n = 0, len(nums) - 1
        while m < n:
            if nums[m] % 2 == 0:
                nums[m], nums[n] = nums[n], nums[m]
                n -= 1
            else:
                m += 1
        return nums


# 保留原始顺序
class Solution:
    def exchange(self, array):
        i, j = 0, len(array)
        while i < j:
            if array[i] % 2 == 1:
                i += 1
            else:
                array.append(array[i])
                del(array[i])
                j -= 1
        return array

class Solution4:
    def exchange(self, array):
        # write code here
        # 没有额外的数组空间。
        # 实际上pop(index)的时间复杂度是O(n)，删除元素时后面的元素往前移动，总的时间复杂度接近O(n^2)
        lenth = len(array)
        move = 0
        index = 0
        while(lenth - move - index > 0):
            if array[index]%2 == 0:
                temp = array.pop(index)
                array.append(temp)
                move += 1
                index -= 1
            index += 1
        return array

a = Solution3()
print(a.exchange([1,2,3,4,5,6,7]))