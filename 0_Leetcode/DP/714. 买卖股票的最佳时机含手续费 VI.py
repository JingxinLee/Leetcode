# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:31 AM 3/5/21
### [714\. 买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

Difficulty: **中等**


给定一个整数数组 `prices`，其中第 `i` 个元素代表了第 `i` 天的股票价格 ；非负整数 `fee` 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

**注意：**这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

**示例 1:**

```
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润:((8 - 1) - 2) + ((9 - 4) - 2) = 8.
```

**注意:**

*   `0 < prices.length <= 50000`.
*   `0 < prices[i] < 50000`.
*   `0 <= fee < 50000`.

"""
import json
from typing import List


class Solution0:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
        T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k][0] - prices[i])

        有2中表示方法：

        在每次买入股票时扣除手续费：
        T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
        T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k][0] - prices[i] - fee)

        在每次卖出股票时扣除手续费：
        T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i] - fee)
        T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k][0] - prices[i])

        """
        n = len(prices)
        if n == 0: return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0] - fee
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] )
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)

        # dp[0][0] = 0  # 卖出的时候有手续费
        # dp[0][1] = -prices[0] # 买入的时候没有手续费， 所以base不用减去fee
        # for i in range(1, n):
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee) # 卖出的时候有手续费， 第一次
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[-1][0]

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
        T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k][0] - prices[i])

        有2中表示方法：

        在每次买入股票时扣除手续费：
        T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
        T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k][0] - prices[i] - fee)

        在每次卖出股票时扣除手续费：
        T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i] - fee)
        T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k][0] - prices[i])

        """
        n = len(prices)
        if n == 0: return 0
        profit0, profit1 = 0, -prices[0]
        for i in range(1, n):
            profit0 = max(profit0, profit1 + prices[i] - fee)
            profit1 = max(profit1, profit0 - prices[i])


        return profit0


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
            line = next(lines)
            fee = int(line);

            ret = Solution().maxProfit(prices, fee)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()