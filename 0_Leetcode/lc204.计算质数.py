# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:25 AM 12/29/20

统计所有小于非负整数n的质数的数量。

示例 1：
输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

示例 2：
输入：n = 0
输出：0

示例 3：
输入：n = 1
输出：0

提示：
0 <= n <= 5 * 106

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-primes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countPrimes1(self, n: int) -> int: # 暴力
        if n <= 1: return 0
        res = 0
        for i in range(2, n):
            for j in range(2, i):
                if i % j == 0: break
            else:
                res += 1
        return res

    def countPrimes(self, n: int) -> int: #
        dp = [1 for _ in range(n)]
        count = 0
        for i in range(2, n):
            if dp[i]:
                count += 1
                j = 2
                while i * j < n: # 如果一个数m是素数，那么所有m * k就都不是素数。另外2是最小的素数
                    dp[i * j] = 0
                    j += 1
        return count

def main():
    import sys
    import io
    def readlines():
        with open('stdin.txt') as f:
            for line in f:
                yield line.strip(('\n'))

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = int(line);

            ret = Solution().countPrimes(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()