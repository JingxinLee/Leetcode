# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:42 PM 1/25/21
### [710\. 黑名单中的随机数](https://leetcode-cn.com/problems/random-pick-with-blacklist/)

Difficulty: **困难**


给定一个包含 [0，n ) 中独特的整数的黑名单 B，写一个函数从 [ 0，n ) 中返回一个**不在** B 中的随机整数。

对它进行优化使其尽量少调用系统方法 `Math.random()` 。

**提示:**

1.  `1 <= N <= 1000000000`
2.  `0 <= B.length < min(100000, N)`
3.  `[0, N)`不包含N，详细参见https://en.wikipedia.org/wiki/Interval_(mathematics)。

**示例 1:**

```
输入:
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
输出: [null,0,0,0]
```

**示例 2:**

```
输入:
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
输出: [null,1,1,1]
```

**示例 3:**

```
输入:
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]
```

**示例 4:**

```
输入:
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
输出: [null,1,3,1]
```

**输入语法说明：**

输入是两个列表：调用成员函数名和调用的参数。`Solution`的构造函数有两个参数，`N` 和黑名单 `B`。`pick` 没有参数，输入参数是一个列表，即使参数为空，也会输入一个 [] 空列表。

"""
import json
from typing import List


class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.N = N
        self.blacklist = blacklist
        self.tail = self.N - len(self.blacklist)
        self.mapping = {}
        for b in self.blacklist:
            self.mapping[b] = 666

        last = self.N - 1
        for b in self.blacklist:
            if b >= self.tail: # 如果 b 已经在区间 [sz, N) 可以直接忽略
                continue
            while last in self.mapping: # while 一直找到不在mapping中的last
                last -= 1
            self.mapping[b] = last
            last -= 1

    def pick(self) -> int:
        index = random.randint(0, self.N - 1) % self.tail  # index只能在tail前面的部分,tail后面的部分用来装blacklist中的
        if index in self.mapping:
            return self.mapping[index]
        return index

    # Your Solution object will be instantiated and called as such:
obj = Solution(5, [4, 0, 3])
print(obj.pick())
print(obj.pick())
print(obj.pick())