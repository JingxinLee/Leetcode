# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:34 PM 1/31/21
### [784\. 字母大小写全排列](https://leetcode-cn.com/problems/letter-case-permutation/)

Difficulty: **中等**


给定一个字符串`S`，通过将字符串`S`中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

```
示例：
输入：S = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

输入：S = "3z4"
输出：["3z4", "3Z4"]

输入：S = "12345"
输出：["12345"]
```

**提示：**

*   `S`的长度不超过`12`。
*   `S`仅由数字和字母组成。

https://leetcode-cn.com/problems/letter-case-permutation/solution/python3-dfshe-bfsliang-chong-jie-fa-by-moffysto/
"""
import json
from typing import List
class Solution:  # DFS
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S: return ['']
        self.res = []
        self.dfs(S, 0, '')
        return self.res

    def dfs(self, s, i, track):
        if i == len(s): # 递归结束条件是指针i走到字符串S末尾
            self.res.append(track)
            return
        if s[i].isdigit():
            self.dfs(s, i+1, track+s[i])
        else:
            self.dfs(s, i+1, track + s[i].lower())
            self.dfs(s, i+1, track + s[i].upper())

class Solution2:
    def letterCasePermutation(self, S: str) -> List[str]:
        """
        如果下一个字符 c 是字母，将当前已遍历过的字符串全排列复制两份，在第一份的每个字符串末尾添加 lowercase(c)，在第二份的每个字符串末尾添加 uppercase(c)。
        如果下一个字符 c 是数字，将 c 直接添加到每个字符串的末尾。
        """
        if not S: return []
        res = [[]]
        for char in S:
            n = len(res)
            if char.isalpha():
                for i in range(n):
                    res.append(res[i][:])
                    res[i].append(char.lower())
                    res[n+i].append(char.upper())
            else:
                for i in range(n):
                    res[i].append(char)
        return ["".join(ans) for ans in res]



def stringToString(input):
    return input[1:-1]


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
            S = stringToString(line)

            ret = Solution().letterCasePermutation(S)

            out = stringArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()