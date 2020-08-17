# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:00 AM 7/22/20
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

示例 1：
输入：n = 3
输出：3

示例 2：
输入：n = 11
输出：0
https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/solution/mian-shi-ti-44-shu-zi-xu-lie-zhong-mou-yi-wei-de-6/
"""
import json

class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        1. 将 101112中的每一位称为 数位 ，记为 n ；
        2. 将 10, 11, 12,⋯ 称为 数字 ，记为 num；
        3. 数字10是一个两位数，称此数字的 位数 为2，记为 digit；
        4. 每 digit位数的起始数字（即：1, 10, 100,⋯），记为 start
        各 digit下的数位数量 count 的计算公式 count = 9 × start × digit
        """
        digit, start, count = 1, 1, 9
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit
        return int(str(num)[(n - 1) % digit])


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

            ret = Solution().findNthDigit(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()