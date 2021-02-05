# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 9:22 AM 1/29/21
### [78\. 子集](https://leetcode-cn.com/problems/subsets/)

Difficulty: **中等**


给你一个整数数组`nums` ，数组中的元素 **互不相同** 。返回该数组所有可能的子集（幂集）。

解集 **不能** 包含重复的子集。你可以按 **任意顺序** 返回解集。

**示例 1：**

```
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**示例 2：**

```
输入：nums = [0]
输出：[[],[0]]
```

**提示：**

*   `1 <= nums.length <= 10`
*   `-10 <= nums[i] <= 10`
*   `nums` 中的所有元素 **互不相同**

https://leetcode-cn.com/problems/subsets/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-gao-/

“排列”问题使用 used 数组来标识选择列表，

而“子集、组合”问题则使用 start 参数。

"""
import json
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        track = []
        self.backtrack(nums, track, 0)
        return self.res

    def backtrack(self, nums, track, start):
        self.res.append(track[:])
        for i in range(start, len(nums)):
            track.append(nums[i])
            self.backtrack(nums, track, i + 1)
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

            ret = Solution().subsets(nums)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()