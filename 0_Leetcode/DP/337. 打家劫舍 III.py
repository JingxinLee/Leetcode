# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:07 PM 3/7/21
### [337\. 打家劫舍 III](https://leetcode-cn.com/problems/house-robber-iii/)

Difficulty: **中等**


在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

**示例 1:**

```
输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释:小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
```

**示例 2:**

```
输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释:小偷一晚能够盗取的最高金额= 4 + 5 = 9.
```

"""
import json
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, root: TreeNode) -> int:
        if not root: return 0
        if root in self.memo:
            return self.memo.get(root)
        # 从root 开抢

        do = root.val + (self.rob(root.left.left) + self.rob(root.left.right) if root.left else 0) + (
            self.rob(root.right.left) + self.rob(root.right.right) if root.right else 0)

        undo = self.rob(root.left) + self.rob(root.right)
        res = max(do, undo)
        self.memo[root] = res
        return res

class Solution2:
    def rob(self, root: TreeNode) -> int:
        # 返回一个大小为 2 的数组.  arrarr[0] 表示不抢 root 的话，得到的最大钱数.  arr[1] 表示抢 root 的话，得到的最大钱数
        def dp(root):
            if not root: return [0, 0]
            left = dp(root.left)   # 得到 大小为 2 的数组
            right = dp(root.right) # 得到 大小为 2 的数组
            do = root.val + left[0] + right[0] # 抢root， 那么left和right就不抢了，也就是第0个
            undo = max(left[0], left[1]) + max(right[0], right[1]) # 不抢root， 那么下一家可以抢，也可以不抢，按照最大的来
            return [undo, do]
        res = dp(root)
        return max(res[0], res[1]) # 0 不抢， 1 抢



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

            ret = Solution().rob(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()