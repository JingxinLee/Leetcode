# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:37 AM 2/17/21
### [583\. 两个字符串的删除操作](https://leetcode-cn.com/problems/delete-operation-for-two-strings/)

Difficulty: **中等**


给定两个单_word1_和_word2_，找到使得_word1_和_word2_相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

**示例：**

```
输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
```

**提示：**

1.  给定单词的长度不超过500。
2.  给定单词中的字符只含有小写字母。

"""
import json
from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word1), len(word2)

        def lcs(m, n):
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            return dp[-1][-1]

        num_lcs = lcs(m, n)
        return m - num_lcs + n - num_lcs


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