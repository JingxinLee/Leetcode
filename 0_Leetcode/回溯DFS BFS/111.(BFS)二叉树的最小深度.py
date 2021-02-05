# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 9:37 AM 2/4/21
### [111\. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)

Difficulty: **简单**


给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

**说明：**叶子节点是指没有子节点的节点。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg)

```
输入：root = [3,9,20,null,null,15,7]
输出：2
```

**示例 2：**

```
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
```

**提示：**

*   树中节点数的范围在 `[0, 10<sup>5</sup>]` 内
*   `-1000 <= Node.val <= 1000`

"""
import json
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        q = deque()
        q.append(root)
        depth = 1 # root 本身就是一层，depth 初始化为 1
        while q:
            size = len(q)

            for i in range(size): # 将当前队列中的 所有节点 向四周扩散 <=> 当前q中的节点,分别进行扩散 而不像DFS那样 只有一个扩散到底
                cur = q.popleft()
                if cur.left is None and cur.right is None: # 判断是否到达终点,也就是叶子节点
                    return depth
                # 将 cur 的相邻节点加入队列
                if cur.left != None:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            # 这里增加步数
            depth += 1

        return depth


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
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);

            ret = Solution().minDepth(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()