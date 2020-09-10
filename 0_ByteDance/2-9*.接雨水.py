# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:44 PM 9/9/20
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
[https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png]
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""
import json
from typing import List

class Solution:
    """
    动态规划
    时间 O(n)
    空间 O(n)
    """
    def trap(self, height: List[int]) -> int:
        # 边界条件
        if not height: return 0
        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n
        ans = 0
        # 初始化
        maxleft[0] = height[0]
        maxright[n-1] = height[n-1]
        # 设置备忘录，分别存储左边和右边最高的柱子高度
        for i in range(1,n):
            maxleft[i] = max(height[i],maxleft[i-1])
        for j in range(n-2,-1,-1):
            maxright[j] = max(height[j],maxright[j+1])
        # 一趟遍历，比较每个位置可以存储多少水
        for i in range(n):
            if min(maxleft[i],maxright[i]) > height[i]:
                ans += min(maxleft[i],maxright[i]) - height[i]
        return ans

class Solution2:
    """
    双指针
    时间 O(n) 遍历了一遍数组
    空间 O(1)
    """
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        left, right = 0, n - 1
        max_left, max_right = height[0], height[-1]
        ans = 0
        while left <= right:
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)
            if max_left < max_right:
                ans += max_left - height[left]
                left += 1
            else:
                ans += max_right - height[right]
                right -= 1
        return ans
class Solution3:
    # https://leetcode-cn.com/problems/trapping-rain-water/solution/shuang-zhi-zhen-an-xing-qiu-geng-hao-li-jie-onsuan/
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        SUM, tmp, high = 0, 0, 1
        while(left <= right):
            while(left <= right and height[left] < high):
                SUM += height[left]
                left += 1
            while(right >= left and height[right] < high):
                SUM += height[right]
                right -= 1
            high += 1
            tmp += right - left + 1
        return tmp - SUM

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
            height = stringToIntegerList(line);

            ret = Solution2().trap(height)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()