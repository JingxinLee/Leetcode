# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:00 AM 2/17/21
### [72\. 编辑距离](https://leetcode-cn.com/problems/edit-distance/)

Difficulty: **困难**


给你两个单词`word1` 和`word2`，请你计算出将`word1`转换成`word2`所使用的最少操作数。

你可以对一个单词进行如下三种操作：

*   插入一个字符
*   删除一个字符
*   替换一个字符

**示例1：**

```
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
```

**示例2：**

```
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
```

**提示：**

*   `0 <= word1.length, word2.length <= 500`
*   `word1` 和 `word2` 由小写英文字母组成

"""
import json
from typing import List


class Solution0:
    def minDistance(self, word1: str, word2: str) -> int: # 递归版本，时间超时
        def dp(i, j):
            if i == -1: return j + 1
            if j == -1: return i + 1
            if word1[i] == word2[j]:
                return dp(i-1, j-1)
            else:
                return min(
                    dp(i, j-1) + 1, # 插入
                    dp(i-1, j) + 1, # 删除
                    dp(i-1, j-1) + 1 # 替换
                )
        return dp(len(word1)-1, len(word2)-1)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        dp[i][j] 表示：将 word1[0..i) 转换成为 word2[0..j) 的方案数。说明：由于要考虑空字符串，这里的下标 i 不包括 word[i]，同理下标 j 不包括 word[j]。
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 多开一行一列是为了保存边界条件，即字符长度为 0 的情况，这一点在字符串的动态规划问题中比较常见
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:  # 以第一个参数dp[1][1]来说，它表示的是word1[0,1) => word2[0,1) 即 word1[0] => word2[0]
                    dp[i][j] = dp[i - 1][j - 1]  # i=1,j=1时，dp[i-1][j-1]为dp[0][0], 它表示的是word1[0,0) => word2[0,0) 即 "" => "", 所以第一个字母相等的话，相当于两个空字符串再进行转化，

                else:
                    insert = dp[i][j - 1] + 1
                    delete = dp[i - 1][j] + 1
                    replace = dp[i - 1][j - 1] + 1
                    dp[i][j] = min(insert, delete, replace)
        return dp[m][n]


def stringToString(input):
    return input[1:-1].decode('string_escape')


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
            word1 = stringToString(line);
            line = next(lines)
            word2 = stringToString(line);

            ret = Solution().minDistance(word1, word2)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()