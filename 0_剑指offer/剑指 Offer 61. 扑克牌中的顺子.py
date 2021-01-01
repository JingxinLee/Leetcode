# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:59 PM 7/28/20

从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例1:
输入: [1,2,3,4,5]
输出: True

示例2:
输入: [0,0,1,2,5]
输出: True

限制：
数组长度为 5
数组的数取值为 [0, 13] .

0个 1个 2个 大小王
"""
import json
from typing import List

class Solution:
    def isStraight(self, nums: List[int]) -> bool: # 集合 + 遍历
        repeat = set()
        maxx, minn = 0, 14
        for num in nums:
            if num == 0: continue
            if num > maxx: maxx = num
            if num < minn: minn = num
            if num in repeat: return False
            repeat.add(num)
        return maxx - minn < 5

    def isStraight2(self, nums: List[int]) -> bool: # 排序 + 遍历
        joker = 0
        nums.sort()
        for i in range(4):
            if nums[i] == 0: joker += 1
            elif nums[i] == nums[i + 1]: return False
        return nums[4] - nums[joker] < 5

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

            ret = Solution().isStraight2(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
