# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 9:14 AM 2/27/21
### [55\. 跳跃游戏](https://leetcode-cn.com/problems/jump-game/)

Difficulty: **中等**


给定一个非负整数数组`nums` ，你最初位于数组的 **第一个下标** 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

**示例1：**

```
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
```

**示例2：**

```
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
```

**提示：**

*   `1 <= nums.length <= 3 * 10<sup>4</sup>`
*   `0 <= nums[i] <= 10<sup>5</sup>`


"""
import json
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:  # 说明i可以到达，计算可以到的i的最远距离;  如果位置不可达 i > rightmost，我们也就不考虑它可以跳跃的最大长度了
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False

class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthers = 0
        for i in range(n-1): # 取不到最后一个
            farthers = max(farthers, i +nums[i])
            if farthers <= i: return False   # 可能碰到了 0，卡住跳不动了
        return farthers >= n - 1

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

            ret = Solution().canJump(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()