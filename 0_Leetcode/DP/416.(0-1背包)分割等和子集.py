# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 5:00 PM 2/24/21
### [416\. 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum/)

Difficulty: **中等**


给定一个**只包含正整数**的**非空**数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

**注意:**

1.  每个数组中的元素不会超过 100
2.  数组的大小不会超过 200

**示例 1:**

```
输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
```

**示例2:**

```
输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.
```
https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/fen-ge-deng-he-zi-ji-by-leetcode-solution/
https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1-bei-bao-wen-ti-xiang-jie-zhen-dui-ben-ti-de-yo/
"""
import json
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sum = 0
        for num in nums:
            sum += num
        if sum % 2 != 0: return False
        target = sum // 2

        # 创建二维状态数组，行：物品索引，列：容量（包括 0）  很多时候，我们需要考虑这个容量为 0 的数值。
        dp = [[False] * (target + 1) for _ in range(n)]  # dp[i][j] 表示从数组的 [0,i]下标范围内选取若干个正整数（可以是 0 个），是否存在一种选取方案使得被选取的正整数的和等于 j
        for i in range(n): # [0,i]范围内可以选择0个数， 如果不选取任何正整数，则被选取的和可以等于 0
            dp[i][0] = True

        if nums[0] <= target: # 先填表格第 0 行，第 1 个数  只能让容积为 它自己 的背包恰好装满
            dp[0][nums[0]] = True

        for i in range(1, n): # 接着从第0行的下面  第1行 开始
            for j in range(1, target+1):
                if nums[i] <= j:   # 此时 【不选择】 nums[i]： 在[0, i - 1] 这个子区间内已经有一部分元素，使得它们的和为 j     或者 【选择】 nums[i] ： [0, i - 1] 这个子区间内就得找到一部分元素，使得它们的和为 j - nums[i]。
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else: # nums[i] > j 也就是当前数字大于背包容量， 所以无法选择当前数字，
                    dp[i][j] = dp[i - 1][j]
        for i in range(n):
            print(dp[i])
        return dp[n-1][target]
##########################################################################################
# [1,5,11,5]
# [True, True, False, False, False, False, False, False, False, False, False, False]
# [True, True, False, False, False, True, True, False, False, False, False, False]
# [True, True, False, False, False, True, True, False, False, False, False, True]
# [True, True, False, False, False, True, True, False, False, False, True, True]
# True
##########################################################################################



##########################################################################################

class Solution1: # 压缩空间
    """
    这里可能会有人困惑为什么压缩到一维时，要采用[逆序]。因为在一维情况下，是根据 dp[j] || dp[j - nums[i]]来推dp[j]的值，
    如不逆序，就无法保证在外循环 i 值保持不变 j 值递增的情况下，dp[j - num[i]]的值不会被当前所放入的nums[i]所修改，
    当j值未到达临界条件前，会一直被nums[i]影响，也即是可能 重复的放入了多次nums[i]，为了避免前面对后面产生影响，故用逆序。

    举个例子，数组为[2,2,3,5]，要找和为6的组合，i = 0时，dp[2]为真，当i自增到1，j = 4时，nums[i] = 2,dp[4] = dp[4] || dp[4 - 2]为true，
    当i不变，j = 6时,dp[6] = dp [6] || dp [6 - 2],而dp[4]为true，所以dp[6] = true,显然是错误的。
    故必须得纠正在正序情况下，i值不变时多次放入nums[i]的情况。

    dp[j] = dp[j] || dp[j - nums[i]] 可以理解为 dp[j] （新）= dp[j] （旧） || dp[j - nums[i]] （旧），如果采用正序的话 dp[j - nums[i]]会被之前的操作更新为新值
    """
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sum = 0
        for num in nums:
            sum += num
        if sum % 2 != 0: return False
        target = sum // 2

        dp = [False] * (target + 1)
        dp[0] = True
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        # print(dp)   dp[6]是不可能的，但是【从前往后】就会导致dp[6]=True， 这是错误的
        return dp[target]

# [2,2,3,5]
# [True, False, True, True, True, True, False]
# False


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

            ret = Solution1().canPartition(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()