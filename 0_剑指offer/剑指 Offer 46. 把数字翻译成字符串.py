# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 10:00 AM 7/22/20
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/mian-shi-ti-46-ba-shu-zi-fan-yi-cheng-zi-fu-chua-6/
"""

import json
class Solution:
    def translateNum(self, num: int) -> int:
        """
        # 动态规划
        状态定义：dp[i]代表以x_i为结尾数字的翻译方案数量
        转移方程：若x_i 和 x_i-1 组成的2位数字可以被翻译， dp[i] = dp[i-1] + dp[i-2] 否则 dp[i] = dp[i-1]
        初始状态： dp[0] = dp[1] = 1    区间为[10,25]      00 01 02...这种的不能被翻译
        """
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            a, b = (a + b if "10" <= s[i - 2:i] <= "25" else a), a
        return a


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
            num = int(line);

            ret = Solution().translateNum(num)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()