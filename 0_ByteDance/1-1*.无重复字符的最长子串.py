# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 9:32 PM 9/8/20

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

  剑指offer 48
"""
import json
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        dp[j]代表以s[j]为结尾的“最长不重复子字符串”的长度. 设s[j]左边距离最近的相同字符为s[i] s[j] = s[i]
        dp[j] = dp[j-1] + 1 if dp[j-1] < j - i => s[i]在dp[j-1] 区间之外
        dp[j] = j - i if dp[j-1] >= j - i    => s[i]在dp[j-1] 区间之内
        """
        # 动态规划 + 哈希表  其中HashTable 记录各字符最后一次出现的索引位置
        dic = {} # 统计 各字符最后一次出现的索引位置
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1) # 获取索引 i  dict.get(key, default = None)  default − This is the Value to be returned in case key does not exist.
            dic[s[j]] = j         # 更新 Hash Table
            tmp = tmp + 1 if tmp < j - i else j - i  # 转移方程
            res = max(res, tmp)
        return res


def stringToString(input):
    return input[1:-1]


def intToString(input):
    if input is None:
        input = 0
    return str(input)


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

            ret = Solution().lengthOfLongestSubstring(s)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()