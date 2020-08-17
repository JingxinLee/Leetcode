# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 10:02 AM 7/22/20
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:
s = "abaccdeff"
返回 "b"

s = ""
返回 " "
"""
import json

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        res = []
        for num in s:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for num in dic.keys():
            if dic[num] == 1:
                res.append(num)
        if res:
            return res[0]
        else:
            return " "


def stringToString(input):
    return input[1:-1]

def charToString(c):
    return json.dumps(c)


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
            s = stringToString(line)

            ret = Solution().firstUniqChar(s)

            out = charToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()