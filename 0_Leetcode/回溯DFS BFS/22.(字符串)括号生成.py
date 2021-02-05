# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:34 PM 1/31/21
### [22\. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)

Difficulty: **中等**


数字 `n`代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 **有效的** 括号组合。

**示例 1：**

```
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
```

**示例 2：**

```
输入：n = 1
输出：["()"]
```

**提示：**

*   `1 <= n <= 8`

"""
import json
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        track = ""
        self.dfs(track, n, n)
        return self.res

    def dfs(self, track, left, right):
        if left == 0 and right == 0:
            self.res.append(track)
            return
        if left > right:
            return

        if left > 0:
            self.dfs(track + '(', left - 1, right)
        if right > 0:
            self.dfs(track + ')', left, right - 1)

def stringToInt(input):
    return int(input)


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
            n = stringToInt(line)

            ret = Solution().generateParenthesis(n)

            out = stringArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()