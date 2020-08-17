# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 下午12:11 2020/7/4

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

提示：
1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用
"""
class CQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []


    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if len(self.stack_in) == 0 and len(self.stack_out) == 0:
            return -1
        if len(self.stack_out) == 0: # 得保证 B 是空的
            while len(self.stack_in) != 0 :
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

class CQueue2:

    def __init__(self):
        self.A = []
        self.B = []


    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()  # B不是空的, 直接删除
        if len(self.A) == 0: return -1  # B是空的 且A也是空的, 返回-1
        while self.A:  # B是空的, A不是空的, 把A的元素加入到B中
            self.B.append(self.A.pop())
        return self.B.pop() # 从B中删除
