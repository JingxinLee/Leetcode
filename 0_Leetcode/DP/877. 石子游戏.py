# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:02 PM 3/2/21
### [877\. 石子游戏](https://leetcode-cn.com/problems/stone-game/)

Difficulty: **中等**


亚历克斯和李用几堆石子在做游戏。偶数堆石子**排成一行**，每堆都有正整数颗石子`piles[i]`。

游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。

亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。

假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回`true`，当李赢得比赛时返回`false`。

**示例：**

```
输入：[5,3,4,5]
输出：true
解释：
亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。
```

**提示：**

1.  `2 <= piles.length <= 500`
2.  `piles.length` 是偶数。
3.  `1 <= piles[i] <= 500`
4.  `sum(piles)`是奇数。

https://leetcode-cn.com/problems/stone-game/solution/shi-zi-you-xi-by-leetcode-solution/
```
"""
import json
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        dp[i][j].first 与 dp[i][j].second分别表示 先手 和 后手 的总石子数，
        第一个人拿了i，剩下的i+1到j他就是后手了，所以第一个人总数为piles[i] + dp[i+1][j].second。 另一个人在i+1到j就是先手了，所以是dp[i+1][j].first
        dp[i][j].first - dp[i][j].second = Math.max(piles[i] + dp[i+1][j].second - dp[i+1][j].first, piles[j] + dp[i][j-1].second - dp[i][j-1].first) ;
                                          = Math.max(piles[i] - (dp[i+1][j].first - dp[i+1][j].second), piles[j] - (dp[i][j-1].first - dp[i][j-1].second))
                                          = Math.max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        """
        length = len(piles)
        dp = [[0] * length for _ in range(length)]
        for i, pile in enumerate(piles):
            dp[i][i] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][length - 1] > 0


class Solution1:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        dp[i][j].first 与 dp[i][j].second分别表示先手和后手的总石子数，
        dp[i][j].first - dp[i][j].second = Math.max(piles[i] + dp[i+1][j].second - dp[i+1][j].first, piles[j] + dp[i][j-1].second - dp[i][j-1].first) ;
                                          = Math.max(piles[i] - (dp[i+1][j].first - dp[i+1][j].second), piles[j] - (dp[i][j-1].first - dp[i][j-1].second))
                                          = Math.max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
       dp[i][j] 的值只和dp[i+1][j] 与 dp[i][j−1] 有关，即在计算 dp 的第 i 行的值时，只需要使用到 dp 的第 i 行和第 i+1行的值，因此可以使用一维数组代替二维数组，对空间进行优化。
        """

        length = len(piles)
        dp = [0] * length
        for i, pile in enumerate(piles):
            dp[i] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[length - 1] > 0


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
            piles = stringToIntegerList(line);

            ret = Solution().stoneGame(piles)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()