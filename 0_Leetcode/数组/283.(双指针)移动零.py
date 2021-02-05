# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:32 PM 1/26/21
### [283\. 移动零](https://leetcode-cn.com/problems/move-zeroes/)

Difficulty: **简单**


给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

**示例:**

```
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
```

**说明**:

1.  必须在原数组上操作，不能拷贝额外的数组。
2.  尽量减少操作次数。

"""
import json
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


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
            nums = stringToIntegerList(line);

            ret = Solution().moveZeroes(nums)

            out = integerListToString(nums)
            if ret is not None:
                print
                "Do not return anything, modify nums in-place instead."
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()