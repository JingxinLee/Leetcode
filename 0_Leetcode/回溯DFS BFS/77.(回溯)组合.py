# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:31 PM 1/29/21
### [77\. 组合](https://leetcode-cn.com/problems/combinations/)

Difficulty: **中等**


给定两个整数 _n_ 和 _k_，返回 1 ... _n_ 中所有可能的 _k_ 个数的组合。

**示例:**

```
输入:n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```
n = 5, k = 3 如下:
递归之前 => [1]
                递归之前 => [1, 2]
                                    递归之前 => [1, 2, 3]
                递归之后 => [1, 2]
                                    递归之前 => [1, 2, 4]
                递归之后 => [1, 2]
                                    递归之前 => [1, 2, 5]
                递归之后 => [1, 2]
递归之后 => [1]
                递归之前 => [1, 3]
                                    递归之前 => [1, 3, 4]
                递归之后 => [1, 3]
                                    递归之前 => [1, 3, 5]
                递归之后 => [1, 3]
递归之后 => [1]
                递归之前 => [1, 4]
                                    递归之前 => [1, 4, 5]
                递归之后 => [1, 4]
递归之后 => [1]
                递归之前 => [1, 5]

递归之后 => [1]

递归之后 => []  -------------------------------------------

递归之前 => [2]
                递归之前 => [2, 3]
                                    递归之前 => [2, 3, 4]
                递归之后 => [2, 3]
                                    递归之前 => [2, 3, 5]
                递归之后 => [2, 3]
递归之后 => [2]
                递归之前 => [2, 4]
                                    递归之前 => [2, 4, 5]
                递归之后 => [2, 4]
递归之后 => [2]
                递归之前 => [2, 5]
递归之后 => [2]

递归之后 => []  -------------------------------------------

递归之前 => [3]
                递归之前 => [3, 4]
                                    递归之前 => [3, 4, 5]
                递归之后 => [3, 4]
递归之后 => [3]
                递归之前 => [3, 5]
递归之后 => [3]

递归之后 => []   -------------------------------------------

递归之前 => [4]
                递归之前 => [4, 5]
递归之后 => [4]

递归之后 => []   -------------------------------------------

递归之前 => [5]

递归之后 => []

[[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]

作者：liweiwei1419
链接：https://leetcode-cn.com/problems/combinations/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-ma-/

例如：n = 6 ，k = 4。
path.size() == 1 的时候，接下来要选择 3 个数，搜索起点最大是 4，最后一个被选的组合是 [4, 5, 6]；
path.size() == 2 的时候，接下来要选择 2 个数，搜索起点最大是 5，最后一个被选的组合是 [5, 6]；
path.size() == 3 的时候，接下来要选择 1 个数，搜索起点最大是 6，最后一个被选的组合是 [6]；

"""
import json
from typing import List


class Solution:
    def __init__(self) -> None:
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        if k <= 0 or n <= 0: return self.res
        track = []
        self.backtrack(n, k, 1, [])
        return self.res

    def backtrack(self, n, k, start, track):
        if len(track) == k:
            self.res.append(track[:])
            return
        # 搜索起点的上界 + 接下来要选择的元素个数 - 1 = n
        #                接下来要选择的元素个数 = k - path.size()
        # 搜索起点的上界 = n - (k - path.size()) + 1
        for i in range(start, n - (k - len(track)) + 1 + 1):
            track.append(i)
            #  下一轮搜索，设置的搜索起点要加 1，因为组合数理  不允许出现重复的元素
            self.backtrack(n, k, i + 1, track)
            track.pop()

def stringToInt(input):
    return int(input)


def int2dArrayToString(input):
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
            line = next(lines)
            k = stringToInt(line)

            ret = Solution().combine(n, k)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()