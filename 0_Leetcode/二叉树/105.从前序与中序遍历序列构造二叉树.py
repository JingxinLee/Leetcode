# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 2:26 PM 1/9/21
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出
前序遍历 preorder =[3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
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
    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd: return None
        rootVal = preorder[preStart]
        index = 0
        for i in range(inStart, inEnd+1): # 都要取到
            if inorder[i] == rootVal:
                index = i
                break

        leftSize = index - inStart
        root = TreeNode(rootVal)
        root.left = self.build(preorder, preStart+1, preStart+leftSize, inorder, inStart, index-1)
        root.right = self.build(preorder, preStart+leftSize+1, preEnd, inorder, index+1, inEnd)

        return root


    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)



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
            preorder = stringToIntegerList(line);
            line = next(lines)
            inorder = stringToIntegerList(line);

            ret = Solution().buildTree(preorder, inorder)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()