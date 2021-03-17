# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 4:43 PM 2/12/21
### [322\. 零钱兑换](https://leetcode-cn.com/problems/coin-change/)

Difficulty: **中等**


给定不同面额的硬币 `coins` 和一个总金额 `amount`。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回`-1`。

你可以认为每种硬币的数量是无限的。

**示例1：**

```
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
```

**示例 2：**

```
输入：coins = [2], amount = 3
输出：-1
```

**示例 3：**

```
输入：coins = [1], amount = 0
输出：0
```

**示例 4：**

```
输入：coins = [1], amount = 1
输出：1
```

**示例 5：**

```
输入：coins = [1], amount = 2
输出：2
```

**提示：**

*   `1 <= coins.length <= 12`
*   `1 <= coins[i] <= 2<sup>31</sup> - 1`
*   `0 <= amount <= 10<sup>4</sup>`

"""
import json
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


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
            coins = stringToIntegerList(line);
            line = next(lines)
            amount = int(line);

            ret = Solution().coinChange(coins, amount)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()