# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 3:20 PM 7/26/20

请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：
输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]

示例 2：
输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
"""
import queue

class MaxQueue:
    # 暴力： 直接实现一个普通的队列，查询最大值时遍历计算。
    def __init__(self):
        self.deque = queue.deque()

    def max_value(self) -> int:
        return max(self.deque) if self.deque else -1  # 求最大值需要遍历当前的整个队列，最坏情况下为 O(n)O(n)。

    def push_back(self, value: int) -> None:
        self.deque.append(value)

    def pop_front(self) -> int:
        return self.deque.popleft() if self.deque else -1

class MaxQueue2:
    # 单调队列： 本质是队列，只能在 数组 头部或尾部 进行 插入/删除 的操作
    # 单调性 ： 从头部到尾部 是 非递增 或 非递减的
    def __init__(self):
        self.deque = queue.deque() # 辅助队列
        self.queue = queue.Queue()

    def max_value(self) -> int: # 维护递减性是为了快速得到最大值，也就是队列头部
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None: #
        while self.deque and self.deque[-1] < value: # 单调不递增， 队列最后的元素 < 插入的元素,那么就pop 直到找到比插入value大的元素 或者队列为空 为止
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque: return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans

class MaxQueue3:
    # 单调队列： 本质是队列，只能在 数组 头部或尾部 进行 插入/删除 的操作
    # 单调性 ： 从头部到尾部 是 非递增 或 非递减的
    def __init__(self):
        from collections import deque
        self.que = deque()    # 原始队列，记录原始数值
        self.sort_que = deque() # 辅助队列，帮助对原始数值进行排序

    def max_value(self) -> int: # 维护递减性是为了快速得到最大值，也就是队列头部
        return self.sort_que[0] if self.sort_que else -1

    def push_back(self, value: int) -> None: #
        while self.sort_que and self.sort_que[-1] < value: # 单调不递增， 队列最后的元素 < 插入的元素,那么就pop 直到找到比插入value大的元素 或者队列为空 为止。 保证了，sort_que的头部总是原始队列que的最大值
            self.sort_que.pop()
        self.que.append(value)
        self.sort_que.append(value)

    def pop_front(self) -> int:
        if not self.que: return -1
        ans = self.que.get() # pop最前面的
        if ans == self.sort_que[0]:
            self.sort_que.popleft()
        return ans

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()