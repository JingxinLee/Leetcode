# -*- coding:utf-8 -*-
"""
author:

Created on 下午2:24 2020/7/4
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.

"""


# Definition for singly-linked list.
import json
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 迭代
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        first_node = head
        second_node = head.next
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        return second_node


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
        # for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
        #     yield line.strip('\n')
        with open('stdin.txt') as f:
            for line in f:
                yield line.strip(('\n'))
            #mylist = [line.rstrip('\n') for line in f]

    lines = readlines()
    while True:
        try:
            line = next(lines)

            head = stringToListNode(line);

            ret = Solution().swapPairs(head)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()