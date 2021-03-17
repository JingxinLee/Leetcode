# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 4:44 PM 3/1/21
### [312\. 戳气球](https://leetcode-cn.com/problems/burst-balloons/)

Difficulty: **困难**


有 `n` 个气球，编号为`0` 到 `n - 1`，每个气球上都标有一个数字，这些数字存在数组 `nums` 中。

现在要求你戳破所有的气球。戳破第 `i` 个气球，你可以获得 `nums[i - 1] * nums[i] * nums[i + 1]` 枚硬币。 这里的 `i - 1` 和 `i + 1` 代表和 `i` 相邻的两个气球的序号。如果 `i - 1`或 `i + 1` 超出了数组的边界，那么就当它是一个数字为 `1` 的气球。

求所能获得硬币的最大数量。

**示例 1：**

```
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
```

**示例 2：**

```
输入：nums = [1,5]
输出：10
```

**提示：**

*   `n == nums.length`
*   `1 <= n <= 500`
*   `0 <= nums[i] <= 100`

https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247485172&idx=1&sn=b860476b205b04f960ea0de6f70d3553&chksm=9bd7f8fcaca071eaeb934ae5573e550699f95e0491c89bafa1c298b852b1f6fc19796ab7ef84&scene=21#wechat_redirect

"""
import json
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        points = [0] * (n + 2)
        points[0] = points[-1] = 1
        for i in range(1, n + 1):
            points[i] = nums[i - 1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]  # dp[i][j] = x表示，[戳破] 气球i和气球j之间（开区间，不包括i和j）的所有气球，可以获得的最高分数为x
        for i in range(n, -1, -1):  # i 应该从下往上
            for j in range(i + 1, n + 2):  # j 应该从左往右
                for k in range(i + 1, j):  # 最后戳破的气球是哪个？  （其中i < k < j）
                    # 在计算dp[i][j]时，dp[i][k] 和 dp[k][j]已经被计算出来了  （其中i < k < j）
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + points[i] * points[k] * points[j])  # 那得先把开区间(i, k)的气球都戳破，再把开区间(k, j)的气球都戳破；最后剩下的气球k，相邻的就是气球i和气球j

        return dp[0][n + 1]


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

            ret = Solution().maxCoins(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()