# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 8:54 PM 12/29/20

"""
# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:01 AM 7/22/20
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例1:
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
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
"""

import json
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: # 正常的动态规划
        if not s : return 0
        n = len(s)
        dic = {s[0]:0}
        dp = [1] * n
        for i in range(1,n):
            last_index = dic.get(s[i], -1)
            dic[s[i]] = i
            if dp[i-1] < i - last_index: # s[last_index]在 dp[i-1]区间之外
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = i - last_index
        return max(dp)

class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int: # 优化了空间的动态规划
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1) # 获取索引 i
            dic[s[j]] = j # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]
            res = max(res, tmp) # max(dp[j - 1], dp[j])
        return res


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

            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()