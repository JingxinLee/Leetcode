# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 下午9:28 2020/7/12
 # 226
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9

镜像输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1

示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
 
限制：
0 <= 节点个数 <= 1000
"""
# Definition for a binary tree node.
import json
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        tmp = root.left  # 因为下一步left节点会改变,所以先暂存一下
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)
        return root

class Solution2:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None: return
        if root.left is None and root.right is None: return root
        root.left, root.right = root.right, root.left
        if root.left: # 左边不为空 就对左边的节点的子节点进行交换
            self.mirrorTree(root.left)
        if root.right: # 右边不为空 就对右边的节点的子节点进行交换
            self.mirrorTree(root.right)
        return root

class Solution3:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        stack = [root]
        while stack: # stack为空时跳出
            node = stack.pop()  # 出栈 记为node
            if node.left: stack.append(node.left)  # 添加node左节点入栈
            if node.right: stack.append(node.right) # 添加node右节点入栈
            node.left, node.right = node.right, node.left  # 交换
        return root

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


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


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

            ret = Solution().mirrorTree(root)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()