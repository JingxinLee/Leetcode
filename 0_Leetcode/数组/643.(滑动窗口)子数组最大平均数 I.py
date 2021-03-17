# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:21 PM 2/4/21
### [643\. 子数组最大平均数 I](https://leetcode-cn.com/problems/maximum-average-subarray-i/)

Difficulty: **简单**


给定 `n` 个整数，找出平均数最大且长度为 `k` 的连续子数组，并输出该最大平均数。

**示例：**

```
输入：[1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
```

**提示：**

*   1 <= `k` <= `n` <= 30,000。
*   所给数据范围 [-10,000，10,000]。

"""
import json
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = windowSum = sum(nums[:k])
        for i in range(k, len(s)):
            windowSum = windowSum - nums[i - k] + nums[i]
            maxSum = max(windowSum, maxSum)
        return maxSum / k

class Solution2: # 暴力法 时间复杂度高
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum1 = 0
        sum2 = 0
        for i in range(k):
            sum1 += nums[i]
        maxnum = sum1 / k

        for i in range(1, len(nums) - k + 1):
            for j in range(i, i + k):
                sum2 += nums[j]
            maxnum = max(maxnum, sum2 / k)
            sum2 = 0
        return maxnum


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
            line = next(lines)
            k = int(line);

            ret = Solution().findMaxAverage(nums, k)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()