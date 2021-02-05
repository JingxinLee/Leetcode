# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 3:33 PM 1/26/21

"""
import json
from typing import List


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk, inStack = [], {}
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
        for c in s:
            count[c] -= 1
            if inStack.get(c):  # c在栈中,直接跳过
                continue
            while len(stk) != 0 and stk[-1] > c:  # 栈顶 > c
                if count[stk[-1]] == 0:  # 当前栈顶 也就是c前面那个如果没有了,就不能pop掉栈顶,break这个while循环
                    break
                inStack[stk.pop()] = False  # 单调, 使得c前面的都不能比c大

            stk.append(c)
            inStack[c] = True
        return ''.join(stk)


def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);

            ret = Solution().removeDuplicateLetters(s)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()