# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:19 PM 2/26/21
### [452\. 用最少数量的箭引爆气球](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/)

Difficulty: **中等**


在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。

一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 `x`<sub style="display: inline;">`start`，</sub>`x`<sub style="display: inline;">`end`，</sub> 且满足  `x<sub style="display: inline;">start</sub> ≤ x ≤ x`<sub style="display: inline;">`end`，</sub>则该气球会被引爆<sub style="display: inline;">。</sub>可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

给你一个数组 `points` ，其中 `points [i] = [x<sub style="display: inline;">start</sub>,x<sub style="display: inline;">end</sub>]` ，返回引爆所有气球所必须射出的最小弓箭数。

**示例 1：**

```
输入：points = [[10,16],[2,8],[1,6],[7,12]]
输出：2
解释：对于该样例，x = 6 可以射爆 [2,8],[1,6] 两个气球，以及 x = 11 射爆另外两个气球
```

**示例 2：**

```
输入：points = [[1,2],[3,4],[5,6],[7,8]]
输出：4
```

**示例 3：**

```
输入：points = [[1,2],[2,3],[3,4],[4,5]]
输出：2
```

**示例 4：**

```
输入：points = [[1,2]]
输出：1
```

**示例 5：**

```
输入：points = [[2,3],[2,3]]
输出：1
```

**提示：**

*   `0 <= points.length <= 10<sup>4</sup>`
*   `points[i].length == 2`
*   `-2<sup>31</sup> <= x<sub style="display: inline;">start</sub> < x<sub style="display: inline;">end</sub> <= 2<sup>31</sup> - 1`

"""
import json
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 0 : return 0
        points.sort(key=lambda x: x[1])
        cnt = 1
        x_end = points[0][1]
        for point in points:
            start = point[0]
            if start > x_end:
                cnt += 1
                x_end = point[1]
        return cnt


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
            points = stringToInt2dArray(line)

            ret = Solution().findMinArrowShots(points)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()