# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 9:58 AM 7/22/20

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，
[2,3,4]的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。

示例 1：
输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]

示例 2：
输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
"""
from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = [] #  Big Queue
        self.B = [] # Smalle Queue


    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B): # 最终加到B： 先加入A 再pop出来加入B
            # heappush(self.A, num)
            # heappush(self.B, -heappop(self.A)) # B是MinQueue 所以 加负号
            heappush(self.B, -heappushpop(self.A, num))

        else:
            # heappush(self.B, -num)
            # heappush(self.A, -heappop(self.B))
            heappush(self.A, -heappushpop(self.B, -num))



    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()