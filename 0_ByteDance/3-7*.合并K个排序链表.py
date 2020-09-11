# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 8:38 PM 9/10/20
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]


提示：
    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
    lists[i] 按 升序 排列
    lists[i].length 的总和不超过 10^4
"""

import json
from typing import List
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        HEAP
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0: return None
        import heapq
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        dummy = ListNode(None)
        cur = dummy
        while heap:
            temp_node = ListNode(heapq.heappop(heap))
            cur.next = temp_node
            cur = temp_node
        return dummy.next

class Solution2: # 分 治
    def merge(self, node_a, node_b):
        dummy = ListNode(None)
        cursor_a, cursor_b, cursor_res = node_a, node_b, dummy
        while cursor_a and cursor_b:
            if cursor_a <= cursor_b:
                cursor_res.next = ListNode(cursor_a.val)
                cursor_a = cursor_a.next
            else:
                cursor_res.next = ListNode(cursor_b.val)
                cursor_b = cursor_b.next
            cursor_res = cursor_res.next
        if cursor_a:
            cursor_res.next = cursor_a
        if cursor_b:
            cursor_res.next = cursor_b
        return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)
        if length == 0: return None
        if length == 1: return lists[0]
        mid = length // 2
        return self.merge(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def stringToListNodeArray(input):
    listNodeArrays = json.loads(input)
    nodes = []
    for listNodeArray in listNodeArrays:
        nodes.append(stringToListNode(json.dumps(listNodeArray)))
    return nodes


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
    def readlines():
        with open('stdin.txt') as f:
            for line in f:
                yield line.strip(('\n'))

    lines = readlines()
    while True:
        try:
            line = next(lines)
            lists = stringToListNodeArray(line)

            ret = Solution().mergeKLists(lists)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()