# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:13 AM 1/24/21
### [76\. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)

Difficulty: **困难**

给你一个字符串 `s` 、一个字符串 `t` 。返回 `s` 中涵盖 `t` 所有字符的最小子串。如果 `s` 中不存在涵盖 `t` 所有字符的子串，则返回空字符串 `""` 。

**注意：**如果 `s` 中存在这样的子串，我们保证它是唯一的答案。

**示例 1：**
```
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
```

**示例 2：**
```
输入：s = "a", t = "a"
输出："a"
```

**提示：**

*   `1 <= s.length, t.length <= 10<sup>5</sup>`
*   `s` 和 `t` 由英文字母组成

**进阶：**你能设计一个在 `o(n)` 时间内解决此问题的算法吗？
"""
import json
from typing import List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        for c in t:
            if c not in need:
                need[c] = 1
            else:
                need[c] += 1
        left = right = 0  # 左闭右开的区间
        valid = 0  # valid 表示窗口中满足need条件的字符个数
        start, length = 0, float('inf')  # 记录最小覆盖子串的起始位置和长度
        while right < len(s):
            a = s[right]
            right += 1
            if a in need:  # 判断 right位置的a 是否在need中
                window[a] = 1 if a not in window else window[a] + 1
                if window[a] == need[a]:  # 如果window和need中的右侧值a 个数相等, valid + 1
                    valid += 1

            while valid == len(need):  # 如果valid就是need的长度,左侧窗口进行 收缩, 更新最终结果相关的 start
                if right - left < length:
                    start = left
                    length = right - left
                b = s[left]  # b是将要移出窗口的字符
                left += 1
                if b in need:  # 判断b是否在need中
                    if window[b] == need[b]:  # 如果b在need中,且与window中的b个数相等, valid - 1
                        valid -= 1
                    window[b] -= 1  # 更新窗口window
        if length == float('inf'):
            return ""
        else:
            return s[start: start + length]


def stringToString(input):
    return input[1:-1]


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
            line = next(lines)
            t = stringToString(line);

            ret = Solution().minWindow(s, t)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()