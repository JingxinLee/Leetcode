# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 9:59 AM 7/22/20
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

示例 1：
输入：n = 12
输出：5

示例 2：
输入：n = 13
输出：6

"""
import json
import math


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 1: return 0
        s = str(n)
        l = len(s)
        if l == 1: return 1
        first_num = int(s[0])
        num_high = math.pow(10, l - 1) if first_num > 1 else int(s[1:]) + 1
        num_sub = first_num * (l - 1) * math.pow(10, l - 2)
        num_else = self.countDigitOne(int(s[1:]))
        return int(num_high + num_sub + num_else)


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
            n = int(line);

            ret = Solution().countDigitOne(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()