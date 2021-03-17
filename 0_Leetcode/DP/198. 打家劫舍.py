# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:17 AM 3/7/21
### [198\. 打家劫舍](https://leetcode-cn.com/problems/house-robber/)

Difficulty: **中等**


你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，**如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警**。

给定一个代表每个房屋存放金额的非负整数数组，计算你 **不触动警报装置的情况下** ，一夜之内能够偷窃到的最高金额。

**示例 1：**

```
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
    偷窃到的最高金额 = 1 + 3 = 4 。
```

**示例 2：**

```
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
    偷窃到的最高金额 = 2 + 9 + 1 = 12 。
```

**提示：**

*   `0 <= nums.length <= 100`
*   `0 <= nums[i] <= 400`

"""
import json
from typing import List


class Solution0:  # 自顶向下 带备忘录
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        def dp(nums, start): # 返回 nums[start..] 能抢到的最大值
            if start >= n:
                return 0
            if memo[start] != -1:
                return memo[start]
            res = max(dp(nums, start +1), nums[start] + dp(nums, start + 2))
            memo[start] = res
            return res
        return dp(nums, 0)

class Solution1:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n +2) # 总共有n个，最后一个是第 n - 1， 还要考虑最后一个的下一次 也就是 n-1+2 = n+1， 所以总共n+1次 也就是n+2个
        for i in range(n-1, -1, -1): # 倒叙 从 n-1开始，一直到第0个
            dp[i] = max(dp[i+1], nums[i] + dp[i+2]) # 2 种情况： 不抢第i个从第i+1个开始抢， 或者 抢劫第i个，那么下一个就得从i+2开始抢
        return dp[0]

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # 状态转移只和dp[i]最近的两个状态有关，所以可以进一步优化，将空间复杂度降低到 O(1)
        dp_i_1, dp_i_2 = 0, 0
        dp_i = 0
        for i in range(n-1, -1, -1):
            dp_i = max(dp_i_1, nums[i] + dp_i_2)
            dp_i_2 = dp_i_1 # 往前移动一个
            dp_i_1 = dp_i   # 往前移动一个
        return dp_i

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

            ret = Solution().rob(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()