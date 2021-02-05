# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 3:52 PM 1/29/21
### [90\. 子集 II](https://leetcode-cn.com/problems/subsets-ii/)

Difficulty: **中等**


给定一个可能包含重复元素的整数数组 _**nums**_，返回该数组所有可能的子集（幂集）。

**说明：**解集不能包含重复的子集。

**示例:**

```
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```
"""
import json
from typing import List


class Solution(object):
    def __init__(self):
        self.res = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        nums.sort()
        track = []
        self.backtrack(nums, track, 0)
        return self.res

    def backtrack(self, nums, track, start):
        self.res.append(track[:])
        for i in range(start, len(nums)):
            # 去除当前选择列表中，与上一个数重复的那个数，引出的分支
            # 当i>start成立时，说明当前列表最少有两个数，做选择的之前，比较一下当前数，与上一个数 (i-1) 是不是相同，相同则 continue,
            if i > start and nums[i] == nums[i-1]:
                continue
            track.append(nums[i])
            self.backtrack(nums, track, i+1)
            track.pop()




def stringToIntegerList(input):
    return json.loads(input)


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

            ret = Solution().subsetsWithDup(nums)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()