# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:00 PM 2/22/21
### [300\. 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)

Difficulty: **中等**


给你一个整数数组 `nums` ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，`[3,6,2,7]` 是数组 `[0,3,1,6,2,2,7]` 的子序列。

**示例 1：**

```
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
```

**示例 2：**

```
输入：nums = [0,1,0,3,2,3]
输出：4
```

**示例 3：**

```
输入：nums = [7,7,7,7,7,7,7]
输出：1
```

**提示：**

*   `1 <= nums.length <= 2500`
*   `-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>`

**进阶：**

*   你可以设计时间复杂度为 `O(n<sup>2</sup>)` 的解决方案吗？
*   你能将算法的时间复杂度降低到 `O(n log(n))` 吗?

"""
import json
from typing import List

class Solution0: # DP ： dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution: # 二分法
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2: return size
        cell = [nums[0]]
        for num in nums[1:]:
            if num > cell[-1]:
                cell.append(num)
                continue
            l, r = 0, len(cell) - 1
            while l < r:
                mid = l + (r - l) // 2
                if cell[mid] < num:  # 找到cell第一个比num大的
                    l = mid + 1
                else:
                    r = mid
            cell[l] = num  # 找到后替换
        return len(cell)


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

            ret = Solution().lengthOfLIS(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()