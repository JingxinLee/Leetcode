# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 12:27 AM 9/9/20
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
 lc 43
"""

import json
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        m, n = len(num1), len(num2)
        ansArr = [0] * (m + n)
        for i in range(m-1, -1, -1):
            x = int(num1[i])
            for j in range(n-1, -1, -1):
                ansArr[i + j + 1] += x * int(num2[j])

        for i in range(m+n-1, 0, -1):
            ansArr[i - 1] += ansArr[i] // 10
            ansArr[i] %= 10
        index = 1 if ansArr[0] == 0 else 0
        ans = "".join(str(x) for x in ansArr[index:])
        return ans
def stringToString(input):
    return input[1:-1]


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
            num1 = stringToString(line);
            line = next(lines)
            num2 = stringToString(line);

            ret = Solution().multiply(num1, num2)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()