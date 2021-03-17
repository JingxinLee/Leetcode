# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:30 AM 3/5/21
### [188\. 买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)

Difficulty: **困难**


给定一个整数数组 `prices` ，它的第`i` 个元素 `prices[i]` 是一支给定的股票在第 `i`天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 **k** 笔交易。

**注意：**你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

**示例 1：**

```
输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
```

**示例 2：**

```
输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
```

**提示：**

*   `0 <= k <= 100`
*   `0 <= prices.length <= 1000`
*   `0 <= prices[i] <= 1000`

   https://leetcode-cn.com/circle/article/qiAgHn/

T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])

    T[i - 1][k][0] 是休息操作可以得到的最大收益，
    T[i - 1][k][1] + prices[i] 是卖出操作可以得到的最大收益。
    注意到允许的最大交易次数是不变的，因为每次交易包含两次成对的操作，买入和卖出。

    确切地说是一次交易包含一次买入和一次卖出，因此只要在两种操作之一更新交易次数。文中使用的是买入操作时更新交易次数，这里也就是说
    卖出操作不会增加交易次数，是因为它前面已经有买入操作了。买入和卖出是一次交易，只有卖出不算一次交易。 只有买入一次，才会后面对应卖出，交易次数才会改变。

    也可以有另一种实现，即卖出操作时更新交易次数。


T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k - 1][0] - prices[i])
    T[i][k][1]，第 i 天进行的操作只能是休息或买入，因为在第 i 天结束时持有的股票数量是 1。
    T[i - 1][k][1] 是休息操作可以得到的最大收益，
    T[i - 1][k - 1][0] - prices[i] 是买入操作可以得到的最大收益。
    注意到允许的最大交易次数减少了一次，因为每次买入操作会使用一次交易。


"""
import json
from typing import List


class Solution0:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        if k >= n // 2:
            return self.maxProfitInfK(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)] # k + 1 储存从 0 到 k
        for i in range(1, k+1): # base 第0天
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]

        for i in range(1, n):
            for j in range(k, 0, -1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        return dp[n-1][k][0]

    def maxProfitInfK(self, prices):
        n = len(prices)
        if n == 0: return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n-1][0]

class Solution: # 第 i 天的最大收益只和第 i - 1 天的最大收益相关，空间复杂度可以降到 O(k)O(k)
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        if k >= n // 2:
            return self.maxProfitInfK(prices)
        dp = [[0] * 2 for _ in range(k + 1)]
        for i in range(1, k+1): # base 第0天
            dp[i][0] = 0
            dp[i][1] = -prices[0]

        for i in range(1, n):
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                dp[j][1] = max(dp[j][1], dp[j-1][0] - prices[i])

        return dp[k][0]

    def maxProfitInfK(self, prices):
        n = len(prices)
        if n == 0: return 0
        profit0 = 0
        profit1 = -prices[0]
        for i in range(1, n):
            profit0 = max(profit0, profit1 + prices[i])
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
            k = int(line);
            line = next(lines)
            prices = stringToIntegerList(line);

            ret = Solution().maxProfit(k, prices)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()