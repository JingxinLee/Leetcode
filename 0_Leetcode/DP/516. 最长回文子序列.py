# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 7:14 PM 2/23/21
### [516\. 最长回文子序列](https://leetcode-cn.com/problems/longest-palindromic-subsequence/)

Difficulty: **中等**


给定一个字符串 `s` ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 `s` 的最大长度为 `1000` 。

**示例 1:**
输入:

```
"bbbab"
```

输出:

```
4
```

一个可能的最长回文子序列为 "bbbb"。

**示例 2:**
输入:

```
"cbbd"
```

输出:

```
2
```

一个可能的最长回文子序列为 "bb"。

**提示：**

*   `1 <= s.length <= 1000`
*   `s` 只包含小写英文字母

"""
import json
from typing import List


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1, -1, -1): # 反着遍历保证正确的状态转移
            for j in range(i+1, n):
                if s[i] == s[j]:     # 如果它俩相等，那么 它俩 加上s[i+1..j-1]中的最长回文子序列就是s[i..j]的最长回文子序列
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]

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
            s = stringToString(line);

            ret = Solution().longestPalindromeSubseq(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()