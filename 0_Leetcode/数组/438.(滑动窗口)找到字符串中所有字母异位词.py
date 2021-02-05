# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 4:25 PM 1/24/21
### [438\. 找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)

Difficulty: **中等**


给定一个字符串**s**和一个非空字符串**p**，找到**s**中所有是**p**的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串**s**和 **p**的长度都不超过 20100。

**说明：**

*   字母异位词指字母相同，但排列不同的字符串。
*   不考虑答案输出的顺序。

**示例1:**

```
输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
```

**示例 2:**

```
输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
```

"""
import json
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = {}
        window = {}
        for c in p:
            need[c] = need.get(c, 0) + 1
        left = right = 0
        valid = 0
        res = []
        while right < len(s):

            a = s[right]

            right += 1
            if a in need:
                window[a] = window.get(a, 0) + 1
                if need[a] == window[a]:
                    valid += 1
            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                b = s[left]
                left += 1
                if b in need:
                    if need[b] == window[b]:
                        valid -= 1
                    window[b] -= 1
        return res


def stringToString(input):
    return input[1:-1]


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


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
            p = stringToString(line);

            ret = Solution().findAnagrams(s, p)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()