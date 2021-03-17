# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:11 AM 2/17/21
### [1143\. 最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)

Difficulty: **中等**


给定两个字符串`text1` 和`text2`，返回这两个字符串的最长公共子序列的长度。

一个字符串的_子序列_是指这样一个新的字符串：[ 它是由原字符串在不改变字符的[ 相对顺序 ]的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。]
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

**示例 1:**

```
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。
```

**示例 2:**

```
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。
```

**示例 3:**

```
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。
```

**提示:**

*   `1 <= text1.length <= 1000`
*   `1 <= text2.length <= 1000`
*   输入的字符串只含有小写英文字符。

"""
import json
from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # dp[i][j]的含义是：对于s1[1..i]和s2[1..j]，它们的 LCS 长度是dp[i][j]
        for i in range(1, m + 1): # 注意是 m + 1 和 n + 1
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]



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
            text1 = stringToString(line);
            line = next(lines)
            text2 = stringToString(line);

            ret = Solution().longestCommonSubsequence(text1, text2)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()