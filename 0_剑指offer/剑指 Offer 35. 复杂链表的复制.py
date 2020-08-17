# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:47 AM 7/19/20

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        p = head
        Hash = {None: None}
        while p:  # 构造Hash
            Hash[p] = Node(p.val)
            p = p.next

        p = head
        while p:  # 构造 next 和 random
            Hash[p].next = Hash[p.next]
            Hash[p].random = Hash[p.random]
            p = p.next
        return Hash[head]

class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}
        def dfs(head):
            if not head: return None
            if head in visited: return visited[head]
            copy = Node(head.val, None, None)
            visited[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)
            return copy
        return dfs(head)

class Solution3:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return copy.deepcopy(head)
