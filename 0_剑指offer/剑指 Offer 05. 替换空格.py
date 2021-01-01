# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 下午12:11 2020/7/4
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."

限制：
0 <= s 的长度 <= 10000
"""
from typing import List
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for i in s:
            if i == " ": res.append('%20')
            else: res.append(i)
        return "".join(res)


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
            s = stringToString(line);

            ret = Solution().replaceSpace(s)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()