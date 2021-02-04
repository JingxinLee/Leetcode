# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:24 AM 1/27/21
### [15\. 三数之和](https://leetcode-cn.com/problems/3sum/)

Difficulty: **中等**


给你一个包含 `n` 个整数的数组`nums`，判断`nums`中是否存在三个元素 _a，b，c ，_使得_a + b + c =_ 0 ？请你找出所有和为 `0` 且不重复的三元组。

**注意：**答案中不可以包含重复的三元组。

**示例 1：**

```
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
```

**示例 2：**

```
输入：nums = []
输出：[]
```

**示例 3：**

```
输入：nums = [0]
输出：[]
```

**提示：**

*   `0 <= nums.length <= 3000`
*   `-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup>`

"""
import json
from typing import List


class Solution:
    def twoSum(self, nums, start, target):
        lo, hi = start, len(nums) - 1
        res = []
        while lo < hi:
            summ = nums[lo] + nums[hi]
            left, right = nums[lo], nums[hi]
            if summ < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
            elif summ > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left: lo += 1
                while lo < hi and nums[hi] == right: hi -= 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.threeSumTarget(nums, 0)

    def threeSumTarget(self, nums, target):
        nums.sort()
        n = len(nums)
        res = []
        i = 0
        while i < n:
            tuples = self.twoSum(nums, i + 1, target - nums[i])  # 找到满足条件的二元组
            for tuple in tuples:
                tuple.append(nums[i])  # 在上面二元组的基础上,加上nums[i] 就是结果三元组
                res.append(tuple)
            while i < n - 1 and nums[i] == nums[i + 1]:  # 保证让第一个数字不重复
                i += 1
            i += 1
        return res


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

            ret = Solution().threeSum(nums)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()