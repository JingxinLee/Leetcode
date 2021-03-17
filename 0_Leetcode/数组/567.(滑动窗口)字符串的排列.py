# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 3:08 PM 1/24/21
### [567\. 字符串的排列](https://leetcode-cn.com/problems/permutation-in-string/)

Difficulty: **中等**


给定两个字符串**s1**和**s2**，写一个函数来判断 **s2** 是否包含 **s1**的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

**示例1:**

```
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
```

**示例2:**

```
输入: s1= "ab" s2 = "eidboaoo"
输出: False
```

**注意：**

1.  输入的字符串只包含小写字母
2.  两个字符串的长度都在 [1, 10,000] 之间

"""
import json
from typing import List
import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = collections.Counter(s1)
        n1, n2 = len(s1), len(s2)
        left = 0
        right = n1 - 1
        counter2 = collections.Counter(s2[:right]) # 统计窗口s2[left, right - 1]内的元素出现的次数
        while right < n2:
            counter2[s2[right]] += 1   #  # 把 right 位置的元素放到 counter2 中. 此时两者个数都为s1长度
            if counter1 == counter2: # 如果滑动窗口内各个元素出现的次数跟 s1 的元素出现次数完全一致，返回 True
                return True
            # 不相等的话就删除左边的, 再右移
            counter2[s2[left]] -= 1
            if counter2[s2[left]] == 0 : # 如果当前 left 位置的元素出现次数为 0， 需要从字典中删除
                del counter2[s2[left]]
            left += 1
            right += 1
        return False


class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        window = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1
        left = right = 0
        valid = 0

        while right < len(s2):
            a = s2[right]
            right += 1  # right要一直到s2的最后
            if a in need:
                window[a] = window.get(a, 0) + 1
                if need[a] == window[a]:
                    valid += 1
            while right - left >= len(s1):  # 差值比s1还长,就得缩减左边了
                # 判断是否找到了合法子串
                if valid == len(need):
                    return True
                b = s2[left]
                left += 1
                if b in need:
                    if need[b] == window[b]:
                        valid -= 1
                    window[b] -= 1
        return False


class Solution3:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        window = {}
        for s in s1:
            need[s] = 1 if s not in need else need[s] + 1
        n1, n2 = len(s1), len(s2)
        for i in range(n1):
            window[s2[i]] = 1 if s2[i] not in window else window[s2[i]] + 1

        for j in range(n1, n2):
            window.pop(s2[j - n1])
            window[j] = 1 if s2[j] not in window else window[j] + 1


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