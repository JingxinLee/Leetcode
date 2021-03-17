# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 3:23 PM 3/4/21
### [651\. 4键键盘](https://leetcode-cn.com/problems/4-keys-keyboard/)

Difficulty: **中等**


假设你有一个特殊的键盘包含下面的按键：

`Key 1: (A)`：在屏幕上打印一个 'A'。

`Key 2: (Ctrl-A)`：选中整个屏幕。

`Key 3: (Ctrl-C)`：复制选中区域到缓冲区。

`Key 4: (Ctrl-V)`：将缓冲区内容输出到上次输入的结束位置，并显示在屏幕上。

现在，你只可以按键 **N** 次（使用上述四种按键），请问屏幕上最多可以显示几个 'A'呢？

**样例 1:**

```
输入: N = 3
输出: 3
解释:
我们最多可以在屏幕上显示三个'A'通过如下顺序按键：
A, A, A
```

**样例 2:**

```
输入: N = 7
输出: 9
解释:
我们最多可以在屏幕上显示九个'A'通过如下顺序按键：
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
```

**注释:**

1.  1 <= N <= 50
2.  结果不会超过 32 位有符号整数范围。


```
"""
import json
from typing import List


class Solution0: # 超时
    def maxA(self, N: int) -> int:
        def dp(n, a_num, copy): # 第一个状态是剩余的按键次数，用n表示；第二个状态是当前屏幕上字符 A 的数量，用a_num表示；第三个状态是剪切板中字符 A 的数量，用copy表示
            if n <= 0: return a_num # base case：当剩余次数n为 0 时，a_num就是我们想要的答案
            return max(dp(n-1, a_num+1, copy), # 按下 A 键，屏幕上加一个字符 同时消耗 1 个操作数
                       dp(n-1, a_num+copy, copy), # 按下 C-V 粘贴，剪切板中的字符加入屏幕 同时消耗 1 个操作数
                       dp(n-2, a_num, a_num)) # 全选和复制必然是联合使用的， 剪切板中 A 的数量变为屏幕上 A 的数量 同时消耗 2 个操作数
        return dp(N, 0, 0)

class Solution1: # 加上备忘录
    def maxA(self, N: int) -> int:
        memo = dict()
        def dp(n, a_num, copy):
            if n <= 0: return a_num
            if (n, a_num, copy) in memo:
                return memo[(n, a_num, copy)]
            memo[(n, a_num, copy)] = max(dp(n-1, a_num+1, copy), dp(n-1, a_num+copy, copy), dp(n-2, a_num, a_num))
            return memo[(n, a_num, copy)]
        return dp(N, 0, 0)

class Solution:
    def maxA(self, N: int) -> int:
        """
        只定义一个「状态」，也就是剩余的敲击次数n
        dp[i] 表示 i 次操作后最多能显示多少个 A
        """
        dp = [0] * (N + 1)
        dp[0] = 0
        for i in range(1, N+1):
            dp[i] = dp[i - 1] + 1  # 按 A 键，就比上次多一个 A 而已
            for j in range(2, i):
                # j 是 C-V的起始点， j之前的2个操作是 C-A 和 C-C。
                # 全选和复制 dp[j-2]， 连续粘贴 i - j次，加上本身， 屏幕上总共 dp[j-2] * (i-j+1) 个 A
                dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
        return dp[N]

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
            N = int(line);

            ret = Solution().maxA(N)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()