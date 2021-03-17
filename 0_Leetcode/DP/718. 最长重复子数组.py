# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 9:29 PM 2/20/21
### [718\. 最长重复子数组](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/)

Difficulty: **中等**


给两个整数数组`A`和`B`，返回两个数组中公共的、长度最长的子数组的长度。

**示例：**

```
输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
```

**提示：**

*   `1 <= len(A), len(B) <= 1000`
*   `0 <= A[i], B[i] < 100`

https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-zhong-fu-zi-shu-zu-by-leetcode-solution/

"""
import json
from typing import List


class Solution:
    """
    dp[i][j] 表示 A[i:] 和 B[j:] 的最长公共前缀，那么答案即为所有 dp[i][j] 中的最大值。
    如果 A[i] == B[j]，那么 dp[i][j] = dp[i + 1][j + 1] + 1，否则 dp[i][j] = 0

    """
    def findLength(self, A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0  # [3][1] = 1 + [4][2]
                ans = max(ans, dp[i][j])
        return ans

class Solution1:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    ans = max(ans, dp[i][j])

        return ans


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
            A = stringToIntegerList(line);
            line = next(lines)
            B = stringToIntegerList(line);

            ret = Solution().findLength(A, B)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()