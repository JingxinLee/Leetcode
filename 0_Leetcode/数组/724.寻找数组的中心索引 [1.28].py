# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 9:23 AM 1/28/21
### [724\. 寻找数组的中心索引](https://leetcode-cn.com/problems/find-pivot-index/)

Difficulty: **简单**


给定一个整数类型的数组`nums`，请编写一个能够返回数组 **“中心索引”** 的方法。

我们是这样定义数组 **中心索引** 的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

**示例 1：**

```
输入：
nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
索引 3 (nums[3] = 6) 的左侧数之和 (1 + 7 + 3 = 11)，与右侧数之和 (5 + 6 = 11) 相等。
同时, 3 也是第一个符合要求的中心索引。
```

**示例 2：**

```
输入：
nums = [1, 2, 3]
输出：-1
解释：
数组中不存在满足此条件的中心索引。
```

**说明：**

*   `nums` 的长度范围为`[0, 10000]`。
*   任何一个`nums[i]` 将会是一个范围在`[-1000, 1000]`的整数。

"""
import json
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums: return -1
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + nums[i]
        summ = sum(nums)

        for i in range(n):
            left = dp[i] - nums[i]
            right = summ - dp[i]
            if left == right:
                return i
        return -1
class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums: return -1
        n = len(nums)
        sum = 0
        for num in nums:
            sum += num

        for i in range(n):
            sum1 += nums[i]
            if sum - sum1 == sum1 - nums[i]:
                return i
        return -1

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

            ret = Solution().pivotIndex(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()