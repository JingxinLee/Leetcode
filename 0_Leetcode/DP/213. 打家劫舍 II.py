# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 4:03 PM 3/7/21
### [213\. 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/)

Difficulty: **中等**


你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 **围成一圈** ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，**如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警** 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 **在不触动警报装置的情况下** ，能够偷窃到的最高金额。

**示例 1：**

```
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
```

**示例 2：**

```
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
```

**示例 3：**

```
输入：nums = [0]
输出：0
```

**提示：**

*   `1 <= nums.length <= 100`
*   `0 <= nums[i] <= 1000`

"""
import json
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        def dp(nums, start, end):  # 仅计算闭区间 [start,end] 的最优结果
            dp_i_1, dp_i_2 = 0, 0
            dp_i = 0
            for i in range(end, start - 1, -1):
                dp_i = max(dp_i_1, nums[i] + dp_i_2)
                dp_i_2 = dp_i_1
                dp_i_1 = dp_i
            return dp_i

        return max(dp(nums, 0, n - 2), dp(nums, 1, n - 1))


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