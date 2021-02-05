# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:32 PM 1/31/21
### [79\. 单词搜索](https://leetcode-cn.com/problems/word-search/)

Difficulty: **中等**


给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

**示例:**

```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
```

**提示：**

*   `board` 和 `word` 中只包含大写和小写英文字母。
*   `1 <= board.length <= 200`
*   `1 <= board[i].length <= 200`
*   `1 <= word.length <= 10^3`

https://leetcode-cn.com/problems/word-search/solution/shou-hua-tu-jie-79-dan-ci-sou-suo-dfs-si-lu-de-cha/

"""
import json
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        used = [[False] * n for _ in range(m)]
        def dfs(row, col, i): # 判断当前点是否是目标路径上的点. row col 当前点的坐标，i当前考察的word字符索引
            if i == len(word): # i 递归结束条件 : 找到了单词的最后一个
                return True
            if row < 0 or row >= m or col < 0 or col >= n: # 越界
                return False
            if used[row][col] or board[row][col] != word[i]:# 已经访问过,或者不是word里的字母
                return False
            # 排除掉上面的false情况，当前点是合格的，可以继续递归考察
            used[row][col] = True #  记录一下当前点被访问了
            if dfs(row+1, col, i+1) or dfs(row-1, col, i+1) or dfs(row, col+1, i+1) or dfs(row, col-1, i+1): # 基于当前点[row,col]，可以为剩下的字符找到路径
                return True
            used[row][col] = False # 不能为剩下字符找到路径，返回false，撤销当前点的访问状态，继续考察别的分支
            return False


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False

class Solution2:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        used = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    used[i][j] = 1
                    if self.backtrack(board, word[1:], used, i, j):
                        return True
                    used[i][j] = 0
        return False

    def backtrack(self, board, word, used, i, j):
        if len(word) == 0: # word长度做递归结束调价条件
            return True

        for direction in self.directions:
            cur_i = i + direction[0]
            cur_j = j + direction[1]

            if cur_i > 0 and cur_i < len(board) and cur_j > 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]: # 要与首字母想等
                if used[cur_i][cur_j] == 1:
                    continue
                used[cur_i][cur_j] = 1
                if self.backtrack(board, word[1:], used, cur_i, cur_j) == True:
                    return True
                used[cur_i][cur_j] = 0
        return False



def stringToChar2dArray(input):
    return json.loads(input)


def stringToString(input):
    return input[1:-1]

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
            line = next(lines)
            word = stringToString(line)

            ret = Solution().exist(board, word)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()