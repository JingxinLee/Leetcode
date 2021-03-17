# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:44 AM 2/17/21
### [712\. 两个字符串的最小ASCII删除和](https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/)

Difficulty: **中等**


给定两个字符串`s1, s2`，找到使两个字符串相等所需删除字符的ASCII值的最小和。

**示例 1:**

```
输入: s1 = "sea", s2 = "eat"
输出: 231
解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
在 "eat" 中删除 "t" 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
```

**示例2:**

```
输入: s1 = "delete", s2 = "leet"
输出: 403
解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
```

**注意:**

*   `0 < s1.length, s2.length <= 1000`。
*   所有字符串中的字符ASCII值在`[97, 122]`之间。

https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/solution/liang-ge-zi-fu-chuan-de-zui-xiao-asciishan-chu-he-/

https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/solution/712-liang-ge-zi-fu-chuan-de-zui-xiao-asc-j9g1/
"""
import json
from typing import List


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        dp[i][j] 表示 字符串 s1[i:] 和 s2[j:]    （s1[i:] 表示字符串 s1 从第 i 位到末尾的子串，s2[j:] 表示字符串 s2 从第 j 位到末尾的子串，字符串下标从 0 开始）
        达到相等所需删除的字符的 ASCII 值的最小和.
        最终的答案为 dp[0][0]
        """
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):  # 当 s1[i:] 和 s2[j:] 中的某一个字符串为空时，dp[i][j] 的值即为另一个非空字符串的所有字符的 ASCII 值之和
            dp[i][n] = dp[i + 1][n] + ord(s1[i])
        for j in range(n - 1, -1, -1):
            dp[m][j] = dp[m][j + 1] + ord(s2[j])

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:  # 不需要删除 也就不用加上删除字符的ASCII值
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i + 1][j] + ord(s1[i]), dp[i][j + 1] + ord(s2[j]))
        return dp[0][0]


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
            s1 = stringToString(line);
            line = next(lines)
            s2 = stringToString(line);

            ret = Solution().minimumDeleteSum(s1, s2)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()