# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:22 AM 1/27/21
### [167\. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

Difficulty: **简单**


给定一个已按照**_升序排列_**的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值index1 和 index2，其中 index1必须小于index2_。_

**说明:**

*   返回的下标值（index1 和 index2）不是从零开始的。
*   你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

**示例:**

```
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
```

"""
import json
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dic = {}
        for i in range(n):
            dic[nums[i]] = i

        for i in range(n):
            other = target - nums[i]
            if other in dic and dic[other] != i:
                return [i + 1, dic[other] + 1]
        return [-1, -1]


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


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
            numbers = stringToIntegerList(line);
            line = next(lines)
            target = int(line);

            ret = Solution().twoSum(numbers, target)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()