# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:14 PM 2/26/21
### [435\. 无重叠区间](https://leetcode-cn.com/problems/non-overlapping-intervals/)

Difficulty: **中等**


给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

**注意:**

1.  可以认为区间的终点总是大于它的起点。
2.  区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

**示例 1:**

```
输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
```

**示例 2:**

```
输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
```

**示例 3:**

```
输入: [ [1,2], [2,3] ]

输出: 0

解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
```

```
"""
import json
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def intervalSchedule(intervals):
            if len(intervals) == 0: return 0
            intervals.sort(key=lambda x: x[1])
            count = 1
            x_end = intervals[0][1]
            for interval in intervals:
                start = interval[0]
                if start >= x_end:
                    count += 1
                    x_end = interval[1]
            return count
        n = len(intervals)
        return n -intervalSchedule(intervals)


def stringToInt2dArray(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            intervals = stringToInt2dArray(line)

            ret = Solution().eraseOverlapIntervals(intervals)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()