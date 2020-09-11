# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 8:35 PM 9/10/20
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以 迭代 或 递归 地反转链表。你能否用两种方法解决这道题？
"""
import json

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        迭代
        :param head:
        :return:
        """
        pre, cur, nxt = None, head, None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        return pre
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归
        :param head:
        :return:
        """
        if not head or not head.next: return head # 如果为空或者只有1个
        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur



def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        with open('stdin.txt') as f:
            for line in f:
                yield line.strip(('\n'))

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);

            ret = Solution().reverseList(head)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()