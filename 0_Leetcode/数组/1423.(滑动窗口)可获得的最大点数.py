# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:58 PM 2/6/21
### [1423\. 可获得的最大点数](https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/)

Difficulty: **中等**


几张卡牌 **排成一行**，每张卡牌都有一个对应的点数。点数由整数数组 `cardPoints` 给出。

每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 `k` 张卡牌。

你的点数就是你拿到手中的所有卡牌的点数之和。

给你一个整数数组 `cardPoints` 和整数 `k`，请你返回可以获得的最大点数。

**示例 1：**

```
输入：cardPoints = [1,2,3,4,5,6,1], k = 3
输出：12
解释：第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12 。
```

**示例 2：**

```
输入：cardPoints = [2,2,2], k = 2
输出：4
解释：无论你拿起哪两张卡牌，可获得的点数总是 4 。
```

**示例 3：**

```
输入：cardPoints = [9,7,7,9,7,7,9], k = 7
输出：55
解释：你必须拿起所有卡牌，可以获得的点数为所有卡牌的点数之和。
```

**示例 4：**

```
输入：cardPoints = [1,1000,1], k = 1
输出：1
解释：你无法拿到中间那张卡牌，所以可以获得的最大点数为 1 。
```

**示例 5：**

```
输入：cardPoints = [1,79,80,1,1,1,200,1], k = 3
输出：202
```

**提示：**

*   `1 <= cardPoints.length <= 10^5`
*   `1 <= cardPoints[i] <= 10^4`
*   `1 <= k <= cardPoints.length`

[1,79,80,1,1,1,200,1]
3

[11,49,100,20,86,29,72]
4

"""
import json
from typing import List
class Solution: # 滑动窗口
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window = n - k  # 找 k 个 最大 <=> 找剩下的 n-k 个 最小
        firstRes = minRes = sum(cardPoints[:n-k])
        res = 0
        for i in range(window, n): # 可以精简 res, 如solution1
            res = firstRes - cardPoints[i - window] + cardPoints[i]
            minRes = min(res, minRes)
            firstRes = res
        return sum(cardPoints) - minRes

class Solution1: # 滑动窗口
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # 滑动窗口大小为 n-k
        windowSize = n - k
        # 选前 n-k 个作为初始值
        s = sum(cardPoints[:windowSize])
        minSum = s
        for i in range(windowSize, n):
            # 滑动窗口每向右移动一格，增加从右侧进入窗口的元素值，并减少从左侧离开窗口的元素值
            s += cardPoints[i] - cardPoints[i - windowSize]
            minSum = min(minSum, s)
        return sum(cardPoints) - minSum


class Solution2: # 暴力算法
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        firstcard = max(cardPoints[0], cardPoints[-1])
        dp = [firstcard]
        if cardPoints[0] == cardPoints[-1]:
            cardPoints.pop()
        else:
            cardPoints.remove(firstcard)
        for i in range(len(cardPoints)):
            card = max(cardPoints[0], cardPoints[-1])
            dp.append(card)
            cardPoints.remove(card)
            if len(dp) == k:
                break

        return sum(dp)


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
            cardPoints = stringToIntegerList(line);
            line = next(lines)
            k = int(line);

            ret = Solution().maxScore(cardPoints, k)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()