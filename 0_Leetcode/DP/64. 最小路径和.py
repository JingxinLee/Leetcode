# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 1:11 PM 2/27/21
### [64\. 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)

Difficulty: **中等**


给定一个包含非负整数的 `m x n`网格`grid` ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

**说明：**每次只能向下或者向右移动一步。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)

```
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
```

**示例 2：**

```
输入：grid = [[1,2,3],[4,5,6]]
输出：12
```

**提示：**

*   `m == grid.length`
*   `n == grid[i].length`
*   `1 <= m, n <= 200`
*   `0 <= grid[i][j] <= 100`

"""
import json
from typing import List


class Solution: # 自顶向下 O(MN）
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dp(grid, i, j):
            if i == 0 and j == 0: return grid[0][0]  # base case
            if i < 0 or j < 0: return float('inf')
            if memo[i][j] != -1: return memo[i][j]  # 避免重复计算
            memo[i][j] = min(dp(grid, i - 1, j), dp(grid, i, j - 1)) + grid[i][
                j]  # dp(grid, i, j)的值取决于dp(grid, i - 1, j)和dp(grid, i, j - 1)返回的值。 将计算结果记入备忘录
            return memo[i][j]

        m, n = len(grid), len(grid[0])
        memo = [[-1] * n for _ in range(m)]
        return dp(grid, m - 1, n - 1)


class Solution2: # 自底向上 O(MN)
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]  # 那如果i或者j等于 0 的时候，就会出现索引越界的错误。 所以我们需要提前计算出dp[0][..]和dp[..][0]，然后让i和j的值从 1 开始迭代
        return dp[m - 1][n - 1]

def stringToInt2dArray(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            grid = stringToInt2dArray(line)

            ret = Solution().minPathSum(grid)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
