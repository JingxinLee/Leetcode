# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 8:51 PM 1/15/21

https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/solution/tu-jie-bing-cha-ji-by-yexiso-nbcz/

https://leetcode-cn.com/problems/redundant-connection/solution/yi-wen-zhang-wo-bing-cha-ji-suan-fa-by-a-fei-8/

https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/solution/li-kou-jia-jia-lian-tong-wen-ti-bing-cha-mt6d/
"""
class UF:  # labuladong版本
    def __init__(self, n):
        self.count = n
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

    def union(self, p, q): # 按 size 进行合并
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ: return

        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        self.count -= 1

    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ

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
        if self.rank[rootP] < self.rank[rootQ]: # 保证rootP大
            rootP, rootQ = rootQ, rootP
        self.rank[rootP] += self.rank[rootQ]
        self.parent[rootQ] = rootP
        self.count -= 1

    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ