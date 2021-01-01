# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 11:00 PM 7/28/20

0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，
因此最后剩下的数字是3。

示例 1：
输入: n = 5, m = 3
输出:3

示例 2：
输入: n = 10, m = 17
输出:2
https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/fn-m-m-x-n-zhe-gong-shi-dao-di-zha-lai-de-by-lucie/

f(n,m) = y  => y是下标，所以就意味着你从index=0开始数，数y+1个数，然后就停，停谁身上谁就是结果。
f(n-1,m)=x  => 有n-1个数的时候从index=0开始数，数x+1个数你就找到这结果了

1.有n个数的时候，我们划掉了下标为 (m-1)%n 的数字:
因为要从0数m个数，那最后肯定落到了下标为 m-1 的数身上了，但这个下标可能超过我们有的最大下标（n-1）了。
所以攒满n个就归零接着数，逢n归零，所以要模n

2.划完了这个数，往后数x+1下，能落到谁身上呢，它的下标是几？
你往后数x+1，它下标肯定变成了(m-1)%n +x+1，和第一步的想法一样，你肯定还是得取模，
所以答案为[(m-1)%n+x+1]%n，则 f(n,m)=[(m-1)%n+x+1]%n  其中 x = f(n-1,m)

① (a+b)%c=((a%c)+(b%c))%c
② a%c=(a%c)%c
由①和②得： f(n,m)=[(m-1)%n+x+1]%n=(m-1)%n%n+(x+1)%n=(m-1)%n+(x+1)%n=(m-1+x+1)%n= (m+x)%n

"""

import json
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return self.f(n, m)
    def f(self, n, m):
        if n == 0: return 0
        x = self.f(n-1, m)
        return (m + x) % n

    def lastRemaining2(self, n: int, m: int) -> int:
        i, a = 0, list(range(n))
        while len(a) > 1:
            i = (i + m - 1) % len(a)
            a.pop(i)
        return a[0]




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
            line = next(lines)
            m = int(line);

            ret = Solution().lastRemaining(n, m)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()