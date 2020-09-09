# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:51 AM 9/9/20

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。

示例 1：
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]

示例 2：
输入：s = "0000"
输出：["0.0.0.0"]

示例 3：
输入：s = "1111"
输出：["1.1.1.1"]

示例 4：
输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]

示例 5：
输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

提示：
0 <= s.length <= 3000
s 仅由数字组成

"""

import json
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        def dfs(count=0, ip='', rem=''):
            if count == 4:
                if rem == '':
                    res.append(ip[:-1])

            if len(rem) > 0:
                dfs(count+1, ip + rem[0] + '.', rem[1:])

            if len(rem) > 1 and rem[0] != 0:
                dfs(count+1, ip + rem[:2] + '.', rem[2:])

            if len(rem) > 2 and rem[0] != 0 and int(rem[:3]) < 256:
                dfs(count+1, ip + rem[:3] + '.', rem[3:])
        dfs(0, '', s)
        return res

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