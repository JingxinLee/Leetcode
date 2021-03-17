# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:28 AM 3/5/21
### [121\. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

Difficulty: **简单**


给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天** 买入这只股票，并选择在 **未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

**示例 1：**

```
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```

**示例 2：**

```
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
```

**提示：**

*   `1 <= prices.length <= 10<sup>5</sup>`
*   `0 <= prices[i] <= 10<sup>4</sup>`

"""
import json
from typing import List
class Solution0:
    def maxProfit(self, prices: List[int]) -> int:
        """
        T[-1][k][0] = T[i][0][0] = 0 的含义： i = -1表示没有股票交易， k = 0 进行了0次交易
        T[-1][k][1] = T[i][0][1] = -Infinity 的含义是在没有进行股票交易时不允许持有股票， 进行0次交易也是不可能有股票的

        T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
        T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k - 1][0] - prices[i])
        本题 k = 1
        T[i][1][0] = max(T[i - 1][1][0], T[i - 1][1][1] + prices[i])
        T[i][1][1] = max(T[i - 1][1][1], T[i - 1][0][0] - prices[i]) = max(T[i - 1][1][1], -prices[i])  # T[i][0][0] = 0
        """
        n = len(prices)
        if n == 0: return 0
        dp = [[0] * 2 for _ in range(n)] # dp[i]][j]代表第i天结束时，持有j=0或1份股票，可以获得的最大收益。 这里没有用参数k， 因为 k 恒等于 1
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[n-1][0]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        profit0, profit1 = 0, -prices[0]
        for i in range(1, n):
            profit0 = max(profit0, profit1 + prices[i])
            profit1 = max(profit1, -prices[i])
        return profit0


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        dp = [0] * n
        minPrice = prices[0]
        for i in range(1, n):
            minPrice = min(minPrice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minPrice)
        return dp[-1]

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        res = 0
        minPrice = prices[0]
        for sell in range(1, n):
            minPrice = min(minPrice, prices[sell])
            res = max(res, prices[sell] - minPrice)
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
            prices = stringToIntegerList(line);

            ret = Solution().maxProfit(prices)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()