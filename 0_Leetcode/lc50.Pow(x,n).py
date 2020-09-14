# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 12:01 PM 9/14/20
实现pow(x, n)，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000

示例2:
输入: 2.10000, 3
输出: 9.26100

示例3:
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/powx-n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0: return 0.0
        res = 1
        if n < 0:
            x, n = 1/x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >> 1
        return res

class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n==1:
            return x
        tmp = self.myPow(x, int(abs(n)/2))+0.0
        if n>0:
            if n%2 == 1:
                return tmp*tmp*x
            else:
                return tmp*tmp
        if n<0:
            if n%2 == 1:
                return 1/(tmp*tmp*x)
            else:
                return 1/(tmp*tmp)

def stringToDouble(input):
    return float(input)


def stringToInt(input):
    return int(input)


def doubleToString(input):
    if input is None:
        input = 0
    return "%.5f" % input


def main():
    import sys
    def readlines():
        with open('stdin.txt') as f:
            for line in f:
                yield line.strip(('\n'))

    lines = readlines()
    while True:
        try:
            line = next(lines)
            x = stringToDouble(line)
            line = next(lines)
            n = stringToInt(line)

            ret = Solution().myPow(x, n)

            out = doubleToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()