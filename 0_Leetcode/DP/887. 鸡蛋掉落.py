# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 9:12 AM 3/1/21
### [887\. 鸡蛋掉落](https://leetcode-cn.com/problems/super-egg-drop/)

Difficulty: **困难**


你将获得 `K` 个鸡蛋，并可以使用一栋从 `1` 到 `N`  共有 `N` 层楼的建筑。

每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

你知道存在楼层 `F` ，满足 `0 <= F <= N` 任何从高于 `F` 的楼层落下的鸡蛋都会碎，从 `F` 楼层或比它低的楼层落下的鸡蛋都不会破。

每次_移动_，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 `X` 扔下（满足 `1 <= X <= N`）。

你的目标是**确切地**知道 `F` 的值是多少。

无论 `F` 的初始值如何，你确定 `F` 的值的最小移动次数是多少？

**示例 1：**

```
输入：K = 1, N = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
如果它没碎，那么我们肯定知道 F = 2 。
因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
```

**示例 2：**

```
输入：K = 2, N = 6
输出：3
```

**示例 3：**

```
输入：K = 3, N = 14
输出：4
```

**提示：**

1.  `1 <= K <= 100`
2.  `1 <= N <= 10000`

"""
import json
from typing import List


class Solution0: # 超时
    def superEggDrop(self, K: int, N: int) -> int:
        """
        动态规划算法的时间复杂度就是子问题个数 × 函数本身的复杂度
        函数本身的复杂度  就是忽略递归部分的复杂度，这里dp函数中有一个 for 循环，所以函数本身的复杂度是 O(N)
        子问题个数  也就是不同状态组合的总数，显然是 两个状态的乘积，也就是 O(KN)
        所以算法的 总时间复杂度 是 O(K*N^2), 空间复杂度 为 子问题个数，即 O(KN)
        """
        memo = {}
        def dp(K, N):
            if K == 1: return N # 当鸡蛋数K为 1 时，显然只能线性扫描所有楼层
            if N == 0: return 0 # 当楼层数N等于 0 时，显然不需要扔鸡蛋
            if (K, N) in memo:
                return memo[(K, N)]
            res = float('inf')
            for i in range(1, N+1): # 最坏情况下 最少 扔鸡蛋次数
                # 如果鸡蛋碎了，那么鸡蛋的个数K应该减一，搜索的楼层区间应该从[1..N]变为[1..i-1]共i-1层楼；
                # 如果鸡蛋没碎，那么鸡蛋的个数K不变，搜索的楼层区间应该从 [1..N]变为[i+1..N]共N-i层楼
                res = min(res, max(dp(K, N - i), dp(K-1, i-1)) + 1)
            memo[(K, N)] = res
            return res
        return dp(K, N)

class Solution1: # 二分法
    def superEggDrop(self, K: int, N: int) -> int:
        """
        动态规划算法的时间复杂度就是   子问题个数 × 函数本身的复杂度。
        函数本身的复杂度 就是忽略递归部分的复杂度，这里dp函数中用了一个 二分搜索 ，所以函数本身的复杂度是 O(logN)。
        子问题个数也就是  不同状态组合的总数，显然是两个状态的乘积，也就是 O(KN)。
        所以算法的总时间复杂度是 O(K*N*logN), 空间复杂度 O(KN)。效率上比之前的算法 O(KN^2) 要高效不少
        """
        memo = {}
        def dp(K, N):
            if K == 1: return N
            if N == 0: return 0
            if (K, N) in memo:
                return memo[(K, N)]
            res = float('inf')

            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(K-1, mid-1)
                not_broken = dp(K, N-mid)
                # res = min(max(碎，没碎) + 1)
                if broken > not_broken: # 碎的 比 不碎 的要多, 所以大部分都碎了，所以要在下半部分找，因为再往上还会碎的更多
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)
            memo[(K, N)] = res
            return res

        return dp(K, N)

class Solution:
    def superEggDrop(self, K: int, N: int) -> int: # 给你K鸡蛋，N层楼，让你求最坏情况下最少的测试次数m
        dp = [[0] * (N + 1) for _ in range(K + 1)] # 确定当前的鸡蛋个数和最多允许的扔鸡蛋次数，就知道能够确定F的最高楼层数
        m = 0
        while dp[K][m] < N: # while循环结束的条件是dp[K][m] == N，也就是给你K个鸡蛋，[允许测试] m 次，最坏情况下最多能测试N层楼   m 是一个[允许]的次数上界，而不是扔了几次
            m += 1
            for k in range(1, K + 1):
                # dp[k][m - 1]就是 [楼上] 的楼层数，因为[鸡蛋个数] k 不变，也就是鸡蛋没碎，[扔鸡蛋次数] m 减一；
                # dp[k - 1][m - 1]就是 [楼下] 的楼层数，因为[鸡蛋个数] k 减一，也就是鸡蛋碎了，同时[扔鸡蛋次数] m 减一。
                dp[k][m] = dp[k][m-1] + dp[k - 1][m - 1] + 1
        return m



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
            K = int(line);
            line = next(lines)
            N = int(line);

            ret = Solution().superEggDrop(K, N)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()