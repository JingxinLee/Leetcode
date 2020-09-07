# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 下午9:27 2020/7/12

输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:

给定的树 A:
   3
  / \
 4  5
/ \
1  2

给定的树 B：

 4
 /
1

返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true

限制：
0 <= 节点个数 <= 10000
"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2: return None
        if pRoot1.val == pRoot2.val and self.helper(pRoot1.left, pRoot2.left) and self.helper(pRoot1.right,
                                                                                              pRoot2.right):
            return True
        return self.isSubStructure(pRoot1.left, pRoot2) or self.isSubStructure(pRoot1.right, pRoot2)

    def helper(self, root1, root2):
        if not root2: return True
        if not root1: return False
        if root1.val == root2.val:
            return self.helper(root1.left, root2.left) and self.helper(root1.right, root2.right)
        else:
            return False

class Solution2:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (
                    recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


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
            A = stringToTreeNode(line);
            line = next(lines)
            B = stringToTreeNode(line);

            ret = Solution().isSubStructure(A, B)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()