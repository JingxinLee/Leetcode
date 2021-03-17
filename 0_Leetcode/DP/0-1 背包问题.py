# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 10:59 AM 2/24/21

给你一个可装载重量为W的背包和N个物品，每个物品有重量和价值两个属性。其中第i个物品的重量为wt[i]，价值为val[i]，现在让你用这个背包装物品，最多能装的价值是多少？

举个简单的例子，输入如下：

N = 3, W = 4
wt = [2, 1, 3]
val = [4, 2, 3]
算法返回 6，选择前两件物品装进背包，总重量 3 小于W，可以获得最大价值 6。

【状态】，就是「背包的容量」和「可选择的物品」。

【选择】，对于每件物品，你能选择什么？选择就是「装进背包」或者「不装进背包」.

dp[i][j] 定义：对于前i个物品，现在背包已经装的容量和为j，这种情况下可以装的最大价值是dp[i][j]

【Base Case】： dp[0][..] = dp[..][0] = 0，因为没有物品或者背包没有空间的时候，能装的最大价值就是 0。

【框架】：
--------------------------------------------------------
for 状态1 in 状态1的所有取值：
    for 状态2 in 状态2的所有取值：
        for ...
            dp[状态1][状态2][...] = 择优(选择1，选择2...)
--------------------------------------------------------

"""
import json
from typing import List
N = 3  # N个物品
W = 4  # 可装载重量为W的背包
wt = [2, 1, 3]
val = [4, 2, 3]


def knapsack(W, N, wt, val):
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            if j < wt[i - 1]: # 当前背包容量装不下， 只能选择不装入背包  wt的第i个为 wt[i-1]， 因为i从1开始，如wt的第1个为wt[1-1] = wt[0]
                dp[i][j] = dp[i - 1][j]
            else: # 此时 j >= wt[i-1]
                dp[i][j] = max(
                    dp[i - 1][j - wt[i - 1]] + val[i - 1], # 选择1：装
                    dp[i - 1][j]  # 选择2： 不装
                )
    for i in range(N + 1):
        print(dp[i])
    return dp[N][W]
# [0, 0, 0, 0, 0]
# [0, 0, 4, 4, 4]
# [0, 2, 4, 6, 6]
# [0, 2, 4, 6, 6]
# 6

def knapsack2(W, N, wt, val):
    dp = [[0] * (W + 1) for _ in range(N)]
    for j in range(wt[0], W+1):
        dp[0][j] = val[0] # 第0个物品 背包重量和为j（wt[0] <= j <= W）时，此时最大的价值就是第0个物品的价值val[0]   如果 wt[0] > j 就装不下了， val为0
    for i in range(1, N):
        for j in range(W + 1):
            if j - wt[i] < 0: # 当前背包容量装不下， 只能选择不装入背包
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j - wt[i]] + val[i],
                    dp[i - 1][j]
                )
    for i in range(N):
        print(dp[i])
    return dp[N-1][W]

# [0, 0, 4, 4, 4]
# [0, 2, 4, 6, 6]
# [0, 2, 4, 6, 6]
# 6

print(knapsack(W, N, wt, val))