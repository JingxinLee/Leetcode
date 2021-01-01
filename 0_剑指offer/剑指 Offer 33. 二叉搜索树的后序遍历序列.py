# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:46 AM 7/19/20

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3

示例 1：
输入: [1,6,3,2,5]
输出: false

示例 2：
输入: [1,3,2,6,5]
输出: true

"""
import json
from typing import List
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):  # 根节点 索引 j
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1  # 左子树[i,m-1]
            m = p  # 第一个大于根节点的节点
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)  # 遇到不满足while条件的跳出，最后通过 p=j 来判断是否为二叉树

        return recur(0, len(postorder) - 1)


def stringToIntegerList(input):
    return json.loads(input)


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
            postorder = stringToIntegerList(line);

            ret = Solution().verifyPostorder(postorder)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()