# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:40 AM 1/31/21
### [60\. 排列序列](https://leetcode-cn.com/problems/permutation-sequence/)

Difficulty: **困难**


给出集合`[1,2,3,...,n]`，其所有元素共有`n!` 种排列。

按大小顺序列出所有排列情况，并一一标记，当`n = 3` 时, 所有排列如下：

1.  `"123"`
2.  `"132"`
3.  `"213"`
4.  `"231"`
5.  `"312"`
6.  `"321"`

给定`n` 和`k`，返回第`k`个排列。

**示例 1：**

```
输入：n = 3, k = 3
输出："213"
```

**示例 2：**

```
输入：n = 4, k = 9
输出："2314"
```

**示例 3：**

```
输入：n = 3, k = 1
输出："123"
```

**提示：**

*   `1 <= n <= 9`
*   `1 <= k <= n!`


"""
import json
from typing import List


class Solution:
    def __init__(self) -> None:
        self.res = []

    def getPermutation(self, n: int, k: int) -> str:
        track = []
        used = [False] * (n+1)
        factorial = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            factorial[i] = factorial[i-1] * i
        self.backtrack(n, k, factorial, track, used, depth=0)
        #return self.res
        return ''.join(str(num) for num in track)


    def backtrack(self, n, k, factorial, track, used, depth):
        if depth == n:
            #self.res.append(''.join(str(j) for j in track[:]))
            return
        cnt = factorial[n - 1 - depth] # 全排列的个数
        for i in range(1, n+1): # 范围是 [1,n]
            if not used[i]:
                if cnt  < k: # 如果全排列的个数 < k 说明不在这一堆,跳过
                    k -= cnt
                    continue
                track.append(i) # 做选择
                used[i] = True  # 记录使用过的
                self.backtrack(n, k, factorial, track, used, depth+1)
                # used[i] = False
                # track.pop()
                return   # 这里要加 return，后面的数没有必要遍历去尝试了

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
            n = int(line);
            line = next(lines)
            k = int(line);

            ret = Solution().getPermutation(n, k)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()