# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 9:11 AM 1/30/21
### [剑指 Offer 38\. 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)

Difficulty: **中等**


输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

**示例:**

```
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
```

**限制：**

`1 <= s 的长度 <= 8`

"""
import json
from typing import List

class Solution:
    def __init__(self) -> None:
        self.res = []

    def permutation(self, s: str) -> List[str]:
        track = []
        n = len(s)
        used = [False] * n
        l = list(s)
        l.sort()
        s = ''.join(l)
        self.backtrack(s, track, used, 0)
        return self.res

    def backtrack(self, s, track, used, depth):
        if depth == len(s):
            self.res.append(''.join(track[:]))
            return
        for i in range(len(s)):
            if used[i]:
                continue
            if i > 0 and s[i] == s[i-1] and not used[i-1]:
                continue

            track.append(s[i])
            used[i] = True

            self.backtrack(s, track, used, depth+1)

            used[i] = False
            track.pop()





def stringToString(input):
    return input[1:-1]


def stringArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line)

            ret = Solution().permutation(s)

            out = stringArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()