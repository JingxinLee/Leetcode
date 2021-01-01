# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 2:58 PM 7/25/20
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
  2
输出: 4

示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4

限制：
1 ≤ k ≤ 二叉搜索树元素个数

"""

import json

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 中序遍历 是从小到大。    中序遍历的倒序 是从大到小
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:  # k=0 说明已经找到目标节点 提前返回
                return
            self.k -= 1  # 从k减到0
            if self.k == 0:  # 记录结果
                self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res

    def kthLargest2(self, root: TreeNode, k: int) -> int:
        self.res, self.k = None, k
        def dfs(root):
            if not root: return
            dfs(root.right)
            self.k -= 1
            if not self.k:
                self.res = root.val
            if self.k > 0: # 可加可不加  加上效率可能更高
                dfs(root.left)
        dfs(root)
        return self.res

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


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
            root = stringToTreeNode(line);
            line = next(lines)
            k = int(line);

            ret = Solution().kthLargest2(root, k)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()