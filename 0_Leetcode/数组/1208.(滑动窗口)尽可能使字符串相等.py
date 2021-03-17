# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:27 PM 2/5/21
### [1208\. 尽可能使字符串相等](https://leetcode-cn.com/problems/get-equal-substrings-within-budget/)

Difficulty: **中等**


给你两个长度相同的字符串，`s` 和 `t`。

将 `s`中的第`i`个字符变到`t`中的第 `i` 个字符需要`|s[i] - t[i]|`的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。

用于变更字符串的最大预算是`maxCost`。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。

如果你可以将 `s` 的子字符串转化为它在 `t` 中对应的子字符串，则返回可以转化的最大长度。

如果 `s` 中没有子字符串可以转化成 `t` 中对应的子字符串，则返回 `0`。

**示例 1：**

```
输入：s = "abcd", t = "bcdf", cost = 3
输出：3
解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。
```

**示例 2：**

```
输入：s = "abcd", t = "cdef", cost = 3
输出：1
解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为 1。
```

**示例 3：**

```
输入：s = "abcd", t = "acde", cost = 0
输出：1
解释：你无法作出任何改动，所以最大长度为 1。
```

**提示：**

*   `1 <= s.length, t.length <= 10^5`
*   `0 <= maxCost <= 10^6`
*   `s` 和`t`都只含小写英文字母。


"""
import json
from typing import List


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = right = 0
        sumCost = 0
        for right in range(len(s)):
            sumCost += abs(ord(s[right]) - ord(t[right]))
            if sumCost > maxCost:  # 此时滑动窗口内的区间不满足条件限制，需要整体向右滑动
                sumCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
        # 该问题的最大长度即对应遍历一遍数据后，滑动窗口的大小
        return len(s) - left


def stringToString(input):
    return input[1:-1].decode('string_escape')


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
            line = next(lines)
            maxCost = int(line);

            ret = Solution().equalSubstring(s, t, maxCost)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()