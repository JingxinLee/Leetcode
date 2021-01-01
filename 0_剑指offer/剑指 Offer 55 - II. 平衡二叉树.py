# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 3:16 PM 7/26/20

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。


示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回false 。
"""

import json
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool: # 从下往上
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1   # 当左（右）子树深度为 -1 ：代表此树的 左（右）子树 不是平衡树，因此剪枝，直接返回 -1 ；
            right = recur(root.right)
            if right == -1: return -1  # 当左（右）子树深度为 -1 ：代表此树的 左（右）子树 不是平衡树，因此剪枝，直接返回 -1 ；
            return max(left, right) + 1 if abs(left - right) <= 1 else -1
        return recur(root) != -1

    def isBalanced2(self, root: TreeNode) -> bool: # 从上往下
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 \
               and self.isBalanced2(root.left) and self.isBalanced2(root.right)
    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1



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

            ret = Solution().isBalanced(root)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()