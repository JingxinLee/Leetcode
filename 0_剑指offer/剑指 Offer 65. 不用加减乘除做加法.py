# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:01 PM 7/28/20

写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

示例:
输入: a = 1, b = 1
输出: 2

提示：
a,b均可能是负数或 0
结果不会溢出 32 位整数
https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/
"""

class Solution:
    def add(self, a: int, b: int) -> int:
        """
        非进位和：　异或运算　　ｎ　＝　ａ ^ b  ：　　1＋０＝１　　　１＋１＝０　　　０＋０＝０
        进位和：　与运算　＋　左移一位　ｃ　＝　ａ & b << 1　　
        s = n + c
        """
        if b == 0: return a
        n = a ^ b
        c = (a & b) << 1
        return add(n, c)

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
            a = int(line);
            line = next(lines)
            b = int(line);

            ret = Solution().add(a, b)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()