# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:11 PM 9/8/20

给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").


示例2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False


注意：

    输入的字符串只包含小写字母
    两个字符串的长度都在 [1, 10,000] 之间

  lc 567

"""
import json

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1);
        l2 = len(s2);

        if l1 > l2: return False;
        dict1 = {};
        dict2 = {};
        s = "abcdefghijklmnopqrstuvwxyz";
        for char in s:
            dict1[char] = 0;
            dict2[char] = 0;
        for i in range(l1):
            dict1[s1[i]] += 1;
            dict2[s2[i]] += 1;
        if dict1 == dict2: return True;

        for i in range(l2 - l1):
            dict2[s2[i + l1]] += 1;
            dict2[s2[i]] -= 1;
            if dict1 == dict2: return True;
        else:
            return False

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
            s1 = stringToString(line);
            line = next(lines)
            s2 = stringToString(line);

            ret = Solution().checkInclusion(s1, s2)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()