# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 下午2:26 2020/7/7
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。
比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
 
说明：
用返回一个整数列表来代替打印
n 为正整数
"""

from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10 ** n):
            res.append(i)
        return res

class Solution2:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1, 10**n))

class Solution3:
    def printNumbers(self, n: int) -> List[int]:
        def dfs(x):
            if x == n:  # 终止条件：已固定完所有位
                res.append(''.join(num))  # 拼接 num 并添加至 res 尾部
                return
            for i in range(10):  # 遍历 0 - 9
                num[x] = str(i)  # 固定第 x 位为 i
                dfs(x + 1)  # 开启固定第 x + 1 位

        num = ['0'] * n  # 起始数字定义为 n 个 0 组成的字符列表
        res = []  # 数字字符串列表
        dfs(0)  # 开启全排列递归
        res = list(map(int, res))  # 将list每个成员从字符串转换成数字，会将字符串前面为0的内容去除
        res.pop(0)  # 删除0
        return res

print(Solution3().printNumbers(2))