# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 7:42 PM 1/30/21
### [40\. 组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii/)

Difficulty: **中等**


给定一个数组`candidates`和一个目标数`target`，找出`candidates`中所有可以使数字和为`target`的组合。

`candidates`中的每个数字在每个组合中只能使用一次。

**说明：**

*   所有数字（包括目标数）都是正整数。
*   解集不能包含重复的组合。

**示例1:**

```
输入: candidates =[10,1,2,7,6,1,5], target =8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

**示例2:**

```
输入: candidates =[2,5,2,1,2], target =5,
所求解集为:
[
 [1,2,2],
 [5]
]
```


这个避免重复当思想是在是太重要了。
这个方法最重要的作用是，可以让同一层级，不出现相同的元素。即
                  1
                 / \
                2   2  这种情况不会发生 但是却允许了不同层级之间的重复即：
               /     \
              5       5
                例2
                  1
                 /
                2      这种情况确是允许的
               /
              2

为何会有这种神奇的效果呢？
首先 cur-1 == cur 是用于判定当前元素是否和之前元素相同的语句。这个语句就能砍掉例1。
可是问题来了，如果把所有当前与之前一个元素相同的都砍掉，那么例二的情况也会消失。
因为当第二个2出现的时候，他就和前一个2相同了。

那么如何保留例2呢？
那么就用cur > begin 来避免这种情况，你发现例1中的两个2是处在同一个层级上的，
例2的两个2是处在不同层级上的。
在一个for循环中，所有被遍历到的数都是属于一个层级的。我们要让一个层级中，
必须出现且只出现一个2，那么就放过第一个出现重复的2，但不放过后面出现的2。
第一个出现的2的特点就是 cur == begin. 第二个出现的2 特点是cur > begin.

https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/
"""
import json
from typing import List

class Solution:
    def __init__(self) -> None:
        self.res = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        track = []
        candidates.sort()
        self.backtrack(candidates, target, track, 0, 0)
        return self.res

    def backtrack(self, nums, target, track, start, summ):
        if summ == target:
            self.res.append(track[:])
            return
        for i in range(start, len(nums)):
            if summ > target or( i > start and nums[i] == nums[i-1]): # 如果summ比target大了,以后的都不用看了, 或者i>start 说明至少2个数,当前数字和前一个数字相同,也重复了,不用看
                continue
            track.append(nums[i])
            self.backtrack(nums, target, track, i+1, summ+nums[i]) # 只能选择一次,所以 i 要 +1
            track.pop()


def stringToIntegerList(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


def int2dArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            candidates = stringToIntegerList(line)
            line = next(lines)
            target = stringToInt(line)

            ret = Solution().combinationSum2(candidates, target)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()