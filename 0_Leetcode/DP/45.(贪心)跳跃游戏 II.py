# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:06 AM 2/27/21
### [45\. 跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii/)

Difficulty: **困难**


给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

**示例:**

```
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
    从下标为 0 跳到下标为 1 的位置，跳1步，然后跳3步到达数组的最后一个位置。
```

**说明:**

假设你总是可以到达数组的最后一个位置。

"""
import json
from typing import List

class Solution0: # DP 超时
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        self.memo = [n] * n
        return self.dp(nums, 0)

    def dp(self, nums, p): # 定义：从索引 p 跳到最后一格，至少需要 dp(nums, p) 步
        n = len(nums)
        if p >= n - 1: return 0 # base case 就是当p超过最后一格时，不需要跳跃
        if self.memo[p] != n: # 已经计算过，直接返回计算过的值
            return self.memo[p]
        steps = nums[p]
        for i in range(1, steps+1):
            subProblem = self.dp(nums, p+i)
            self.memo[p] = min(self.memo[p], subProblem + 1)
        return self.memo[p]

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end, farthest = 0, 0 # end是上次跳跃的最右边的点， farthest是目前能跳到的最远位置
        steps = 0
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                steps += 1
                end = farthest
        return steps


def stringToIntegerList(input):
    return json.loads(input)


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
            nums = stringToIntegerList(line);

            ret = Solution().jump(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()