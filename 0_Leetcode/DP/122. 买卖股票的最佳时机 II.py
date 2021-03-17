# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:28 AM 3/5/21
### [122\. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

Difficulty: **简单**


给定一个数组，它的第 _i_ 个元素是一支给定股票第 _i_ 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

**注意：**你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

**示例 1:**

```
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
```

**示例 2:**

```
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
    因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
```

**示例3:**

```
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

**提示：**

*   `1 <= prices.length <= 3 * 10 ^ 4`
*   `0 <= prices[i]<= 10 ^ 4`

    点睛之笔： 既然交易次数没有限制，为什么还要考虑 k？你还想让 k 最大取多少啊？  k 是最大的交易次数

如果 k 为正无穷，则 k 和 k - 1 可以看成是相同的，因此有 T[i - 1][k - 1][0] = T[i - 1][k][0] 和 T[i - 1][k - 1][1] = T[i - 1][k][1]。
每天仍有两个未知变量：T[i][k][0] 和 T[i][k][1]，其中 k 为正无穷，状态转移方程如下：
    T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
    T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k - 1][0] - prices[i]) = max(T[i - 1][k][1], T[i - 1][k][0] - prices[i])  # T[i - 1][k - 1][0] = T[i - 1][k][0]


"""
import json
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n-1][0]

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        profit0, profit1 = 0, -prices[0]
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
            prices = stringToIntegerList(line);

            ret = Solution().maxProfit(prices)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()