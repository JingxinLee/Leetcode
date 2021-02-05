# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 7:56 PM 1/27/21
### [18\. 四数之和](https://leetcode-cn.com/problems/4sum/)

Difficulty: **中等**


给定一个包含_n_ 个整数的数组`nums`和一个目标值`target`，判断`nums`中是否存在四个元素 _a，__b，c_和 _d_，
使得_a_ + _b_ + _c_ + _d_的值与`target`相等？找出所有满足条件且不重复的四元组。

**注意：**

答案中不可以包含重复的四元组。

**示例：**

```
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
import json
from typing import List


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """


def stringToIntegerList(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


def int2dArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line)
            line = next(lines)
            target = stringToInt(line)

            ret = Solution().fourSum(nums, target)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()