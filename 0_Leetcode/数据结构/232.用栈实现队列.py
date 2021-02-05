# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 8:26 PM 1/21/21

"""
import json
from typing import List
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.A = []
        self.B = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.A.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.B.pop()



    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.B == []:
            while self.A:
                self.B.append(self.A.pop())
        return self.B[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.A == [] and self.B == []




# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
print(param_3)
param_4 = obj.pop()
print(param_4)
param_5 = obj.empty()
print(param_5)