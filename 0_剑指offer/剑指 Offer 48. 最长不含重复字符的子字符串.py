# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:01 AM 7/22/20
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:
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
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

import json
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        dp[j]代表以s[j]为结尾的“最长不重复子字符串”的长度. 设s[j]左边距离最近的相同字符为s[i]
        dp[j] = dp[j-1] + 1 if dp[j-1] < j - i => s[i]在dp[j-1] 区间之外
        dp[j] = j - i if dp[j-1] >= j - i    => s[i]在dp[j-1] 区间之内
        """
        # 动态规划 + 哈希表  其中HashTable 记录各字符最后一次出现的索引位置
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1) # dict.get(key, default = None)  default − This is the Value to be returned in case key does not exist.
            dic[s[j]] = j
            tmp = tmp + 1 if tmp < j - i else j - i
            res = max(res, tmp)
        return res



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

            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()