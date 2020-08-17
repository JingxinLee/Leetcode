# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 下午9:30 2020/7/12
  # 54
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 
限制：
0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        l, r, t, b = 0, n - 1, 0, m - 1
        res = []
        while True:
            for i in range(l, r + 1):
                res.append(matrix[t][i])  # left -> right
            t += 1
            if t > b: break

            for i in range(t, b + 1):
                res.append(matrix[i][r])  # top -> bottom
            r -= 1
            if r < l: break

            for i in range(r, l - 1, -1):  # 最后一行倒着走
                res.append(matrix[b][i])  # right -> left
            b -= 1
            if b < t: break

            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])  # bottom -> top
            l += 1
            if l > r: break
        return res
