# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 8:41 PM 2/23/21
### [53\. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)

Difficulty: **简单**


给定一个整数数组 `nums` ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

**示例 1：**

```
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
```

**示例 2：**

```
输入：nums = [1]
输出：1
```

**示例 3：**

```
输入：nums = [0]
输出：0
```

**示例 4：**

```
输入：nums = [-1]
输出：-1
```

**示例 5：**

```
输入：nums = [-100000]
输出：-100000
```

**提示：**

*   `1 <= nums.length <= 3 * 10<sup>4</sup>`
*   `-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup>`

**进阶：**如果你已经实现复杂度为 `O(n)` 的解法，尝试使用更为精妙的 **分治法** 求解。

"""
import json
from typing import List
class Solution0: # DP
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        dp = [nums[0]] * n
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)

class Solution: # DP优化空间
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        dp0 = nums[0]
        dp1 = 0
        res = dp0
        for i in range(1, n):
            dp1 = max(nums[i], nums[i] + dp0)
            dp0 = dp1
            res = max(res, dp1)
        return res


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

            ret = Solution().maxSubArray(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()