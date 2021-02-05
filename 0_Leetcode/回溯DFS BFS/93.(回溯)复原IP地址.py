# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 2:51 PM 1/31/21
### [93\. 复原IP地址](https://leetcode-cn.com/problems/restore-ip-addresses/)

Difficulty: **中等**


给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

**有效的 IP 地址** 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 `0`），整数之间用 `'.'` 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 **有效的** IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 **无效的** IP 地址。

**示例 1：**

```
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
```

**示例 2：**

```
输入：s = "0000"
输出：["0.0.0.0"]
```

**示例 3：**

```
输入：s = "1111"
输出：["1.1.1.1"]
```

**示例 4：**

```
输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
```

**示例 5：**

```
输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

**提示：**

*   `0 <= s.length <= 3000`
*   `s` 仅由数字组成


"""
import json
from typing import List


class Solution:
    def __init__(self) -> None:
        self.res = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        track = ""
        self.backtrack(s, track, 0)
        return self.res

    def backtrack(self, s, track, depth):
        if depth == 4:
            # have 4 chunk and use up all digits
            if not s: self.res.append(track[:-1]) # track[-1]是 '.' 不能加上
            return
        for i in range(1, 4):
            # prevent index overflow
            if i > len(s): continue
            # take 1 digit is always good
            # take 2 or 3 digits, first digit cannot be '0'
            if i > 1 and s[0] == '0': continue
            # take 3 digits, cannot greater than 255
            if i > 2 and int(s[:3]) > 255: continue
            self.backtrack(s[i:], track + s[:i] + '.', depth + 1)

class Solution2:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def dfs(count=0, ip='', rem=''):
            if count == 4:
                if rem == '':
                    res.append(ip[:-1])
                else:
                    return
            if len(rem) > 0:
                dfs(count+1, ip + rem[0] + '.', rem[1:])
            if len(rem) > 1 and rem[0] != '0':
                dfs(count+1, ip + rem[:2] + '.', rem[2:])
            if len(rem) > 2 and rem[0] != '0' and int(rem[0:3]) < 256:
                dfs(count+1, ip + rem[:3] + '.', rem[3:])
        dfs(0, '', s)
        return res
def stringToString(input):
    return input[1:-1].decode('string_escape')


def stringArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line)

            ret = Solution().restoreIpAddresses(s)

            out = stringArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()