# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:29 AM 3/5/21
### [123\. 买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)

Difficulty: **困难**


给定一个数组，它的第`i` 个元素是一支给定的股票在第 `i`天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成**两笔**交易。

**注意：**你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

**示例1:**

```
输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
    随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
```

**示例 2：**

```
输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
    因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
```

**示例 3：**

```
输入：prices = [7,6,4,3,1]
输出：0
解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
```

**示例 4：**

```
输入：prices = [1]
输出：0
```

**提示：**

*   `1 <=prices.length <= 10^5
*   `0 <=prices[i] <= 10^5


"""
import json
from typing import List


class Solution0:
    def maxProfit(self, prices: List[int]) -> int:
        """
        T[i][2][0] = max(T[i - 1][2][0], T[i - 1][2][1] + prices[i])
        T[i][2][1] = max(T[i - 1][2][1], T[i - 1][1][0] - prices[i])
        T[i][1][0] = max(T[i - 1][1][0], T[i - 1][1][1] + prices[i])
        T[i][1][1] = max(T[i - 1][1][1], T[i - 1][0][0] - prices[i]) = max(T[i - 1][1][1], -prices[i])   # T[i][0][0] = 0
        """
        n = len(prices)
        if n == 0: return 0
        # dp = [[[0] * 2] * 3 for _ in range(n)] # 这种是浅拷贝， 不行
        dp = [[[0] * 2 for _ in range(3)] for _ in range(n)] # # 最大是2笔交易，所以 k设置3个 储存 0 1 2
        dp[0][1][0] = 0
        dp[0][1][1] = -prices[0]
        dp[0][2][0] = 0
        dp[0][2][1] = -prices[0]
        for i in range(1, n):
            dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i])
            dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][0] - prices[i])
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i])
        return dp[n - 1][2][0]


class Solution: # 注意到第 i 天的最大收益只和第 i - 1 天的最大收益相关，空间复杂度可以降到 O(1)O(1)
    def maxProfit(self, prices: List[int]) -> int:
        """
        T[i][1][1] = max(T[i - 1][1][1], T[i - 1][0][0] - prices[i]) = max(T[i - 1][1][1], -prices[i])   # T[i][0][0] = 0
        T[i][1][0] = max(T[i - 1][1][0], T[i - 1][1][1] + prices[i])
        T[i][2][1] = max(T[i - 1][2][1], T[i - 1][1][0] - prices[i]) #
        T[i][2][0] = max(T[i - 1][2][0], T[i - 1][2][1] + prices[i])
        """
        n = len(prices)
        if n == 0: return 0
        profitOne0, profitOne1, profitTwo0, profitTwo1 = 0, -prices[0], 0, -prices[0]    # 第一个维度 i 舍弃，  One Two 代表第二个维度， 0 1 代表第三个维度
        for i in range(1, n):
            profitOne1 = max(profitOne1, -prices[i])
            profitOne0 = max(profitOne0, profitOne1 + prices[i])
            profitTwo1 = max(profitTwo1, profitOne0 - prices[i])  # 注意 这里是 profitOne0 - prices[i]
            profitTwo0 = max(profitTwo0, profitTwo1 + prices[i])

        return profitTwo0
# [3,3,5,0,0,3,1,4]
#
# [[[0,0],[0,-3],[0,-3]],
#  [[0,0],[0,-3],[0,-3]],
#  [[0,0],[2,-3],[2,-3]],
#  [[0,0],[2,0],[2,2]],
#  [[0,0],[2,0],[2,2]],
#  [[0,0],[3,0],[5,2]],
#  [[0,0],[3,0],[5,2]],
#  [[0,0],[4,0],[6,2]]]
#
# [[[0, -3], [0, -3], [0, -3]],
#  [[0, -3], [0, -3], [0, -3]],
#  [[2, -3], [2, -3], [2, -3]],
#  [[2, 2], [2, 2], [2, 2]],
#  [[2, 2], [2, 2], [2, 2]],
#  [[5, 2], [5, 2], [5, 2]],
#  [[5, 4], [5, 4], [5, 4]],
#  [[8, 4], [8, 4], [8, 4]]]


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