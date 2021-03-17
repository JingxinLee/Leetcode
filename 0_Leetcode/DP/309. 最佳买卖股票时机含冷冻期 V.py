# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:31 AM 3/5/21
### [309\. 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

Difficulty: **中等**


给定一个整数数组，其中第_i_个元素代表了第_i_天的股票价格 。

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

*   你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
*   卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

**示例:**

```
输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
```

"""
import json
from typing import List


class Solution0:
    def maxProfit(self, prices: List[int]) -> int:
        """
        T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
        T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k][0] - prices[i])

        如果要在第 i 天买入股票，第二个状态转移方程中就不能使用 T[i - 1][k][0]，而应该使用 T[i - 2][k][0]

        T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
        T[i][k][1] = max(T[i - 1][k][1], T[i - 2][k][0] - prices[i])
        """
        n = len(prices)
        if n == 0: return 0
        dp = [[0] * 2 for _ in range(n)] # k无穷大， 所以省略k这个维度
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        return dp[-1][0]


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
            prices = stringToIntegerList(line);

            ret = Solution().maxProfit(prices)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()