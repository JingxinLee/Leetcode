# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:13 PM 1/9/21
给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

两棵树重复是指它们具有相同的结构以及相同的结点值。

示例 1：

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
下面是两个重复的子树：

      2
     /
    4
和

    4
因此，你需要以列表的形式返回上述重复子树的根结点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-duplicate-subtrees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.res = []
        self.memo = {}

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if root is None:return self.res
        self.traverse(root)
        return self.res

    def traverse(self, root):
        """序列化二叉树,采用后续遍历"""
        # 空节点，用 # 号代替
        if root is None: return "#"

        left = self.traverse(root.left)  # left为string类型
        right = self.traverse(root.right)  # right也为string类型

        # 描述整棵树
        subtree = left + "," + right + "," + str(root.val)  # subtree也为string类型

        if subtree in self.memo.keys() and self.memo[subtree] == 1:
            self.res.append(root)
            self.memo[subtree] += 1
        elif subtree not in self.memo.keys():
            self.memo[subtree] = 1

        return subtree




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


def treeNodeArrayToString(treeNodeArray):
    serializedTreeNodes = []
    for treeNode in treeNodeArray:
        serializedTreeNode = treeNodeToString(treeNode)
        serializedTreeNodes.append(serializedTreeNode)
    return "[{}]".format(', '.join(serializedTreeNodes))


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line)

            ret = Solution().findDuplicateSubtrees(root)

            out = treeNodeArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()