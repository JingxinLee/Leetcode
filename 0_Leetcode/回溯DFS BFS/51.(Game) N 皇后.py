# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:44 PM 1/28/21
### [51\. N 皇后](https://leetcode-cn.com/problems/n-queens/)

Difficulty: ** 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。   示例 1： 输入：n = 4 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]] 解释：如上图所示，4 皇后问题存在两个不同的解法。 示例 2： 输入：n = 1 输出：[["Q"]]   提示： 1 <= n <= 9 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。 **


**n 皇后问题** 研究的是如何将 `n` 个皇后放置在 `n×n` 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 `n` ，返回所有不同的 **n皇后问题** 的解决方案。


每一种解法包含一个不同的 **n 皇后问题** 的棋子放置方案，该方案中 `'Q'` 和 `'.'` 分别代表了皇后和空位。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

```
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
```

**示例 2：**

```
输入：n = 1
输出：[["Q"]]
```

**提示：**

*   `1 <= n <= 9`
*   皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
https://leetcode-cn.com/problems/n-queens/solution/gen-ju-di-46-ti-quan-pai-lie-de-hui-su-suan-fa-si-/
https://leetcode-cn.com/problems/n-queens/solution/shou-hua-tu-jie-cong-jing-dian-de-nhuang-hou-wen-t/
"""
import json
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        trace = ['.' * n] * n
        self.backtrack(trace, 0)
        return self.res

    def backtrack(self, trace: List[str], row: int):
        if row == len(trace): # len(trace)是一个固定值, row 是从0 加到它为止
            ret = list(trace)
            self.res.append(ret)
            return
        for col in range(len(trace[0])):
            # 排除不合法选择
            if not self.isValid(trace, row, col):
                continue
            # 做选择
            trace[row] = self.replaceChar(trace[row], col, 'Q')
            # 进入下一行决策
            self.backtrack(trace, row + 1)
            # 撤销选择
            trace[row] = self.replaceChar(trace[row], col, '.')

    def isValid(self, trace, row, col): # 因为是逐行回溯,所以只能看上面的行, 下面的行还没做看不了. 所以检查 左上和右上.
        n = len(trace)
        # 判断当前列有没有皇后,因为他是一行一行往下走的，我们只需要检查走过的行数即可，
        # 通俗一点就是判断当前坐标位置的上面有没有皇后
        for i in range(n):
            if trace[i][col] == 'Q':
                return False
        # 检查左上
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if trace[i][j] == 'Q':
                return False
        # 检查右上
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if trace[i][j] == 'Q':
                return False
        return True

    def replaceChar(self, string: str, idx: int, char: str) -> str:
        strList = list(string)
        strList[idx] = char
        s = ''.join(strList)
        return s



def stringToInt(input):
    return int(input)


def string2dArrayToString(input):
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

            ret = Solution().solveNQueens(n)

            out = string2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()