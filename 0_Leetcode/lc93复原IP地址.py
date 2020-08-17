# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:12 AM 7/26/20

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

示例:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""

import json
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        回 溯 法
        :type s: str
        :rtype: List[str]
        """
        r = []

        def restore(count=0, ip='', s=''): # count record split times, ip record ip, s record remaining string
            if count == 4:
                if s == '':
                    r.append(ip[:-1])
                return
            if len(s) > 0:
                restore(count + 1, ip + s[0] + '.', s[1:])
            if len(s) > 1 and s[0] != '0':
                restore(count + 1, ip + s[:2] + '.', s[2:])
            if len(s) > 2 and s[0] != '0' and int(s[0:3]) < 256:
                restore(count + 1, ip + s[:3] + '.', s[3:])

        restore(0, '', s)
        return r


def stringToString(input):
    return input[1:-1]


def stringArrayToString(input):
    return json.dumps(input)


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

            ret = Solution().restoreIpAddresses(s)

            out = stringArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()