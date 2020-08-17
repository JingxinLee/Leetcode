# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 下午1:34 2020/7/5
# 343 动 态 规 划  & 贪 心 #
给你一根长度为 n 的绳子，请把绳子剪成[整数]长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

提示:
2 <= n <= 58

"""
class Solution:
    def cuttingRope(self, n: int) -> int:
        # 动态规划
        dp = [0] * (n + 1) # dp[i]表示长度为i的绳子的最大乘积值
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                tmp = max(j,dp[j]) * max(i-j,dp[i-j])
                dp[i] = max(dp[i],tmp)
        return dp[-1]

class Solution2:
    def cuttingRope(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]  # dp[0] dp[1]其实没用
        dp[2] = 1  # 初始化
        for i in range(3, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))
        return dp[n]

class Solution3:
    def cuttingRope(self, n: int) -> int:
        s = [1]*(n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                s[i] = max(s[i], s[j]*(i-j), j*(i-j))
        return s[n]

