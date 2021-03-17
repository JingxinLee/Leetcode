# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:00 PM 2/15/21
### [485\. 最大连续1的个数](https://leetcode-cn.com/problems/max-consecutive-ones/)

Difficulty: **简单**


给定一个二进制数组， 计算其中最大连续1的个数。

**示例 1:**

```
输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
```

**注意：**

*   输入的数组只包含 `0` 和`1`。
*   输入数组的长度是正整数，且不超过 10,000。

"""
import json
from typing import List


class Solution0:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        if nums[0] == 1:
            dp[0] = 1
        else:
            dp[0] = 0

        for i in range(1, n):
            if nums[i] == 0:
                dp[i] = 0
            else:
                dp[i] = dp[i - 1] + 1
        return max(dp)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            if nums[i] == 1 and nums[i] == nums[i-1]:
                nums[i] = nums[i-1] + 1
        return max(nums)

def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);

            ret = Solution().findMaxConsecutiveOnes(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()