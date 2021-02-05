# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 7:05 PM 1/21/21

"""
import json
from typing import List


class MaxPQ:
    def __init__(self, cap):
        self.N = 0
        self.cap = cap
        self.pq = [None] * (self.cap + 1)

    def parent(self, root):
        return root / 2
    def left(self, root):
        return root * 2
    def right(self, root):
        return root * 2 + 1

    def max(self):
        return self.pq[1]

    def insert(self, e):
        self.N += 1
        self.pq[self.N] = e
        self.swim(self.N)

    def delMax(self):
        max = pq[1]
        self.swap(1, self.N)
        pq[self.N] = None
        self.N  -= 1
        self.sink(1)
        return max


    def swim(self, k):
        while k > 1 and self.less(self.parent(k), k): # 父节点 < 子节点
            self.swap(self.parent(k), k)
            k = self.parent(k)

    def sink(self, k):
        while self.left(k) <= self.N: # 沉到堆底就沉不下去了
            # 假设左边节点较大
            older = self.left(k)
            if self.right(k) <= self.N and self.less(older, self.right(k)): # 右边的大
                older = self.right(k)
            if self.less(older, k):  # 节点k比2个孩子都大,不用下沉了
                break
            self.swap(k, older)
            k = older


    def swap(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def less(self, i, j):
        return self.pq[i] < self.pq[j]