# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 11:48 AM 7/19/20

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left)
            if self.pre:  # pre不为空，cur左侧有pre节点 需要进行以下操作
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur  # pre是cur左侧的节点，即上一次迭代中的cur。pre为空，cur左侧没有节点，cur为头结点
            self.pre = cur  # pre 移动到 cur
            dfs(cur.right)
        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

a = Solution()
node = Node([4,2,5,1,3])
print(a.treeToDoublyList(node))