# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 3:19 PM 1/16/21

给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或"a!=b"。
在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回true，否则返回 false。

示例 1：
输入：["a==b","b!=a"]
输出：false
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。

示例 2：
输入：["b==a","a==b"]
输出：true
解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。

示例 3：
输入：["a==b","b==c","a==c"]
输出：true

示例 4：
输入：["a==b","b!=c","c==a"]
输出：false

示例 5：
输入：["c==c","b==d","x!=z"]
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/satisfiability-of-equality-equations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

https://www.runoob.com/python3/python3-ascii-character.html
"""
import json
from typing import List


class UF:
    def __init__(self, n):
        self.parent = [None] * n
        self.size = [None] * n
        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ: return
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]

    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(26)
        for eq in equations:
            if eq[1] == '=':
                x = eq[0]
                y = eq[3]
                uf.union(ord(x) - ord('a'), ord(y) - ord('a'))

        for eq in equations:
            if eq[1] != '=':
                x = eq[0]
                y = eq[3]
                if uf.connected(ord(x) - ord('a'), ord(y) - ord('a')):
                    return False
        return True


def stringToStringArray(input):
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
            equations = stringToStringArray(line)

            ret = Solution().equationsPossible(equations)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()