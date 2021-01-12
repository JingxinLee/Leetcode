# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 1:47 PM 1/11/21

给你一个字符串s，以及该字符串中的一些「索引对」数组pairs，其中pairs[i] =[a, b]表示字符串中的两个索引（编号从 0 开始）。
你可以 任意多次交换 在pairs中任意一对索引处的字符。
返回在经过若干次交换后，s可以变成的按字典序最小的字符串。

示例 1:
输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"

示例 2：
输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[0] 和 s[2], s = "acbd"
交换 s[1] 和 s[2], s = "abcd"

示例 3：
输入：s = "cba", pairs = [[0,1],[1,2]]
输出："abc"
解释：
交换 s[0] 和 s[1], s = "bca"
交换 s[1] 和 s[2], s = "bac"
交换 s[0] 和 s[1], s = "abc"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-string-with-swaps
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import json
from typing import List

class Solution(object):
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        u = self.Union(len(s))
        for x, y in pairs:
            u.union(x, y)
        arr, s = u.getIndexArr(), list(s)
        for idxs in arr:
            idxs.sort()
            cs = [s[i] for i in idxs]
            cs.sort()
            j = 0
            for i in idxs:
                s[i] = cs[j]
                j += 1
        return ''.join(s)

    class Union:
        def __init__(self, N):
            self.parents = {}
            for i in range(N):
                self.parents[i] = i

        def find(self, x):
            if self.parents[x] != x:
                original = self.find(self.parents[x])
                self.parents[x] = original
            return self.parents[x]

        def union(self, x, y):
            if x > y: x, y = y, x
            rootX, rootY = self.find(x), self.find(y)
            if rootX != rootY:
                self.parents[rootX] = rootY
                self.parents[x] = rootY

        def getIndexArr(self):
            N = len(self.parents)
            arr = [[] for _ in range(N)]
            for i in range(N):
                self.find(i)
            for k, v in self.parents.items():
                arr[v].append(k)
            return [v for v in arr if len(v) > 1]


def stringToString(input):
    return input[1:-1]

def stringToInt2dArray(input):
    return json.loads(input)


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
            line = next(lines)
            pairs = stringToInt2dArray(line)

            ret = Solution().smallestStringWithSwaps(s, pairs)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()