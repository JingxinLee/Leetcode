# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:58 PM 7/28/20

把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1:
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]

示例2:
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]

限制：
1 <= n <= 11
---------------------
n个骰子，一共有 6**n 种情况
n=1, 和为s的情况有 F(n,s)=1 s=1,2,3,4,5,6
n>1 , F(n,s) = F(n-1,s-1)+F(n-1,s-2) +F(n-1,s-3)+F(n-1,s-4)+F(n-1,s-5)+F(n-1,s-6)
可以看作是从前(n-1)个骰子投完之后的状态转移过来。

假设f(m,n)表示投第m个骰子的时候，点数之和为n出现的次数，投第m个骰子的点数之和只与投第m-1个骰子有关。我们得到递归方程：
f(m,n)=f(m-1,n-1)+f(m-1,n-2)+f(m-1,n-3)+f(m-1,n-4)+f(m-1,n-5)+f(m-1,n-6)
表示本轮点数之和为n出现次数等于上一轮点数之和为n-1,n-2,n-3,n-4,n-5,n-6出现的次数之和。

当有3个骰子，我们可以将2个骰子放在一组A，另一个骰子为一组B，计算那2个筛子为一组的A的值+1个骰子为一组的B值，
如果现在我们要求3个骰子掷出来的点数为9，那么我们要求的是B组点数必须在1~6之间，
因此当B组掷出1的时候，另一组就是8，直到B组掷到6，A组就是3，所以我们看的是A组的3~8.

再拿2个骰子举例子，A组为一个骰子，B组为一个骰子，我们固定A组，B组可能的取值是1~6，
因此当A组为5的时候，B组从1~4，【也就是说总和为5， B组可以为 1 2 3 4， 不能是5， 因为B为5，A为0不可能出现。】
所以计算的结果是5-1,5-2,5-3,5-4是4,3,2,1, 这代表的是在一个骰子的时候掷出4，3，2，1的次数。

当A组为8的时候，要注意的是，由于B组只能掷出1~6的值，所以计算的结果是 8-1,8-2,8-3,8-4,8-5,8-6,8-7 .
为什么没有8-7，刚说了，因为B组只能掷出1~6的值，所以计算的结果是7,6,5,4,3,2.

我们假定从2个骰子开始，A组一定是2-1个骰子的结果，B组永远是1个骰子的结果;假定从3个骰子开始，A组一定是3-1个骰子的结果，而B组永远是1个骰子的结果。
而n个骰子的结果一定是A组中n-1个骰子的结果；
A组中的n-1个的结果相加就是n个骰子的可能的结果，如果需要再细化一下描述，
当有n个骰子的时候，我们计算掷出一个k点数的可能性的个数，这个k一定是n-1个骰子的时候的A组中k-1~k-6的总和，这个A组就是n-1个骰子掷出k-1~k-6的个数。
https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/pythondong-tai-gui-hua-yu-di-gui-ban-ben-by-alg_bi/
"""

class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        dp = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]
        for i in range(1, 7):
            dp[1][i] = 1  # 投第一个骰子时候 点数和为 i 的次数    [表示状态]


        for i in range(2, n + 1): # 第i个骰子
            for j in range(i, 6 * i + 1): #  和为 j:  2个骰子最少和为2， 3个骰子最少和为3
                for k in range(1, 7):  # 1 2 3 4 5 6   F(n,s) = F(n-1,s-1)+F(n-1,s-2) +F(n-1,s-3)+F(n-1,s-4)+F(n-1,s-5)+F(n-1,s-6)
                    dp[i][j] += dp[i - 1][j - k]  # [找出状态转移方程]
        res = []
        for i in range(n, n * 6 + 1):
            res.append(dp[n][i] * 1.0 / 6**n)
        print(dp)
        return res




def stringToInt(input):
    return int(input)


def doubleToString(input):
    if input is None:
        input = 0
    return "%.5f" % input


def doubleListToString(nums, len_of_list=None):
    if nums is None or len_of_list == 0:
        return "[]"

    if len_of_list is None:
        len_of_list = len(nums)

    serializedDoubles = []
    for num in nums:
        serializedDoubles.append(doubleToString(num))
    return "[{}]".format(','.join(serializedDoubles))


def main():
    import sys
    def readlines():
        with open('stdin.txt') as f:
            for line in f:
                yield line.strip(('\n'))

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = stringToInt(line)

            ret = Solution().twoSum(n)

            out = doubleListToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()