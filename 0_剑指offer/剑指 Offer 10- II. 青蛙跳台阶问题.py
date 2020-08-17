# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 下午10:35 2020/7/4
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例:
输入: n = 0
输出: 1  不跳也是一种情况
示例 1：
输入：n = 2
输出：2

示例 2：
输入：n = 1
输出：21

提示：
0 <= n <= 100

"""

def numWays(n: int) -> int:
    a, b = 0, 1
    for i in range(1,n+1):
        a, b = b, a+b
    return b%1000000007

#print(numWays(0))

########################################################################################################################

def numWays2(n: int) -> int:
    def countingFunc(stairsRemaining,savedResults):
        if stairsRemaining < 0:
            return 0
        if stairsRemaining == 0:
            return 1
        if savedResults[stairsRemaining]:
            return savedResults[stairsRemaining]
        savedResults[stairsRemaining] = countingFunc(stairsRemaining-1,savedResults) + countingFunc(stairsRemaining-2,savedResults)
        return savedResults[stairsRemaining]
    return countingFunc(n,{})

print(numWays2(3))

########################################################################################################################

class Solution:
    def __init__(self):
        self.dic = {0:1,1:1, 2:2}
    def numWays(self, n: int) -> int:
        if n not in self.dic:
            self.dic[n] = (self.numWays(n-1) + self.numWays(n-2))%1000000007
        return self.dic[n]

########################################################################################################################
