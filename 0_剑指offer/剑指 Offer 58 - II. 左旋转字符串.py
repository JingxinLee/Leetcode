# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 3:19 PM 7/26/20

字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：
输入: s = "abcdefg", k = 2
输出: "cdefgab"

示例 2：
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
"""

import json
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res) #  注意是‘’ 不是‘ ’ 字母与字母之间没有空格

    def reverseLeftWords2(self, s: str, n: int) -> str: # 简化上面的方法
        res = []
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)])  # 通过 取余 来简化
        return ''.join(res)


    def reverseLeftWords3(self, s: str, n: int) -> str: # 字符串遍历拼接
        res = "" # 字符串 "" 代替列表 []
        for i in range(n, len(s)):
            res += s[i]
        for i in range(n):
            res += s[i]
        return res

    def reverseLeftWords4(self, s: str, n: int) -> str: # 简化上面的方法
        res = ""
        for i in range(n, n + len(s)):
            res += s[i % len(s)]  # 通过 取余 来简化
        return res

    def reverseLeftWords5(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


def stringToString(input):
    return input[1:-1].decode('string_escape')


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
            s = stringToString(line);
            line = next(lines)
            n = int(line);

            ret = Solution().reverseLeftWords(s, n)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()