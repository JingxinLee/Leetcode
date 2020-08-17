# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 上午11:03 2020/7/7
实现函数double Power(double base, int exponent)，求base的exponent次方。
不得使用库函数，同时不需要考虑大数问题。

示例 1:
输入: 2.00000, 10
输出: 1024.00000

示例 2:
输入: 2.10000, 3
输出: 9.26100

示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
 
说明:
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 and n < 0: return 0
        absn = n
        if n < 0: absn = -n
        res = self.Power(x, absn)
        if n < 0: res = 1 / res
        return res

    def Power(self, x, n):
        if n == 0: return 1
        if n == 1: return x
        result = self.Power(x, n >> 1)
        result *= result
        if n & 1:
            result *= x
        return result

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        res = 1
        if n < 0 : x, n = 1/x, -n
        while n:
            if n & 1: res *= x  # 奇数
            x *= x  # 偶数的时候
            n >>= 1
        return res