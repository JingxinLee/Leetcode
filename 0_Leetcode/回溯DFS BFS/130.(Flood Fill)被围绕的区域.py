# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:32 PM 1/31/21
### [130\. 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)

Difficulty: **中等**


给定一个二维的矩阵，包含`'X'`和`'O'`（**字母 O**）。

找到所有被 `'X'` 围绕的区域，并将这些区域里所有的`'O'` 用 `'X'` 填充。

**示例:**

```
X X X X
X O O X
X X O X
X O X X
```

运行你的函数后，矩阵变为：

```
X X X X
X X X X
X X X X
X O X X
```

**解释:**

被围绕的区间不会存在于边界上，换句话说，任何边界上的`'O'`都不会被填充为`'X'`。
任何不在边界上，或不与边界上的`'O'`相连的`'O'`最终都会被填充为`'X'`。
如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。


"""
import json
from typing import List


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """


def stringToChar2dArray(input):
    return json.loads(input)


def char2dArrayToString(input):
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
            board = stringToChar2dArray(line)

            ret = Solution().solve(board)

            out = char2dArrayToString(board)
            if ret is not None:
                print("Do not return anything, modify board in-place instead.")
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()