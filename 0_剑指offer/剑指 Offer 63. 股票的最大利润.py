# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:00 PM 7/28/20

假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

前i日最大利润=max(前(i−1)日最大利润,第i日价格−前i日最低价格) dp[i]=max(dp[i−1],prices[i]−min(prices[0:i]))

降低时间复杂度： 前 i 日的最低价格 min(prices[0:i]) 时间复杂度为 O(i) 。而在遍历 prices时，可以借助一个变量（记为成本 cost）每日更新最低价格。
优化后的转移方程为： dp[i]=max(dp[i−1],prices[i]−min(cost,prices[i])

降低空间复杂度：由于 dp[i]只与dp[i−1], prices[i], cost相关，因此可使用一个变量（记为利润 profit）代替 dp列表。
优化后的转移方程为： profit=max(profit,prices[i]−min(cost,prices[i])

"""
import json
from types import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, cost = 0, float("+inf")
        for price in prices:
            cost = min(cost, price)
            #profit = max(profit, price - min(cost, price))
            profit = max(profit, price - cost)
        return profit


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        with open('stdin.txt') as f:
            for line in f:
                yield line.strip(('\n'))

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