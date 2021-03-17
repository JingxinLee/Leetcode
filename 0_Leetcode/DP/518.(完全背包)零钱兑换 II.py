# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 9:55 PM 2/25/21
### [518\. 零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2/)

Difficulty: **中等**


给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。

**示例 1:**

```
输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

**示例 2:**

```
输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
```

**示例 3:**

```
输入: amount = 10, coins = [10]
输出: 1
```

**注意****:**

你可以假设：

*   0 <= amount (总金额) <= 5000
*   1 <= coin (硬币面额) <= 5000
*   硬币种类不超过 500 种
*   结果符合 32 位符号整数

"""
import json
from typing import List

class Solution0:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n +1)] # 若只使用前i个物品，当背包容量为j时，有dp[i][j]种方法可以装满背包
        for i in range(n+1): # 如果凑出的目标金额为 0，那么“无为而治”就是唯一的一种凑法 <=> 凑出总金额为0 元， 就有1种方法，那就是0个硬币
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j >= coins[i-1]: # 背包大， 可以装 也可以不装，
                    # dp[i][j-coins[i-1]]也不难理解，如果你决定使用这个面值的硬币，那么就应该关注如何凑出金额j - coins[i-1]。
                    # 比如说，你想用面值为 2 的硬币凑出金额 5，那么如果你知道了凑出金额 3 的方法，再加上一枚面额为 2 的硬币，不就可以凑出 5 了嘛。
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount]


class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        if n == 0:
            if amount == 0:
                return 1
            else:
                return 0

        dp = [[0] * (amount + 1) for _ in range(n)]  # dp[i][j]：硬币列表的前缀子区间 [0, i] 能够凑成总金额为 j 的组合数
        for i in range(n):  # 凑出总金额为0 元， 就有1种方法，那就是0个硬币
            dp[i][0] = 1
        for i in range(coins[0], amount + 1, coins[0]):  # 第 1 行只考虑第 1 枚硬币 coins[0]，能够组合出的容量只有 coins[0] 的整数倍数 coins[0] 2coins[0] 都是 1 + 1 + 1 这1种形式凑成
            dp[0][i] = 1

        for i in range(1, n):
            for j in range(amount + 1):
                if j - coins[i] >= 0:
                    # 把这第i个物品装入了背包，也就是说你使用coins[i]这个面值的硬币，那么dp[i][j]应该等于dp[i][j-coins[i-1]]
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]  # 你想用面值为 2 的硬币凑出金额 5，那么如果你知道了凑出金额 3 的方法，再加上一枚面额为 2 的硬币，不就可以凑出 5 了嘛
                else:
                    dp[i][j] = dp[i - 1][j]  # 不把这第i个物品装入背包
        return dp[n - 1][amount]

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1  # base case
        for i in range(n):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    dp[j] += dp[j - coins[i]]
        return dp[amount]


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
            amount = int(line);
            line = next(lines)
            coins = stringToIntegerList(line);

            ret = Solution().change(amount, coins)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()