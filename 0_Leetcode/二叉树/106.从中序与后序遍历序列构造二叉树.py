# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 4:06 PM 1/9/21
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出
中序遍历 inorder =[9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
    def build(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        if inStart > inEnd: return None
        rootVal = postorder[postEnd]

        index = 0
        for i in range(inStart, inEnd+1):
            if inorder[i] == rootVal:
                index =  i
                break

        leftSize = index - inStart
        root = TreeNode(rootVal)
        root.left = self.build(inorder, inStart, index-1,
                               postorder, postStart, postStart+leftSize-1)
        root.right = self.build(inorder, index+1, inEnd,
                                postorder, postStart+leftSize, postEnd-1)

        return root


    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.build(inorder, 0, len(inorder)-1,
                          postorder, 0, len(postorder)-1)

def stringToIntegerList(input):
    return json.loads(input)


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
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            inorder = stringToIntegerList(line);
            line = next(lines)
            postorder = stringToIntegerList(line);

            ret = Solution().buildTree(inorder, postorder)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()