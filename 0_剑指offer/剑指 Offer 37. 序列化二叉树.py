# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 11:48 AM 7/19/20
请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"

"""
import json
from typing import List
import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    class Codec:

        def serialize(self, root):
            """Encodes a tree to a single string.

            :type root: TreeNode
            :rtype: str
            """
            if not root: return "[]"
            queue, res = collections.deque(), []  # 先进先出 用queue
            queue.append(root)
            while queue:
                node = queue.popleft()
                if node:
                    res.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append("null")
            return '[' + ','.join(res) + ']'  # +号就是把字符串拼接起来的意思，因为中括号是字符串类型，所以要加一个''

        def deserialize(self, data):
            """Decodes your encoded data to tree.

            :type data: str
            :rtype: TreeNode
            """
            if data == "[]": return
            vals, i = data[1:-1].split(','), 1
            root = TreeNode(int(vals[0]))
            queue = collections.deque()
            queue.append(root)
            while queue:
                node = queue.popleft()
                if vals[i] != 'null':
                    node.left = TreeNode(int(vals[i]))
                    queue.append(node.left)
                i += 1

                if vals[i] != 'null':
                    node.right = TreeNode(int(vals[i]))
                    queue.append(node.right)
                i += 1
            return root

    # Your Codec object will be instantiated and called as such:


# codec = Codec()
# codec.deserialize(codec.serialize(root))

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
            codec = Solution().Codec()
            ret = codec.deserialize(codec.serialize(root))

            #ret = Solution().Codec(root)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()