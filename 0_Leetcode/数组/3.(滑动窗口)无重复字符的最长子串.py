# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:05 PM 1/24/21
### [3\. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

Difficulty: **中等**


给定一个字符串，请你找出其中不含有重复字符的**最长子串**的长度。

**示例1:**

```
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

**示例 2:**

```
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

**示例 3:**

```
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
```

**示例 4:**

```
输入: s = ""
输出: 0
```

**提示：**

*   `0 <= s.length <= 5 * 10<sup>4</sup>`
*   `s`由英文字母、数字、符号和空格组成

"""
import json
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = right = 0
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1

            # 判断是否要收缩
            while window[c] > 1:  # 超过１个重复了
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right - left)  # 上面的right是加过１的，所以不用right - left 再 + 1了
        return res


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

            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()