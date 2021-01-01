# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:47 AM 7/19/20

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:
给定如下二叉树，以及目标和sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""
import json
from typing import List
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object): # DFS 回溯
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res, path = [], []

        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:  # 确定为叶子节点
                res.append(list(path)) # 记录路径时若直接执行 res.append(path) ，则是将 path 对象加入了 res；后续 path 改变时， res 中的 path 对象也会随之改变。 相当于复制了一个 path 并加入到 res 。
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, sum)
        return res

class Solution2(object): # DFS 迭代
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # DFS + 迭代
        if not root: return []
        stack = [(root, root.val, [root.val])]
        res = []
        while stack:
            node, val, temp = stack.pop()
            if val == sum and not node.left and not node.right: res.append(temp)
            if node.right:
                stack.append((node.right, val+node.right.val, temp+[node.right.val]))
            if node.left:
                stack.append((node.left, val+node.left.val, temp+[node.left.val]))
        return res

class Solution3(object): # BFS + 迭代
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # BFS + 迭代
        if not root: return []
        queue = [(root, root.val, [root.val])]
        res = []
        while queue:
            node, val, temp = queue.pop(0) # 会把结果不对的pop掉
            if val == sum and not node.left and not node.right: res.append(temp)
            if node.left:
                queue.append((node.left, val+node.left.val, temp+[node.left.val]))
            if node.right:
                queue.append((node.right, val+node.right.val, temp+[node.right.val]))
        return res

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


def stringToInt(input):
    return int(input)


def int2dArrayToString(input):
    return json.dumps(input)


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
            root = stringToTreeNode(line)
            line = next(lines)
            sum = stringToInt(line)

            ret = Solution3().pathSum(root, sum)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()