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

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2: return None
        if pRoot1.val == pRoot2.val and self.helper(pRoot1.left, pRoot2.left) and self.helper(pRoot1.right,
                                                                                              pRoot2.right):
            return True
        return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

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

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
