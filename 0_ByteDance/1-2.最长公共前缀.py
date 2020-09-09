# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:41 PM 9/8/20

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
 Leetcode 14
 https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
"""
import json
# 纵向比较
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        length, counts = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or c != strs[j][i] for j in range(1, counts)):
                return strs[0][:i]
        return strs[0]


def stringToStringArray(input):
    return json.loads(input)


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
            strs = stringToStringArray(line)

            ret = Solution().longestCommonPrefix(strs)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()