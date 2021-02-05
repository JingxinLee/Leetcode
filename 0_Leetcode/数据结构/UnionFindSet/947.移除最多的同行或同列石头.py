# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 8:21 PM 1/16/21
n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。

如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。

给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。

示例 1：
输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
输出：5
解释：一种移除 5 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。

示例 2：
输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
输出：3
解释：一种移除 3 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,0] 同行。
2. 移除石头 [2,0] ，因为它和 [0,0] 同列。
3. 移除石头 [0,2] ，因为它和 [0,0] 同行。
石头 [0,0] 和 [1,1] 不能移除，因为它们没有与另一块石头同行/列。

示例 3：
输入：stones = [[0,0]]
输出：0
解释：[0,0] 是平面上唯一一块石头，所以不可以移除它。

提示：
1 <= stones.length <= 1000
0 <= xi, yi <= 104
不会有两块石头放在同一个坐标点上

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

    1. 将行和列转化到同一个维度（也就是说将行和列仅仅当作一个数字就行）
    2. 当我们遍历到一个点(x, y)时，直接将x与y进行合并（说明该行和该列行的所有点都属于同一个并查集）
    3. 最后用stones的大小减去并查集的个数即可
    4. 但是，x和y的值可能冲突，所以这里我们将x加上10001（题目范围限定为10000）

https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/solution/tu-jie-bing-cha-ji-by-yexiso-nbcz/
https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/solution/li-kou-jia-jia-lian-tong-wen-ti-bing-cha-mt6d/
https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/solution/947-yi-chu-zui-duo-de-tong-xing-huo-tong-ezha/

"""
import json
from typing import List


class UF:  # 优化的并查集 无rank
    def __init__(self):
        self.parent = {}
        self.count = 0

    def find(self, x):
        if x not in self.parent:
            self.count += 1
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, p, q):  # 按 size 进行合并
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ: return
        self.parent[rootP] = rootQ
        self.count -= 1

    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UF()
        for i in range(n):
            uf.union(stones[i][0] + 10001, stones[i][1])
        return n - uf.count


class UF2:  # 优化的并查集 有rank
    def __init__(self):
        self.parent = {}
        self.count = 0
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.count += 1
            self.parent[x] = x
            self.rank[x] = 1
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, p, q):  # 按 size 进行合并
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ: return
        if self.rank[rootP] < self.rank[rootQ]:
            rootP, rootQ = rootQ, rootP
        self.rank[rootP] += self.rank[rootQ]
        self.parent[rootQ] = rootP
        self.count -= 1

    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ


class Solution2:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UF()
        for i in range(n):
            uf.union(stones[i][0] + 10001, stones[i][1])
        return n - uf.count


def stringToInt2dArray(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            stones = stringToInt2dArray(line)

            ret = Solution().removeStones(stones)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()